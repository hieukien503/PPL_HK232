from Emitter import Emitter

from Frame import Frame
from abc import ABC
from main.zcode.utils.Visitor import *
from main.zcode.utils.AST import *
from main.zcode.utils.Utils import *
from typing import List

from CodeGenError import *

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value
    
    def __repr__(self) -> str:
        return f"Symbol(Name: {self.name}, Return Type: {self.mtype.rettype if type(self.mtype) is MType else self.mtype})"

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [[
            Symbol("readNumber", MType([], NumberType()), CName(self.libName)),
            Symbol("writeNumber", MType([NumberType()], VoidType()), CName(self.libName)),
            Symbol("readBool", MType([], BoolType()), CName(self.libName)),
            Symbol("writeBool", MType([BoolType()], VoidType()), CName(self.libName)),
            Symbol("readString", MType([], StringType()), CName(self.libName)),
            Symbol("writeString", MType([StringType()], VoidType()), CName(self.libName))
        ]]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)

class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        self.value = value

class CName(Val):
    def __init__(self, value):
        self.value = value

class ClassType(Type):
    def __init__(self, name):
        self.name = name

class CodeGenVisitor(Visitor, Utils):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.className = 'ZCodeClass'
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.clinit = None
        self.funcType = "undefined"
        self.has_return = False
        self.buffer: List[List[str]] = [[]]
        self.dynamic: List[List[VarDecl]] = [[]]
        self.varDecl_init = []
        self.hasUpdate = False
        self.func_name = ""
    
    def defaultValue(self, typ_):
        varType = type(typ_)
        if varType is NumberType:
            return NumberLiteral(0.0)
        
        elif varType is StringType:
            return StringLiteral("")
        
        elif varType is BoolType:
            return BooleanLiteral(False)
        
        else:
            expr = []
            if len(typ_.size) == 1:
                for x in range(int(typ_.size[0])):
                    expr += [self.defaultValue(typ_.eleType)]

                return ArrayLiteral(expr)
            else:
                dimen = typ_.size
                for x in range(int(dimen[0])):
                    temp = self.defaultValue(ArrayType(dimen[1:], typ_.eleType))
                    expr += [temp]

                return ArrayLiteral(expr)

    def updateType(self, name: str, typ_, sym): # Update unknown type for variable and function
        for idx1 in range(len(sym)):
            flag = False
            for idx2 in range(len(sym[idx1])):
                if sym[idx1][idx2].name == name:
                    if sym[idx1][idx2].mtype is None:
                        sym[idx1][idx2].mtype = typ_
                    
                    else:
                        sym[idx1][idx2].mtype = MType(sym[idx1][idx2].mtype.partype, typ_)
                    
                    flag = True
                    break

            if flag:
                break
    
    def updateArrayLiteral(self, expr: ArrayLiteral, typ_: ArrayType, o):
        for val in expr.value:
            if type(val) is Id:
                rt = typ_.eleType if len(typ_.size) == 1 else ArrayType(typ_.size[1:], typ_.eleType)
                self.updateType(val.name, rt, o.sym)
                self.update(val, typ_.eleType, self.defaultValue(rt), o)
            
            elif type(val) is ArrayLiteral:
                self.updateArrayLiteral(val, ArrayType(typ_.size[1:], typ_.eleType), o)
    
    def update(self, name: Id, typ_: Type, varInit: Expr, o) -> None:
        for idx1 in range(len(self.dynamic) - 1, -1, -1):
            for idx2 in range(len(self.dynamic[idx1])):
                if self.dynamic[idx1][idx2].name.name == name.name:
                    self.hasUpdate = True
                    o.sym[0] += [self.visit(VarDecl(name, typ_, None, varInit), o if idx1 > 0 else SubBody(None, o.sym))]
                    self.hasUpdate = False
                    self.dynamic[idx1].pop(idx2)
                    return

    def visitProgram(self, ast: Program, o):
        self.buffer[-1].append(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        func_decl = []
        declList = []
        for decl in ast.decl:
            if isinstance(decl, FuncDecl) and decl.body is None:
                func_decl += [decl]
            
            elif isinstance(decl, FuncDecl) and decl.body is not None:
                flag = False
                for idx in range(len(func_decl)):
                    if func_decl[idx].name == decl.name:
                        func_decl[idx] = decl
                        flag = True
                        break
                
                if not flag:
                    func_decl += [decl]

                e.sym[0] += [Symbol(decl.name.name, MType(list(map(lambda x: x.varType, decl.param)), None), CName(self.className))]
            
            else:
                if decl.varInit is not None:
                    self.varDecl_init += [Assign(decl.name, decl.varInit)]
                
                declList += [decl]
        
        for decl in declList:
            e.sym[0] += [self.visit(decl, e)]
        
        self.genMETHOD(FuncDecl(Id("<init>"), [], Block([])), e, Frame("<init>", VoidType()))

        
        for func in func_decl:
            self.visit(func, e)

        if self.varDecl_init != []:
            self.clinit = "<clinit>"
            self.genMETHOD(FuncDecl(Id("<clinit>"), [], Block(self.varDecl_init)), e, Frame("<clinit>", VoidType()))
            self.clinit = None
        
        self.emit.buff = [element for sublist in self.buffer for element in sublist]
        self.emit.emitEPILOG()
        
    def genMETHOD(self, ast: FuncDecl, o, frame):  # Use if we know the return type of function
        method_name = ast.name.name
        isInit = method_name == "<init>"
        isMain = method_name == "main" and len(ast.param) == 0
        intype = [ArrayType([], StringType())] if isMain else list(map(lambda x: x.varType, ast.param))
        frame.enterScope(True)

        if isInit:
            self.buffer[-1].append(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
            o.sym = [[]] + o.sym
        
        elif isMain:
            self.buffer[-1].append(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
            o.sym = [[Symbol("args", ArrayType([], StringType()), Index(frame.currIndex - 1))]] + o.sym
        
        else:
            o.sym = [[]] + o.sym
            for param in ast.param:
                idx = frame.getNewIndex()
                o.sym[0] += [Symbol(param.name.name, param.varType, Index(idx))]
                self.buffer[-1].append(self.emit.emitVAR(idx, param.name.name, param.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
        
        self.buffer[-1].append(self.emit.emitLABEL(frame.getStartLabel(), frame))

        if isInit:
            self.buffer[-1].append(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.buffer[-1].append(self.emit.emitINVOKESPECIAL(frame))
        
        self.visit(ast.body, SubBody(frame, o.sym))
        self.buffer[-1].append(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if not self.has_return:
            self.buffer[-1].append(self.emit.emitRETURN(VoidType(), frame))

        self.buffer[-1].append(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

        rettype = self.funcType if type(self.funcType) is not str else frame.returnType
        if isMain or isInit or len(ast.param) > 0:
            for idx in range(len(self.buffer[-1]) - 1, -1, -1):
                if self.buffer[-1][idx].find(".var 0") != -1:
                    self.buffer[-1].insert(idx, self.emit.emitMETHOD(method_name, MType(intype, rettype), not isInit, frame))
                    break
        
        else:
            for idx in range(len(self.buffer[-1]) - 1, -1, -1):
                if self.buffer[-1][idx] == "Label0:\n":
                    self.buffer[-1].insert(idx, self.emit.emitMETHOD(method_name, MType(intype, rettype), not isInit, frame))
                    break


        self.has_return = False
        self.funcType = "undefinied"
        o.sym = o.sym[1:]

    def visitFuncDecl(self, ast: FuncDecl, o):
        if ast.name.name in ["<clinit>", "<init>", "main"]:
            self.genMETHOD(ast, o, Frame(ast.name.name, VoidType()))
        
        else:
            self.func_name = ast.name.name
            if type(ast.body) is Return:
                if ast.body.expr is None:
                    self.funcType = VoidType()
                
                else:
                    self.funcType = self.visit(ast.body.expr, Access(Frame(ast.name.name, None), o.sym, False))[1]

            self.updateType(ast.name.name, self.funcType, o.sym)
            frame = Frame(ast.name.name, self.funcType)
            self.genMETHOD(FuncDecl(ast.name, ast.param, ast.body), o, frame)

    def visitVarDecl(self, ast: VarDecl, o):
        for idx in range(len(o.sym[0])):
            if o.sym[0][idx].name == ast.name.name:
                o.sym[0].pop(idx)
                break

        if ast.varType is None and ast.varInit is None:
            self.dynamic[-1].append(ast)
            if o.frame is None:
                return Symbol(ast.name.name, ast.varType, CName(self.className))
            else:
                o.frame.currIndex -= 1
                sym = Symbol(ast.name.name, ast.varType, Index(o.frame.currIndex + 1))
                o.frame.getNewIndex()
                return sym
        
        buffIdx = -1
        if self.hasUpdate is True:
            for idx in range(len(self.dynamic) - 1, -1, -1):
                if self.lookup(ast.name.name, self.dynamic[idx], lambda x: x.name.name) is None:
                    buffIdx = -1
                
                else:
                    buffIdx = idx
                    break

        if o.frame is None:
            frame = Frame(ast.name.name, ast.varType)
            if ast.varInit is None:
                code = self.emit.emitATTRIBUTE(ast.name.name, ast.varType, False, CName(self.className))
                if buffIdx == 0:
                    for idx in range(len(self.buffer[buffIdx])):
                        if self.buffer[buffIdx][idx].find('.super java.lang.Object') != -1:
                            self.buffer[buffIdx].insert(idx + 1, code)
                            break
                
                else:
                    self.buffer[buffIdx] = [code] + self.buffer[buffIdx] if buffIdx != -1 else self.buffer[-1] + [code]

                return Symbol(ast.name.name, ast.varType, CName(self.className))
            
            else:
                init, rt = self.visit(ast.varInit, SubBody(frame, o.sym))
                if rt is None:
                    if type(ast.varInit) is not ArrayLiteral:
                        self.update(ast.varInit, ast.varType, self.defaultValue(ast.varType), o)
                        self.updateType(ast.varInit.name, ast.varType, o.sym)
                    
                    else:
                        self.updateArrayLiteral(ast.varInit, ast.varType, o)
                    
                    rt = ast.varType

                code = self.emit.emitATTRIBUTE(ast.name.name, rt, False, CName(self.className))
                if buffIdx == 0:
                    for idx in range(len(self.buffer[buffIdx])):
                        self.varDecl_init.append(ast)
                        if self.buffer[buffIdx][idx].find('.super java.lang.Object') != -1:
                            self.buffer[buffIdx].insert(idx + 1, code)
                            break
                
                else:
                    self.buffer[buffIdx] = [code] + self.buffer[buffIdx] if buffIdx != -1 else self.buffer[-1] + [code]

                return Symbol(ast.name.name, rt, CName(self.className))
            
        else:
            if ast.varInit is None:
                return self.visit(VarDecl(ast.name, ast.varType, None, self.defaultValue(ast.varType)), o)
                
            else:
                varIdx = o.frame.getNewIndex()
                init, rt = self.visit(ast.varInit, o)
                init = init + self.emit.emitALOAD(rt, o.frame) if type(ast.varInit) is ArrayCell else init
                if rt is None:
                    if type(ast.varInit) is not ArrayLiteral:
                        self.updateType(ast.varInit.name, ast.varType, o.sym)
                        self.update(ast.varInit, ast.varType, self.defaultValue(ast.varType), o)
                    
                    else:
                        self.updateArrayLiteral(ast.varInit, ast.varType, o)
                    
                    init = self.visit(ast.varInit, Access(o.frame, o.sym, False))[0]
                    rt = ast.varType

                code = self.emit.emitVAR(varIdx, ast.name.name, rt, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame) + init + self.emit.emitWRITEVAR(ast.name.name, rt, varIdx, o.frame)
                if buffIdx == 0:
                    self.varDecl_init.append(ast)
                    for idx in range(len(self.buffer[buffIdx])):
                        if self.buffer[buffIdx][idx].find('.super java.lang.Object') != -1:
                            self.buffer[buffIdx].insert(idx + 1, code)
                            break
                
                else:
                    self.buffer[-1].append(code)
                    
                return Symbol(ast.name.name, rt, Index(varIdx))
    
    def visitNumberLiteral(self, ast, o):
        if type(o) is Frame:
            return self.emit.emitPUSHFCONST(str(ast.value), o), NumberType()
        
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), NumberType()
    
    def visitStringLiteral(self, ast, o):
        if type(o) is Frame:
            return self.emit.emitPUSHCONST("\"" + ast.value + "\"", StringType(), o), StringType()
        
        return self.emit.emitPUSHCONST("\"" + ast.value + "\"", StringType(), o.frame), StringType()

    def visitBooleanLiteral(self, ast, o):
        if type(o) is Frame:
            return self.emit.emitPUSHICONST(str(ast.value).lower(), o), BoolType()
        
        return self.emit.emitPUSHICONST(str(ast.value).lower(), o.frame), BoolType()
    
    def visitBinaryOp(self, ast, o):
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)

        if ast.op == "...":
            if type(ast.left) is StringLiteral and type(ast.right) is StringLiteral:
                o.frame.pop()
                o.frame.pop()
                return self.visit(StringLiteral(ast.left.value + ast.right.value), o)
            
            else:
                e1val, e2val = None, None
                if e1t is None:
                    e1val = StringLiteral("")
                    self.updateType(ast.left.name, StringType(), o.sym)
                    self.update(ast.left, StringType(), e1val, o)
                
                if e2t is None:
                    e2val = StringLiteral("")
                    self.updateType(ast.right.name, StringType(), o.sym)
                    self.update(ast.right, StringType(), e2val, o)
                
                if e1val is not None and e2val is None:
                    return self.visit(BinaryOp(ast.op, e1val, ast.right))

                elif e2val is not None and e1val is None:
                    return self.visit(BinaryOp(ast.op, ast.left, e2val))
                
                else:
                    code1 = e1c + ("" if type(ast.left) is not ArrayCell else self.emit.emitALOAD(e1t, o.frame))
                    code2 = e2c + ("" if type(ast.right) is not ArrayCell else self.emit.emitALOAD(e2t, o.frame))
                    code = code1 + code2 + "\tinvokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;\n"
                    return code, StringType()
            
        elif ast.op == "==":
            if type(ast.left) is StringLiteral and type(ast.right) is StringLiteral:
                o.frame.pop()
                o.frame.pop()
                return self.visit(BooleanLiteral(ast.left.value == ast.right.value), o)
            
            else:
                e1val, e2val = None, None
                if e1t is None:
                    e1val = StringLiteral("")
                    self.updateType(ast.left.name, StringType(), o.sym)
                    self.update(ast.left, StringType(), e1val, o)
                
                if e2t is None:
                    e2val = StringLiteral("")
                    self.updateType(ast.right.name, StringType(), o.sym)
                    self.update(ast.right, StringType(), e2val, o)
                
                if e1val is not None and e2val is None:
                    return self.visit(BinaryOp(ast.op, e1val, ast.right))

                elif e2val is not None and e1val is None:
                    return self.visit(BinaryOp(ast.op, ast.left, e2val))
                
                else:
                    code1 = e1c + ("" if type(ast.left) is not ArrayCell else self.emit.emitALOAD(e1t, o.frame))
                    code2 = e2c + ("" if type(ast.right) is not ArrayCell else self.emit.emitALOAD(e2t, o.frame))
                    code = code1 + code2 + "\tinvokevirtual java/lang/String/equals(Ljava/lang/Object;)Z\n"
                    return code, BoolType()
            
        
        else:
            e1val, e2val = None, None
            if e1t is None:
                if ast.op in ['+', '-', '*', '/', '%', '>', '<', '>=', '<=', '=', '!=']:
                    e1val = self.defaultValue(NumberType())
                    self.updateType(ast.left.name, NumberType(), o.sym)
                    self.update(ast.left, NumberType(), e1val, o)
                
                else:
                    e1val = self.defaultValue(BoolType())
                    self.updateType(ast.left.name, BoolType(), o.sym)
                    self.update(ast.left, BoolType(), e1val, o)
                
            
            if e2t is None:
                if ast.op in ['+', '-', '*', '/', '%', '>', '<', '>=', '<=', '=', '!=']:
                    e2val = self.defaultValue(NumberType())
                    self.updateType(ast.right.name, NumberType(), o.sym)
                    self.update(ast.right, NumberType(), e2val, o)
                
                else:
                    e2val = self.defaultValue(BoolType())
                    self.updateType(ast.right.name, BoolType(), o.sym)
                    self.update(ast.right, BoolType(), e2val, o)
            
            if e1val is not None and e2val is None:
                return self.visit(BinaryOp(ast.op, e1val, ast.right))

            elif e2val is not None and e1val is None:
                return self.visit(BinaryOp(ast.op, ast.left, e2val))
            
            else:
                code1 = e1c + ("" if type(ast.left) is not ArrayCell else self.emit.emitALOAD(e1t, o.frame))
                code2 = e2c + ("" if type(ast.right) is not ArrayCell else self.emit.emitALOAD(e2t, o.frame))
                if ast.op in ['+', '-']:
                    return code1 + code2 + self.emit.emitADDOP(ast.op, e1t, o.frame), e1t
                
                elif ast.op in ['*', '/']:
                    return code1 + code2 + self.emit.emitMULOP(ast.op, e1t, o.frame), e1t
                
                elif ast.op in ['<', '>', '<=', '>=', '!=', '=']:
                    return code1 + code2 + self.emit.emitREOP("==" if ast.op == '=' else ast.op, e1t, o.frame), BoolType()
                
                elif ast.op == 'and':
                    label1 = o.frame.getNewLabel()
                    label2 = o.frame.getNewLabel()
                    code1 = code1 + self.emit.emitIFTRUE(label1, o.frame) + self.emit.emitPUSHICONST(0, o.frame) + self.emit.emitGOTO(label2, o.frame)
                    code2 = self.emit.emitLABEL(label1, o.frame) + code2 + self.emit.emitLABEL(label2, o.frame)
                    return code1 + code2, BoolType()
                
                elif ast.op == 'or':
                    label1 = o.frame.getNewLabel()
                    label2 = o.frame.getNewLabel()
                    code1 = code1 + self.emit.emitIFFALSE(label1, o.frame) + self.emit.emitPUSHICONST(1, o.frame) + self.emit.emitGOTO(label2, o.frame)
                    code2 = self.emit.emitLABEL(label1, o.frame) + code2 + self.emit.emitLABEL(label2, o.frame)
                    return code1 + code2, BoolType()
                
                elif ast.op == '%':
                    code = code1 + code2 + self.emit.emitFMOD(o.frame)
                    return code, NumberType()
                    """
                    code = code1 + code2 + self.emit.emitMULOP('/', e1t, o.frame) + self.emit.emitI2F(o.frame) + self.emit.emitF2I(o.frame) + self.emit.emitMULOP('*', e1t, o.frame) + self.emit.emitADDOP('-', e1t, o.frame)
                    return code1 + code2 + code, NumberType()
                    """
    
    def visitUnaryOp(self, ast, o):
        bodyCode, bodyType = self.visit(ast.operand, o)
        bodyCode += ("" if type(ast.operand) is not ArrayCell else self.emit.emitALOAD(bodyType, o.frame))
        if ast.op == 'not':
            if bodyType is None:
                self.updateType(ast.operand.name, BoolType(), o.sym)
                self.update(ast.operand, BoolType(), BooleanLiteral(False), o)
                return self.visit(UnaryOp(ast.op, BooleanLiteral(False)))
            
            return bodyCode + self.emit.emitNOT(bodyType, o.frame), bodyType
        
        else:
            if bodyType is None:
                self.updateType(ast.operand.name, NumberType(), o.sym)
                self.update(ast.operand, NumberType(), NumberLiteral(0.0), o)
                return self.visit(UnaryOp(ast.op, NumberLiteral(0.0)))
            
            return bodyCode + self.emit.emitNEGOP(bodyType, o.frame), bodyType
    
    def visitBreak(self, ast, o):
        self.buffer[-1].append(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))

    def visitContinue(self, ast, o):
        self.buffer[-1].append(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))
    
    def visitReturn(self, ast, o):
        self.has_return = True
        if ast.expr is None:
            self.buffer[-1].append(self.emit.emitRETURN(VoidType(), o.frame))
            self.funcType = VoidType()

        else:
            expcode, exptype = self.visit(ast.expr, Access(o.frame, o.sym, False))
            if exptype is None:
                self.updateType(ast.expr.name, self.funcType, o.sym)
                self.update(ast.expr, self.funcType, self.defaultValue(self.funcType), o)
                expcode = self.visit(self.defaultValue(self.funcType), Access(o.frame, o.sym, False))[0]
            
            else:
                self.funcType = exptype
            
            if type(ast.expr) is ArrayCell:
                expcode += self.emit.emitALOAD(exptype, o.frame)

            self.buffer[-1].append(expcode + self.emit.emitRETURN(exptype, o.frame))
        
        for idx in range(len(o.sym[-1])):
            if o.sym[-1][idx].name == self.func_name:
                o.sym[-1][idx].mtype.rettype = self.funcType
                break

    
    def visitIf(self, ast: If, o):
        if_exprCode, if_exprType = self.visit(ast.expr, Access(o.frame, o.sym, False))
        if if_exprType is None:
            self.updateType(ast.expr.name, BoolType(), o.sym)
            self.update(ast.expr, BoolType(), BooleanLiteral(False), o)
            if_exprCode = self.visit(BooleanLiteral(False), o)[0]

        self.buffer[-1].append(if_exprCode)
        labelElif = o.frame.getNewLabel()
        labelElse = o.frame.getNewLabel()
        labelExit = o.frame.getNewLabel()
        self.buffer[-1].append(self.emit.emitIFFALSE(labelElif if ast.elifStmt != [] else (labelElse if ast.elseStmt is not None else labelExit), o.frame))
        self.visit(ast.thenStmt, o)
        self.buffer[-1].append(self.emit.emitGOTO(labelExit, o.frame) if ast.elseStmt else "")

        if ast.elifStmt != []:
            for idx in range(len(ast.elifStmt)):
                stmt = ast.elifStmt[idx]
                self.buffer[-1].append(self.emit.emitLABEL(labelElif, o.frame))
                labelElif = o.frame.getNewLabel() if idx != len(ast.elifStmt) - 1 else (labelElse if ast.elseStmt is not None else labelExit)
                if_exprCode, if_exprType = self.visit(stmt[0], Access(o.frame, o.sym, False))
                if if_exprType is None:
                    self.updateType(stmt[0].name, BoolType(), o.sym)
                    self.update(stmt[0], BoolType(), BooleanLiteral(False), o)
                    if_exprCode = self.visit(BooleanLiteral(False), Access(o.frame, o.sym, False))[0]
                
                self.buffer[-1].append(if_exprCode)
                self.buffer[-1].append(self.emit.emitIFFALSE(labelElif, o.frame))
                self.visit(stmt[1], o)
                self.buffer[-1].append(self.emit.emitGOTO(labelExit, o.frame))
        
        if ast.elseStmt is not None:
            self.buffer[-1].append(self.emit.emitLABEL(labelElse, o.frame))
            self.visit(ast.elseStmt, o)
        
        self.buffer[-1].append(self.emit.emitLABEL(labelExit, o.frame))

    def visitFor(self, ast: For, o):
        frame = o.frame
        code, typ = self.visit(ast.name, o)
        if typ is None:
            self.updateType(ast.name, NumberType(), o.sym)
            self.update(ast.name, NumberType(), NumberLiteral(0.0), o)
            self.visit(VarDecl(ast.name, NumberType(), None, NumberLiteral(0.0)), o)
        
        self.buffer[-1].append(code)
        exp, exptype = self.visit(ast.condExpr, o)
        if exptype is None:
            self.updateType(ast.condExpr.name, BoolType(), o.sym)
            self.update(ast.condExpr, BoolType(), BooleanLiteral(False), o)
            exp = self.visit(BooleanLiteral(False), o)[0]

        frame.enterLoop()
        label1 = frame.getContinueLabel()
        label2 = frame.getBreakLabel()
        label3 = frame.getNewLabel()
        # o.frame.conLabel += [frame.getNewLabel()]
        self.buffer[-1].append(self.emit.emitLABEL(label3, frame))
        self.buffer[-1].append(exp)
        self.buffer[-1].append(self.emit.emitIFTRUE(label2, frame))
        self.visit(ast.body, o)
        self.buffer[-1].append(self.emit.emitLABEL(label1, frame))
        self.visit(Assign(ast.name, BinaryOp('+', ast.name, ast.updExpr)), o)
        self.buffer[-1].append(self.emit.emitGOTO(label3, frame))
        self.buffer[-1].append(self.emit.emitLABEL(label2, frame))
        frame.exitLoop()
        for sublist in o.sym:
            sym = self.lookup(ast.name.name, sublist, lambda x: x.name)
            if sym is not None:
                if type(sym.value) is CName:
                    self.buffer[-1].append(self.emit.emitPUTSTATIC(sym.value.value + "." + sym.name, sym.mtype, frame))
                
                else:
                    self.buffer[-1].append(self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, frame))
                
                break
    
    def visitBlock(self, ast: Block, o):
        self.buffer.append([])
        self.dynamic.append([])
        self.has_return = False
        glenv = SubBody(o.frame, [[]] + o.sym)
        for stmt in ast.stmt:
            if type(stmt) is VarDecl:
                glenv.sym[0] += [self.visit(stmt, glenv)]

            else:
                self.visit(stmt, glenv)
        
        for idx in range(len(o.sym[-1])):
            if o.sym[-1][idx].name == self.func_name and not self.has_return:
                self.funcType = VoidType()
                o.sym[-1][idx].mtype.rettype = VoidType()
                break

        self.buffer[-2].extend(self.buffer[-1])
        self.buffer.pop()
        self.dynamic.pop()
    
    def visitAssign(self, ast: Assign, o):
        frame = o.frame
        frame.push()
        frame.push()
        rhsCode, rhsType = self.visit(ast.rhs, Access(o.frame, o.sym, False))
        lhsCode, lhsType = self.visit(ast.lhs, Access(o.frame, o.sym, True))

        if rhsType is None:
            self.updateType(ast.rhs.name, lhsType, o.sym)
            self.update(ast.rhs, lhsType, self.defaultValue(lhsType), o)
            return
        
        elif lhsType is None:
            self.updateType(ast.lhs.name, rhsType, o.sym)
            self.update(ast.lhs, rhsType, ast.rhs, o)
            lhsType = rhsType
            return

        if type(ast.rhs) is ArrayCell:
            rhsCode += self.emit.emitALOAD(rhsType, frame)

        self.buffer[-1].append(rhsCode + lhsCode) if type(ast.lhs) is not ArrayCell else self.buffer[-1].append(lhsCode + rhsCode + self.emit.emitASTORE(lhsType, frame))
        frame.pop()
        frame.pop()

    def visitId(self, ast: Id, o):
        sym = None
        for x in o.sym:
            flag = False
            for y in x:
                if y.name == ast.name:
                    sym = y
                    flag = True
                    break

            if flag is True:
                break
        
        _type = sym.mtype
        if _type is None:
            return "", None
        
        if not isinstance(sym.value, Index):
            if isinstance(o, Access) and o.isLeft is True:
                return self.emit.emitPUTSTATIC(sym.value.value + "." + sym.name, _type, o.frame), sym.mtype
            
            else:
                return self.emit.emitGETSTATIC(sym.value.value + "." + sym.name, _type, o.frame), sym.mtype
            
        else:
            if isinstance(o, Access) and o.isLeft is True:
                return self.emit.emitWRITEVAR(sym.name, _type, sym.value.value, o.frame), sym.mtype
            
            else:
                return self.emit.emitREADVAR(sym.name, _type, sym.value.value, o.frame), sym.mtype
    
    def visitCallExpr(self, ast: CallExpr, o):
        frame = o.frame
        nenv = o.sym[-1]
        sym = None
        for x in range(len(nenv)):
            if nenv[x].name == ast.name.name:
                sym = nenv[x]

        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())
        
        for x in range(len(ast.args)):
            str1, typ1 = self.visit(ast.args[x], Access(frame, o.sym, False, True))
            if type(ast.args[x]) is ArrayCell:
                str1 += self.emit.emitALOAD(typ1, frame)

            temp = in_[1] + [typ1]
            in_ = (in_[0] + str1, in_[1] + temp)

        return in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + ast.name.name, ctype, frame), ctype.rettype
    
    def visitCallStmt(self, ast: CallStmt, o):
        func_name = ast.name.name
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym[-1]
        sym = next(filter(lambda x: ast.name.name == x.name, nenv), None)
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())

        for x in range(len(ast.args)):
            str1, typ1 = self.visit(ast.args[x], Access(frame, o.sym, False, True))
            if type(ast.args[x]) is ArrayCell:
                str1 += self.emit.emitALOAD(typ1, frame)

            temp = in_[1] + [typ1]
            in_ = (in_[0] + str1, in_[1] + temp)
        
        self.buffer[-1].append(in_[0])
        self.buffer[-1].append(self.emit.emitINVOKESTATIC(cname + "/" + func_name, ctype, frame))
    
    def visitNumberType(self, ast, param):
        pass

    def visitStringType(self, ast, param):
        pass

    def visitBoolType(self, ast, param):
        pass

    def visitArrayType(self, ast, param):
        pass
    
    def visitArrayLiteral(self, ast: ArrayLiteral, o):
        frame = o.frame if type(o) is not Frame else o
        code = self.emit.emitPUSHCONST(str(len(ast.value)), NumberType(), frame)
        typ = None
        for val in ast.value:
            typ = self.visit(val, o)[1]
            if typ is not None:
                break
        
        if typ is None:
            return "", None
        
        targetType = ArrayType([len(ast.value)] + ([] if type(typ) is not ArrayType else typ.size), typ if type(typ) is not ArrayType else typ.eleType)
        for idx in range(len(ast.value)):
            val = ast.value[idx]
            if type(val) is not ArrayLiteral:
                rc, rt = self.visit(val, o)
                if rt is None:
                    rt = ArrayType(targetType.size[1:], targetType.eleType) if len(targetType.size) > 1 else targetType.eleType
                    self.updateType(val.name, rt, o.sym)
                    self.update(val, rt, self.defaultValue(rt), o)
                    rc = self.visit(self.defaultValue(rt), o)[0]
                
                code += (self.emit.emitANEWARRAY(rt, frame) if type(rt) in [ArrayType, StringType] else self.emit.emitNEWARRAY(rt, frame)) if idx == 0 else ""
                code += self.emit.emitDUP(frame) + self.emit.emitPUSHCONST(str(idx), NumberType(), frame) + rc + self.emit.emitASTORE(rt, frame)
            
            else:
                rc, rt = self.visit(val, o)
                if rt is None:
                    rt = ArrayType(targetType.size[1:], targetType.eleType) if len(targetType.size) > 1 else targetType.eleType
                    self.updateArrayLiteral(val, rt, o)
                    rc = self.visit(val, o)[0]

                code += self.emit.emitANEWARRAY(rt, frame) if idx == 0 else ""
                code += self.emit.emitDUP(frame) + self.emit.emitPUSHCONST(str(idx), NumberType(), frame) + rc + self.emit.emitASTORE(rt, frame)
            
        return code, targetType
            
    def visitArrayCell(self, ast: ArrayCell, o):
        frame = o.frame
        code, rt = self.visit(ast.arr, Access(o.frame, o.sym, False))
        sym = None
        if type(ast.arr) is CallExpr:
            for symbol in o.sym[-1]:
                if symbol.name == ast.arr.name.name:
                    sym = symbol
                    break
        
        else:
            flag = False
            for sym1 in o.sym:
                for sym2 in sym1:
                    if sym2.name == ast.arr.name:
                        sym = sym2
                        flag = True
                        break
                
                if flag:
                    break
        
        _type = sym.mtype if type(ast.arr) is Id else sym.mtype.rettype
        dimension = _type.size
        for x in range(len(ast.idx)):
            dimension = dimension[1:]
            e1c, e1t = self.visit(ast.idx[x], Access(frame, o.sym, False, False))
            code += e1c + self.emit.emitF2I(o.frame)

            if x < len(ast.idx) - 1:
                code += self.emit.emitALOAD(ArrayType(dimension, _type.eleType), o.frame)

        if dimension == []:
            return code, _type.eleType
        
        else:
            return code, ArrayType(dimension, _type.eleType)