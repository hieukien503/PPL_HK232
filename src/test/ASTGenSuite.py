import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
	def test_301(self):
		input = '''
bool yzJ[50.53,6.98,49.53] <- MrG()
'''
		expect = '''Program([VarDecl(Id(yzJ), ArrayType([50.53, 6.98, 49.53], BoolType), None, CallExpr(Id(MrG), []))])'''
		self.assertTrue(TestAST.test(input, expect, 301))

	def test_302(self):
		input = '''
string tvPE[97.16] <- [DF, not ["JpHP"], 12.79]
string m32o <- aavL
'''
		expect = '''Program([VarDecl(Id(tvPE), ArrayType([97.16], StringType), None, ArrayLit(Id(DF), UnaryOp(not, ArrayLit(StringLit(JpHP))), NumLit(12.79))), VarDecl(Id(m32o), StringType, None, Id(aavL))])'''
		self.assertTrue(TestAST.test(input, expect, 302))

	def test_303(self):
		input = '''
func gN9k (number o1)
	return 91.87

bool WyC
bool DjFI[13.05,95.9,18.44] <- jBVr
'''
		expect = '''Program([FuncDecl(Id(gN9k), [VarDecl(Id(o1), NumberType, None, None)], Return(NumLit(91.87))), VarDecl(Id(WyC), BoolType, None, None), VarDecl(Id(DjFI), ArrayType([13.05, 95.9, 18.44], BoolType), None, Id(jBVr))])'''
		self.assertTrue(TestAST.test(input, expect, 303))

	def test_304(self):
		input = '''
func BVn (bool BQ)	return
func vlwG ()	return
func dWQu (number vbG, string Q_7L, bool P5E)	return RNv

'''
		expect = '''Program([FuncDecl(Id(BVn), [VarDecl(Id(BQ), BoolType, None, None)], Return()), FuncDecl(Id(vlwG), [], Return()), FuncDecl(Id(dWQu), [VarDecl(Id(vbG), NumberType, None, None), VarDecl(Id(Q_7L), StringType, None, None), VarDecl(Id(P5E), BoolType, None, None)], Return(Id(RNv)))])'''
		self.assertTrue(TestAST.test(input, expect, 304))

	def test_305(self):
		input = '''
func KhA (number G7, bool fMr[63.86,13.91], string fEg9[71.44,85.25,90.47])	return rtH
func oD ()	return

bool Rghl[76.32,59.59] <- "maF"
func fq (number EJ)
	begin
		continue
		return
		begin
			Xm(true, "pELl")
			continue
		end
	end
'''
		expect = '''Program([FuncDecl(Id(KhA), [VarDecl(Id(G7), NumberType, None, None), VarDecl(Id(fMr), ArrayType([63.86, 13.91], BoolType), None, None), VarDecl(Id(fEg9), ArrayType([71.44, 85.25, 90.47], StringType), None, None)], Return(Id(rtH))), FuncDecl(Id(oD), [], Return()), VarDecl(Id(Rghl), ArrayType([76.32, 59.59], BoolType), None, StringLit(maF)), FuncDecl(Id(fq), [VarDecl(Id(EJ), NumberType, None, None)], Block([Continue, Return(), Block([CallStmt(Id(Xm), [BooleanLit(True), StringLit(pELl)]), Continue])]))])'''
		self.assertTrue(TestAST.test(input, expect, 305))

	def test_306(self):
		input = '''
string DaJ <- JQ
func MD (bool s0I[61.35,91.85])
	return
func OJ (number AW)	return
func Ti (number Owbf)
	return false

'''
		expect = '''Program([VarDecl(Id(DaJ), StringType, None, Id(JQ)), FuncDecl(Id(MD), [VarDecl(Id(s0I), ArrayType([61.35, 91.85], BoolType), None, None)], Return()), FuncDecl(Id(OJ), [VarDecl(Id(AW), NumberType, None, None)], Return()), FuncDecl(Id(Ti), [VarDecl(Id(Owbf), NumberType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 306))

	def test_307(self):
		input = '''
number zI <- 53.52
func A3S (number oqyR[99.46,81.19], bool uv[88.55,62.65,61.86], bool zRNQ[80.77,80.24])
	begin
		break
		zS(Prue)
	end
func muR (string GLys)
	return "QQLiR"

'''
		expect = '''Program([VarDecl(Id(zI), NumberType, None, NumLit(53.52)), FuncDecl(Id(A3S), [VarDecl(Id(oqyR), ArrayType([99.46, 81.19], NumberType), None, None), VarDecl(Id(uv), ArrayType([88.55, 62.65, 61.86], BoolType), None, None), VarDecl(Id(zRNQ), ArrayType([80.77, 80.24], BoolType), None, None)], Block([Break, CallStmt(Id(zS), [Id(Prue)])])), FuncDecl(Id(muR), [VarDecl(Id(GLys), StringType, None, None)], Return(StringLit(QQLiR)))])'''
		self.assertTrue(TestAST.test(input, expect, 307))

	def test_308(self):
		input = '''
func ZN (number fGV, string biH[23.07,81.72], number Or)	return D5

var hF <- 37.85
'''
		expect = '''Program([FuncDecl(Id(ZN), [VarDecl(Id(fGV), NumberType, None, None), VarDecl(Id(biH), ArrayType([23.07, 81.72], StringType), None, None), VarDecl(Id(Or), NumberType, None, None)], Return(Id(D5))), VarDecl(Id(hF), None, var, NumLit(37.85))])'''
		self.assertTrue(TestAST.test(input, expect, 308))

	def test_309(self):
		input = '''
bool WkS[11.17,47.69,45.82] <- 1.82
func w7I ()	return
func tV (number a2e[94.74,35.12,7.54])
	begin
		sM <- sKZO
		number o8[30.69,12.97,10.76]
		break
	end

'''
		expect = '''Program([VarDecl(Id(WkS), ArrayType([11.17, 47.69, 45.82], BoolType), None, NumLit(1.82)), FuncDecl(Id(w7I), [], Return()), FuncDecl(Id(tV), [VarDecl(Id(a2e), ArrayType([94.74, 35.12, 7.54], NumberType), None, None)], Block([AssignStmt(Id(sM), Id(sKZO)), VarDecl(Id(o8), ArrayType([30.69, 12.97, 10.76], NumberType), None, None), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 309))

	def test_310(self):
		input = '''
func nhu (bool euG[36.66,58.45], string fjR[17.15,35.98])	begin
		string PH <- dy
	end

func zt4 (string cZTf[1.29,46.13], bool X8yk[63.02,92.67], string GqM[74.13,30.19])	begin
		number Sh <- OpZ
		if (true)
		if (56.35) if (true)
		if (false)
		break
		else number cw[22.85]
		elif ("PdyY") gz(5.36)
		elif (ZO)
		oH[62.52, "aL"] <- false
		elif (rHa7)
		begin
			break
			Pz24[Ab, false, "GDLsQ"] <- 18.63
			for G6 until "QTCaQ" by 30.29
				begin
				end
		end
		elif (emU)
		xc[31.12, h64l, 72.21] <- "Gb"
		elif ("EAUw")
		return
		else tigx("lRKp", true)
		elif ("IuV") if (20.44)
		eg(hp, false)
		elif (true) continue
		elif (95.55)
		if (90.88)
		if (17.49) return Ww5n
		elif (17.23) break
		elif (true)
		continue
		elif ("E")
		for Wq until true by T49
			continue
		elif ("CS") string aIiy[85.3,48.7]
		elif (Bv)
		kEJR <- "JGF"
		elif (sI)
		for e7gD until false by false
			cCX(true, "S")
		elif (false)
		gwZM[false, false, "z"] <- "i"
		else string ply[65.27,43.97,68.66]
		elif ("ZN")
		BdKq(JOy, 25.75)
		elif (rgb) for wM1D until 11.52 by "L"
			string YSiz <- 90.85
		else return
	end

var Yn <- "SciI"
'''
		expect = '''Program([FuncDecl(Id(nhu), [VarDecl(Id(euG), ArrayType([36.66, 58.45], BoolType), None, None), VarDecl(Id(fjR), ArrayType([17.15, 35.98], StringType), None, None)], Block([VarDecl(Id(PH), StringType, None, Id(dy))])), FuncDecl(Id(zt4), [VarDecl(Id(cZTf), ArrayType([1.29, 46.13], StringType), None, None), VarDecl(Id(X8yk), ArrayType([63.02, 92.67], BoolType), None, None), VarDecl(Id(GqM), ArrayType([74.13, 30.19], StringType), None, None)], Block([VarDecl(Id(Sh), NumberType, None, Id(OpZ)), If((BooleanLit(True), If((NumLit(56.35), If((BooleanLit(True), If((BooleanLit(False), Break), [], VarDecl(Id(cw), ArrayType([22.85], NumberType), None, None))), [(StringLit(PdyY), CallStmt(Id(gz), [NumLit(5.36)])), (Id(ZO), AssignStmt(ArrayCell(Id(oH), [NumLit(62.52), StringLit(aL)]), BooleanLit(False))), (Id(rHa7), Block([Break, AssignStmt(ArrayCell(Id(Pz24), [Id(Ab), BooleanLit(False), StringLit(GDLsQ)]), NumLit(18.63)), For(Id(G6), StringLit(QTCaQ), NumLit(30.29), Block([]))])), (Id(emU), AssignStmt(ArrayCell(Id(xc), [NumLit(31.12), Id(h64l), NumLit(72.21)]), StringLit(Gb))), (StringLit(EAUw), Return())], CallStmt(Id(tigx), [StringLit(lRKp), BooleanLit(True)]))), [(StringLit(IuV), If((NumLit(20.44), CallStmt(Id(eg), [Id(hp), BooleanLit(False)])), [(BooleanLit(True), Continue), (NumLit(95.55), If((NumLit(90.88), If((NumLit(17.49), Return(Id(Ww5n))), [(NumLit(17.23), Break), (BooleanLit(True), Continue), (StringLit(E), For(Id(Wq), BooleanLit(True), Id(T49), Continue)), (StringLit(CS), VarDecl(Id(aIiy), ArrayType([85.3, 48.7], StringType), None, None)), (Id(Bv), AssignStmt(Id(kEJR), StringLit(JGF))), (Id(sI), For(Id(e7gD), BooleanLit(False), BooleanLit(False), CallStmt(Id(cCX), [BooleanLit(True), StringLit(S)]))), (BooleanLit(False), AssignStmt(ArrayCell(Id(gwZM), [BooleanLit(False), BooleanLit(False), StringLit(z)]), StringLit(i)))], VarDecl(Id(ply), ArrayType([65.27, 43.97, 68.66], StringType), None, None))), [(StringLit(ZN), CallStmt(Id(BdKq), [Id(JOy), NumLit(25.75)])), (Id(rgb), For(Id(wM1D), NumLit(11.52), StringLit(L), VarDecl(Id(YSiz), StringType, None, NumLit(90.85))))], Return()))], None))], None)), [], None)])), VarDecl(Id(Yn), None, var, StringLit(SciI))])'''
		self.assertTrue(TestAST.test(input, expect, 310))

	def test_311(self):
		input = '''
number xIvB[69.86]
'''
		expect = '''Program([VarDecl(Id(xIvB), ArrayType([69.86], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 311))

	def test_312(self):
		input = '''
func VZAH (number IC5P, bool XazO[43.61])
	return "nin"
string vj[47.23,65.31]
func OO9 (bool ll3, number L9u6[51.85,15.1])	return false
bool q66g
bool hX <- pc
'''
		expect = '''Program([FuncDecl(Id(VZAH), [VarDecl(Id(IC5P), NumberType, None, None), VarDecl(Id(XazO), ArrayType([43.61], BoolType), None, None)], Return(StringLit(nin))), VarDecl(Id(vj), ArrayType([47.23, 65.31], StringType), None, None), FuncDecl(Id(OO9), [VarDecl(Id(ll3), BoolType, None, None), VarDecl(Id(L9u6), ArrayType([51.85, 15.1], NumberType), None, None)], Return(BooleanLit(False))), VarDecl(Id(q66g), BoolType, None, None), VarDecl(Id(hX), BoolType, None, Id(pc))])'''
		self.assertTrue(TestAST.test(input, expect, 312))

	def test_313(self):
		input = '''
string DBv_
bool DKx[63.93,60.64,24.82] <- "AVz"
'''
		expect = '''Program([VarDecl(Id(DBv_), StringType, None, None), VarDecl(Id(DKx), ArrayType([63.93, 60.64, 24.82], BoolType), None, StringLit(AVz))])'''
		self.assertTrue(TestAST.test(input, expect, 313))

	def test_314(self):
		input = '''
bool RM03[48.47,1.39,68.47] <- "jyj"
var z7L <- Xr
func Is ()	return
'''
		expect = '''Program([VarDecl(Id(RM03), ArrayType([48.47, 1.39, 68.47], BoolType), None, StringLit(jyj)), VarDecl(Id(z7L), None, var, Id(Xr)), FuncDecl(Id(Is), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 314))

	def test_315(self):
		input = '''
func S0zw ()	return true
func Ie (number YD[63.26,54.44,55.9], string HQ_Z[81.01,68.36], bool Fdt)	return

bool yR <- "CzR"
var s00 <- yHJ9
func vm (string mNoz[21.99,2.49], number EZN, bool FK)	return false
'''
		expect = '''Program([FuncDecl(Id(S0zw), [], Return(BooleanLit(True))), FuncDecl(Id(Ie), [VarDecl(Id(YD), ArrayType([63.26, 54.44, 55.9], NumberType), None, None), VarDecl(Id(HQ_Z), ArrayType([81.01, 68.36], StringType), None, None), VarDecl(Id(Fdt), BoolType, None, None)], Return()), VarDecl(Id(yR), BoolType, None, StringLit(CzR)), VarDecl(Id(s00), None, var, Id(yHJ9)), FuncDecl(Id(vm), [VarDecl(Id(mNoz), ArrayType([21.99, 2.49], StringType), None, None), VarDecl(Id(EZN), NumberType, None, None), VarDecl(Id(FK), BoolType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 315))

	def test_316(self):
		input = '''
func aO (string vmtS, string t9C_)
	return true

string f6[79.83,50.58]
func Aj (number xaJ, number er, string DL8)	begin
		n0A <- 87.7
		begin
			for R2a until true by true
				break
		end
		yQbT(40.43, "lPc", "Rx")
	end

func Ng (number zd[42.46])	return "fzAZ"

dynamic qjP
'''
		expect = '''Program([FuncDecl(Id(aO), [VarDecl(Id(vmtS), StringType, None, None), VarDecl(Id(t9C_), StringType, None, None)], Return(BooleanLit(True))), VarDecl(Id(f6), ArrayType([79.83, 50.58], StringType), None, None), FuncDecl(Id(Aj), [VarDecl(Id(xaJ), NumberType, None, None), VarDecl(Id(er), NumberType, None, None), VarDecl(Id(DL8), StringType, None, None)], Block([AssignStmt(Id(n0A), NumLit(87.7)), Block([For(Id(R2a), BooleanLit(True), BooleanLit(True), Break)]), CallStmt(Id(yQbT), [NumLit(40.43), StringLit(lPc), StringLit(Rx)])])), FuncDecl(Id(Ng), [VarDecl(Id(zd), ArrayType([42.46], NumberType), None, None)], Return(StringLit(fzAZ))), VarDecl(Id(qjP), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 316))

	def test_317(self):
		input = '''
var xC81 <- AC0c
bool Jg
func D3y ()
	return

string Du7P[7.55,89.71,22.04]
bool bx <- 15.89
'''
		expect = '''Program([VarDecl(Id(xC81), None, var, Id(AC0c)), VarDecl(Id(Jg), BoolType, None, None), FuncDecl(Id(D3y), [], Return()), VarDecl(Id(Du7P), ArrayType([7.55, 89.71, 22.04], StringType), None, None), VarDecl(Id(bx), BoolType, None, NumLit(15.89))])'''
		self.assertTrue(TestAST.test(input, expect, 317))

	def test_318(self):
		input = '''
string sjz[34.62,73.33]
func iFb (bool rpi[0.49,53.42], string rI[4.84,21.81,71.87], string Qj4)	return
func P82D (string ATK[46.42,8.4], string sHgU[93.58,69.48,40.21], bool WEw[0.79,44.58,13.2])	return

'''
		expect = '''Program([VarDecl(Id(sjz), ArrayType([34.62, 73.33], StringType), None, None), FuncDecl(Id(iFb), [VarDecl(Id(rpi), ArrayType([0.49, 53.42], BoolType), None, None), VarDecl(Id(rI), ArrayType([4.84, 21.81, 71.87], StringType), None, None), VarDecl(Id(Qj4), StringType, None, None)], Return()), FuncDecl(Id(P82D), [VarDecl(Id(ATK), ArrayType([46.42, 8.4], StringType), None, None), VarDecl(Id(sHgU), ArrayType([93.58, 69.48, 40.21], StringType), None, None), VarDecl(Id(WEw), ArrayType([0.79, 44.58, 13.2], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 318))

	def test_319(self):
		input = '''
func wvY ()	return
func MD (number j1R[3.1,6.57])
	return

func dERw ()	return

'''
		expect = '''Program([FuncDecl(Id(wvY), [], Return()), FuncDecl(Id(MD), [VarDecl(Id(j1R), ArrayType([3.1, 6.57], NumberType), None, None)], Return()), FuncDecl(Id(dERw), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 319))

	def test_320(self):
		input = '''
string Xs[35.85,1.76]
func fY (bool wNw, bool EXW9[91.81,35.49,10.87])
	begin
		YnPq <- "RXI"
	end
'''
		expect = '''Program([VarDecl(Id(Xs), ArrayType([35.85, 1.76], StringType), None, None), FuncDecl(Id(fY), [VarDecl(Id(wNw), BoolType, None, None), VarDecl(Id(EXW9), ArrayType([91.81, 35.49, 10.87], BoolType), None, None)], Block([AssignStmt(Id(YnPq), StringLit(RXI))]))])'''
		self.assertTrue(TestAST.test(input, expect, 320))

	def test_321(self):
		input = '''
dynamic RCSb
func sx (number wvI)	begin
		number aCzE[34.58] <- 13.5
		nqIL[20.75, VpIt, true] <- "yw"
	end
func n4W (number GQPf, bool YNB, string grV[10.51,64.22])
	return false
func RK (bool DP, bool R1[72.26])	begin
		string hteP
	end
'''
		expect = '''Program([VarDecl(Id(RCSb), None, dynamic, None), FuncDecl(Id(sx), [VarDecl(Id(wvI), NumberType, None, None)], Block([VarDecl(Id(aCzE), ArrayType([34.58], NumberType), None, NumLit(13.5)), AssignStmt(ArrayCell(Id(nqIL), [NumLit(20.75), Id(VpIt), BooleanLit(True)]), StringLit(yw))])), FuncDecl(Id(n4W), [VarDecl(Id(GQPf), NumberType, None, None), VarDecl(Id(YNB), BoolType, None, None), VarDecl(Id(grV), ArrayType([10.51, 64.22], StringType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(RK), [VarDecl(Id(DP), BoolType, None, None), VarDecl(Id(R1), ArrayType([72.26], BoolType), None, None)], Block([VarDecl(Id(hteP), StringType, None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 321))

	def test_322(self):
		input = '''
func jq9 (string Y6A, string F7[11.27,51.49], string DAS)	return x1AU

func xj (bool HXm[79.01,94.21], number yq, bool vyp[46.23,88.93])	return
'''
		expect = '''Program([FuncDecl(Id(jq9), [VarDecl(Id(Y6A), StringType, None, None), VarDecl(Id(F7), ArrayType([11.27, 51.49], StringType), None, None), VarDecl(Id(DAS), StringType, None, None)], Return(Id(x1AU))), FuncDecl(Id(xj), [VarDecl(Id(HXm), ArrayType([79.01, 94.21], BoolType), None, None), VarDecl(Id(yq), NumberType, None, None), VarDecl(Id(vyp), ArrayType([46.23, 88.93], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 322))

	def test_323(self):
		input = '''
func ICr (number u0, bool BfKZ[16.57])
	return
var wq <- false
'''
		expect = '''Program([FuncDecl(Id(ICr), [VarDecl(Id(u0), NumberType, None, None), VarDecl(Id(BfKZ), ArrayType([16.57], BoolType), None, None)], Return()), VarDecl(Id(wq), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 323))

	def test_324(self):
		input = '''
func iJEA ()
	begin
		if (55.56)
		for Bc07 until 36.73 by "hSCqh"
			for AkH until "n" by "g"
				zI <- false
	end
string xo
func iK (number am72[74.96,90.4,30.92], number jQ[85.3,38.53,22.48], bool NIx[1.21,41.73,3.89])
	begin
		for BGvV until zyN by ONP
			string gc8 <- true
		for XJO until ouk by 36.58
			number RQcE[7.28] <- true
		break
	end
func BdQ (bool U4Y)	begin
		Qasg()
		break
		if (32.27)
		continue
		elif ("vu")
		begin
			for DZj until true by 18.06
				vf()
		end
		elif (3.25) begin
		end
		elif (36.18)
		wR(BGz, prdj, 41.09)
	end
'''
		expect = '''Program([FuncDecl(Id(iJEA), [], Block([If((NumLit(55.56), For(Id(Bc07), NumLit(36.73), StringLit(hSCqh), For(Id(AkH), StringLit(n), StringLit(g), AssignStmt(Id(zI), BooleanLit(False))))), [], None)])), VarDecl(Id(xo), StringType, None, None), FuncDecl(Id(iK), [VarDecl(Id(am72), ArrayType([74.96, 90.4, 30.92], NumberType), None, None), VarDecl(Id(jQ), ArrayType([85.3, 38.53, 22.48], NumberType), None, None), VarDecl(Id(NIx), ArrayType([1.21, 41.73, 3.89], BoolType), None, None)], Block([For(Id(BGvV), Id(zyN), Id(ONP), VarDecl(Id(gc8), StringType, None, BooleanLit(True))), For(Id(XJO), Id(ouk), NumLit(36.58), VarDecl(Id(RQcE), ArrayType([7.28], NumberType), None, BooleanLit(True))), Break])), FuncDecl(Id(BdQ), [VarDecl(Id(U4Y), BoolType, None, None)], Block([CallStmt(Id(Qasg), []), Break, If((NumLit(32.27), Continue), [(StringLit(vu), Block([For(Id(DZj), BooleanLit(True), NumLit(18.06), CallStmt(Id(vf), []))])), (NumLit(3.25), Block([])), (NumLit(36.18), CallStmt(Id(wR), [Id(BGz), Id(prdj), NumLit(41.09)]))], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 324))

	def test_325(self):
		input = '''
func ifQ (bool pH, string hX[75.84])
	return "OEswb"

func B0 (string sf)
	return kh_

func DHk (number yk6s[91.12,78.73])
	begin
		zEQs(41.4, iv)
		for Nn29 until "t" by Zjd1
			continue
		begin
			E7uu()
		end
	end
func in1 ()	begin
	end

func LdSt (bool nX)
	return
'''
		expect = '''Program([FuncDecl(Id(ifQ), [VarDecl(Id(pH), BoolType, None, None), VarDecl(Id(hX), ArrayType([75.84], StringType), None, None)], Return(StringLit(OEswb))), FuncDecl(Id(B0), [VarDecl(Id(sf), StringType, None, None)], Return(Id(kh_))), FuncDecl(Id(DHk), [VarDecl(Id(yk6s), ArrayType([91.12, 78.73], NumberType), None, None)], Block([CallStmt(Id(zEQs), [NumLit(41.4), Id(iv)]), For(Id(Nn29), StringLit(t), Id(Zjd1), Continue), Block([CallStmt(Id(E7uu), [])])])), FuncDecl(Id(in1), [], Block([])), FuncDecl(Id(LdSt), [VarDecl(Id(nX), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 325))

	def test_326(self):
		input = '''
bool MY[27.72,0.61] <- 2.39
'''
		expect = '''Program([VarDecl(Id(MY), ArrayType([27.72, 0.61], BoolType), None, NumLit(2.39))])'''
		self.assertTrue(TestAST.test(input, expect, 326))

	def test_327(self):
		input = '''
dynamic RlT
func dke (number a8Uz[2.51,54.19])
	return

'''
		expect = '''Program([VarDecl(Id(RlT), None, dynamic, None), FuncDecl(Id(dke), [VarDecl(Id(a8Uz), ArrayType([2.51, 54.19], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 327))

	def test_328(self):
		input = '''
number ykE
string E4P
'''
		expect = '''Program([VarDecl(Id(ykE), NumberType, None, None), VarDecl(Id(E4P), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 328))

	def test_329(self):
		input = '''
func Xf ()	return true

'''
		expect = '''Program([FuncDecl(Id(Xf), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 329))

	def test_330(self):
		input = '''
var eu <- 42.47
func jgDp (bool JlQ, bool sdi, string J4K[47.37,96.81])
	return false
'''
		expect = '''Program([VarDecl(Id(eu), None, var, NumLit(42.47)), FuncDecl(Id(jgDp), [VarDecl(Id(JlQ), BoolType, None, None), VarDecl(Id(sdi), BoolType, None, None), VarDecl(Id(J4K), ArrayType([47.37, 96.81], StringType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 330))

	def test_331(self):
		input = '''
func lX (bool KNow, string rfp3)
	return true

'''
		expect = '''Program([FuncDecl(Id(lX), [VarDecl(Id(KNow), BoolType, None, None), VarDecl(Id(rfp3), StringType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 331))

	def test_332(self):
		input = '''
func FU (number Gfq[39.15,33.52,86.15], bool lB[36.55], bool liQ[48.6])
	return
func ml (string sY8K[47.77,75.75,25.61], number ABN[52.97])	begin
		break
		B0(GdNb, 14.06)
	end

'''
		expect = '''Program([FuncDecl(Id(FU), [VarDecl(Id(Gfq), ArrayType([39.15, 33.52, 86.15], NumberType), None, None), VarDecl(Id(lB), ArrayType([36.55], BoolType), None, None), VarDecl(Id(liQ), ArrayType([48.6], BoolType), None, None)], Return()), FuncDecl(Id(ml), [VarDecl(Id(sY8K), ArrayType([47.77, 75.75, 25.61], StringType), None, None), VarDecl(Id(ABN), ArrayType([52.97], NumberType), None, None)], Block([Break, CallStmt(Id(B0), [Id(GdNb), NumLit(14.06)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 332))

	def test_333(self):
		input = '''
bool kOy[93.65,26.23,97.57]
func MgHw ()
	return

number wA0z[89.63]
func x7E (bool Vm, bool aa)	return false

bool VQ3k <- VQL
'''
		expect = '''Program([VarDecl(Id(kOy), ArrayType([93.65, 26.23, 97.57], BoolType), None, None), FuncDecl(Id(MgHw), [], Return()), VarDecl(Id(wA0z), ArrayType([89.63], NumberType), None, None), FuncDecl(Id(x7E), [VarDecl(Id(Vm), BoolType, None, None), VarDecl(Id(aa), BoolType, None, None)], Return(BooleanLit(False))), VarDecl(Id(VQ3k), BoolType, None, Id(VQL))])'''
		self.assertTrue(TestAST.test(input, expect, 333))

	def test_334(self):
		input = '''
func iv69 ()
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(iv69), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 334))

	def test_335(self):
		input = '''
func LaWm (number BNh[80.94,90.52,59.69], bool yv9H[59.6])
	begin
		return edl
		for KvA until Q3 by s7k
			if (MVC) if ("GhTw") begin
				eJ1z[59.01] <- 7.84
				string ey[50.69,98.78,78.71]
				for RaIR until 33.72 by GwV
					break
			end
			elif (true)
			for howA until 48.39 by st_
				if (93.6) for kSRl until 61.81 by 10.63
					xy[gr6U] <- false
				else break
			elif ("gG")
			if (48.28) if (false)
			jG0U(true, RAl)
			elif (47.94)
			Tm(DF_y, tDPL, 99.47)
			elif (true)
			return false
			elif (a9ZL)
			break
			elif (false) break
			else if (false) return 70.74
			elif ("lUSiB") if (true) return 88.66
			else for SfCg until true by 89.04
				continue
			elif (true) if (false)
			return
			elif (false) string Ka <- 57.7
			elif (true) begin
				break
				begin
					if (sJq) return 94.91
					elif (B0dP)
					Vo()
					elif ("lwg") continue
					return
				end
				ZY(MD, true, pQXT)
			end
			else BK[false, "nXkt"] <- "zqpo"
	end

func clLu ()	begin
		if (E8U)
		if (21.63) for Fj until 49.83 by "xlmI"
			continue
		elif ("H")
		LbU("OUS")
		elif (true)
		begin
			return "aj"
		end
		elif ("WOD")
		return
		elif (95.65)
		q1V("xBV")
		elif (true) number aNB[56.03,3.32]
		elif (20.75)
		dynamic KCe
		elif ("zGZrs") number hr[4.56,50.12]
		else string Lp
		continue
		begin
			return j2
		end
	end
'''
		expect = '''Program([FuncDecl(Id(LaWm), [VarDecl(Id(BNh), ArrayType([80.94, 90.52, 59.69], NumberType), None, None), VarDecl(Id(yv9H), ArrayType([59.6], BoolType), None, None)], Block([Return(Id(edl)), For(Id(KvA), Id(Q3), Id(s7k), If((Id(MVC), If((StringLit(GhTw), Block([AssignStmt(ArrayCell(Id(eJ1z), [NumLit(59.01)]), NumLit(7.84)), VarDecl(Id(ey), ArrayType([50.69, 98.78, 78.71], StringType), None, None), For(Id(RaIR), NumLit(33.72), Id(GwV), Break)])), [(BooleanLit(True), For(Id(howA), NumLit(48.39), Id(st_), If((NumLit(93.6), For(Id(kSRl), NumLit(61.81), NumLit(10.63), AssignStmt(ArrayCell(Id(xy), [Id(gr6U)]), BooleanLit(False)))), [], Break))), (StringLit(gG), If((NumLit(48.28), If((BooleanLit(False), CallStmt(Id(jG0U), [BooleanLit(True), Id(RAl)])), [(NumLit(47.94), CallStmt(Id(Tm), [Id(DF_y), Id(tDPL), NumLit(99.47)])), (BooleanLit(True), Return(BooleanLit(False))), (Id(a9ZL), Break), (BooleanLit(False), Break)], If((BooleanLit(False), Return(NumLit(70.74))), [(StringLit(lUSiB), If((BooleanLit(True), Return(NumLit(88.66))), [], For(Id(SfCg), BooleanLit(True), NumLit(89.04), Continue))), (BooleanLit(True), If((BooleanLit(False), Return()), [(BooleanLit(False), VarDecl(Id(Ka), StringType, None, NumLit(57.7))), (BooleanLit(True), Block([Break, Block([If((Id(sJq), Return(NumLit(94.91))), [(Id(B0dP), CallStmt(Id(Vo), [])), (StringLit(lwg), Continue)], None), Return()]), CallStmt(Id(ZY), [Id(MD), BooleanLit(True), Id(pQXT)])]))], AssignStmt(ArrayCell(Id(BK), [BooleanLit(False), StringLit(nXkt)]), StringLit(zqpo))))], None))), [], None))], None)), [], None))])), FuncDecl(Id(clLu), [], Block([If((Id(E8U), If((NumLit(21.63), For(Id(Fj), NumLit(49.83), StringLit(xlmI), Continue)), [(StringLit(H), CallStmt(Id(LbU), [StringLit(OUS)])), (BooleanLit(True), Block([Return(StringLit(aj))])), (StringLit(WOD), Return()), (NumLit(95.65), CallStmt(Id(q1V), [StringLit(xBV)])), (BooleanLit(True), VarDecl(Id(aNB), ArrayType([56.03, 3.32], NumberType), None, None)), (NumLit(20.75), VarDecl(Id(KCe), None, dynamic, None)), (StringLit(zGZrs), VarDecl(Id(hr), ArrayType([4.56, 50.12], NumberType), None, None))], VarDecl(Id(Lp), StringType, None, None))), [], None), Continue, Block([Return(Id(j2))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 335))

	def test_336(self):
		input = '''
func Bi (string Dkcp[98.13], number g05F[66.6,18.83,19.15])
	begin
		if (62.85)
		return
		elif (20.19)
		begin
		end
		break
	end

func rN (bool vALW, string BZWV)	return "BB"

string Hoj[58.45,13.17,7.01]
'''
		expect = '''Program([FuncDecl(Id(Bi), [VarDecl(Id(Dkcp), ArrayType([98.13], StringType), None, None), VarDecl(Id(g05F), ArrayType([66.6, 18.83, 19.15], NumberType), None, None)], Block([If((NumLit(62.85), Return()), [(NumLit(20.19), Block([]))], None), Break])), FuncDecl(Id(rN), [VarDecl(Id(vALW), BoolType, None, None), VarDecl(Id(BZWV), StringType, None, None)], Return(StringLit(BB))), VarDecl(Id(Hoj), ArrayType([58.45, 13.17, 7.01], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 336))

	def test_337(self):
		input = '''
func vWgy (number be[10.98,1.46,64.71], bool NSm, number ba5[99.45,63.44])
	return
func zr2E (bool M4ZX, bool dpRv[1.97,98.03,31.19])	begin
		return
		if (FwJ)
		string vw4[5.58,17.34] <- 63.6
		elif (true) Rv <- rv
		elif (41.93) Iewt(true, true)
		elif ("iqQE")
		return "ZFD"
		elif (RA)
		Lyk("Ifb", false, false)
		elif (false) if ("dMFp") if ("joy") bool LMtK
		elif (true) begin
		end
		elif (i8A)
		x1[uTV] <- 11.96
		elif (true) return KX
		else continue
		elif (true) continue
		elif ("u") return eOi
		elif (true)
		begin
			for Ygs_ until cr7S by Uin
				dynamic deF <- "RMUn"
			break
			begin
				bool MfV[44.21,73.32]
				dynamic SURJ <- false
			end
		end
		elif (false) bool dG4[65.73,8.43] <- "Ba"
		else return
		else Y16P()
		number inb <- A0
	end
func UN (number Gl)	begin
		bool Gm[41.65,99.91,17.65]
	end
number Yx <- false
'''
		expect = '''Program([FuncDecl(Id(vWgy), [VarDecl(Id(be), ArrayType([10.98, 1.46, 64.71], NumberType), None, None), VarDecl(Id(NSm), BoolType, None, None), VarDecl(Id(ba5), ArrayType([99.45, 63.44], NumberType), None, None)], Return()), FuncDecl(Id(zr2E), [VarDecl(Id(M4ZX), BoolType, None, None), VarDecl(Id(dpRv), ArrayType([1.97, 98.03, 31.19], BoolType), None, None)], Block([Return(), If((Id(FwJ), VarDecl(Id(vw4), ArrayType([5.58, 17.34], StringType), None, NumLit(63.6))), [(BooleanLit(True), AssignStmt(Id(Rv), Id(rv))), (NumLit(41.93), CallStmt(Id(Iewt), [BooleanLit(True), BooleanLit(True)])), (StringLit(iqQE), Return(StringLit(ZFD))), (Id(RA), CallStmt(Id(Lyk), [StringLit(Ifb), BooleanLit(False), BooleanLit(False)])), (BooleanLit(False), If((StringLit(dMFp), If((StringLit(joy), VarDecl(Id(LMtK), BoolType, None, None)), [(BooleanLit(True), Block([])), (Id(i8A), AssignStmt(ArrayCell(Id(x1), [Id(uTV)]), NumLit(11.96))), (BooleanLit(True), Return(Id(KX)))], Continue)), [(BooleanLit(True), Continue), (StringLit(u), Return(Id(eOi))), (BooleanLit(True), Block([For(Id(Ygs_), Id(cr7S), Id(Uin), VarDecl(Id(deF), None, dynamic, StringLit(RMUn))), Break, Block([VarDecl(Id(MfV), ArrayType([44.21, 73.32], BoolType), None, None), VarDecl(Id(SURJ), None, dynamic, BooleanLit(False))])])), (BooleanLit(False), VarDecl(Id(dG4), ArrayType([65.73, 8.43], BoolType), None, StringLit(Ba)))], Return()))], CallStmt(Id(Y16P), [])), VarDecl(Id(inb), NumberType, None, Id(A0))])), FuncDecl(Id(UN), [VarDecl(Id(Gl), NumberType, None, None)], Block([VarDecl(Id(Gm), ArrayType([41.65, 99.91, 17.65], BoolType), None, None)])), VarDecl(Id(Yx), NumberType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 337))

	def test_338(self):
		input = '''
func NYiI (string F0, number v9J, bool VlB[29.09,16.68])	return true

number Pj[4.68,26.15,25.32]
'''
		expect = '''Program([FuncDecl(Id(NYiI), [VarDecl(Id(F0), StringType, None, None), VarDecl(Id(v9J), NumberType, None, None), VarDecl(Id(VlB), ArrayType([29.09, 16.68], BoolType), None, None)], Return(BooleanLit(True))), VarDecl(Id(Pj), ArrayType([4.68, 26.15, 25.32], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 338))

	def test_339(self):
		input = '''
number SxJ[24.82]
func Vo ()	return true
'''
		expect = '''Program([VarDecl(Id(SxJ), ArrayType([24.82], NumberType), None, None), FuncDecl(Id(Vo), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 339))

	def test_340(self):
		input = '''
func lq2S (string TFcp[63.4])	begin
	end
func Yt (bool NK8B)	return "FQ"
func Gbt ()
	begin
		if ("z")
		begin
			kli1[55.09, true, "Bz"] <- uZ
		end
		else kO <- TS
	end
func D97R (number pC[57.33,53.49,79.82], bool NE2z[59.7])
	begin
		continue
		AK3I <- "Hhjp"
		continue
	end
string M7K6 <- "HnuAQ"
'''
		expect = '''Program([FuncDecl(Id(lq2S), [VarDecl(Id(TFcp), ArrayType([63.4], StringType), None, None)], Block([])), FuncDecl(Id(Yt), [VarDecl(Id(NK8B), BoolType, None, None)], Return(StringLit(FQ))), FuncDecl(Id(Gbt), [], Block([If((StringLit(z), Block([AssignStmt(ArrayCell(Id(kli1), [NumLit(55.09), BooleanLit(True), StringLit(Bz)]), Id(uZ))])), [], AssignStmt(Id(kO), Id(TS)))])), FuncDecl(Id(D97R), [VarDecl(Id(pC), ArrayType([57.33, 53.49, 79.82], NumberType), None, None), VarDecl(Id(NE2z), ArrayType([59.7], BoolType), None, None)], Block([Continue, AssignStmt(Id(AK3I), StringLit(Hhjp)), Continue])), VarDecl(Id(M7K6), StringType, None, StringLit(HnuAQ))])'''
		self.assertTrue(TestAST.test(input, expect, 340))

	def test_341(self):
		input = '''
func SP (number eCLI)	begin
		begin
			dynamic h3 <- V0
			begin
				continue
				return
			end
			break
		end
		for UZy until rKv_ by PhE
			break
		y30[HHm, 31.88, false] <- 87.39
	end

number J6EL
string EJu[1.79]
string Gf
'''
		expect = '''Program([FuncDecl(Id(SP), [VarDecl(Id(eCLI), NumberType, None, None)], Block([Block([VarDecl(Id(h3), None, dynamic, Id(V0)), Block([Continue, Return()]), Break]), For(Id(UZy), Id(rKv_), Id(PhE), Break), AssignStmt(ArrayCell(Id(y30), [Id(HHm), NumLit(31.88), BooleanLit(False)]), NumLit(87.39))])), VarDecl(Id(J6EL), NumberType, None, None), VarDecl(Id(EJu), ArrayType([1.79], StringType), None, None), VarDecl(Id(Gf), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 341))

	def test_342(self):
		input = '''
func ysz (number e5xb)
	return

func XW (number JK, string cNc3[32.74,97.05,36.39])
	return 91.46

dynamic tr0h
'''
		expect = '''Program([FuncDecl(Id(ysz), [VarDecl(Id(e5xb), NumberType, None, None)], Return()), FuncDecl(Id(XW), [VarDecl(Id(JK), NumberType, None, None), VarDecl(Id(cNc3), ArrayType([32.74, 97.05, 36.39], StringType), None, None)], Return(NumLit(91.46))), VarDecl(Id(tr0h), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 342))

	def test_343(self):
		input = '''
string qNW8[53.5]
func H1 ()	return

string nm <- "L"
string YRYY
'''
		expect = '''Program([VarDecl(Id(qNW8), ArrayType([53.5], StringType), None, None), FuncDecl(Id(H1), [], Return()), VarDecl(Id(nm), StringType, None, StringLit(L)), VarDecl(Id(YRYY), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 343))

	def test_344(self):
		input = '''
string oZ[15.8,35.94,61.1] <- 17.59
func M0 (number Gq[45.04])
	return "QKPtQ"

func IgiR ()
	begin
		if (34.55)
		continue
		elif (jKO)
		jN3(true, false)
		elif (95.11) YMHO[fmBF, 13.84] <- 92.5
		elif (false)
		NffE <- ZQ2
		else if (59.33) if (79.46) number zz0[63.01,33.72]
		elif (z2Yb) break
		elif (wu)
		break
		elif (syA)
		for DCQZ until 83.88 by RO91
			b2Y <- false
		elif (52.06)
		dynamic KfD
		elif (true)
		for BA88 until XaYH by QzGd
			begin
				ea[true, "Mj", 66.88] <- 65.58
				string sJ
				dynamic pCy
			end
	end

bool n6e[75.75,67.65,74.73]
bool QV[49.52]
'''
		expect = '''Program([VarDecl(Id(oZ), ArrayType([15.8, 35.94, 61.1], StringType), None, NumLit(17.59)), FuncDecl(Id(M0), [VarDecl(Id(Gq), ArrayType([45.04], NumberType), None, None)], Return(StringLit(QKPtQ))), FuncDecl(Id(IgiR), [], Block([If((NumLit(34.55), Continue), [(Id(jKO), CallStmt(Id(jN3), [BooleanLit(True), BooleanLit(False)])), (NumLit(95.11), AssignStmt(ArrayCell(Id(YMHO), [Id(fmBF), NumLit(13.84)]), NumLit(92.5))), (BooleanLit(False), AssignStmt(Id(NffE), Id(ZQ2)))], If((NumLit(59.33), If((NumLit(79.46), VarDecl(Id(zz0), ArrayType([63.01, 33.72], NumberType), None, None)), [(Id(z2Yb), Break), (Id(wu), Break), (Id(syA), For(Id(DCQZ), NumLit(83.88), Id(RO91), AssignStmt(Id(b2Y), BooleanLit(False)))), (NumLit(52.06), VarDecl(Id(KfD), None, dynamic, None)), (BooleanLit(True), For(Id(BA88), Id(XaYH), Id(QzGd), Block([AssignStmt(ArrayCell(Id(ea), [BooleanLit(True), StringLit(Mj), NumLit(66.88)]), NumLit(65.58)), VarDecl(Id(sJ), StringType, None, None), VarDecl(Id(pCy), None, dynamic, None)])))], None)), [], None))])), VarDecl(Id(n6e), ArrayType([75.75, 67.65, 74.73], BoolType), None, None), VarDecl(Id(QV), ArrayType([49.52], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 344))

	def test_345(self):
		input = '''
func L9h ()
	begin
		break
		continue
		R0[DQ] <- C5UN
	end
func UT (string J7S[62.93,27.75,95.11])	return uG
'''
		expect = '''Program([FuncDecl(Id(L9h), [], Block([Break, Continue, AssignStmt(ArrayCell(Id(R0), [Id(DQ)]), Id(C5UN))])), FuncDecl(Id(UT), [VarDecl(Id(J7S), ArrayType([62.93, 27.75, 95.11], StringType), None, None)], Return(Id(uG)))])'''
		self.assertTrue(TestAST.test(input, expect, 345))

	def test_346(self):
		input = '''
var pxOr <- "G"
'''
		expect = '''Program([VarDecl(Id(pxOr), None, var, StringLit(G))])'''
		self.assertTrue(TestAST.test(input, expect, 346))

	def test_347(self):
		input = '''
func cje (number V5B, number Wre4[82.27,28.8], string PYbx[79.27,9.36])
	return

'''
		expect = '''Program([FuncDecl(Id(cje), [VarDecl(Id(V5B), NumberType, None, None), VarDecl(Id(Wre4), ArrayType([82.27, 28.8], NumberType), None, None), VarDecl(Id(PYbx), ArrayType([79.27, 9.36], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 347))

	def test_348(self):
		input = '''
func FG (number QmcO[59.56], bool mNM6, number WOrD[35.72,96.52,45.12])	begin
		Xh()
		return
	end
'''
		expect = '''Program([FuncDecl(Id(FG), [VarDecl(Id(QmcO), ArrayType([59.56], NumberType), None, None), VarDecl(Id(mNM6), BoolType, None, None), VarDecl(Id(WOrD), ArrayType([35.72, 96.52, 45.12], NumberType), None, None)], Block([CallStmt(Id(Xh), []), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 348))

	def test_349(self):
		input = '''
var nTx <- 96.79
number Xcq[15.12,32.92] <- UFyS
number oj4b[11.95,68.98]
'''
		expect = '''Program([VarDecl(Id(nTx), None, var, NumLit(96.79)), VarDecl(Id(Xcq), ArrayType([15.12, 32.92], NumberType), None, Id(UFyS)), VarDecl(Id(oj4b), ArrayType([11.95, 68.98], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 349))

	def test_350(self):
		input = '''
func jJrj (number xB[41.01,86.1,2.43], number Bib[72.58,30.13,33.19], bool PDh[62.77,70.99,95.35])
	return

'''
		expect = '''Program([FuncDecl(Id(jJrj), [VarDecl(Id(xB), ArrayType([41.01, 86.1, 2.43], NumberType), None, None), VarDecl(Id(Bib), ArrayType([72.58, 30.13, 33.19], NumberType), None, None), VarDecl(Id(PDh), ArrayType([62.77, 70.99, 95.35], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 350))

	def test_351(self):
		input = '''
func C_ (number w8oK[71.37])
	return
bool q3lB[17.75,5.93,29.03] <- 48.73
string mRYM[97.2] <- true
func sfM (string gf)
	return JZ5

'''
		expect = '''Program([FuncDecl(Id(C_), [VarDecl(Id(w8oK), ArrayType([71.37], NumberType), None, None)], Return()), VarDecl(Id(q3lB), ArrayType([17.75, 5.93, 29.03], BoolType), None, NumLit(48.73)), VarDecl(Id(mRYM), ArrayType([97.2], StringType), None, BooleanLit(True)), FuncDecl(Id(sfM), [VarDecl(Id(gf), StringType, None, None)], Return(Id(JZ5)))])'''
		self.assertTrue(TestAST.test(input, expect, 351))

	def test_352(self):
		input = '''
bool kb[55.07,92.42] <- "M"
func IaN_ ()	return

number TX[39.31,40.25,66.82] <- 20.2
bool Zp <- false
func NB ()	begin
		Sd_ <- true
		RkgJ("vTHK", "wA")
	end

'''
		expect = '''Program([VarDecl(Id(kb), ArrayType([55.07, 92.42], BoolType), None, StringLit(M)), FuncDecl(Id(IaN_), [], Return()), VarDecl(Id(TX), ArrayType([39.31, 40.25, 66.82], NumberType), None, NumLit(20.2)), VarDecl(Id(Zp), BoolType, None, BooleanLit(False)), FuncDecl(Id(NB), [], Block([AssignStmt(Id(Sd_), BooleanLit(True)), CallStmt(Id(RkgJ), [StringLit(vTHK), StringLit(wA)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 352))

	def test_353(self):
		input = '''
string PrbJ[47.5]
func BTH ()
	begin
		break
		return
	end
bool lv1[75.47]
func tg (string MIh2)
	return false
'''
		expect = '''Program([VarDecl(Id(PrbJ), ArrayType([47.5], StringType), None, None), FuncDecl(Id(BTH), [], Block([Break, Return()])), VarDecl(Id(lv1), ArrayType([75.47], BoolType), None, None), FuncDecl(Id(tg), [VarDecl(Id(MIh2), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 353))

	def test_354(self):
		input = '''
func kO6 (bool lGx2[19.89], number sz[9.98,72.71])	return GpX

'''
		expect = '''Program([FuncDecl(Id(kO6), [VarDecl(Id(lGx2), ArrayType([19.89], BoolType), None, None), VarDecl(Id(sz), ArrayType([9.98, 72.71], NumberType), None, None)], Return(Id(GpX)))])'''
		self.assertTrue(TestAST.test(input, expect, 354))

	def test_355(self):
		input = '''
var xE8 <- 95.12
number SUFo[59.78,19.46,50.92]
func mel (number Qw, bool GxJ, string tw)	return
func Wt (number JNL, bool zNE5[9.88])
	return

'''
		expect = '''Program([VarDecl(Id(xE8), None, var, NumLit(95.12)), VarDecl(Id(SUFo), ArrayType([59.78, 19.46, 50.92], NumberType), None, None), FuncDecl(Id(mel), [VarDecl(Id(Qw), NumberType, None, None), VarDecl(Id(GxJ), BoolType, None, None), VarDecl(Id(tw), StringType, None, None)], Return()), FuncDecl(Id(Wt), [VarDecl(Id(JNL), NumberType, None, None), VarDecl(Id(zNE5), ArrayType([9.88], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 355))

	def test_356(self):
		input = '''
bool VLy[42.78,66.73]
func m6 ()
	return

number hTui <- BK62
func wnca (bool Ns1[0.53], number lNS_[39.78,32.58], number ZJ6)
	return false

'''
		expect = '''Program([VarDecl(Id(VLy), ArrayType([42.78, 66.73], BoolType), None, None), FuncDecl(Id(m6), [], Return()), VarDecl(Id(hTui), NumberType, None, Id(BK62)), FuncDecl(Id(wnca), [VarDecl(Id(Ns1), ArrayType([0.53], BoolType), None, None), VarDecl(Id(lNS_), ArrayType([39.78, 32.58], NumberType), None, None), VarDecl(Id(ZJ6), NumberType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 356))

	def test_357(self):
		input = '''
func qLRE (string ADRb[82.36,6.7], string lB, string Kbn)	return 30.61

func D4F (bool QL[26.84,70.07])
	begin
	end
func Ow9y (number uZD)	return 31.97

'''
		expect = '''Program([FuncDecl(Id(qLRE), [VarDecl(Id(ADRb), ArrayType([82.36, 6.7], StringType), None, None), VarDecl(Id(lB), StringType, None, None), VarDecl(Id(Kbn), StringType, None, None)], Return(NumLit(30.61))), FuncDecl(Id(D4F), [VarDecl(Id(QL), ArrayType([26.84, 70.07], BoolType), None, None)], Block([])), FuncDecl(Id(Ow9y), [VarDecl(Id(uZD), NumberType, None, None)], Return(NumLit(31.97)))])'''
		self.assertTrue(TestAST.test(input, expect, 357))

	def test_358(self):
		input = '''
var sV4 <- true
'''
		expect = '''Program([VarDecl(Id(sV4), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 358))

	def test_359(self):
		input = '''
func mhO (number sep[19.84,15.2])
	begin
	end
func Fie (bool EW, number zcl[90.01,79.67])	return "Vm"

string HnbU
func i30Z ()
	begin
		return
	end

'''
		expect = '''Program([FuncDecl(Id(mhO), [VarDecl(Id(sep), ArrayType([19.84, 15.2], NumberType), None, None)], Block([])), FuncDecl(Id(Fie), [VarDecl(Id(EW), BoolType, None, None), VarDecl(Id(zcl), ArrayType([90.01, 79.67], NumberType), None, None)], Return(StringLit(Vm))), VarDecl(Id(HnbU), StringType, None, None), FuncDecl(Id(i30Z), [], Block([Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 359))

	def test_360(self):
		input = '''
string EE[1.68,30.17,92.46]
bool H187[80.73,65.14]
string QyXE[51.58,84.64,3.27] <- 66.67
'''
		expect = '''Program([VarDecl(Id(EE), ArrayType([1.68, 30.17, 92.46], StringType), None, None), VarDecl(Id(H187), ArrayType([80.73, 65.14], BoolType), None, None), VarDecl(Id(QyXE), ArrayType([51.58, 84.64, 3.27], StringType), None, NumLit(66.67))])'''
		self.assertTrue(TestAST.test(input, expect, 360))

	def test_361(self):
		input = '''
func WQ (string zCJ, bool NVT)
	return

'''
		expect = '''Program([FuncDecl(Id(WQ), [VarDecl(Id(zCJ), StringType, None, None), VarDecl(Id(NVT), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 361))

	def test_362(self):
		input = '''
func rz23 (string eL, string xfVk, string c6[75.61,40.74,24.45])	return 60.64
'''
		expect = '''Program([FuncDecl(Id(rz23), [VarDecl(Id(eL), StringType, None, None), VarDecl(Id(xfVk), StringType, None, None), VarDecl(Id(c6), ArrayType([75.61, 40.74, 24.45], StringType), None, None)], Return(NumLit(60.64)))])'''
		self.assertTrue(TestAST.test(input, expect, 362))

	def test_363(self):
		input = '''
func R_Od ()	begin
		string xxg[49.52,44.43,82.8]
		continue
		R5()
	end
func I9e (number P_)
	return kw3
func dQzq (bool HD, number jT)	return

'''
		expect = '''Program([FuncDecl(Id(R_Od), [], Block([VarDecl(Id(xxg), ArrayType([49.52, 44.43, 82.8], StringType), None, None), Continue, CallStmt(Id(R5), [])])), FuncDecl(Id(I9e), [VarDecl(Id(P_), NumberType, None, None)], Return(Id(kw3))), FuncDecl(Id(dQzq), [VarDecl(Id(HD), BoolType, None, None), VarDecl(Id(jT), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 363))

	def test_364(self):
		input = '''
number JBsb[13.7,83.7] <- 25.67
'''
		expect = '''Program([VarDecl(Id(JBsb), ArrayType([13.7, 83.7], NumberType), None, NumLit(25.67))])'''
		self.assertTrue(TestAST.test(input, expect, 364))

	def test_365(self):
		input = '''
func OIJW (number W3, string YT, bool vS[54.07,30.2,18.47])	return "d"
number tDyv[85.62,56.1] <- 55.63
func g3 (number soMl[8.93,78.21])	return

'''
		expect = '''Program([FuncDecl(Id(OIJW), [VarDecl(Id(W3), NumberType, None, None), VarDecl(Id(YT), StringType, None, None), VarDecl(Id(vS), ArrayType([54.07, 30.2, 18.47], BoolType), None, None)], Return(StringLit(d))), VarDecl(Id(tDyv), ArrayType([85.62, 56.1], NumberType), None, NumLit(55.63)), FuncDecl(Id(g3), [VarDecl(Id(soMl), ArrayType([8.93, 78.21], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 365))

	def test_366(self):
		input = '''
func lV5 ()
	return m0_W
'''
		expect = '''Program([FuncDecl(Id(lV5), [], Return(Id(m0_W)))])'''
		self.assertTrue(TestAST.test(input, expect, 366))

	def test_367(self):
		input = '''
bool JFM <- pCj
func eBV (bool Dg[2.26], bool Fa)	return

func vQ (bool EpK8[98.67,91.1,33.92], bool Oj[69.25,12.32,86.15], string aT[93.16,53.51])	begin
	end
func nXWD (bool wCo)	begin
		dynamic L_L
		continue
	end
number Ss <- 37.01
'''
		expect = '''Program([VarDecl(Id(JFM), BoolType, None, Id(pCj)), FuncDecl(Id(eBV), [VarDecl(Id(Dg), ArrayType([2.26], BoolType), None, None), VarDecl(Id(Fa), BoolType, None, None)], Return()), FuncDecl(Id(vQ), [VarDecl(Id(EpK8), ArrayType([98.67, 91.1, 33.92], BoolType), None, None), VarDecl(Id(Oj), ArrayType([69.25, 12.32, 86.15], BoolType), None, None), VarDecl(Id(aT), ArrayType([93.16, 53.51], StringType), None, None)], Block([])), FuncDecl(Id(nXWD), [VarDecl(Id(wCo), BoolType, None, None)], Block([VarDecl(Id(L_L), None, dynamic, None), Continue])), VarDecl(Id(Ss), NumberType, None, NumLit(37.01))])'''
		self.assertTrue(TestAST.test(input, expect, 367))

	def test_368(self):
		input = '''
number ghq
dynamic Fl
dynamic zS <- 10.94
string jd[8.5,99.27]
'''
		expect = '''Program([VarDecl(Id(ghq), NumberType, None, None), VarDecl(Id(Fl), None, dynamic, None), VarDecl(Id(zS), None, dynamic, NumLit(10.94)), VarDecl(Id(jd), ArrayType([8.5, 99.27], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 368))

	def test_369(self):
		input = '''
func V0 (number G1, number LW[24.28,72.76])	return
'''
		expect = '''Program([FuncDecl(Id(V0), [VarDecl(Id(G1), NumberType, None, None), VarDecl(Id(LW), ArrayType([24.28, 72.76], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 369))

	def test_370(self):
		input = '''
func uzb ()	begin
	end
string D2T[26.35]
dynamic ux2
func BtZ (string BOyd, string I0)	return 81.6

'''
		expect = '''Program([FuncDecl(Id(uzb), [], Block([])), VarDecl(Id(D2T), ArrayType([26.35], StringType), None, None), VarDecl(Id(ux2), None, dynamic, None), FuncDecl(Id(BtZ), [VarDecl(Id(BOyd), StringType, None, None), VarDecl(Id(I0), StringType, None, None)], Return(NumLit(81.6)))])'''
		self.assertTrue(TestAST.test(input, expect, 370))

	def test_371(self):
		input = '''
func Xho (string Co, number VNOm, string VH[26.24,21.75,70.76])
	return "F"
number yrT6[17.52]
'''
		expect = '''Program([FuncDecl(Id(Xho), [VarDecl(Id(Co), StringType, None, None), VarDecl(Id(VNOm), NumberType, None, None), VarDecl(Id(VH), ArrayType([26.24, 21.75, 70.76], StringType), None, None)], Return(StringLit(F))), VarDecl(Id(yrT6), ArrayType([17.52], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 371))

	def test_372(self):
		input = '''
bool bF[75.4] <- true
func PWH (string mAa, string i_X)	return

'''
		expect = '''Program([VarDecl(Id(bF), ArrayType([75.4], BoolType), None, BooleanLit(True)), FuncDecl(Id(PWH), [VarDecl(Id(mAa), StringType, None, None), VarDecl(Id(i_X), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 372))

	def test_373(self):
		input = '''
var uRCS <- 82.17
bool Xcm5[41.42] <- false
bool v3A[43.9,52.29]
bool IG[14.64] <- "OodQh"
'''
		expect = '''Program([VarDecl(Id(uRCS), None, var, NumLit(82.17)), VarDecl(Id(Xcm5), ArrayType([41.42], BoolType), None, BooleanLit(False)), VarDecl(Id(v3A), ArrayType([43.9, 52.29], BoolType), None, None), VarDecl(Id(IG), ArrayType([14.64], BoolType), None, StringLit(OodQh))])'''
		self.assertTrue(TestAST.test(input, expect, 373))

	def test_374(self):
		input = '''
func ml (bool zMN_[62.87,38.46])
	return

func nMXM (bool a39, string Y_k[10.92], string QoUS)
	return
func Lex ()
	begin
		break
		return 98.28
		vf()
	end
func lxW (string Cw[13.27], number waM[46.15])	begin
		wolt[true, zXGI, 45.04] <- vEx
		begin
		end
	end

string OX
'''
		expect = '''Program([FuncDecl(Id(ml), [VarDecl(Id(zMN_), ArrayType([62.87, 38.46], BoolType), None, None)], Return()), FuncDecl(Id(nMXM), [VarDecl(Id(a39), BoolType, None, None), VarDecl(Id(Y_k), ArrayType([10.92], StringType), None, None), VarDecl(Id(QoUS), StringType, None, None)], Return()), FuncDecl(Id(Lex), [], Block([Break, Return(NumLit(98.28)), CallStmt(Id(vf), [])])), FuncDecl(Id(lxW), [VarDecl(Id(Cw), ArrayType([13.27], StringType), None, None), VarDecl(Id(waM), ArrayType([46.15], NumberType), None, None)], Block([AssignStmt(ArrayCell(Id(wolt), [BooleanLit(True), Id(zXGI), NumLit(45.04)]), Id(vEx)), Block([])])), VarDecl(Id(OX), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 374))

	def test_375(self):
		input = '''
func TC ()
	return
func TeP (string qZ, number RyNC[31.13,44.79], number F7m)
	return
'''
		expect = '''Program([FuncDecl(Id(TC), [], Return()), FuncDecl(Id(TeP), [VarDecl(Id(qZ), StringType, None, None), VarDecl(Id(RyNC), ArrayType([31.13, 44.79], NumberType), None, None), VarDecl(Id(F7m), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 375))

	def test_376(self):
		input = '''
func qzb (number UR[70.74,45.6,23.18])
	begin
	end
func o6 (string WtS, number fM)	return 83.56
func TGug (bool Prb, number He)	begin
		continue
	end

var QW <- DA
'''
		expect = '''Program([FuncDecl(Id(qzb), [VarDecl(Id(UR), ArrayType([70.74, 45.6, 23.18], NumberType), None, None)], Block([])), FuncDecl(Id(o6), [VarDecl(Id(WtS), StringType, None, None), VarDecl(Id(fM), NumberType, None, None)], Return(NumLit(83.56))), FuncDecl(Id(TGug), [VarDecl(Id(Prb), BoolType, None, None), VarDecl(Id(He), NumberType, None, None)], Block([Continue])), VarDecl(Id(QW), None, var, Id(DA))])'''
		self.assertTrue(TestAST.test(input, expect, 376))

	def test_377(self):
		input = '''
func zSTG (number Gx, string nbaJ[31.99,14.85,33.29], string IBrO)	begin
		begin
			break
			for fvb9 until 69.17 by false
				number fb[50.43,88.67,18.9] <- 72.06
		end
	end
func jSqT (number Hk0)
	return

string kwd <- e0
func cxmX (bool zL, string dp)
	return h3g
'''
		expect = '''Program([FuncDecl(Id(zSTG), [VarDecl(Id(Gx), NumberType, None, None), VarDecl(Id(nbaJ), ArrayType([31.99, 14.85, 33.29], StringType), None, None), VarDecl(Id(IBrO), StringType, None, None)], Block([Block([Break, For(Id(fvb9), NumLit(69.17), BooleanLit(False), VarDecl(Id(fb), ArrayType([50.43, 88.67, 18.9], NumberType), None, NumLit(72.06)))])])), FuncDecl(Id(jSqT), [VarDecl(Id(Hk0), NumberType, None, None)], Return()), VarDecl(Id(kwd), StringType, None, Id(e0)), FuncDecl(Id(cxmX), [VarDecl(Id(zL), BoolType, None, None), VarDecl(Id(dp), StringType, None, None)], Return(Id(h3g)))])'''
		self.assertTrue(TestAST.test(input, expect, 377))

	def test_378(self):
		input = '''
string NYZI
func nXmb (number e4o7[15.19], string GD[5.69,24.53])
	begin
		Nyfh(jp, 85.71)
	end
number OfX0[25.71,1.35,86.89] <- true
func oYy (string OgiP, number kkvP[36.01], number wTWC)
	return
string ipV[98.22,88.3] <- false
'''
		expect = '''Program([VarDecl(Id(NYZI), StringType, None, None), FuncDecl(Id(nXmb), [VarDecl(Id(e4o7), ArrayType([15.19], NumberType), None, None), VarDecl(Id(GD), ArrayType([5.69, 24.53], StringType), None, None)], Block([CallStmt(Id(Nyfh), [Id(jp), NumLit(85.71)])])), VarDecl(Id(OfX0), ArrayType([25.71, 1.35, 86.89], NumberType), None, BooleanLit(True)), FuncDecl(Id(oYy), [VarDecl(Id(OgiP), StringType, None, None), VarDecl(Id(kkvP), ArrayType([36.01], NumberType), None, None), VarDecl(Id(wTWC), NumberType, None, None)], Return()), VarDecl(Id(ipV), ArrayType([98.22, 88.3], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 378))

	def test_379(self):
		input = '''
number ZFIZ
'''
		expect = '''Program([VarDecl(Id(ZFIZ), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 379))

	def test_380(self):
		input = '''
string uMp[79.42,13.65,58.89]
func AcbD (number XYhB[4.29,85.76,10.41], string stW1)	return false
func YH (bool do[75.69,19.24,56.69], bool RB6C[37.74], string ru)	return

func H9cG (bool kgBB)	return true

'''
		expect = '''Program([VarDecl(Id(uMp), ArrayType([79.42, 13.65, 58.89], StringType), None, None), FuncDecl(Id(AcbD), [VarDecl(Id(XYhB), ArrayType([4.29, 85.76, 10.41], NumberType), None, None), VarDecl(Id(stW1), StringType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(YH), [VarDecl(Id(do), ArrayType([75.69, 19.24, 56.69], BoolType), None, None), VarDecl(Id(RB6C), ArrayType([37.74], BoolType), None, None), VarDecl(Id(ru), StringType, None, None)], Return()), FuncDecl(Id(H9cG), [VarDecl(Id(kgBB), BoolType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 380))

	def test_381(self):
		input = '''
func QUk (number ZRZI, string UviR[4.64,52.57,93.51], number k2E)	return
func U1u (string P_PC, number XF[56.19])
	return
func fbY (number jejq)
	return 67.25
'''
		expect = '''Program([FuncDecl(Id(QUk), [VarDecl(Id(ZRZI), NumberType, None, None), VarDecl(Id(UviR), ArrayType([4.64, 52.57, 93.51], StringType), None, None), VarDecl(Id(k2E), NumberType, None, None)], Return()), FuncDecl(Id(U1u), [VarDecl(Id(P_PC), StringType, None, None), VarDecl(Id(XF), ArrayType([56.19], NumberType), None, None)], Return()), FuncDecl(Id(fbY), [VarDecl(Id(jejq), NumberType, None, None)], Return(NumLit(67.25)))])'''
		self.assertTrue(TestAST.test(input, expect, 381))

	def test_382(self):
		input = '''
func bP ()
	return true

'''
		expect = '''Program([FuncDecl(Id(bP), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 382))

	def test_383(self):
		input = '''
dynamic TdJ3 <- 8.96
number rCoL[3.55] <- hXdn
bool sbtp[38.04,61.44] <- 72.86
bool dw
string Nx <- false
'''
		expect = '''Program([VarDecl(Id(TdJ3), None, dynamic, NumLit(8.96)), VarDecl(Id(rCoL), ArrayType([3.55], NumberType), None, Id(hXdn)), VarDecl(Id(sbtp), ArrayType([38.04, 61.44], BoolType), None, NumLit(72.86)), VarDecl(Id(dw), BoolType, None, None), VarDecl(Id(Nx), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 383))

	def test_384(self):
		input = '''
number f8HY[32.53]
string kJD[61.87,35.61] <- "Jqj"
func MYYg ()
	return

'''
		expect = '''Program([VarDecl(Id(f8HY), ArrayType([32.53], NumberType), None, None), VarDecl(Id(kJD), ArrayType([61.87, 35.61], StringType), None, StringLit(Jqj)), FuncDecl(Id(MYYg), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 384))

	def test_385(self):
		input = '''
var Yb <- false
var Mo <- R5A
number yI[9.27,34.97,1.73] <- 6.38
'''
		expect = '''Program([VarDecl(Id(Yb), None, var, BooleanLit(False)), VarDecl(Id(Mo), None, var, Id(R5A)), VarDecl(Id(yI), ArrayType([9.27, 34.97, 1.73], NumberType), None, NumLit(6.38))])'''
		self.assertTrue(TestAST.test(input, expect, 385))

	def test_386(self):
		input = '''
func Yqe4 (number VVD, string swbT)	return

string ii[47.11,27.93,43.21]
func Ci (number zp[92.21])	begin
		wqj[j6XK, Hu, "Wmfh"] <- hgPr
		jHu <- ug
		break
	end
number YIil[7.65,29.31,82.6]
'''
		expect = '''Program([FuncDecl(Id(Yqe4), [VarDecl(Id(VVD), NumberType, None, None), VarDecl(Id(swbT), StringType, None, None)], Return()), VarDecl(Id(ii), ArrayType([47.11, 27.93, 43.21], StringType), None, None), FuncDecl(Id(Ci), [VarDecl(Id(zp), ArrayType([92.21], NumberType), None, None)], Block([AssignStmt(ArrayCell(Id(wqj), [Id(j6XK), Id(Hu), StringLit(Wmfh)]), Id(hgPr)), AssignStmt(Id(jHu), Id(ug)), Break])), VarDecl(Id(YIil), ArrayType([7.65, 29.31, 82.6], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 386))

	def test_387(self):
		input = '''
bool fq <- true
dynamic mRc <- 13.42
func dWuq ()	return "KEbn"
func Jqi (number SW)
	return kYNq

dynamic Dq <- LIF
'''
		expect = '''Program([VarDecl(Id(fq), BoolType, None, BooleanLit(True)), VarDecl(Id(mRc), None, dynamic, NumLit(13.42)), FuncDecl(Id(dWuq), [], Return(StringLit(KEbn))), FuncDecl(Id(Jqi), [VarDecl(Id(SW), NumberType, None, None)], Return(Id(kYNq))), VarDecl(Id(Dq), None, dynamic, Id(LIF))])'''
		self.assertTrue(TestAST.test(input, expect, 387))

	def test_388(self):
		input = '''
func yXl (bool EuB, number DCc[52.4,91.74,11.03])	return true

bool JqZU[60.56]
string fFOG[48.99,50.0,51.73] <- "nC"
'''
		expect = '''Program([FuncDecl(Id(yXl), [VarDecl(Id(EuB), BoolType, None, None), VarDecl(Id(DCc), ArrayType([52.4, 91.74, 11.03], NumberType), None, None)], Return(BooleanLit(True))), VarDecl(Id(JqZU), ArrayType([60.56], BoolType), None, None), VarDecl(Id(fFOG), ArrayType([48.99, 50.0, 51.73], StringType), None, StringLit(nC))])'''
		self.assertTrue(TestAST.test(input, expect, 388))

	def test_389(self):
		input = '''
dynamic nP
number OLct
number iFu[4.38,34.13]
dynamic E_sq <- true
'''
		expect = '''Program([VarDecl(Id(nP), None, dynamic, None), VarDecl(Id(OLct), NumberType, None, None), VarDecl(Id(iFu), ArrayType([4.38, 34.13], NumberType), None, None), VarDecl(Id(E_sq), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 389))

	def test_390(self):
		input = '''
bool mVGm[89.17,13.8] <- 29.43
func MoRf (number ZdF3[22.18,89.72], bool uT0M)
	return "E"
func uO0 ()	return false
'''
		expect = '''Program([VarDecl(Id(mVGm), ArrayType([89.17, 13.8], BoolType), None, NumLit(29.43)), FuncDecl(Id(MoRf), [VarDecl(Id(ZdF3), ArrayType([22.18, 89.72], NumberType), None, None), VarDecl(Id(uT0M), BoolType, None, None)], Return(StringLit(E))), FuncDecl(Id(uO0), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 390))

	def test_391(self):
		input = '''
string viuW <- false
string TLe[60.89] <- false
number uvK[21.66]
'''
		expect = '''Program([VarDecl(Id(viuW), StringType, None, BooleanLit(False)), VarDecl(Id(TLe), ArrayType([60.89], StringType), None, BooleanLit(False)), VarDecl(Id(uvK), ArrayType([21.66], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 391))

	def test_392(self):
		input = '''
func a5 (bool Rb_4, number jA[54.07], number Tzf)	return 91.46

func Sw ()
	return false
'''
		expect = '''Program([FuncDecl(Id(a5), [VarDecl(Id(Rb_4), BoolType, None, None), VarDecl(Id(jA), ArrayType([54.07], NumberType), None, None), VarDecl(Id(Tzf), NumberType, None, None)], Return(NumLit(91.46))), FuncDecl(Id(Sw), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 392))

	def test_393(self):
		input = '''
func FAm (bool gc)	begin
	end

func MTfQ ()
	return

func Yj (number xbM[91.03])	return
func Gg2C ()
	begin
		if (true)
		begin
		end
		elif (97.51)
		begin
		end
		elif (true) if (true)
		n1lP[true, true] <- false
		elif (n_AH)
		for C0 until "Ol" by DHvH
			return true
		elif (BY)
		Yk("qySJM", 33.4, DGu)
		elif (58.09)
		dynamic kTHj <- false
		elif (true) Nz <- HW
		else string iA[67.51,84.87,82.18]
		elif (false)
		continue
	end

string wnAv[84.53,10.74,16.19]
'''
		expect = '''Program([FuncDecl(Id(FAm), [VarDecl(Id(gc), BoolType, None, None)], Block([])), FuncDecl(Id(MTfQ), [], Return()), FuncDecl(Id(Yj), [VarDecl(Id(xbM), ArrayType([91.03], NumberType), None, None)], Return()), FuncDecl(Id(Gg2C), [], Block([If((BooleanLit(True), Block([])), [(NumLit(97.51), Block([])), (BooleanLit(True), If((BooleanLit(True), AssignStmt(ArrayCell(Id(n1lP), [BooleanLit(True), BooleanLit(True)]), BooleanLit(False))), [(Id(n_AH), For(Id(C0), StringLit(Ol), Id(DHvH), Return(BooleanLit(True)))), (Id(BY), CallStmt(Id(Yk), [StringLit(qySJM), NumLit(33.4), Id(DGu)])), (NumLit(58.09), VarDecl(Id(kTHj), None, dynamic, BooleanLit(False))), (BooleanLit(True), AssignStmt(Id(Nz), Id(HW)))], VarDecl(Id(iA), ArrayType([67.51, 84.87, 82.18], StringType), None, None))), (BooleanLit(False), Continue)], None)])), VarDecl(Id(wnAv), ArrayType([84.53, 10.74, 16.19], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 393))

	def test_394(self):
		input = '''
func xEw (bool IyoY, string ynY[14.72], string ub[72.79,27.76])	begin
		for HBu until true by 43.85
			Z9(false)
	end
number Q1ax <- false
'''
		expect = '''Program([FuncDecl(Id(xEw), [VarDecl(Id(IyoY), BoolType, None, None), VarDecl(Id(ynY), ArrayType([14.72], StringType), None, None), VarDecl(Id(ub), ArrayType([72.79, 27.76], StringType), None, None)], Block([For(Id(HBu), BooleanLit(True), NumLit(43.85), CallStmt(Id(Z9), [BooleanLit(False)]))])), VarDecl(Id(Q1ax), NumberType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 394))

	def test_395(self):
		input = '''
number qa
func El (string BkUR, bool ZHR)	return ut
number GVv[25.03,29.41,2.13] <- "wjuV"
string cRDZ
func JZzm (number nz0G[94.77,10.23,0.94], bool BS_, bool bonc)
	begin
		break
		Qt(true)
		Pdt[42.68, true] <- 4.85
	end

'''
		expect = '''Program([VarDecl(Id(qa), NumberType, None, None), FuncDecl(Id(El), [VarDecl(Id(BkUR), StringType, None, None), VarDecl(Id(ZHR), BoolType, None, None)], Return(Id(ut))), VarDecl(Id(GVv), ArrayType([25.03, 29.41, 2.13], NumberType), None, StringLit(wjuV)), VarDecl(Id(cRDZ), StringType, None, None), FuncDecl(Id(JZzm), [VarDecl(Id(nz0G), ArrayType([94.77, 10.23, 0.94], NumberType), None, None), VarDecl(Id(BS_), BoolType, None, None), VarDecl(Id(bonc), BoolType, None, None)], Block([Break, CallStmt(Id(Qt), [BooleanLit(True)]), AssignStmt(ArrayCell(Id(Pdt), [NumLit(42.68), BooleanLit(True)]), NumLit(4.85))]))])'''
		self.assertTrue(TestAST.test(input, expect, 395))

	def test_396(self):
		input = '''
number yL0[72.49,15.37,39.98]
func aO (string J3T)	begin
		rc("ItUB", "CMNhO")
		begin
			break
			mFy <- "vXzKR"
		end
	end

'''
		expect = '''Program([VarDecl(Id(yL0), ArrayType([72.49, 15.37, 39.98], NumberType), None, None), FuncDecl(Id(aO), [VarDecl(Id(J3T), StringType, None, None)], Block([CallStmt(Id(rc), [StringLit(ItUB), StringLit(CMNhO)]), Block([Break, AssignStmt(Id(mFy), StringLit(vXzKR))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 396))

	def test_397(self):
		input = '''
dynamic Sl3l <- true
func Tr9 (bool B60[15.41,23.66,27.77], string WwzK)
	begin
		dDr <- WO
		if (57.69)
		Ckm("WIhM", "OYA", 18.29)
		elif (true)
		continue
		elif (false)
		begin
			if (Dm_u)
			IyI[wCFj] <- "i"
			elif (75.37) break
			elif (CEpk) string YR <- "RqYSP"
			elif (xr) for R5Jt until 33.9 by 85.19
				for degu until true by Mw3l
					BSIG[4.05, 21.07, "FmcVi"] <- 40.9
			elif (false) break
			else continue
		end
		elif (qSJ)
		for m5 until 76.72 by true
			for wt until false by 65.85
				return yP
		else return tEd1
		number c3
	end

'''
		expect = '''Program([VarDecl(Id(Sl3l), None, dynamic, BooleanLit(True)), FuncDecl(Id(Tr9), [VarDecl(Id(B60), ArrayType([15.41, 23.66, 27.77], BoolType), None, None), VarDecl(Id(WwzK), StringType, None, None)], Block([AssignStmt(Id(dDr), Id(WO)), If((NumLit(57.69), CallStmt(Id(Ckm), [StringLit(WIhM), StringLit(OYA), NumLit(18.29)])), [(BooleanLit(True), Continue), (BooleanLit(False), Block([If((Id(Dm_u), AssignStmt(ArrayCell(Id(IyI), [Id(wCFj)]), StringLit(i))), [(NumLit(75.37), Break), (Id(CEpk), VarDecl(Id(YR), StringType, None, StringLit(RqYSP))), (Id(xr), For(Id(R5Jt), NumLit(33.9), NumLit(85.19), For(Id(degu), BooleanLit(True), Id(Mw3l), AssignStmt(ArrayCell(Id(BSIG), [NumLit(4.05), NumLit(21.07), StringLit(FmcVi)]), NumLit(40.9))))), (BooleanLit(False), Break)], Continue)])), (Id(qSJ), For(Id(m5), NumLit(76.72), BooleanLit(True), For(Id(wt), BooleanLit(False), NumLit(65.85), Return(Id(yP)))))], Return(Id(tEd1))), VarDecl(Id(c3), NumberType, None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 397))

	def test_398(self):
		input = '''
number dV
func CZ (bool mC[33.97,15.05], number E7V)	begin
		begin
			for GPu8 until 13.4 by "FmW"
				if (false)
				begin
				end
				elif (true) if (10.26) if ("t")
				if (false)
				return "jpH"
				elif (YDQ2)
				return zTKt
				elif (true)
				if (Enbv)
				bool YxG
				else bool fq8v[47.57,69.45] <- 46.6
				elif ("FdVTI")
				for B9y until 68.45 by IpP
					qfL(W7ZG, "qTe", u9)
				elif (true)
				for OZ until 8.07 by "qLc"
					return EtF
				elif (Smn) continue
				elif (true)
				if (B9) return
				elif (53.62) continue
				else begin
					continue
					for d5w8 until pv9 by true
						begin
						end
				end
				elif (12.32)
				TLM[true] <- "wbpSW"
			break
		end
		begin
			pxZz <- false
			return
		end
		WhXh("uHBYf")
	end

func jQ21 (number Q6ce[48.06,11.2], bool g9qg[16.98,78.93,69.78], bool sau)
	return 5.31

'''
		expect = '''Program([VarDecl(Id(dV), NumberType, None, None), FuncDecl(Id(CZ), [VarDecl(Id(mC), ArrayType([33.97, 15.05], BoolType), None, None), VarDecl(Id(E7V), NumberType, None, None)], Block([Block([For(Id(GPu8), NumLit(13.4), StringLit(FmW), If((BooleanLit(False), Block([])), [(BooleanLit(True), If((NumLit(10.26), If((StringLit(t), If((BooleanLit(False), Return(StringLit(jpH))), [(Id(YDQ2), Return(Id(zTKt))), (BooleanLit(True), If((Id(Enbv), VarDecl(Id(YxG), BoolType, None, None)), [], VarDecl(Id(fq8v), ArrayType([47.57, 69.45], BoolType), None, NumLit(46.6)))), (StringLit(FdVTI), For(Id(B9y), NumLit(68.45), Id(IpP), CallStmt(Id(qfL), [Id(W7ZG), StringLit(qTe), Id(u9)]))), (BooleanLit(True), For(Id(OZ), NumLit(8.07), StringLit(qLc), Return(Id(EtF)))), (Id(Smn), Continue), (BooleanLit(True), If((Id(B9), Return()), [(NumLit(53.62), Continue)], Block([Continue, For(Id(d5w8), Id(pv9), BooleanLit(True), Block([]))]))), (NumLit(12.32), AssignStmt(ArrayCell(Id(TLM), [BooleanLit(True)]), StringLit(wbpSW)))], None)), [], None)), [], None))], None)), Break]), Block([AssignStmt(Id(pxZz), BooleanLit(False)), Return()]), CallStmt(Id(WhXh), [StringLit(uHBYf)])])), FuncDecl(Id(jQ21), [VarDecl(Id(Q6ce), ArrayType([48.06, 11.2], NumberType), None, None), VarDecl(Id(g9qg), ArrayType([16.98, 78.93, 69.78], BoolType), None, None), VarDecl(Id(sau), BoolType, None, None)], Return(NumLit(5.31)))])'''
		self.assertTrue(TestAST.test(input, expect, 398))

	def test_399(self):
		input = '''
func HDG (bool opH[41.64,4.46])	return

string gM4[80.0,3.14,51.05]
'''
		expect = '''Program([FuncDecl(Id(HDG), [VarDecl(Id(opH), ArrayType([41.64, 4.46], BoolType), None, None)], Return()), VarDecl(Id(gM4), ArrayType([80.0, 3.14, 51.05], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 399))

	def test_400(self):
		input = '''
bool bVy
func VxX (bool RN9)
	return "C"

bool mGhh
func Atf (string l59h[7.72])	return "b"

func loh (number jQ4s[63.01,63.28], bool U_Z)
	return
'''
		expect = '''Program([VarDecl(Id(bVy), BoolType, None, None), FuncDecl(Id(VxX), [VarDecl(Id(RN9), BoolType, None, None)], Return(StringLit(C))), VarDecl(Id(mGhh), BoolType, None, None), FuncDecl(Id(Atf), [VarDecl(Id(l59h), ArrayType([7.72], StringType), None, None)], Return(StringLit(b))), FuncDecl(Id(loh), [VarDecl(Id(jQ4s), ArrayType([63.01, 63.28], NumberType), None, None), VarDecl(Id(U_Z), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 400))
