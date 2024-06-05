import os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener
import subprocess

from main.zcode.parser.ZCodeLexer import ZCodeLexer as LexerSol
from main.zcode.parser.ZCodeParser import ZCodeParser as ParserSol
from lexererr import *
from main.zcode.checker.StaticChecker import StaticChecker
from main.zcode.checker.StaticError import *

TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"
JASMIN_JAR = "./external/jasmin.jar"
from main.zcode2.parser.ZCodeLexer import ZCodeLexer as LexerTest
from main.zcode2.parser.ZCodeParser import ZCodeParser as ParserTest
from main.zcode.codegen.CodeGenerator import CodeGenerator

def writeToFile(num: int, line: str, expect: str, error: str = None) -> None:
    dest = open('./compile_log.txt', 'a')
    if error is not None:
        dest.write(f'Testcase {num}: Failed to compile\nError: {error}\n')

    elif line == expect:
        dest.write(f'Testcase {num}: Passed\n')
    
    else:
        dest.write(f'Testcase {num}: Failed\nExpect: {expect}\nGot: {line}\n')
    
    dest.close()

class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        TestLexer.check(SOL_DIR, inputfile, num)
        dest = open(SOL_DIR + str(num) + ".txt", "r")
        line = dest.read()
        writeToFile(num, line, expect)
        return line == expect

    @staticmethod
    def check(soldir, inputfile, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        lexer = LexerTest(inputfile)
        try:
            TestLexer.printLexeme(dest, lexer)
        except (ErrorToken, IllegalEscape, UncloseString) as err:
            dest.write(err.message)
        finally:
            dest.close()

    @staticmethod
    def printLexeme(dest, lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text+",")
            TestLexer.printLexeme(dest, lexer)
        else:
            dest.write("<EOF>")


class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line " + str(line) +
                              " col " + str(column) + ": " + offendingSymbol.text)


NewErrorListener.INSTANCE = NewErrorListener()


class SyntaxException(Exception):
    def __init__(self, msg):
        self.message = msg


class TestParser:
    @staticmethod
    def createErrorListener():
        return NewErrorListener.INSTANCE

    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        TestParser.check(SOL_DIR, inputfile, num)
        dest = open(SOL_DIR + str(num) + ".txt", "r")
        line = dest.read()
        writeToFile(num, line, expect)
        return line == expect

    @staticmethod
    def check(soldir, inputfile, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        lexer = LexerTest(inputfile)
        listener = TestParser.createErrorListener()
        tokens = CommonTokenStream(lexer)
        parser = ParserTest(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()

class TestAST:
    @staticmethod
    def createErrorListener():
        return NewErrorListener.INSTANCE
    
    @staticmethod
    def createParseTree(input, num):
        inputfile = TestUtil.makeSource(input, num)
        try:
            listener = TestAST.createErrorListener()
            lexerTest = LexerTest(inputfile)
            tokensTest = CommonTokenStream(lexerTest)
            parserTest = ParserTest(tokensTest)
            parserTest.removeErrorListeners()
            parserTest.addErrorListener(listener)
            treeTest = parserTest.program()
            return treeTest
        
        except SyntaxException as f:
            writeToFile(num, "", "", f.message)
        
        except Exception as e:
            writeToFile(num, "", "", str(e))
            
    
    @staticmethod
    def test(input, expect, num):
        from main.zcode2.astgen.ASTGeneration import ASTGeneration
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "w")
        parseTest = TestAST.createParseTree(input, num)
        try:
            asttree = ASTGeneration().visit(parseTest) if parseTest is not None else None
            if asttree is None:
                return False
            
            dest.write(str(asttree))
            dest.close()
            dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
            line = dest.read()
            writeToFile(num, line, expect)
            return line == expect

        except Exception as e:
            writeToFile(num, "", "", str(e))

class TestChecker:
    @staticmethod
    def test(input, expect, num):
        from main.zcode.astgen.ASTGeneration import ASTGeneration
        if type(input) is str:
            inputfile = TestUtil.makeSource(input, num)
            lexer = LexerSol(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = ParserSol(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input), num)
            asttree = input

        try:
            TestChecker.check(SOL_DIR, asttree, num)

        except Exception as e:
            writeToFile(num, "", "", str(e))
            return False

        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        writeToFile(num, line, expect)
        return line == expect

    @staticmethod
    def check(soldir, asttree, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        checker = StaticChecker(asttree)
        try:
            res = checker.check()
            if res is None:
                dest.write("")
        except StaticError as se:
            dest.write(str(se))
        finally:
            dest.close()

class TestCodeGen():
    @staticmethod
    def test(input, expect, num):
        from main.zcode.astgen.ASTGeneration import ASTGeneration
        if type(input) is str:
            inputfile = TestUtil.makeSource(input, num)
            lexer = LexerSol(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = ParserSol(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input), num)
            asttree = input

        TestCodeGen.check(SOL_DIR, asttree, num)

        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        writeToFile(num, line, expect)
        return line == expect

    @staticmethod
    def check(soldir, asttree, num):
        codeGen = CodeGenerator()
        path = os.path.join(soldir, str(num))
        if not os.path.isdir(path):
            os.mkdir(path)

        f = open(os.path.join(soldir, str(num) + ".txt"), "w")
        try:
            # check = StaticChecker(asttree).check()
            codeGen.gen(asttree, path)

            subprocess.run('javac ./lib/io.java')
            subprocess.call("java  -jar " + JASMIN_JAR + " " + path + "/*.j", shell=True, stderr=subprocess.STDOUT)

            cmd = "java -cp ./lib" + os.pathsep + ". ZCodeClass"
            subprocess.run(cmd, shell=True, stdout=f, timeout=10)

        except subprocess.TimeoutExpired:
            f.write("Time out\n")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(
                e.cmd, e.returncode, e.output))
        except Exception as e:
            from traceback import format_exc
            print(format_exc())
            writeToFile(num, "", "", str(e))
        finally:
            f.close()