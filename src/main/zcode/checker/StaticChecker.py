from main.zcode.utils.AST import *
from main.zcode.checker.StaticError import *
from main.zcode.utils.Visitor import *
from main.zcode.utils.Utils import *
from typing import List

class VarSym:
    def __init__(self, name: str, typ: Type = None) -> None:
        self.name = name
        self.typ = typ

class FuncSym:
    def __init__(self, name: str, params: List[VarSym] = [], typ: Type = None, body: Stmt = None) -> None:
        self.name = name
        self.params = params
        self.typ = typ
        self.body = body

class StaticChecker(Visitor, Utils):
    def __init__(self, ast: AST) -> None:
        self.ast = ast
        self.env = [[
            FuncSym("readNumber", [], NumberType()),
            FuncSym("readString", [], StringType()),
            FuncSym("readBool", [], BoolType()),
            FuncSym("writeBool", [VarSym("", BoolType())], VoidType()),
            FuncSym("writeString", [VarSym("", StringType())], VoidType()),
            FuncSym("writeNumber", [VarSym("", NumberType())], VoidType())
        ]]
        self.has_return = False
        self.func_name = None
        self.resolved = True
        self.no_body = []
        self.in_loop = []
        self.arr_ast = []
        self.curr_var_name = None
        self.list_return = []
        self.scope = 0
    
    def check(self) -> None:
        self.visit(self.ast, self.env)
    
    def resolveType(self, expr: Id | CallExpr | CallStmt | ArrayLiteral, typ: Type, param):  # Assume that name is found
        if type(expr) is Id:
            idex = None
            for idx in range(len(param)):
                sym = self.lookup(expr.name, param[idx], lambda x: x.name)
                if sym is not None and type(sym) is VarSym:
                    idex = idx
                    break
            
            if idex is not None:
                for idx in range(len(param[idex])):
                    if type(param[idex][idx]) is VarSym and param[idex][idx].name == expr.name:
                        param[idex][idx] = VarSym(sym.name, typ)
        
        elif type(expr) in [CallExpr, CallStmt]:
            for idx in range(len(param[-1])):
                if type(param[-1][idx]) is FuncSym and param[-1][idx].name == expr.name.name and param[-1][idx].typ is None:
                    sym = param[-1][idx]
                    param[-1][idx] = FuncSym(sym.name, sym.params, typ, sym.body)

        else:
            if type(typ) is not ArrayType:
                self.resolved = False

            else:
                if len(expr.value) != typ.size[0]:
                    self.resolved = False

                for val in expr.value:
                    self.resolveType(val, typ.eleType if len(typ.size) == 1 else ArrayType(typ.size[1:], typ.eleType), param)
    
    def visitProgram(self, ast: Program, param):
        for decl in ast.decl:
            self.visit(decl, param)

        if self.no_body != []:
            raise NoDefinition(self.no_body[0].name.name)
        
        flag = False
        for func in param[0]:
            if type(func) is FuncSym and func.name == "main" and type(func.typ) is VoidType and func.params == []:
                flag = True
                break
        
        if not flag:
            raise NoEntryPoint()

    def visitVarDecl(self, ast: VarDecl, param):
        if self.lookup(ast.name.name, param[0], lambda x: x.name) is not None:
            raise Redeclared(Variable(), ast.name.name)
        
        self.curr_var_name = ast.name.name
        lhsType = ast.varType
        if ast.varInit is not None:
            rhsType = self.visit(ast.varInit, param)
            if lhsType is not None and rhsType is not None:
                if type(lhsType) is not type(rhsType):
                    raise TypeMismatchInStatement(ast)
                
                else:
                    if type(rhsType) is ArrayType:
                        if len(rhsType.size) > len(lhsType.size):
                            raise TypeMismatchInStatement(ast)
                        
                        if len(rhsType.size) == len(lhsType.size) and rhsType.size != lhsType.size:
                            raise TypeMismatchInStatement(ast)
                        
                        if rhsType.eleType is None:
                            self.resolveType(ast.varInit, lhsType, param)
                            if self.resolved is False:
                                raise TypeCannotBeInferred(ast)
                            
                            rhsType = lhsType

                        if type(rhsType.eleType) is not type(lhsType.eleType) or rhsType.size != lhsType.size:
                            raise TypeMismatchInStatement(ast)
                        
                    param[0] += [VarSym(ast.name.name, lhsType)]
            
            else:
                if (rhsType is None or (rhsType is not None and type(rhsType) is ArrayType and rhsType.eleType is None)) and lhsType is None:
                    raise TypeCannotBeInferred(ast)
                
                elif rhsType is None and lhsType is not None:
                    if type(ast.varInit) in [Id, CallExpr, ArrayLiteral]:
                        self.resolveType(ast.varInit, lhsType, param)
                        if self.resolved is False:
                            raise TypeCannotBeInferred(ast)
                        
                        param[0] += [VarSym(ast.name.name, lhsType)]
                    
                    else:
                        raise TypeCannotBeInferred(ast)
                
                else:
                    param[0] += [VarSym(ast.name.name, rhsType)]
        
        else:
            param[0] += [VarSym(ast.name.name, lhsType)]
        
        self.arr_ast = []
        self.curr_var_name = None
    
    def visitFuncDecl(self, ast: FuncDecl, param):
        func = self.lookup(ast.name.name, param[-1], lambda x: x.name)
        if func is not None and ((type(func) is VarSym) or (func.body is not None or (func.body is None and ast.body is None))):
            raise Redeclared(Function(), ast.name.name)
        
        params = []
        for param_decl in ast.param:
            if self.lookup(param_decl.name.name, params, lambda x: x.name) is not None:
                raise Redeclared(Parameter(), param_decl.name.name)

            else:
                params += [VarSym(param_decl.name.name, self.visit(param_decl.varType, param))]
        
        param = [params] + param
        
        if ast.body is None:
            self.no_body += [ast]
            param[-1] += [FuncSym(ast.name.name, params, None, None)]
        
        else:
            self.func_name = ast.name.name
            for f in self.no_body:
                if f.name.name == self.func_name:
                    self.no_body.remove(f)
            
            func_found = False
            for idx in range(len(param[-1])):
                if type(param[-1][idx]) is FuncSym and param[-1][idx].name == ast.name.name:
                    func_found = True
                    if len(param[-1][idx].params) != len(params):
                        raise Redeclared(Function(), ast.name.name)
                    
                    for idex in range(len(params)):
                        if type(param[-1][idx].params[idex].typ) is not type(params[idex].typ) or (type(param[-1][idx].params[idex].typ) is ArrayType and (param[-1][idx].params[idex].typ.size != params[idex].typ.size or type(param[-1][idx].params[idex].typ.eleType) is not type(params[idex].typ.eleType))):
                            raise Redeclared(Function(), ast.name.name)
                    
                    self.visit(ast.body, param)
                    break
            
            if not func_found:
                param[-1] += [FuncSym(ast.name.name, params, None, ast.body)]
                self.visit(ast.body, param)
        
        self.has_return = False
        param = param[1:]
        self.list_return = []

    def visitNumberLiteral(self, ast: NumberLiteral, param):
        return NumberType()

    def visitStringLiteral(self, ast: StringLiteral, param):
        return StringType()
    
    def visitBooleanLiteral(self, ast: BooleanLiteral, param):
        return BoolType()
    
    def visitNumberType(self, ast: NumberType, param):
        return NumberType()
    
    def visitBoolType(self, ast: BoolType, param):
        return BoolType()
    
    def visitStringType(self, ast: StringType, param):
        return StringType()

    def visitArrayType(self, ast: ArrayType, param):
        return ArrayType(ast.size, ast.eleType)
    
    def visitReturn(self, ast: Return, param):
        if self.has_return:
            return
        
        self.has_return = True
        self.list_return += [ast]
        if ast.expr is None:
            for idx in range(len(param[-1])):
                if type(param[-1][idx]) is FuncSym and param[-1][idx].name == self.func_name:
                    if param[-1][idx].typ is None:
                        param[-1][idx].typ = VoidType()
                        break
                    
                    else:
                        if type(param[-1][idx].typ) is not VoidType:
                            raise TypeMismatchInStatement(ast)
        
        else:
            rettype = self.visit(ast.expr, param)
            func = self.lookup(self.func_name, param[-1], lambda x: x.name)
            if func.typ is None:
                if rettype is None:
                    raise TypeCannotBeInferred(ast)
                
                else:
                    for idx in range(len(param[-1])):
                        if type(param[-1][idx]) is FuncSym and param[-1][idx].name == self.func_name:
                            sym = param[-1][idx]
                            param[-1][idx] = FuncSym(sym.name, sym.params, rettype, sym.body)
                
            else:
                if type(func.typ) is VoidType:
                    raise TypeMismatchInStatement(ast)
                
                if rettype is None:
                    if self.resolved is False:
                        raise TypeCannotBeInferred(ast)
                    
                    elif type(ast.expr) in [Id, CallExpr, ArrayLiteral]:
                        self.resolveType(ast.expr, func.typ, param)
                        if self.resolved is False:
                            raise TypeCannotBeInferred(ast)
                    
                    else:
                        raise TypeCannotBeInferred(ast)
                
                else:
                    if type(func.typ) is not type(rettype):
                        raise TypeMismatchInStatement(ast)
                    
                    else:
                        if type(rettype) is ArrayType:
                            if len(rettype.size) > len(func.typ.size):
                                raise TypeMismatchInStatement(ast)
                            
                            if len(rettype.size) == len(func.typ.size) and rettype.size != func.typ.size:
                                raise TypeMismatchInStatement(ast)
                            
                            if rettype.eleType is None:
                                self.resolveType(ast.expr, func.typ, param)
                                if self.resolved is False:
                                    raise TypeCannotBeInferred(ast)
                                
                                rettype = func.typ

                            if type(rettype.eleType) is not type(func.typ.eleType) or rettype.size != func.typ.size:
                                raise TypeMismatchInStatement(ast)
        
        self.arr_ast = []
    
    def visitId(self, ast: Id, param):
        if self.curr_var_name is not None and ast.name == self.curr_var_name:
            raise Undeclared(Identifier(), ast.name)
        
        self.resolved = True
        found = None
        for para in param:
            sym = self.lookup(ast.name, para, lambda x: x.name)
            if sym is not None and type(sym) is VarSym:
                found = para
                break
        
        if found is None:
            raise Undeclared(Identifier(), ast.name)
        
        else:
            for idx in range(len(found)):
                if found[idx].name == ast.name and type(found[idx]) is VarSym:
                    return found[idx].typ
    
    def visitBreak(self, ast: Break, param):
        if self.in_loop == []:
            raise MustInLoop(ast)

        self.arr_ast = []
    
    def visitContinue(self, ast: Continue, param):
        if self.in_loop == []:
            raise MustInLoop(ast)
        
        self.arr_ast = []
    
    def visitBlock(self, ast: Block, param):
        param = [[]] + param
        self.scope += 1
        for stmt in ast.stmt:
            self.visit(stmt, param)
        
        if self.list_return == [] and self.scope == 1:
            for idx in range(len(param[-1])):
                if type(param[-1][idx]) is FuncSym and param[-1][idx].name == self.func_name:
                    if param[-1][idx].typ is None:
                        param[-1][idx].typ = VoidType()
                        break
                    
                    elif type(param[-1][idx].typ) is not VoidType:
                        raise FunctionNotReturn(self.func_name)
        
        self.scope -= 1
        self.has_return = False
        param = param[1:]
        self.arr_ast = []
    
    def visitCallExpr(self, ast: CallExpr, param):
        if self.curr_var_name is not None and ast.name.name == self.curr_var_name:
            raise TypeMismatchInExpression(ast)
        
        self.resolved = True
        exclude_last = param[:-1]
        for para in exclude_last:
            if self.lookup(ast.name.name, para, lambda x: x.name) is not None:
                raise TypeMismatchInExpression(ast)
            
        found = self.lookup(ast.name.name, param[-1], lambda x: x.name)
        if found is None:
            raise Undeclared(Function(), ast.name.name)
        
        if found is not None and type(found) is not FuncSym:
            raise TypeMismatchInExpression(ast)
        
        else:
            if type(found.typ) is VoidType:
                raise TypeMismatchInExpression(ast)
            
            if len(ast.args) != len(found.params):
                raise TypeMismatchInExpression(ast)
            
            for idx in range(len(ast.args)):
                arg_typ = self.visit(ast.args[idx], param)
                if arg_typ is None:
                    if type(ast.args[idx]) in [Id, CallExpr, ArrayLiteral]:
                        self.resolveType(ast.args[idx], found.params[idx].typ, param)
                        if self.resolved is False:
                            return None
                    
                    else:
                        return None
                
                elif arg_typ is None:
                    self.resolved = False
                    return None
                
                else:
                    if type(arg_typ) is not type(found.params[idx].typ):
                        raise TypeMismatchInExpression(ast)
                    
                    else:
                        if type(arg_typ) is ArrayType:
                            if len(arg_typ.size) > len(found.params[idx].typ.size):
                                raise TypeMismatchInExpression(ast)
                            
                            if len(arg_typ.size) == len(found.params[idx].typ.size) and arg_typ.size != found.params[idx].typ.size:
                                raise TypeMismatchInExpression(ast)
                            
                            if arg_typ.eleType is None:
                                self.resolveType(ast.args[idx], found.params[idx].typ, param)
                                if self.resolved is False:
                                    return None
                                
                                arg_typ = found.params[idx].typ

                            if type(arg_typ.eleType) is not type(found.params[idx].typ.eleType) or arg_typ.size != found.params[idx].typ.size:
                                raise TypeMismatchInExpression(ast)
            
            return found.typ
    
    def visitCallStmt(self, ast: CallStmt, param):
        self.resolved = True
        exclude_last = param[:-1]
        for para in exclude_last:
            if self.lookup(ast.name.name, para, lambda x: x.name) is not None:
                raise TypeMismatchInStatement(ast)
            
        found = self.lookup(ast.name.name, param[-1], lambda x: x.name)
        if found is None or (found is not None and type(found) is not FuncSym):
            raise Undeclared(Function(), ast.name.name)
        
        else:
            if found.typ is not None and type(found.typ) is not VoidType:
                raise TypeMismatchInStatement(ast)
            
            if len(ast.args) != len(found.params):
                raise TypeMismatchInStatement(ast)
            
            for idx in range(len(ast.args)):
                arg_typ = self.visit(ast.args[idx], param)
                if arg_typ is None and type(ast.args[idx]) in [Id, CallExpr, ArrayLiteral]:
                    self.resolveType(ast.args[idx], found.params[idx].typ, param)
                    if self.resolved is False:
                        raise TypeCannotBeInferred(ast)
                
                elif arg_typ is None:
                    raise TypeCannotBeInferred(ast)
                
                else:
                    if type(arg_typ) is not type(found.params[idx].typ):
                        raise TypeMismatchInStatement(ast)
                    
                    else:
                        if type(arg_typ) is ArrayType:
                            if len(arg_typ.size) > len(found.params[idx].typ.size):
                                raise TypeMismatchInStatement(ast)
                            
                            if len(arg_typ.size) == len(found.params[idx].typ.size) and arg_typ.size != found.params[idx].typ.size:
                                raise TypeMismatchInStatement(ast)
                            
                            if arg_typ.eleType is None:
                                self.resolveType(ast.args[idx], found.params[idx].typ, param)
                                if self.resolved is False:
                                    raise TypeCannotBeInferred(ast)
                                
                                arg_typ = found.params[idx].typ

                            if type(arg_typ.eleType) is not type(found.params[idx].typ.eleType) or arg_typ.size != found.params[idx].typ.size:
                                raise TypeMismatchInStatement(ast)
                                
            
            if found.typ is None:
                self.resolveType(ast, VoidType(), param)
        
        self.arr_ast = []
    
    def visitAssign(self, ast: Assign, param):
        rhsType, lhsType = self.visit(ast.rhs, param), self.visit(ast.lhs, param)
        if (rhsType is None or (rhsType is not None and type(rhsType) is ArrayType and rhsType.eleType is None)) and lhsType is None:
            raise TypeCannotBeInferred(ast)
        
        if rhsType is not None and lhsType is None:
            if type(ast.lhs) is Id:
                self.resolveType(ast.lhs, rhsType, param)
            
            else:
                raise TypeCannotBeInferred(ast)
        
        elif rhsType is None and lhsType is not None:
            if type(ast.rhs) in [Id, CallExpr, ArrayLiteral]:
                self.resolveType(ast.rhs, lhsType, param)
                if self.resolved is False:
                    raise TypeCannotBeInferred(ast)
            
            else:
                raise TypeCannotBeInferred(ast)
        
        else:
            if type(lhsType) is VoidType:
                raise TypeMismatchInStatement(ast)
            
            elif type(lhsType) is not type(rhsType):
                raise TypeMismatchInStatement(ast)
            
            else:
                if type(lhsType) is ArrayType:
                    if len(rhsType.size) > len(lhsType.size):
                            raise TypeMismatchInStatement(ast)
                        
                    if len(rhsType.size) == len(lhsType.size) and rhsType.size != lhsType.size:
                        raise TypeMismatchInStatement(ast)
                    
                    if rhsType.eleType is None:
                        self.resolveType(ast.varInit, lhsType, param)
                        if self.resolved is False:
                            raise TypeCannotBeInferred(ast)
                        
                        rhsType = lhsType

                    if type(rhsType.eleType) is not type(lhsType.eleType) or rhsType.size != lhsType.size:
                        raise TypeMismatchInStatement(ast)
        
        self.arr_ast = []
    
    def visitIf(self, ast: If, param):
        cond_typ = self.visit(ast.expr, param)
        if cond_typ is None:
            if type(ast.expr) in [Id, CallExpr, ArrayLiteral]:
                self.resolveType(ast.expr, BoolType(), param)
                cond_typ = BoolType()
            
            else:
                raise TypeCannotBeInferred(ast)
        
        if type(cond_typ) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.thenStmt, param)
        if self.list_return != [] and self.scope == 1:
            self.list_return = []

        self.has_return = False
        for elifExpr, elif_stmt in ast.elifStmt:
            cond_typ = self.visit(elifExpr, param)
            if cond_typ is None:
                if type(elifExpr) in [Id, CallExpr, ArrayLiteral]:
                    self.resolveType(elifExpr, BoolType(), param)
                    if self.resolved is False:
                        raise TypeCannotBeInferred(ast)
                    
                    cond_typ = BoolType()
                
                else:
                    raise TypeCannotBeInferred(ast)

            if type(cond_typ) is not BoolType:
                raise TypeMismatchInStatement(ast)
            
            self.visit(elif_stmt, param)
            if self.list_return != [] and self.scope == 1:
                self.list_return = []
            
            self.has_return = False
        
        if ast.elseStmt:
            self.visit(ast.elseStmt, param)
        
        self.arr_ast = []
    
    def visitFor(self, ast: For, param):
        self.in_loop += [True]
        scala_typ = self.visit(ast.name, param)
        if scala_typ is None:
            self.resolveType(ast.name, NumberType(), param)
            scala_typ = NumberType()
        
        if type(scala_typ) is not NumberType:
            raise TypeMismatchInStatement(ast)

        cond_typ = self.visit(ast.condExpr, param)
        if cond_typ is None:
            if type(ast.condExpr) in [Id, CallExpr, ArrayLiteral]:
                self.resolveType(ast.condExpr, BoolType(), param)
                cond_typ = BoolType()
                if self.resolved is False:
                    raise TypeCannotBeInferred(ast)
            
            else:
                raise TypeCannotBeInferred(ast)
            
        if type(cond_typ) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        update_typ = self.visit(ast.updExpr, param)
        if update_typ is None:
            if type(ast.updExpr) in [Id, CallExpr, ArrayLiteral]:
                self.resolveType(ast.updExpr, NumberType(), param)
                update_typ = NumberType()
                if self.resolved is False:
                    raise TypeCannotBeInferred(ast)
            
            else:
                raise TypeCannotBeInferred(ast)
            
        if type(update_typ) is not NumberType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.body, param)
        if self.list_return != [] and self.scope == 1:
            self.list_return = []

        self.arr_ast = []
        self.in_loop = self.in_loop[1:]
    
    def visitUnaryOp(self, ast: UnaryOp, param):
        exprType = self.visit(ast.operand, param)
        if ast.op == '-':
            if exprType is None:
                if type(ast.operand) in [Id, CallExpr, ArrayLiteral]:
                    self.resolveType(ast.operand, NumberType(), param)
                    if self.resolved is False:
                        return None
                    
                    else:
                        return NumberType()
                    
                else:
                    return None
            
            else:
                if type(exprType) is not NumberType:
                    raise TypeMismatchInExpression(ast)
                
                else:
                    return NumberType()
        
        else:
            if exprType is None:
                if type(ast.operand) in [Id, CallExpr, ArrayLiteral]:
                    self.resolveType(ast.operand, BoolType(), param)
                    if self.resolved is False:
                        return None
                    
                    else:
                        return BoolType()
                    
                else:
                    return None
            
            else:
                if type(exprType) is not BoolType:
                    raise TypeMismatchInExpression(ast)
                
                else:
                    return BoolType()
    
    def visitBinaryOp(self, ast: BinaryOp, param):
        if ast.op in ['+', '-', '*', '/', '%', '=', '!=', '>', '<', '>=', '<=']:
            expr1 = self.visit(ast.left, param)
            if expr1 is None:
                if type(ast.left) in [Id, CallExpr, ArrayLiteral]:
                    self.resolveType(ast.left, NumberType(), param)
                    expr1 = NumberType()
                    if self.resolved is False:
                        return None
                
                else:
                    return None
            
            expr2 = self.visit(ast.right, param)
            if expr2 is None:
                if type(ast.right) in [Id, CallExpr, ArrayLiteral]:
                    self.resolveType(ast.right, NumberType(), param)
                    expr2 = NumberType()
                    if self.resolved is False:
                        return None
                
                else:
                    return None
            
            if type(expr1) is not NumberType or type(expr2) is not NumberType:
                raise TypeMismatchInExpression(ast)
            
            return NumberType() if ast.op in ['+', '-', '*', '/', '%'] else BoolType()
        
        elif ast.op in ['and', 'or']:
            expr1 = self.visit(ast.left, param)
            if expr1 is None:
                if type(ast.left) in [Id, CallExpr, ArrayLiteral]:
                    self.resolveType(ast.left, BoolType(), param)
                    expr1 = BoolType()
                    if self.resolved is False:
                        return None
                
                else:
                    return None
            
            expr2 = self.visit(ast.right, param)
            if expr2 is None:
                if type(ast.right) in [Id, CallExpr, ArrayLiteral]:
                    self.resolveType(ast.right, BoolType(), param)
                    expr2 = BoolType()
                    if self.resolved is False:
                        return None
                
                else:
                    return None
            
            if type(expr1) is not BoolType or type(expr2) is not BoolType:
                raise TypeMismatchInExpression(ast)
            
            return BoolType()

        else:
            expr1 = self.visit(ast.left, param)
            if expr1 is None:
                if type(ast.left) in [Id, CallExpr, ArrayLiteral]:
                    self.resolveType(ast.left, StringType(), param)
                    expr1 = StringType()
                    if self.resolved is False:
                        return None
                
                else:
                    return None
            
            expr2 = self.visit(ast.right, param)
            if expr2 is None:
                if type(ast.right) in [Id, CallExpr, ArrayLiteral]:
                    self.resolveType(ast.right, StringType(), param)
                    expr2 = StringType()
                    if self.resolved is False:
                        return None

                else:
                    return None
            
            if type(expr1) is not StringType or type(expr2) is not StringType:
                raise TypeMismatchInExpression(ast)
            
            return StringType() if ast.op == '...' else BoolType()
    
    def visitArrayCell(self, ast: ArrayCell, param):
        self.resolved = True
        first = self.visit(ast.arr, param)
        if first is None:
            self.resolved = False
            return None
        
        else:
            if type(first) is not ArrayType:
                raise TypeMismatchInExpression(ast)
            
            else:
                if len(first.size) < len(ast.idx):
                    raise TypeMismatchInExpression(ast)
                
                else:
                    for idx in range(len(ast.idx)):
                        typ = self.visit(ast.idx[idx], param)
                        if typ is None:
                            if type(ast.idx[idx]) in [Id, CallExpr, ArrayLiteral]:
                                self.resolveType(ast.idx[idx], NumberType(), param)
                                if self.resolved is False:
                                    return None
                                
                                else:
                                    typ = NumberType()
                            
                            else:
                                return None
                        
                        if type(typ) is not NumberType:
                            raise TypeMismatchInExpression(ast)
                    
                    return first.eleType if len(first.size) == len(ast.idx) else ArrayType(first.size[len(ast.idx):], first.eleType)
            
    def visitArrayLiteral(self, ast: ArrayLiteral, param):
        self.arr_ast += [ast]
        typ = None
        for val in ast.value:
            typ = self.visit(val, param)
            if typ is not None:
                break

        if typ is not None:
            for idx in range(len(ast.value)):
                val_typ = self.visit(ast.value[idx], param)
                if val_typ is None:
                    if type(ast.value[idx]) in [Id, CallExpr, ArrayLiteral]:
                        self.resolveType(ast.value[idx], typ, param)
                        if self.resolved is False:
                            return None
                        
                        else:
                            val_typ = typ

                    else:
                        return None

                if type(val_typ) is not type(typ):
                    raise TypeMismatchInExpression(self.arr_ast[0])

                else:
                    if type(val_typ) is ArrayType:
                        if len(val_typ.size) == len(typ.size) and val_typ.size != typ.size:
                            raise TypeMismatchInExpression(self.arr_ast[0])
                        
                        if val_typ.eleType is not None:
                            for val in ast.value:
                                valType = self.visit(val, param)
                                if type(valType) is ArrayType and valType.eleType is None:
                                    self.resolveType(val, val_typ, param)
                                    if self.resolved is False:
                                        return None
                        
                            if typ.eleType is None:
                                typ = val_typ
                        
                        else:
                            if typ.eleType is not None:
                                self.resolveType(ast.value[idx], typ, param)
                                if self.resolved is False:
                                    return None
                                
                                val_typ = typ
                            
                            else:
                                if len(typ.size) <= len(val_typ.size) and val_typ.size[:len(typ.size)] == typ.size:
                                    typ = val_typ
                                
                                elif len(typ.size) > len(val_typ.size) and typ.size[:len(val_typ.size)] == val_typ.size:
                                    val_typ = typ
                                
                                else:
                                    raise TypeMismatchInExpression(self.arr_ast[0])
                        
                        if type(val_typ.eleType) is not type(typ.eleType) or val_typ.size != typ.size:
                            raise TypeMismatchInExpression(self.arr_ast[0])
            
            if type(typ) is not ArrayType:
                self.arr_ast = self.arr_ast[:-1]
                return ArrayType([len(ast.value)], typ)
            
            else:
                self.arr_ast = self.arr_ast[:-1]
                return ArrayType([len(ast.value)] + typ.size, typ.eleType)