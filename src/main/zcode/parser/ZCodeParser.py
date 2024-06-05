# Generated from ./main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,50,375,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        5,0,68,8,0,10,0,12,0,71,9,0,1,0,1,0,1,0,5,0,76,8,0,10,0,12,0,79,
        9,0,1,0,1,0,1,1,1,1,3,1,85,8,1,1,1,4,1,88,8,1,11,1,12,1,89,1,2,1,
        2,3,2,94,8,2,1,2,1,2,1,2,3,2,99,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,112,8,2,3,2,114,8,2,1,3,1,3,1,3,1,3,3,3,120,
        8,3,1,4,1,4,1,5,1,5,1,5,1,5,3,5,128,8,5,1,5,1,5,5,5,132,8,5,10,5,
        12,5,135,9,5,1,5,1,5,3,5,139,8,5,1,6,1,6,1,6,1,6,1,6,3,6,146,8,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,157,8,7,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,3,8,168,8,8,1,9,1,9,1,9,1,9,1,9,5,9,175,8,9,
        10,9,12,9,178,9,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,188,8,9,10,
        9,12,9,191,9,9,1,9,1,9,5,9,195,8,9,10,9,12,9,198,9,9,1,9,1,9,1,9,
        3,9,203,8,9,1,10,1,10,1,10,1,10,1,11,1,11,3,11,211,8,11,1,12,1,12,
        1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,225,8,13,
        10,13,12,13,228,9,13,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,3,16,
        238,8,16,1,17,1,17,1,17,3,17,243,8,17,1,17,1,17,1,18,1,18,4,18,249,
        8,18,11,18,12,18,250,1,18,5,18,254,8,18,10,18,12,18,257,9,18,1,18,
        4,18,260,8,18,11,18,12,18,261,5,18,264,8,18,10,18,12,18,267,9,18,
        1,18,1,18,1,19,1,19,1,19,1,19,1,19,3,19,276,8,19,1,20,1,20,1,20,
        1,20,1,20,3,20,283,8,20,1,21,1,21,1,21,1,21,1,21,1,21,5,21,291,8,
        21,10,21,12,21,294,9,21,1,22,1,22,1,22,1,22,1,22,1,22,5,22,302,8,
        22,10,22,12,22,305,9,22,1,23,1,23,1,23,1,23,1,23,1,23,5,23,313,8,
        23,10,23,12,23,316,9,23,1,24,1,24,1,24,3,24,321,8,24,1,25,1,25,1,
        25,3,25,326,8,25,1,26,1,26,3,26,330,8,26,1,27,1,27,3,27,334,8,27,
        1,27,1,27,1,27,1,27,1,28,1,28,1,28,3,28,343,8,28,1,28,1,28,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,3,29,354,8,29,1,30,1,30,1,30,1,30,
        1,30,3,30,361,8,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,5,32,370,8,
        32,10,32,12,32,373,9,32,1,32,0,3,42,44,46,33,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,0,5,1,0,11,13,2,0,28,30,32,35,2,0,17,17,19,19,1,0,23,24,
        1,0,25,27,396,0,69,1,0,0,0,2,84,1,0,0,0,4,113,1,0,0,0,6,119,1,0,
        0,0,8,121,1,0,0,0,10,123,1,0,0,0,12,145,1,0,0,0,14,156,1,0,0,0,16,
        167,1,0,0,0,18,169,1,0,0,0,20,204,1,0,0,0,22,210,1,0,0,0,24,212,
        1,0,0,0,26,217,1,0,0,0,28,231,1,0,0,0,30,233,1,0,0,0,32,235,1,0,
        0,0,34,239,1,0,0,0,36,246,1,0,0,0,38,275,1,0,0,0,40,282,1,0,0,0,
        42,284,1,0,0,0,44,295,1,0,0,0,46,306,1,0,0,0,48,320,1,0,0,0,50,325,
        1,0,0,0,52,329,1,0,0,0,54,333,1,0,0,0,56,339,1,0,0,0,58,353,1,0,
        0,0,60,360,1,0,0,0,62,362,1,0,0,0,64,366,1,0,0,0,66,68,5,45,0,0,
        67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,
        0,0,0,71,69,1,0,0,0,72,77,3,2,1,0,73,76,5,45,0,0,74,76,3,2,1,0,75,
        73,1,0,0,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,
        0,78,80,1,0,0,0,79,77,1,0,0,0,80,81,5,0,0,1,81,1,1,0,0,0,82,85,3,
        4,2,0,83,85,3,10,5,0,84,82,1,0,0,0,84,83,1,0,0,0,85,87,1,0,0,0,86,
        88,5,45,0,0,87,86,1,0,0,0,88,89,1,0,0,0,89,87,1,0,0,0,89,90,1,0,
        0,0,90,3,1,0,0,0,91,94,3,8,4,0,92,94,5,15,0,0,93,91,1,0,0,0,93,92,
        1,0,0,0,94,95,1,0,0,0,95,98,5,42,0,0,96,97,5,31,0,0,97,99,3,38,19,
        0,98,96,1,0,0,0,98,99,1,0,0,0,99,114,1,0,0,0,100,101,5,18,0,0,101,
        102,5,42,0,0,102,103,5,31,0,0,103,114,3,38,19,0,104,105,3,8,4,0,
        105,106,5,42,0,0,106,107,5,39,0,0,107,108,3,6,3,0,108,111,5,40,0,
        0,109,110,5,31,0,0,110,112,3,38,19,0,111,109,1,0,0,0,111,112,1,0,
        0,0,112,114,1,0,0,0,113,93,1,0,0,0,113,100,1,0,0,0,113,104,1,0,0,
        0,114,5,1,0,0,0,115,116,5,43,0,0,116,117,5,41,0,0,117,120,3,6,3,
        0,118,120,5,43,0,0,119,115,1,0,0,0,119,118,1,0,0,0,120,7,1,0,0,0,
        121,122,7,0,0,0,122,9,1,0,0,0,123,124,5,22,0,0,124,125,5,42,0,0,
        125,127,5,37,0,0,126,128,3,12,6,0,127,126,1,0,0,0,127,128,1,0,0,
        0,128,129,1,0,0,0,129,133,5,38,0,0,130,132,5,45,0,0,131,130,1,0,
        0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,138,1,0,
        0,0,135,133,1,0,0,0,136,139,3,32,16,0,137,139,3,36,18,0,138,136,
        1,0,0,0,138,137,1,0,0,0,138,139,1,0,0,0,139,11,1,0,0,0,140,141,3,
        14,7,0,141,142,5,41,0,0,142,143,3,12,6,0,143,146,1,0,0,0,144,146,
        3,14,7,0,145,140,1,0,0,0,145,144,1,0,0,0,146,13,1,0,0,0,147,148,
        3,8,4,0,148,149,5,42,0,0,149,157,1,0,0,0,150,151,3,8,4,0,151,152,
        5,42,0,0,152,153,5,39,0,0,153,154,3,6,3,0,154,155,5,40,0,0,155,157,
        1,0,0,0,156,147,1,0,0,0,156,150,1,0,0,0,157,15,1,0,0,0,158,168,3,
        4,2,0,159,168,3,18,9,0,160,168,3,20,10,0,161,168,3,26,13,0,162,168,
        3,28,14,0,163,168,3,30,15,0,164,168,3,34,17,0,165,168,3,32,16,0,
        166,168,3,36,18,0,167,158,1,0,0,0,167,159,1,0,0,0,167,160,1,0,0,
        0,167,161,1,0,0,0,167,162,1,0,0,0,167,163,1,0,0,0,167,164,1,0,0,
        0,167,165,1,0,0,0,167,166,1,0,0,0,168,17,1,0,0,0,169,170,5,3,0,0,
        170,171,5,37,0,0,171,172,3,38,19,0,172,176,5,38,0,0,173,175,5,45,
        0,0,174,173,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,
        0,0,177,179,1,0,0,0,178,176,1,0,0,0,179,180,3,16,8,0,180,196,1,0,
        0,0,181,182,5,45,0,0,182,183,5,5,0,0,183,184,5,37,0,0,184,185,3,
        38,19,0,185,189,5,38,0,0,186,188,5,45,0,0,187,186,1,0,0,0,188,191,
        1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,192,1,0,0,0,191,189,
        1,0,0,0,192,193,3,16,8,0,193,195,1,0,0,0,194,181,1,0,0,0,195,198,
        1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,202,1,0,0,0,198,196,
        1,0,0,0,199,200,5,45,0,0,200,201,5,4,0,0,201,203,3,16,8,0,202,199,
        1,0,0,0,202,203,1,0,0,0,203,19,1,0,0,0,204,205,3,22,11,0,205,206,
        5,31,0,0,206,207,3,38,19,0,207,21,1,0,0,0,208,211,5,42,0,0,209,211,
        3,24,12,0,210,208,1,0,0,0,210,209,1,0,0,0,211,23,1,0,0,0,212,213,
        5,42,0,0,213,214,5,39,0,0,214,215,3,64,32,0,215,216,5,40,0,0,216,
        25,1,0,0,0,217,218,5,6,0,0,218,219,5,42,0,0,219,220,5,7,0,0,220,
        221,3,38,19,0,221,222,5,8,0,0,222,226,3,38,19,0,223,225,5,45,0,0,
        224,223,1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,226,227,1,0,0,0,
        227,229,1,0,0,0,228,226,1,0,0,0,229,230,3,16,8,0,230,27,1,0,0,0,
        231,232,5,1,0,0,232,29,1,0,0,0,233,234,5,2,0,0,234,31,1,0,0,0,235,
        237,5,14,0,0,236,238,3,38,19,0,237,236,1,0,0,0,237,238,1,0,0,0,238,
        33,1,0,0,0,239,240,5,42,0,0,240,242,5,37,0,0,241,243,3,64,32,0,242,
        241,1,0,0,0,242,243,1,0,0,0,243,244,1,0,0,0,244,245,5,38,0,0,245,
        35,1,0,0,0,246,248,5,20,0,0,247,249,5,45,0,0,248,247,1,0,0,0,249,
        250,1,0,0,0,250,248,1,0,0,0,250,251,1,0,0,0,251,265,1,0,0,0,252,
        254,3,16,8,0,253,252,1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,255,
        256,1,0,0,0,256,259,1,0,0,0,257,255,1,0,0,0,258,260,5,45,0,0,259,
        258,1,0,0,0,260,261,1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,
        264,1,0,0,0,263,255,1,0,0,0,264,267,1,0,0,0,265,263,1,0,0,0,265,
        266,1,0,0,0,266,268,1,0,0,0,267,265,1,0,0,0,268,269,5,21,0,0,269,
        37,1,0,0,0,270,271,3,40,20,0,271,272,5,36,0,0,272,273,3,40,20,0,
        273,276,1,0,0,0,274,276,3,40,20,0,275,270,1,0,0,0,275,274,1,0,0,
        0,276,39,1,0,0,0,277,278,3,42,21,0,278,279,7,1,0,0,279,280,3,42,
        21,0,280,283,1,0,0,0,281,283,3,42,21,0,282,277,1,0,0,0,282,281,1,
        0,0,0,283,41,1,0,0,0,284,285,6,21,-1,0,285,286,3,44,22,0,286,292,
        1,0,0,0,287,288,10,2,0,0,288,289,7,2,0,0,289,291,3,44,22,0,290,287,
        1,0,0,0,291,294,1,0,0,0,292,290,1,0,0,0,292,293,1,0,0,0,293,43,1,
        0,0,0,294,292,1,0,0,0,295,296,6,22,-1,0,296,297,3,46,23,0,297,303,
        1,0,0,0,298,299,10,2,0,0,299,300,7,3,0,0,300,302,3,46,23,0,301,298,
        1,0,0,0,302,305,1,0,0,0,303,301,1,0,0,0,303,304,1,0,0,0,304,45,1,
        0,0,0,305,303,1,0,0,0,306,307,6,23,-1,0,307,308,3,48,24,0,308,314,
        1,0,0,0,309,310,10,2,0,0,310,311,7,4,0,0,311,313,3,48,24,0,312,309,
        1,0,0,0,313,316,1,0,0,0,314,312,1,0,0,0,314,315,1,0,0,0,315,47,1,
        0,0,0,316,314,1,0,0,0,317,318,5,16,0,0,318,321,3,48,24,0,319,321,
        3,50,25,0,320,317,1,0,0,0,320,319,1,0,0,0,321,49,1,0,0,0,322,323,
        7,3,0,0,323,326,3,50,25,0,324,326,3,52,26,0,325,322,1,0,0,0,325,
        324,1,0,0,0,326,51,1,0,0,0,327,330,3,54,27,0,328,330,3,58,29,0,329,
        327,1,0,0,0,329,328,1,0,0,0,330,53,1,0,0,0,331,334,5,42,0,0,332,
        334,3,56,28,0,333,331,1,0,0,0,333,332,1,0,0,0,334,335,1,0,0,0,335,
        336,5,39,0,0,336,337,3,64,32,0,337,338,5,40,0,0,338,55,1,0,0,0,339,
        340,5,42,0,0,340,342,5,37,0,0,341,343,3,64,32,0,342,341,1,0,0,0,
        342,343,1,0,0,0,343,344,1,0,0,0,344,345,5,38,0,0,345,57,1,0,0,0,
        346,354,5,42,0,0,347,348,5,37,0,0,348,349,3,38,19,0,349,350,5,38,
        0,0,350,354,1,0,0,0,351,354,3,60,30,0,352,354,3,56,28,0,353,346,
        1,0,0,0,353,347,1,0,0,0,353,351,1,0,0,0,353,352,1,0,0,0,354,59,1,
        0,0,0,355,361,5,43,0,0,356,361,5,44,0,0,357,361,5,9,0,0,358,361,
        5,10,0,0,359,361,3,62,31,0,360,355,1,0,0,0,360,356,1,0,0,0,360,357,
        1,0,0,0,360,358,1,0,0,0,360,359,1,0,0,0,361,61,1,0,0,0,362,363,5,
        39,0,0,363,364,3,64,32,0,364,365,5,40,0,0,365,63,1,0,0,0,366,371,
        3,38,19,0,367,368,5,41,0,0,368,370,3,38,19,0,369,367,1,0,0,0,370,
        373,1,0,0,0,371,369,1,0,0,0,371,372,1,0,0,0,372,65,1,0,0,0,373,371,
        1,0,0,0,41,69,75,77,84,89,93,98,111,113,119,127,133,138,145,156,
        167,176,189,196,202,210,226,237,242,250,255,261,265,275,282,292,
        303,314,320,325,329,333,342,353,360,371
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'break'", "'continue'", "'if'", "'else'", 
                     "'elif'", "'for'", "'until'", "'by'", "'true'", "'false'", 
                     "'number'", "'bool'", "'string'", "'return'", "'dynamic'", 
                     "'not'", "'and'", "'var'", "'or'", "'begin'", "'end'", 
                     "'func'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'='", "'!='", "'<-'", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", 
                      "FOR", "UNTIL", "BY", "TRUE", "FALSE", "NUMBER", "BOOL", 
                      "STRING", "RETURN", "DYNAMIC", "NOT", "AND", "VAR", 
                      "OR", "BEGIN", "END", "FUNC", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "STR_EQ", "EQ", "NOT_EQ", "REV_ARROW", 
                      "LT", "LTE", "GT", "GTE", "CONCAT", "LR", "RR", "LS", 
                      "RS", "COMMA", "ID", "NUM_LIT", "STR_LIT", "NEWLINE", 
                      "CMT", "WS", "ERROR_CHAR", "UNCLOSED_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_var_decl = 2
    RULE_num_list = 3
    RULE_vartype = 4
    RULE_func_decl = 5
    RULE_params = 6
    RULE_param = 7
    RULE_stmt = 8
    RULE_if_stmt = 9
    RULE_assign_stmt = 10
    RULE_lhs = 11
    RULE_elem_array = 12
    RULE_for_stmt = 13
    RULE_break_stmt = 14
    RULE_continue_stmt = 15
    RULE_return_stmt = 16
    RULE_func_call_stmt = 17
    RULE_block_stmt = 18
    RULE_expr = 19
    RULE_expr1 = 20
    RULE_expr2 = 21
    RULE_expr3 = 22
    RULE_expr4 = 23
    RULE_expr5 = 24
    RULE_expr6 = 25
    RULE_expr7 = 26
    RULE_array_cell = 27
    RULE_func_call = 28
    RULE_operands = 29
    RULE_literals = 30
    RULE_array_lit = 31
    RULE_expr_list = 32

    ruleNames =  [ "program", "decl", "var_decl", "num_list", "vartype", 
                   "func_decl", "params", "param", "stmt", "if_stmt", "assign_stmt", 
                   "lhs", "elem_array", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "func_call_stmt", "block_stmt", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "array_cell", "func_call", "operands", "literals", 
                   "array_lit", "expr_list" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    IF=3
    ELSE=4
    ELIF=5
    FOR=6
    UNTIL=7
    BY=8
    TRUE=9
    FALSE=10
    NUMBER=11
    BOOL=12
    STRING=13
    RETURN=14
    DYNAMIC=15
    NOT=16
    AND=17
    VAR=18
    OR=19
    BEGIN=20
    END=21
    FUNC=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26
    MOD=27
    STR_EQ=28
    EQ=29
    NOT_EQ=30
    REV_ARROW=31
    LT=32
    LTE=33
    GT=34
    GTE=35
    CONCAT=36
    LR=37
    RR=38
    LS=39
    RS=40
    COMMA=41
    ID=42
    NUM_LIT=43
    STR_LIT=44
    NEWLINE=45
    CMT=46
    WS=47
    ERROR_CHAR=48
    UNCLOSED_STRING=49
    ILLEGAL_ESCAPE=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.DeclContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.DeclContext,i)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 66
                self.match(ZCodeParser.NEWLINE)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.decl()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184376592384) != 0):
                self.state = 75
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45]:
                    self.state = 73
                    self.match(ZCodeParser.NEWLINE)
                    pass
                elif token in [11, 12, 13, 15, 18, 22]:
                    self.state = 74
                    self.decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Func_declContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 15, 18]:
                self.state = 82
                self.var_decl()
                pass
            elif token in [22]:
                self.state = 83
                self.func_decl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 87 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 86
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 89 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def vartype(self):
            return self.getTypedRuleContext(ZCodeParser.VartypeContext,0)


        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def REV_ARROW(self):
            return self.getToken(ZCodeParser.REV_ARROW, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def num_list(self):
            return self.getTypedRuleContext(ZCodeParser.Num_listContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = ZCodeParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11, 12, 13]:
                    self.state = 91
                    self.vartype()
                    pass
                elif token in [15]:
                    self.state = 92
                    self.match(ZCodeParser.DYNAMIC)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 95
                self.match(ZCodeParser.ID)
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 96
                    self.match(ZCodeParser.REV_ARROW)
                    self.state = 97
                    self.expr()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.match(ZCodeParser.VAR)
                self.state = 101
                self.match(ZCodeParser.ID)
                self.state = 102
                self.match(ZCodeParser.REV_ARROW)
                self.state = 103
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.vartype()
                self.state = 105
                self.match(ZCodeParser.ID)
                self.state = 106
                self.match(ZCodeParser.LS)
                self.state = 107
                self.num_list()
                self.state = 108
                self.match(ZCodeParser.RS)
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 109
                    self.match(ZCodeParser.REV_ARROW)
                    self.state = 110
                    self.expr()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Num_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def num_list(self):
            return self.getTypedRuleContext(ZCodeParser.Num_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_num_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum_list" ):
                return visitor.visitNum_list(self)
            else:
                return visitor.visitChildren(self)




    def num_list(self):

        localctx = ZCodeParser.Num_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_num_list)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(ZCodeParser.NUM_LIT)
                self.state = 116
                self.match(ZCodeParser.COMMA)
                self.state = 117
                self.num_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(ZCodeParser.NUM_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vartype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartype" ):
                return visitor.visitVartype(self)
            else:
                return visitor.visitChildren(self)




    def vartype(self):

        localctx = ZCodeParser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vartype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LR(self):
            return self.getToken(ZCodeParser.LR, 0)

        def RR(self):
            return self.getToken(ZCodeParser.RR, 0)

        def params(self):
            return self.getTypedRuleContext(ZCodeParser.ParamsContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = ZCodeParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(ZCodeParser.FUNC)
            self.state = 124
            self.match(ZCodeParser.ID)
            self.state = 125
            self.match(ZCodeParser.LR)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0):
                self.state = 126
                self.params()


            self.state = 129
            self.match(ZCodeParser.RR)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 130
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 136
                self.return_stmt()
                pass
            elif token in [20]:
                self.state = 137
                self.block_stmt()
                pass
            elif token in [45]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def params(self):
            return self.getTypedRuleContext(ZCodeParser.ParamsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = ZCodeParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_params)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.param()
                self.state = 141
                self.match(ZCodeParser.COMMA)
                self.state = 142
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(ZCodeParser.VartypeContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def num_list(self):
            return self.getTypedRuleContext(ZCodeParser.Num_listContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.vartype()
                self.state = 148
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.vartype()
                self.state = 151
                self.match(ZCodeParser.ID)
                self.state = 152
                self.match(ZCodeParser.LS)
                self.state = 153
                self.num_list()
                self.state = 154
                self.match(ZCodeParser.RS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmtContext,0)


        def func_call_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 158
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 159
                self.if_stmt()
                pass

            elif la_ == 3:
                self.state = 160
                self.assign_stmt()
                pass

            elif la_ == 4:
                self.state = 161
                self.for_stmt()
                pass

            elif la_ == 5:
                self.state = 162
                self.break_stmt()
                pass

            elif la_ == 6:
                self.state = 163
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.state = 164
                self.func_call_stmt()
                pass

            elif la_ == 8:
                self.state = 165
                self.return_stmt()
                pass

            elif la_ == 9:
                self.state = 166
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LR(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.LR)
            else:
                return self.getToken(ZCodeParser.LR, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def RR(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.RR)
            else:
                return self.getToken(ZCodeParser.RR, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmtContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.ELIF)
            else:
                return self.getToken(ZCodeParser.ELIF, i)

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(ZCodeParser.IF)
            self.state = 170
            self.match(ZCodeParser.LR)
            self.state = 171
            self.expr()
            self.state = 172
            self.match(ZCodeParser.RR)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 173
                self.match(ZCodeParser.NEWLINE)
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 179
            self.stmt()
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 181
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 182
                    self.match(ZCodeParser.ELIF)
                    self.state = 183
                    self.match(ZCodeParser.LR)
                    self.state = 184
                    self.expr()
                    self.state = 185
                    self.match(ZCodeParser.RR)
                    self.state = 189
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==45:
                        self.state = 186
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 191
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 192
                    self.stmt() 
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 199
                self.match(ZCodeParser.NEWLINE)
                self.state = 200
                self.match(ZCodeParser.ELSE)
                self.state = 201
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def REV_ARROW(self):
            return self.getToken(ZCodeParser.REV_ARROW, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = ZCodeParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.lhs()
            self.state = 205
            self.match(ZCodeParser.REV_ARROW)
            self.state = 206
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def elem_array(self):
            return self.getTypedRuleContext(ZCodeParser.Elem_arrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_lhs)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.elem_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elem_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elem_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElem_array" ):
                return visitor.visitElem_array(self)
            else:
                return visitor.visitChildren(self)




    def elem_array(self):

        localctx = ZCodeParser.Elem_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_elem_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(ZCodeParser.ID)
            self.state = 213
            self.match(ZCodeParser.LS)
            self.state = 214
            self.expr_list()
            self.state = 215
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(ZCodeParser.FOR)
            self.state = 218
            self.match(ZCodeParser.ID)
            self.state = 219
            self.match(ZCodeParser.UNTIL)
            self.state = 220
            self.expr()
            self.state = 221
            self.match(ZCodeParser.BY)
            self.state = 222
            self.expr()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 223
                self.match(ZCodeParser.NEWLINE)
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 229
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(ZCodeParser.RETURN)
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 236
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LR(self):
            return self.getToken(ZCodeParser.LR, 0)

        def RR(self):
            return self.getToken(ZCodeParser.RR, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_stmt" ):
                return visitor.visitFunc_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def func_call_stmt(self):

        localctx = ZCodeParser.Func_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_func_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(ZCodeParser.ID)
            self.state = 240
            self.match(ZCodeParser.LR)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31473545577984) != 0):
                self.state = 241
                self.expr_list()


            self.state = 244
            self.match(ZCodeParser.RR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmtContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(ZCodeParser.BEGIN)
            self.state = 248 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 247
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 250 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 39582419974222) != 0):
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398047885390) != 0):
                    self.state = 252
                    self.stmt()
                    self.state = 257
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 259 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 258
                        self.match(ZCodeParser.NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 261 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 268
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr)
        try:
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.expr1()
                self.state = 271
                self.match(ZCodeParser.CONCAT)
                self.state = 272
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def NOT_EQ(self):
            return self.getToken(ZCodeParser.NOT_EQ, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LTE(self):
            return self.getToken(ZCodeParser.LTE, 0)

        def GTE(self):
            return self.getToken(ZCodeParser.GTE, 0)

        def STR_EQ(self):
            return self.getToken(ZCodeParser.STR_EQ, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.expr2(0)
                self.state = 278
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66303557632) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 279
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 292
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 287
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 288
                    _la = self._input.LA(1)
                    if not(_la==17 or _la==19):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 289
                    self.expr3(0) 
                self.state = 294
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 298
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 299
                    _la = self._input.LA(1)
                    if not(_la==23 or _la==24):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 300
                    self.expr4(0) 
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 314
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 309
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 310
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 311
                    self.expr5() 
                self.state = 316
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr5)
        try:
            self.state = 320
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(ZCodeParser.NOT)
                self.state = 318
                self.expr5()
                pass
            elif token in [9, 10, 23, 24, 37, 39, 42, 43, 44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr6)
        self._la = 0 # Token type
        try:
            self.state = 325
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 323
                self.expr6()
                pass
            elif token in [9, 10, 37, 39, 42, 43, 44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_cell(self):
            return self.getTypedRuleContext(ZCodeParser.Array_cellContext,0)


        def operands(self):
            return self.getTypedRuleContext(ZCodeParser.OperandsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr7)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.array_cell()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.operands()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_cellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_cell

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_cell" ):
                return visitor.visitArray_cell(self)
            else:
                return visitor.visitChildren(self)




    def array_cell(self):

        localctx = ZCodeParser.Array_cellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_array_cell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 331
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 332
                self.func_call()
                pass


            self.state = 335
            self.match(ZCodeParser.LS)
            self.state = 336
            self.expr_list()
            self.state = 337
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LR(self):
            return self.getToken(ZCodeParser.LR, 0)

        def RR(self):
            return self.getToken(ZCodeParser.RR, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(ZCodeParser.ID)
            self.state = 340
            self.match(ZCodeParser.LR)
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31473545577984) != 0):
                self.state = 341
                self.expr_list()


            self.state = 344
            self.match(ZCodeParser.RR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LR(self):
            return self.getToken(ZCodeParser.LR, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RR(self):
            return self.getToken(ZCodeParser.RR, 0)

        def literals(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralsContext,0)


        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = ZCodeParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_operands)
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.match(ZCodeParser.LR)
                self.state = 348
                self.expr()
                self.state = 349
                self.match(ZCodeParser.RR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 351
                self.literals()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 352
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def STR_LIT(self):
            return self.getToken(ZCodeParser.STR_LIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def array_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Array_litContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = ZCodeParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_literals)
        try:
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.match(ZCodeParser.NUM_LIT)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.match(ZCodeParser.STR_LIT)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 357
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 358
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 5)
                self.state = 359
                self.array_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = ZCodeParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(ZCodeParser.LS)
            self.state = 363
            self.expr_list()
            self.state = 364
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMA)
            else:
                return self.getToken(ZCodeParser.COMMA, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = ZCodeParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.expr()
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 367
                self.match(ZCodeParser.COMMA)
                self.state = 368
                self.expr()
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            self._predicates = dict()
        self._predicates[21] = self.expr2_sempred
        self._predicates[22] = self.expr3_sempred
        self._predicates[23] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




