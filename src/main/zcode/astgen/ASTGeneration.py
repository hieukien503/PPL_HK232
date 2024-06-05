from main.zcode.parser.ZCodeVisitor import ZCodeVisitor
from main.zcode.parser.ZCodeParser import ZCodeParser
from main.zcode.utils.AST import *
from typing import List, Tuple

class ASTGeneration (ZCodeVisitor):
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.decl()])
    
    def visitDecl(self, ctx: ZCodeParser.DeclContext):
        return self.visit(ctx.var_decl()) if ctx.var_decl() else self.visit(ctx.func_decl())
    
    def visitVar_decl(self, ctx: ZCodeParser.Var_declContext):
        name = ctx.ID().getText()
        varType = None if (ctx.VAR() or ctx.DYNAMIC()) else (self.visit(ctx.vartype()) if not ctx.LS() else ArrayType(self.visit(ctx.num_list()), self.visit(ctx.vartype())))
        modifier = "var" if ctx.VAR() else ("dynamic" if ctx.DYNAMIC() else None)
        varInit = None if not ctx.expr() else self.visit(ctx.expr())
        return VarDecl(Id(name), varType, modifier, varInit)
    
    def visitFunc_decl(self, ctx: ZCodeParser.Func_declContext):
        name = ctx.ID().getText()
        params = self.visit(ctx.params()) if ctx.params() else []
        body = self.visit(ctx.return_stmt()) if ctx.return_stmt() else (self.visit(ctx.block_stmt()) if ctx.block_stmt() else None)
        return FuncDecl(Id(name), params, body)

    def visitParams(self, ctx: ZCodeParser.ParamsContext):
        return [self.visit(ctx.param())] + (self.visit(ctx.params()) if ctx.params() else [])
    
    def visitParam(self, ctx: ZCodeParser.ParamContext):
        name = ctx.ID().getText()
        varType = self.visit(ctx.vartype()) if not ctx.LS() else ArrayType(self.visit(ctx.num_list()), self.visit(ctx.vartype()))
        modifier = None
        varInit = None
        return VarDecl(Id(name), varType, modifier, varInit)
    
    def visitVartype(self, ctx: ZCodeParser.VartypeContext):
        return NumberType() if ctx.NUMBER() else (StringType() if ctx.STRING() else BoolType())
    
    def visitAssign_stmt(self, ctx: ZCodeParser.Assign_stmtContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))
    
    def visitLhs(self, ctx: ZCodeParser.LhsContext):
        return Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.elem_array())

    
    def visitIf_stmt(self, ctx: ZCodeParser.If_stmtContext):
        cond_expr = self.visit(ctx.expr(0))
        thenStmt = self.visit(ctx.stmt(0))
        elifStmt: List[Tuple[Expr, Stmt]] = []
        for i in range(1, len(ctx.expr())):
            elifStmt += [(self.visit(ctx.expr(i)), self.visit(ctx.stmt(i)))]
        
        elseStmt = None if len(ctx.stmt()) == len(ctx.expr()) else self.visit(ctx.stmt()[-1])
        return If(cond_expr, thenStmt, elifStmt, elseStmt)
    
    def visitFor_stmt(self, ctx: ZCodeParser.For_stmtContext):
        name = ctx.ID().getText()
        cond_expr = self.visit(ctx.expr(0))
        upd_expr = self.visit(ctx.expr(1))
        stmt = self.visit(ctx.stmt())
        return For(Id(name), cond_expr, upd_expr, stmt)
    
    def visitBreak_stmt(self, ctx: ZCodeParser.Break_stmtContext):
        return Break()
    
    def visitReturn_stmt(self, ctx: ZCodeParser.Return_stmtContext):
        return Return(self.visit(ctx.expr()) if ctx.expr() else None)
    
    def visitContinue_stmt(self, ctx: ZCodeParser.Continue_stmtContext):
        return Continue()
    
    def visitBlock_stmt(self, ctx: ZCodeParser.Block_stmtContext):
        return Block([self.visit(x) for x in ctx.stmt()])
    
    def visitStmt(self, ctx: ZCodeParser.StmtContext):
        return self.visitChildren(ctx)
    
    def visitFunc_call_stmt(self, ctx: ZCodeParser.Func_call_stmtContext):
        return CallStmt(Id(ctx.ID().getText()), self.visit(ctx.expr_list()) if ctx.expr_list() else [])
    
    def visitExpr_list(self, ctx: ZCodeParser.Expr_listContext):
        return [self.visit(x) for x in ctx.expr()]
    
    def visitNum_list(self, ctx: ZCodeParser.Num_listContext):
        return [float(ctx.NUM_LIT().getText())] + (self.visit(ctx.num_list()) if ctx.num_list() else [])
    
    def visitExpr(self, ctx: ZCodeParser.ExprContext):
        return BinaryOp(ctx.CONCAT().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1))) if ctx.CONCAT() else self.visitChildren(ctx)
    
    def visitExpr1(self, ctx: ZCodeParser.Expr1Context):
        op = ctx.EQ().getText() if ctx.EQ() else (
            ctx.NOT_EQ().getText() if ctx.NOT_EQ() else (
                ctx.LT().getText() if ctx.LT() else (
                    ctx.LTE().getText() if ctx.LTE() else (
                        ctx.GT().getText() if ctx.GT() else (
                            ctx.GTE().getText() if ctx.GTE() else (
                                ctx.STR_EQ().getText() if ctx.STR_EQ() else None
                            )
                        )
                    )
                )
            )
        )

        return BinaryOp(op, self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1))) if op else self.visitChildren(ctx)
    
    def visitExpr2(self, ctx: ZCodeParser.Expr2Context):
        op = ctx.AND().getText() if ctx.AND() else (ctx.OR().getText() if ctx.OR() else None)
        return BinaryOp(op, self.visit(ctx.expr2()), self.visit(ctx.expr3())) if op else self.visit(ctx.expr3())
    
    def visitExpr3(self, ctx: ZCodeParser.Expr3Context):
        op = ctx.ADD().getText() if ctx.ADD() else (ctx.SUB().getText() if ctx.SUB() else None)
        return BinaryOp(op, self.visit(ctx.expr3()), self.visit(ctx.expr4())) if op else self.visit(ctx.expr4())
    
    def visitExpr4(self, ctx: ZCodeParser.Expr4Context):
        op = ctx.MUL().getText() if ctx.MUL() else (
            ctx.DIV().getText() if ctx.DIV() else (
                ctx.MOD().getText() if ctx.MOD() else None
            )
        )
        return BinaryOp(op, self.visit(ctx.expr4()), self.visit(ctx.expr5())) if op else self.visit(ctx.expr5())
    
    def visitExpr5(self, ctx: ZCodeParser.Expr5Context):
        return UnaryOp(ctx.NOT().getText(), self.visit(ctx.expr5())) if ctx.NOT() else self.visit(ctx.expr6())
    
    def visitExpr6(self, ctx: ZCodeParser.Expr6Context):
        op = ctx.ADD().getText() if ctx.ADD() else (ctx.SUB().getText() if ctx.SUB() else None)
        return UnaryOp(op, self.visit(ctx.expr6())) if op else self.visit(ctx.expr7())
    
    def visitExpr7(self, ctx: ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)
    
    def visitArray_cell(self, ctx: ZCodeParser.Array_cellContext):
        return ArrayCell(Id(ctx.ID().getText()) if ctx.ID() else self.visitFunc_call(ctx.func_call()), 
                         self.visit(ctx.expr_list()))
    
    def visitFunc_call(self, ctx: ZCodeParser.Func_callContext):
        return CallExpr(Id(ctx.ID().getText()), [] if not ctx.expr_list() else self.visit(ctx.expr_list()))
    
    def visitArray_lit(self, ctx: ZCodeParser.Array_litContext):
        return ArrayLiteral(self.visit(ctx.expr_list()))
    
    def visitLiterals(self, ctx: ZCodeParser.LiteralsContext):
        return NumberLiteral(float(ctx.NUM_LIT().getText())) if ctx.NUM_LIT() else (
            StringLiteral(ctx.STR_LIT().getText()) if ctx.STR_LIT() else (
                BooleanLiteral(True if ctx.TRUE() else False) if ctx.TRUE() or ctx.FALSE() else self.visit(ctx.array_lit())
            )
        )
    
    def visitOperands(self, ctx: ZCodeParser.OperandsContext):
        return Id(ctx.ID().getText()) if ctx.ID() else (
            self.visit(ctx.expr()) if ctx.expr() else  (
                self.visit(ctx.literals()) if ctx.literals() else self.visit(ctx.func_call())
            )
        )
    
    def visitElem_array(self, ctx: ZCodeParser.Elem_arrayContext):
        return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.expr_list()))