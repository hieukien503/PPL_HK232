import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_101(self):
		self.assertTrue(TestLexer.test("G3^x&m", "G3,Error Token ^", 101))

	def test_102(self):
		self.assertTrue(TestLexer.test("xYI85N5T", "xYI85N5T,<EOF>", 102))

	def test_103(self):
		self.assertTrue(TestLexer.test("uuo@", "uuo,Error Token @", 103))

	def test_104(self):
		self.assertTrue(TestLexer.test('''## kLy;}@(EF*9Z"a''', '''<EOF>''', 104))

	def test_105(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 105))

	def test_106(self):
		self.assertTrue(TestLexer.test("S", "S,<EOF>", 106))

	def test_107(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 107))

	def test_108(self):
		self.assertTrue(TestLexer.test('''## 9$wgd>e9''', '''<EOF>''', 108))

	def test_109(self):
		self.assertTrue(TestLexer.test('''## z>(Iyu!TU6q/K.S3:''', '''<EOF>''', 109))

	def test_110(self):
		self.assertTrue(TestLexer.test('''## _c"]<hn71I''', '''<EOF>''', 110))

	def test_111(self):
		self.assertTrue(TestLexer.test('''## iyjQKT5|C[u3''', '''<EOF>''', 111))

	def test_112(self):
		self.assertTrue(TestLexer.test('''"
'""''', '''Unclosed String: ''', 112))

	def test_113(self):
		self.assertTrue(TestLexer.test("540", "540,<EOF>", 113))

	def test_114(self):
		self.assertTrue(TestLexer.test("1.393", "1.393,<EOF>", 114))

	def test_115(self):
		self.assertTrue(TestLexer.test('''## 0T5>^`tw#2''', '''<EOF>''', 115))

	def test_116(self):
		self.assertTrue(TestLexer.test("915.921", "915.921,<EOF>", 116))

	def test_117(self):
		self.assertTrue(TestLexer.test("8.230", "8.230,<EOF>", 117))

	def test_118(self):
		self.assertTrue(TestLexer.test('''"+"''', '''+,<EOF>''', 118))

	def test_119(self):
		self.assertTrue(TestLexer.test('''"|\\o'""''', '''Illegal Escape In String: |\\o''', 119))

	def test_120(self):
		self.assertTrue(TestLexer.test('''"\\ov"''', '''Illegal Escape In String: \\o''', 120))

	def test_121(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 121))

	def test_122(self):
		self.assertTrue(TestLexer.test('''## %c0DQL?,dr''', '''<EOF>''', 122))

	def test_123(self):
		self.assertTrue(TestLexer.test("O^", "O,Error Token ^", 123))

	def test_124(self):
		self.assertTrue(TestLexer.test("U6", "U6,<EOF>", 124))

	def test_125(self):
		self.assertTrue(TestLexer.test("863E98", "863E98,<EOF>", 125))

	def test_126(self):
		self.assertTrue(TestLexer.test('''"'"
'""''', '''Unclosed String: '"''', 126))

	def test_127(self):
		self.assertTrue(TestLexer.test("597E+71", "597E+71,<EOF>", 127))

	def test_128(self):
		self.assertTrue(TestLexer.test('''"w'"\\p'"	R"''', '''Illegal Escape In String: w'"\\p''', 128))

	def test_129(self):
		self.assertTrue(TestLexer.test('''"
1'"M7"''', '''Unclosed String: ''', 129))

	def test_130(self):
		self.assertTrue(TestLexer.test('''## T,G!(lh''', '''<EOF>''', 130))

	def test_131(self):
		self.assertTrue(TestLexer.test('''## WN-G}s@?N?lPCi7.J''', '''<EOF>''', 131))

	def test_132(self):
		self.assertTrue(TestLexer.test('''## JuSU''', '''<EOF>''', 132))

	def test_133(self):
		self.assertTrue(TestLexer.test("6E-33", "6E-33,<EOF>", 133))

	def test_134(self):
		self.assertTrue(TestLexer.test('''## pRMa9oOWTmv`}1#''', '''<EOF>''', 134))

	def test_135(self):
		self.assertTrue(TestLexer.test("j", "j,<EOF>", 135))

	def test_136(self):
		self.assertTrue(TestLexer.test('''## 7!TaY%@''', '''<EOF>''', 136))

	def test_137(self):
		self.assertTrue(TestLexer.test("1.975E11", "1.975E11,<EOF>", 137))

	def test_138(self):
		self.assertTrue(TestLexer.test("^Aaj#^HdR", "Error Token ^", 138))

	def test_139(self):
		self.assertTrue(TestLexer.test("95E-49", "95E-49,<EOF>", 139))

	def test_140(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 140))

	def test_141(self):
		self.assertTrue(TestLexer.test('''## Y`nDmnHC"4~vt''', '''<EOF>''', 141))

	def test_142(self):
		self.assertTrue(TestLexer.test('''## CK*P''', '''<EOF>''', 142))

	def test_143(self):
		self.assertTrue(TestLexer.test("487.390", "487.390,<EOF>", 143))

	def test_144(self):
		self.assertTrue(TestLexer.test('''"E^'"b'""''', '''E^'"b'",<EOF>''', 144))

	def test_145(self):
		self.assertTrue(TestLexer.test("172.079E79", "172.079E79,<EOF>", 145))

	def test_146(self):
		self.assertTrue(TestLexer.test('''## p9CREUSK<uI1`}T''', '''<EOF>''', 146))

	def test_147(self):
		self.assertTrue(TestLexer.test("343.468E-74", "343.468E-74,<EOF>", 147))

	def test_148(self):
		self.assertTrue(TestLexer.test('''## ,-F*[?Vyg''', '''<EOF>''', 148))

	def test_149(self):
		self.assertTrue(TestLexer.test("ocQC1cuG5p", "ocQC1cuG5p,<EOF>", 149))

	def test_150(self):
		self.assertTrue(TestLexer.test("863e+34", "863e+34,<EOF>", 150))

	def test_151(self):
		self.assertTrue(TestLexer.test("72", "72,<EOF>", 151))

	def test_152(self):
		self.assertTrue(TestLexer.test("b2eYLfK8l", "b2eYLfK8l,<EOF>", 152))

	def test_153(self):
		self.assertTrue(TestLexer.test('''"j'"'""''', '''j'"'",<EOF>''', 153))

	def test_154(self):
		self.assertTrue(TestLexer.test("25.269", "25.269,<EOF>", 154))

	def test_155(self):
		self.assertTrue(TestLexer.test("S", "S,<EOF>", 155))

	def test_156(self):
		self.assertTrue(TestLexer.test("269.992", "269.992,<EOF>", 156))

	def test_157(self):
		self.assertTrue(TestLexer.test("37.773", "37.773,<EOF>", 157))

	def test_158(self):
		self.assertTrue(TestLexer.test("BBMjeVTmW0", "BBMjeVTmW0,<EOF>", 158))

	def test_159(self):
		self.assertTrue(TestLexer.test('''## (#''', '''<EOF>''', 159))

	def test_160(self):
		self.assertTrue(TestLexer.test('''## ^C''', '''<EOF>''', 160))

	def test_161(self):
		self.assertTrue(TestLexer.test("7e+96", "7e+96,<EOF>", 161))

	def test_162(self):
		self.assertTrue(TestLexer.test("884", "884,<EOF>", 162))

	def test_163(self):
		self.assertTrue(TestLexer.test('''"'"=
'""''', '''Unclosed String: '"=''', 163))

	def test_164(self):
		self.assertTrue(TestLexer.test("Eu", "Eu,<EOF>", 164))

	def test_165(self):
		self.assertTrue(TestLexer.test("8E+03", "8E+03,<EOF>", 165))

	def test_166(self):
		self.assertTrue(TestLexer.test('''"
I"''', '''Unclosed String: ''', 166))

	def test_167(self):
		self.assertTrue(TestLexer.test("^A6Rzp8rR", "Error Token ^", 167))

	def test_168(self):
		self.assertTrue(TestLexer.test('''## F]R''', '''<EOF>''', 168))

	def test_169(self):
		self.assertTrue(TestLexer.test('''"\\i'"_)1'""''', '''Illegal Escape In String: \\i''', 169))

	def test_170(self):
		self.assertTrue(TestLexer.test("rfr", "rfr,<EOF>", 170))

	def test_171(self):
		self.assertTrue(TestLexer.test('''"'"\\z{"''', '''Illegal Escape In String: '"\\z''', 171))

	def test_172(self):
		self.assertTrue(TestLexer.test("704.832", "704.832,<EOF>", 172))

	def test_173(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 173))

	def test_174(self):
		self.assertTrue(TestLexer.test('''"
`'""''', '''Unclosed String: ''', 174))

	def test_175(self):
		self.assertTrue(TestLexer.test('''"'"d'""''', '''\'"d'",<EOF>''', 175))

	def test_176(self):
		self.assertTrue(TestLexer.test("O", "O,<EOF>", 176))

	def test_177(self):
		self.assertTrue(TestLexer.test('''## 0Gb?=4TLc`W,z%''', '''<EOF>''', 177))

	def test_178(self):
		self.assertTrue(TestLexer.test("906.950e-91", "906.950e-91,<EOF>", 178))

	def test_179(self):
		self.assertTrue(TestLexer.test('''"'"~*
-="''', '''Unclosed String: '"~*''', 179))

	def test_180(self):
		self.assertTrue(TestLexer.test("RV$wa&85", "RV,Error Token $", 180))

	def test_181(self):
		self.assertTrue(TestLexer.test('''## 9''', '''<EOF>''', 181))

	def test_182(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 182))

	def test_183(self):
		self.assertTrue(TestLexer.test('''"\\v "''', '''Illegal Escape In String: \\v''', 183))

	def test_184(self):
		self.assertTrue(TestLexer.test('''## lk;VXZAKT_p#{fk''', '''<EOF>''', 184))

	def test_185(self):
		self.assertTrue(TestLexer.test('''":'"
'"'"&"''', '''Unclosed String: :'"''', 185))

	def test_186(self):
		self.assertTrue(TestLexer.test('''"$'"'""''', '''$'"'",<EOF>''', 186))

	def test_187(self):
		self.assertTrue(TestLexer.test('''## r]]o~2I7PpVcl''', '''<EOF>''', 187))

	def test_188(self):
		self.assertTrue(TestLexer.test('''"Ug"''', '''Ug,<EOF>''', 188))

	def test_189(self):
		self.assertTrue(TestLexer.test("74.296e51", "74.296e51,<EOF>", 189))

	def test_190(self):
		self.assertTrue(TestLexer.test("537.359E52", "537.359E52,<EOF>", 190))

	def test_191(self):
		self.assertTrue(TestLexer.test('''"$'""''', '''$'",<EOF>''', 191))

	def test_192(self):
		self.assertTrue(TestLexer.test('''## C''', '''<EOF>''', 192))

	def test_193(self):
		self.assertTrue(TestLexer.test("246", "246,<EOF>", 193))

	def test_194(self):
		self.assertTrue(TestLexer.test("91", "91,<EOF>", 194))

	def test_195(self):
		self.assertTrue(TestLexer.test("3.423E63", "3.423E63,<EOF>", 195))

	def test_196(self):
		self.assertTrue(TestLexer.test("D#tdlepwj", "D,Error Token #", 196))

	def test_197(self):
		self.assertTrue(TestLexer.test("5.628", "5.628,<EOF>", 197))

	def test_198(self):
		self.assertTrue(TestLexer.test("hkqsBmt", "hkqsBmt,<EOF>", 198))

	def test_199(self):
		self.assertTrue(TestLexer.test('''## ^,Hb/Q.g''', '''<EOF>''', 199))

	def test_200(self):
		self.assertTrue(TestLexer.test("1E+05", "1E+05,<EOF>", 200))
