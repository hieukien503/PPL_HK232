import os
import subprocess
import sys
import unittest

for path in ['./test/', './main/zcode/parser/', './main/zcode/utils/', './main/zcode/astgen/', './main/zcode/checker/', './main/zcode/codegen/']:
    sys.path.append(path)

ANTLR_JAR = os.environ.get('ANTLR_JAR')
TARGET_DIR = './main/zcode/parser'

def processFileAST(ASTGenSrc: str = './main/zcode2/astgen/ASTGeneration.py'):
    inputList = []
    with open(ASTGenSrc) as f:
        inputList = f.readlines()
        if 'zcode2' in ASTGenSrc:
            inputList[0] = "from main.zcode2.parser.ZCodeVisitor import ZCodeVisitor\n"
            inputList[1] = "from main.zcode2.parser.ZCodeParser import ZCodeParser\n"
            inputList[2] = "from main.zcode.utils.AST import *\n"
        
        else:
            inputList[0] = "from main.zcode.parser.ZCodeVisitor import ZCodeVisitor\n"
            inputList[1] = "from main.zcode.parser.ZCodeParser import ZCodeParser\n"
            inputList[2] = "from main.zcode.utils.AST import *\n"

        f.close()

    with open(ASTGenSrc, 'w') as f:
        f.writelines(inputList)
        f.close()

def processFileChecker(CheckerSrc: str = './main/zcode2/checker/StaticChecker.py'):
    inputList = []
    with open(CheckerSrc) as f:
        inputList = f.readlines()
        inputList[0] = "from main.zcode.utils.AST import *\n"
        inputList[1] = "from main.zcode.checker.StaticError import *\n"
        inputList[2] = "from main.zcode.utils.Visitor import *\n"
        inputList[3] = "from main.zcode.utils.Utils import *\n"

        for idx in range(len(inputList)):
            if inputList[idx].find('class StaticChecker') != -1:
                inputList[idx] = "class StaticChecker(Visitor, Utils):\n"
                break

        f.close()

    with open(CheckerSrc, 'w') as f:
        f.writelines(inputList)
        f.close()

def plagiarismChecker():
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    MAX_ACCEPT_PLAGIARISM = 0.65

    staticFile = ['./main/zcode/checker/StaticChecker.py', './main/zcode2/checker/StaticChecker.py']
    contents = [open(file).read() for file in staticFile]
    extractWord = ['from main.zcode.utils.AST import *\n',
                   'from main.zcode.checker.StaticError import *\n'
                   'from main.zcode.utils.Visitor import *\n',
                   'from main.zcode.utils.Utils import *\n',
                   'class StaticChecker(Visitor, Utils):\n'
                   'def __init__', 'def check(self):\n',
                   'def visitArrayType', 'def visitStringType', 'def visitBoolType', 'def visitNumberType',
                   'def visitBlock', 'def visitCallStmt', 'def visitIf', 'def visitFor', 'def visitAssign',
                   'def visitBreak', 'def visitContinue', 'def visitReturn', 'def visitArrayLiteral',
                   'def visitBooleanLiteral', 'def visitStringLiteral', 'def visitNumberLiteral',
                   'def visitArrayCell', 'def visitCallExpr', 'def visitUnaryOp', 'def visitBinaryOp',
                   'def visitId', 'def visitFuncDecl', 'def visitVarDecl','def visitProgram'
                   ]

    contents = [content.replace(kw, '') for kw in extractWord for content in contents]

    def create_tfidf_vector(docs):
        return TfidfVectorizer().fit_transform(docs).toarray()
    
    docs = create_tfidf_vector(contents)

    solVec, testVec = docs[0], docs[1]
    score = cosine_similarity([solVec, testVec])[0][1]
    return score >= MAX_ACCEPT_PLAGIARISM, score

def main(argv):
    if len(argv) not in [1, 2]:
        printUsage()
    
    elif argv[0] == 'gen':
        subprocess.run(["java", "-jar", ANTLR_JAR, "-o", TARGET_DIR,
                        "-no-listener", "-visitor", "-Xexact-output-dir", "./main/zcode/parser/ZCode.g4"])
    
    elif argv[0] == 'test':
        if os.path.exists('./main/zcode2/parser'):
            subprocess.run(["java", "-jar", ANTLR_JAR, "-o", './main/zcode2/parser',
                        "-no-listener", "-visitor", "-Xexact-output-dir", "./main/zcode2/parser/ZCode.g4"])
        
        else:
            subprocess.run(["java", "-jar", ANTLR_JAR, "-o", './main/zcode/parser',
                        "-no-listener", "-visitor", "-Xexact-output-dir", "./main/zcode/parser/ZCode.g4"])
        
        dest = open('./compile_log.txt', 'w')
        dest.write('COMPILATION RESULT:\n')
        dest.close()
        if argv[1] in ['LexerSuite', 'ParserSuite', 'ASTGenSuite', 'CheckerSuite', 'CodeGenSuite']:
            if argv[1] == 'ASTGenSuite':
                processFileAST()
            
            elif argv[1] == 'CheckerSuite':
                processFileAST('./main/zcode/astgen/ASTGeneration.py')
                processFileChecker('./main/zcode2/checker/StaticChecker.py')
                # isPlagiarism, score = plagiarismChecker()
                # print(f'{round(score * 100, 2)}%')
                # if isPlagiarism:
                #     raise RuntimeError(f'Plagiarism detected with similiarity {round(score * 100, 2)}%. Stop checking this file!')
                
                # else:
                #     print(f'{round(score * 100, 2)}%')

            exec(f'from {argv[1]} import {argv[1]}')
            exec(f'getAndTest({argv[1]})')

        else:
            printUsage()
    
    elif argv[0] == 'genTest':
        if argv[1] in ['LexerSuite', 'ParserSuite', 'ASTGenSuite']:
            subprocess.run(f"python genTestCase.py {argv[1]}")
        
        else:
            printUsage()
    
    elif argv[0] == 'clean':
        files = ['ZCodeLexer.py', 'ZCodeParser.py', 'ZCodeLexer.tokens', 'ZCode.interp', 'ZCode.tokens', 'ZCodeLexer.interp', 'ZCodeVisitor.py']
        for file in files:
            if os.path.exists('./main/zcode/parser') and os.path.isfile(f'./main/zcode/parser/{file}'):
                os.remove(f'./main/zcode/parser/{file}')

            if os.path.exists('./main/zcode2/parser') and os.path.isfile(f'./main/zcode2/parser/{file}'):
                os.remove(f'./main/zcode2/parser/{file}')
            
            if os.path.exists('../target') and os.path.isfile(f'../target/{file}'):
                os.remove(f'../target/{file}')

    else:
        printUsage()

def getAndTest(cls):
    from io import StringIO
    testLoader = unittest.TestLoader()
    suite = testLoader.loadTestsFromTestCase(cls)
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    stream.seek(0)
    res = stream.read().split('\n')[0]
    dest = open('./compile_log.txt', 'a')
    dest.write(f"Score: {res.count('.')}/{result.testsRun}")
    dest.close()
    
def printUsage():
    print('python run.py clean') # Clean the generated file in target folder and ./main/zcode/parser folder
    print('python run.py gen')   # Remember to run this code before generating testcases
    print('python run.py test LexerSuite')
    print('python run.py test ParserSuite')
    print('python run.py test ASTGenSuite')
    print('python run.py test CheckerSuite')
    print('python run.py test CodeGenSuite')

if __name__ == '__main__':
    main(sys.argv[1:])