import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_201(self):
		input = '''
func GZ (dynamic uzna[587.235,79.184,22], bool PRZW, dynamic QuQd)
	return

func MSv (var ps, bool Gc[53E23], bool Pr[7])	begin
		begin
		end
	end

## M<nVy,n.^B|
func MtIl (var uj[2e31,8.234,89.609], string rCVw[19.742e78], dynamic Dm)	return

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 201))

	def test_202(self):
		input = '''
dynamic TFHq
## t
func i0 (dynamic WA5_[860.948E73,196e74], var ofh)
	begin
		continue
		break
	end
bool Jig[49] <- "r'""
'''
		expect = '''Error on line 4 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 202))

	def test_203(self):
		input = '''
string L8 ## Yk}Vx~%I4|M_A<tG$
func ep (bool hY)
	begin
		## 7
		##  >
		## OnC=OX%6A
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 203))

	def test_204(self):
		input = '''
## -hjp:eh
bool HD1j[75.199E+59,505E20] <- Ry[false, "'"", 29]
func nm (dynamic OYH)	return rdwr

'''
		expect = '''Error on line 4 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 204))

	def test_205(self):
		input = '''
var pv[3E94] <- Co ## 9StJ[BK
dynamic hp[96.385] <- true
## 7!h)Kq=
string Q7O6[813.121e76] <- true
dynamic i0 <- "'"~r" ## i0}
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 205))

	def test_206(self):
		input = '''
bool jLE[96E-83,33,6.119] <- 875e-40 ## Gb<&`8Sg!o2F.v!oo
func kOu (dynamic pPw[5,70e+88])
	return

'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 206))

	def test_207(self):
		input = '''
func A0 (number T4r[0,836E-85], number N4V[46.289E+80,86e+75])
	begin
		dynamic RP[484.836,25.076e+02]
		## [~ZyiE
		break
	end
## q*
number g3 <- nEf ## :{s!@tAX5]p
'''
		expect = '''Error on line 4 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 207))

	def test_208(self):
		input = '''
func RB5 (bool GJg[999,1.044,852E+29], string Vw, number POpH[6.634e+24])	begin
		## p=:MRgU%X+Ym!8(|"sbK
	end
## ?(7ub
func S9 (var LjM6, bool ZcT2)
	return " '"/2%"
'''
		expect = '''Error on line 6 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 208))

	def test_209(self):
		input = '''
bool VjwE[2] <- 132e+82
## GFB9./]RE"|10}o7#J
## vq7Cq}K.dsNqg@a
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 209))

	def test_210(self):
		input = '''
## u8|ZhV/dSI6$+@z_
## |@k]@mep@o>=gb*"|;+N
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 210))

	def test_211(self):
		input = '''
bool Cz[12e+70,78E+77,8e-60] ## %!N)R{8e-gs A4^5e6L
## 4Cini2qPa
## OeT%9BNOt2;u:&{
func BZ (dynamic y4sC[870,0], number zBL, dynamic o09A)	return AbZ

'''
		expect = '''Error on line 5 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 211))

	def test_212(self):
		input = '''
## n29@
## NL|sC4MQ1Pytj
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 212))

	def test_213(self):
		input = '''
number ONH
dynamic zeo[8.041,9,95] <- 8.308E+09 ## ",Hdc$%VZ!YO7Ez*C4
bool hxCh
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 213))

	def test_214(self):
		input = '''
string Boxh ## ,o,7<
func PSBS (bool Ap[58E-83,619.569], string nb, bool n0G)
	return "'"'"!'""

## _t|JHGL+h(DY
## ]^NRRLU*UEj U#
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 214))

	def test_215(self):
		input = '''
## ">EUPj
## fO.8{Ho2L:4?Q7U#iE,
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 215))

	def test_216(self):
		input = '''
## ,xw:
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 216))

	def test_217(self):
		input = '''

func Dzw (number rXX)	begin
		break
		for zJ until 48.83 by false
			WT(9.89, "X", Qd)
		if (true)
		continue
		elif (true)
		if (false) F_()
		elif (26.7)
		for R6 until gWlU by 82.97
			var YTSg <- true
		elif (37.13)
		number KDz
		else if (true)
		begin
			CxY()
			CV(VM)
		end
		elif (EMs6) Jd <- 58.03
		elif ("mXesV")
		bool WGhR <- 75.43
		elif ("JbH") break
		elif (85.28) if (true)
		ksk <- 57.49
		elif (25.41) begin
			break
			return
			begin
				gc()
				if (80.05) for dD until 5.47 by 36.37
					continue
				elif (32.0) break
				elif (Tn)
				begin
					n0vu(xM)
					return
				end
				elif (false)
				for iKY until "atxYp" by "eF"
					dynamic ozzg
				elif (88.43) if (11.84)
				break
				elif (uUvl) Kj9D <- "c"
				elif (lH)
				continue
				elif ("EB")
				break
				elif ("fEDLz")
				string BWe[98.87,0.41]
				elif (99.27)
				whP("b", cNS, 98.58)
				else continue
				elif (true)
				break
				JOzP("lIaN", "n", true)
			end
		end
		elif (Uw) continue
		elif (XJ) begin
			if ("YAO")
			break
			elif (ONsr) Me <- BSV
			elif (17.18)
			if (true)
			continue
			elif ("xnhH")
			for DZw until true by 15.4
				VPq <- "K"
			elif (51.07)
			begin
				begin
				end
				for id until false by "rnL"
					for ZrX until "IsE" by 75.12
						if (H0)
						begin
							begin
							end
						end
						elif ("A")
						if (true) N7jx <- qdJL
						elif ("noFh") zuce <- TF
						elif (aBQ3) if (true)
						continue
						elif (true) begin
							Td()
							if ("Iw")
							continue
							elif (46.21)
							continue
							elif (28.65)
							return NFQ
							elif ("V") continue
							elif ("Fzeox") begin
								begin
								end
								bool AWgQ[55.51,35.62]
								if (14.04) continue
								elif (true) continue
								elif (false)
								return
								elif ("K") string vKLm[52.13]
								elif (YH_)
								continue
							end
							for bY until Vi3R by zumQ
								var ETg <- "PDArI"
						end
						elif (yaPX)
						string xT
						elif (false) break
						elif ("Xa")
						for fZ until EtR by 47.78
							for D3Vv until g_0Y by "x"
								if (nuyH) begin
									if (96.02)
									hbg[ppDB, true] <- QTBT
									else for Bml until JdK by false
										return 88.8
								end
								elif ("ZDY")
								Rp3e()
								elif (Hpm) vxj("eB", "z")
								elif (4.61)
								begin
									U3I <- "tg"
								end
								elif (false)
								return
								elif (zp) continue
								else begin
									for qIFn until "q" by 4.17
										begin
											break
										end
								end
						elif ("QwXuJ")
						R4(gl, gq3h)
						elif (92.59)
						continue
						elif ("R")
						ClQ <- false
						elif (false)
						continue
						elif ("VMdYf") if (MztO)
						begin
							break
							continue
						end
						else wHSt[false] <- 5.69
			end
			elif (53.09)
			xH0i <- 13.49
			elif (16.89)
			for NV until XkV9 by false
				return
			elif ("S")
			continue
			else return
			elif (false)
			bool rAaY[56.21,63.36] <- true
			elif (true) begin
				for sX9 until mVl by "N"
					cs[false, false] <- 51.15
				return
			end
			else if (dEcc) for xaw until "u" by "MxU"
				break
			elif (89.95)
			bool tSZ
			elif ("apQBr")
			continue
			elif (hz)
			continue
			else break
		end
		elif (false) break
		elif ("zor")
		continue
		elif (VNFW)
		for GJI until XR9R by false
			var mml <- "HCvI"
		else string AJvv[61.44,41.91] <- Xp
	end
func Gyb (bool Op1)
	return dtn
number uM <- sX
func AyaO ()	begin
		ZM9Q(18.19, false, 63.93)
	end

string nGgQ

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 217))

	def test_218(self):
		input = '''
bool PfjE[73e+28] <- false ## ll
dynamic nro
func mtv (string cS44)	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 218))

	def test_219(self):
		input = '''
var ax[2e-89] <- v5
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 219))

	def test_220(self):
		input = '''
dynamic kcu ## K{ru5~bNuqotG
## CJw3
## J
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 220))

	def test_221(self):
		input = '''
func GMu (var ic[999e+86,4], string ZcHQ[3,74])	return
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 221))

	def test_222(self):
		input = '''
func qje (string Xn[65.924E-70])
	return 22

## 6`7Az%^b,LWaXBR7&y
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 222))

	def test_223(self):
		input = '''
func AQHw (bool uMz[1,70E-22,84.641e70])
	begin
		for L5 until V0GU by 93e+78
			break
		## 6Hr
		## s@h>Or].2?0eD>
	end

func bq (string sZQR, bool Tmg_)	begin
		## DJ
		var Ow
		## k(lbd_
	end

string EZeJ[1.957E-96,39.614,61.862E-25] <- "'"" ## B~M|*~7OO^Z/oQ
'''
		expect = '''Error on line 12 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 223))

	def test_224(self):
		input = '''
func qHNV ()	return
func P8OS (dynamic fs0[5], var xnFp)	return
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 224))

	def test_225(self):
		input = '''
## B
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 225))

	def test_226(self):
		input = '''
func Pyw (string Q1[6.616e-52,9.697E35,2e-97], var Zz)	begin
		## 0S"[ ym]+:u!$e}
		break
	end

'''
		expect = '''Error on line 2 col 47: var'''
		self.assertTrue(TestParser.test(input, expect, 226))

	def test_227(self):
		input = '''
func A18 (number Pp[25.437,462.908E71,448E+27], string xgRU[773e+07])
	return

func TiM0 (var GMPx, string vI)
	return
'''
		expect = '''Error on line 5 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 227))

	def test_228(self):
		input = '''
number Gqi[5,6e+47,78e96]
string foe <- zPNf
## DUn(/{@#a;/T?,qDY
## S.0IUibm
## :gLj"(ey
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 228))

	def test_229(self):
		input = '''
## i/<Vsw{sg;dbc"gEXa|
func Jb (var P8sQ[57.478E-21], var p3d[96.334,38e+52,190], string EpI[49])
	return "0'"Z'""
'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 229))

	def test_230(self):
		input = '''
## PWkF^@[P
## o=Ht&"CSs$qc9|~H
var JTs[68E-14] ## :d
func IY (string N3j, string VaQ[6.064e32,6E55,29.014E45])
	return 74
func tdx (string x2I, string a9U[45], bool Pm1)
	return "'"@'""

'''
		expect = '''Error on line 4 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 230))

	def test_231(self):
		input = '''
string Kj[6E-16,2.137e22] ## wQ|k(oPt )z!#B[2:Co
func Rr ()
	begin
		begin
			## ST|c3sv_nW
			return
			continue
		end
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 231))

	def test_232(self):
		input = '''
func MZC ()
	begin
		for D2 until EV by "'"'"AN"
			return lC
		## BHwbp^>"j}H+.9
	end
func ECFx (var xb)	begin
		## dszOFj3#m0,c-H+g{nXq
		## rE?.]H2YcwDd^Fd"+
		continue
	end

'''
		expect = '''Error on line 8 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 232))

	def test_233(self):
		input = '''
func PBu (var OzHM[255.733], string vp[1.834e-22], dynamic ifH)	return

## rM{m-z):g/5Jk
func Kv7 (bool Dc[1,399.986e-94], string I1B[67E29,5.424], number OE4[82.129e+66])
	return

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 233))

	def test_234(self):
		input = '''
var Kaj4 <- pGX
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 234))

	def test_235(self):
		input = '''
bool c5MK[950E09,283.857]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 235))

	def test_236(self):
		input = '''
dynamic nj[41,54.146E-22] <- TF8e ## Q[0k}gJm8m~$L
## WdUt20%
bool wAv ## 2!7CS=q8er<d+Wf$
func ZaLZ (string Q_p, dynamic Srb[0.127E-06,14], bool qTik[595,99.423])
	begin
	end

## u<Px-otL_78~b[X("wE
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 236))

	def test_237(self):
		input = '''
dynamic Cuw <- "'"" ## X.!
## xXuWaN3mH[bz]N>&
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 237))

	def test_238(self):
		input = '''
bool dJ0[4] ## "!EMy0nUgOk^]s<J
func sI (string tR, dynamic p4[925], dynamic QIX[3.377E-15,0E76,47.626])
	return
bool aKuq <- false
'''
		expect = '''Error on line 3 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 238))

	def test_239(self):
		input = '''
## sJ
func LQX ()	begin
		if (false)
		for NM until zaK by roA
			DC2("'"v'"W")
		elif ("K'"'"u")
		return
		elif (kK)
		break
		elif (true) for oOtD until 401e25 by false
			UXzH <- "'"'"_A"
		string I81 ## Q#/c+^
	end
## z%la+PE*XGZCpR2p_1i}
dynamic p8P[4.676e+23,36] ## Dlt"X8npvv
func cbmN (string na[3.694,241e+00,11e-34])
	return

'''
		expect = '''Error on line 16 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 239))

	def test_240(self):
		input = '''
var To8z
string hX <- Q7l
## {q}0
var KHm[208,615,317]
## M8:L.cAFN
'''
		expect = '''Error on line 2 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 240))

	def test_241(self):
		input = '''
bool R8a4[414.338] <- 70.630E-66 ## 1j;}6ZzjZn8seE
## 1yJ#[m52f
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 241))

	def test_242(self):
		input = '''
## )4PH;,Yd99HdV(}~
## 3)uh
number YZ <- Fc ## #3aY1b8J-0w;FL[
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 242))

	def test_243(self):
		input = '''
bool DkN <- "H(p" ## %K
number URZF <- Q7UB
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 243))

	def test_244(self):
		input = '''
## H3p7
var Z8 <- 42e-29
## ."ER8S%?lf![6uy=<
## aaU.?#R~V3"g.A&_/
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 244))

	def test_245(self):
		input = '''
dynamic s0b ## 1,*jzL*|1p0`gH}?P
func aIj (number Pj)	return

func Ty ()	begin
	end
func BeDg (string PhM, var RTzW, dynamic Nm[8E38,97.821E54,67.759])	return
'''
		expect = '''Error on line 7 col 23: var'''
		self.assertTrue(TestParser.test(input, expect, 245))

	def test_246(self):
		input = '''
func bU_p (bool pWL, string fG22[707e57])	begin
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 246))

	def test_247(self):
		input = '''
number l1O <- "E'"'">" ## 146Heg:
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 247))

	def test_248(self):
		input = '''
## }P4{u
## Nb
## "}ax<|R*/s.Il
dynamic f_Ts[49.989E58] <- true ## azLzkkq<e>0pWaRK
'''
		expect = '''Error on line 5 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 248))

	def test_249(self):
		input = '''
## GjC}hWo
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 249))

	def test_250(self):
		input = '''
func bxg ()
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 250))

	def test_251(self):
		input = '''
func lqvS ()	begin
	end
string pYgk <- false ## 6/`+]iD
## -*HtQB%<}x2w8p(3|5/o
func fM1 (dynamic kQM, dynamic ut, string Ny)	begin
		continue
		##  h#yyFEZI-G
	end

'''
		expect = '''Error on line 6 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 251))

	def test_252(self):
		input = '''
func g0 (var uTvE[522.923e-76], bool xTu[737e-93,491.113e-64], bool nT[631])
	return "s'""

func Rj4 (dynamic dDo[7.614E+69])	return "v.`'""
var GVUS[64.185e-92]
func JgRa (bool veF, var G9[26,0], var R5l[858E+53])
	begin
		## G?@
		continue
	end
## 01WEo0{"vo3
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 252))

	def test_253(self):
		input = '''
number eg[261.828e69] ## pcF?:)*_p*5Q]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 253))

	def test_254(self):
		input = '''
number Mc <- false
## Kl%o
## np3uW58[jmmd@-LAIry
var O4C ## &HTPj9;W`YmA[<
'''
		expect = '''Error on line 5 col 25: 
'''
		self.assertTrue(TestParser.test(input, expect, 254))

	def test_255(self):
		input = '''
## %N
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 255))

	def test_256(self):
		input = '''
func tb ()	begin
		if (soBd) continue
		elif (ma)
		return 146E74
		elif (false)
		break
	end

var zR <- PXR ## z?$E?REl"%>w
number oPWt ## gGw+co[k)e{sqU
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 256))

	def test_257(self):
		input = '''
dynamic YJvM[6.927E-48,97E-01,8]
func xT ()	begin
		break
		## %CY^<6D, %_KQMU?
		## *V*
	end

var r4t ## GU,yfUGh|nj2{t]
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 257))

	def test_258(self):
		input = '''
## ZFR^y
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 258))

	def test_259(self):
		input = '''
## V5LQ~fghu4 gfp/KgQgF
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 259))

	def test_260(self):
		input = '''
## j4@M#kkf >:a.AWx
## }]O.O)qmE,0r}%PoUW#U
## ^3@QoQ!
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 260))

	def test_261(self):
		input = '''
var C7 <- "'"*"
func qu (number ypI[948E+31,31.812])
	begin
		## hA_5U$ExCFc?NpDb
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 261))

	def test_262(self):
		input = '''
## I
string CIgc[10.581,3e54,66e+51]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 262))

	def test_263(self):
		input = '''
var tAVl[226,80.255,92.679e84]
func TL (var I96e, var p6q[497e-27,68])
	return 7E+91

func KnyU (string gnPl[0])
	begin
		## &Z@L
		## RT2U+_N`i$`65y@&"b3Q
		return true
	end

'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 263))

	def test_264(self):
		input = '''
## DhR6Wm
string vX <- 8E+78
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 264))

	def test_265(self):
		input = '''
## yb.h*Sh(E&_/QR_IQ+4-
## c!= 5#@1c
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 265))

	def test_266(self):
		input = '''
## `ts=TS
var h5bv[28.410,0,21]
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 266))

	def test_267(self):
		input = '''
bool U5J ## -1E?_XDjLI+L
number lE[94e+25] <- "1" ## k}{8b60Axd+
func Y4_F (number eo[28.354E+45])	return v5oz

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 267))

	def test_268(self):
		input = '''
## P8q/56BT+9eHatK,z
func M9 (string eQEP[105,912.874e85,680.148], number awU)	return p1
## fDFU-_,0A9B
func DZ (number EzkW)
	begin
		continue
		## ANi{G
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 268))

	def test_269(self):
		input = '''
number uCy ## dZw_+*
## joQ@*
string vNsu[1e-97,8,54.049E58]
## !bsjWdZg/1`
## SQ>yisYh;Z``X*A|qP
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 269))

	def test_270(self):
		input = '''
number M2u[95,0.031e-16,7] <- BkV ## 8orn#B
var y1X
dynamic mhxF <- "'"K'""
## %}bMSaq35[@[0y!,mU
'''
		expect = '''Error on line 3 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 270))

	def test_271(self):
		input = '''
var bK[2] ## )jK@oN|(i"$oD2JXUvE
number MA[637.869,379,79.629e-40]
func jNCN ()
	begin
		## ZaQ[9maRb+1H5tux`[
		## No3eQ>Vh
		## *G+,(j4;=I;;iy:
	end
func xAYo (dynamic KT)	return
## *E9,9~_&qJx
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 271))

	def test_272(self):
		input = '''
dynamic ehn[36E+40,28.601e13,602] <- "'"" ## Id?:v+,X_%Qw`M<iZQ}
string Y34i <- G8Q ## <z3x-l[!I>LIx%AD(e
func Sv_e (dynamic dD[85.234E+57,284.100e-41,30e+52])	return true
## t*iVNY^*
dynamic kYC[813.515,71.019] <- "JQ_'"J" ## sz$vJq*o*]AIs5=UE
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 272))

	def test_273(self):
		input = '''
## 8tv~$.9+6:w9fKBx
string cp <- ")'"" ## UT,|/2/v
## !QK
func FFG ()
	return "'"pX'""
func DJSW ()
	begin
		## y:?h3E; 
		## >V
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 273))

	def test_274(self):
		input = '''
number Om
func QjgU ()
	return

bool RKBA[84.722,949e-07] ## (,j6@h{ow*Q5qF^B
## 4|c|S5lsFt/Z[]HS;
var r_Nr[2.603e+57,3e-76,17.022] ## _
'''
		expect = '''Error on line 8 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 274))

	def test_275(self):
		input = '''
## kEagIeB&Yn
func ma ()
	return Smtv
## g%P56CHn
func jWI (number Jf6Z[0.406e+85,11.485e-64], number Wjn)
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 275))

	def test_276(self):
		input = '''
var Qa <- 98.701E+49 ## WYIy[S
## dR-D}
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 276))

	def test_277(self):
		input = '''
string jc[6.338E59] ## 3z( Mlsq2esIl+j&,on+
func CD (dynamic Lz[2.961e73,1], string N4d, number PQxE)	return "["

'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 277))

	def test_278(self):
		input = '''
dynamic klA7 <- true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 278))

	def test_279(self):
		input = '''
## M8g] 5g<Wj4x
## M4S7S#EEi:Brin&
bool mQp <- false ## mW"6Kx{
func i_Kr (number ZB, string Bh, bool Jvw2)
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 279))

	def test_280(self):
		input = '''
func knC ()
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 280))

	def test_281(self):
		input = '''
## S
func kE ()	begin
		## /weB6-sH_]H#k-{D4y?Z
	end

func bbvG ()	begin
		## 8mT8]n@Fz52n"Xnn0
	end

func yEo (dynamic LV[772,0e41], string WANh, bool Ta3E[9e-71,88E+16,28.245E-19])
	return true
'''
		expect = '''Error on line 11 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 281))

	def test_282(self):
		input = '''
## S*Iz
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 282))

	def test_283(self):
		input = '''
## Eb!kKWmJ
string t0L[43.469,64.089E76] <- 282e+81 ## n@_HABJd
func Bi9 ()
	return "'"'"'""

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 283))

	def test_284(self):
		input = '''
## |&wSWE72
## jfW~xHn_
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 284))

	def test_285(self):
		input = '''
## tv6>Dd
## [ovAee
func I18 (bool jS)
	begin
		## *:4@0!?":%O^E
	end
## 5qefJmGK1pJyQ_0|
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 285))

	def test_286(self):
		input = '''
## s
func Ns4 (var f4mZ, bool l0[5E50,283.983e+78])
	return

var wDxv <- 41.982E+18
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 286))

	def test_287(self):
		input = '''
## 7trNy(
## z[677RTg
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 287))

	def test_288(self):
		input = '''
## .I b
func z7 (bool wrM[282.416,3,832.110E-69])	return "'"'"'"('""
dynamic oZLY[549.852,12.556e25,42.730E-27] <- yW_h
## /kDD-ZNXmBE D
## P~$23t`(uGjrnoF^d P4
'''
		expect = '''Error on line 4 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 288))

	def test_289(self):
		input = '''
func Fh (number ReWN, dynamic TdA[3], number Ry[4E+45])
	return
var ZFO9
func xP ()	return

func BtBP (var yeYe[400e+86,9,5], var ev0S[156.081,8e-47])
	begin
	end
func X9C (dynamic MW5b)
	begin
	end

'''
		expect = '''Error on line 2 col 22: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 289))

	def test_290(self):
		input = '''
string M5Ld[4.309,490.971E80,38.662e+19]
## 5l4rHO|;Q8raJ)4d{~2j
string G18[404.191e+61,952E+99,927.973e+27]
func Iis (var ZB, number wY)
	begin
		continue
	end
number Gb ## #|[6(}Oh
'''
		expect = '''Error on line 5 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 290))

	def test_291(self):
		input = '''
func Xf (string aj4[752.686E-26], number yZp[352.901])
	return 44e01

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 291))

	def test_292(self):
		input = '''
## 29LE(tQ
bool tXjJ[4] <- 253.605E60
dynamic VR[57,903] <- "w'"?A" ## TTk
bool mN ## RzzheK0a_+E;t
'''
		expect = '''Error on line 4 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 292))

	def test_293(self):
		input = '''
## 2n7@+0R5S1#jLro~U()7
## 4O@q[c$
## MRtkX[]LrK)ndoAB3
## >To
'''
		expect = '''Error on line 6 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 293))

	def test_294(self):
		input = '''
number iSTq ## 6OLBz
func e8d (number EHP[4.539E04,668.832,9.228E+00], string V7z[9.210,251], dynamic C_)
	return FSCh

## Q`-jNr1k<.Aak?(M.k
'''
		expect = '''Error on line 3 col 73: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 294))

	def test_295(self):
		input = '''
## hT8fe-<Sl$ 
string THgJ[430.199E+58,81.214e90,74.102]
func lTO (string MVI)	return kn
number jW2L[441,90E-44] <- Z8 ## ^pFUOx)r%?^:wK>
## }=Hg*+e
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 295))

	def test_296(self):
		input = '''
dynamic EiX3[92] <- true
## WE=G)$[e_
func J6W (string gW4G, number DE_[7.951,22.281], number D89)	return
func ds (number iRhu[3])	return
func rc4 (string Qo)	begin
	end
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 296))

	def test_297(self):
		input = '''
func gy (var Ym[6E-03,65e-20], string JuvS[55e+07])	return pj

bool sV[8.854,567,99] <- true
number Q3 <- 420.187 ## mi)D48[TKDP4T,2hiY
## ELCHsOW
number T9[784.441,1.842E+62,60E+30]
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 297))

	def test_298(self):
		input = '''
func Qbgb (var JmP[3,184,1.889E31], bool M5ba)	return 4.623E88

'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 298))

	def test_299(self):
		input = '''
var D0[4.969] ## p;e[S=Nn]6k4f"
func wWsB (bool A3[684.485e44], string H4q)
	begin
		## ZZ/@MrXo h$b~~)
		## G- >]*XB
		## )
	end
## 90H">Cit}oUry(,{@ 
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 299))

	def test_300(self):
		input = '''
bool A4
## a@sxhjAJJ]# Qkc7Qpz
## h)%TL;a
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 300))
