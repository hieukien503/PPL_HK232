# import unittest
# from TestUtils import TestChecker

# class CheckerSuite(unittest.TestCase):
#     def test401(self):
#         input = """
# func f()
# begin
#     dynamic x
#     x <- [[1, 2, 3], [4, 5, 6]]
#     return x[0, 0]
# end

# func main()
# begin
#     number x <- f()
# end

# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 401))
    
#     def test402(self):
#         input = """
# func f(number x)

# func main()
# begin
#     number x <- f(2)
#     writeNumber(x)
# end

# func f(number x)
# begin
#     if (x >= 2) return f(x - 1) + f(x - 2)
#     return 1
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 402))
    
#     def test403(self):
#         input = """
# func main()
# begin
#     var x <- [[1, 2, 3], [4, 5, 6]]
#     var y <- x[0, 0] + 1
#     writeBool(y)
# end

# """
#         expect = "Type Mismatch In Statement: CallStmt(Id(writeBool), [Id(y)])"
#         self.assertTrue(TestChecker.test(input, expect, 403))
    
#     def test404(self):
#         input = """
# dynamic x
# func main()
# begin
#     var y <- x[0, 0] + 1
#     writeNumber(y)
# end

# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(y), None, var, BinaryOp(+, ArrayCell(Id(x), [NumLit(0.0), NumLit(0.0)]), NumLit(1.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 404))
    
#     def test405(self):
#         input = """
# dynamic x
# func main()
# begin
#     x <- [1, 2, 3, 4, 5, 6]
#     var y <- x[0, 0] + 1
#     writeNumber(y)
# end

# """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(0.0), NumLit(0.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 405))
    
#     def test406(self):
#         input = """
# dynamic x <- f(2)
# func f(number x)

# func main()
# begin

# end
# """
#         expect = "Undeclared Function: f"
#         self.assertTrue(TestChecker.test(input, expect, 406))
    
#     def test407(self):
#         input = """
# func f(number x)

# dynamic x <- f(2) + 1

# func f(number y)
# begin
#     if (y <= 1) return 1
#     return y * f(y - 1)
# end

# func main()
# begin
#     return 2
# end
# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 407))
    
#     def test408(self):
#         input = """
# func f(number x)

# dynamic x <- f(2) + 1

# func main()
# begin
#     return
# end
# """
#         expect = "No Function Definition: f"
#         self.assertTrue(TestChecker.test(input, expect, 408))
    
#     def test409(self):
#         input = """
# func f(number x[2, 3])
#     return x[2]

# func main()
# begin
#     number x[2, 3] <- [[1, 2, 3], [4, 5, 6]]
#     writeNumber(f()[2])
# end
# """
#         expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
#         self.assertTrue(TestChecker.test(input, expect, 409))
    
#     def test410(self):
#         input = """
# func f(number x[2, 3])
#     return x

# func main()
# begin
#     number x[2, 3] <- [[1, 2, 3], [4, 5, 6]]
#     writeNumber(f(x)[0, 1])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 410))
    
#     def test411(self):
#         input = """
# func f(number x[2, 3])
#     return x

# func main()
# begin
#     dynamic x <- [[1, 2, 3], [4, 5, 6]]
#     var y <- x[0, 0]
#     writeString(y)
# end
# """
#         expect = "Type Mismatch In Statement: CallStmt(Id(writeString), [Id(y)])"
#         self.assertTrue(TestChecker.test(input, expect, 411))
    
#     def test412(self):
#         input = """
# func f(number x[2, 3], number i, number j)
#     return x[i, j]

# func main()
# begin
#     dynamic x <- [[1, 2, 3], [4, 5, 6]]
#     var i <- 0
#     for i until i >= 2 by 1
#         for j until j >= 3 by 1
#             writeNumber(f(x, i, j))
# end
# """
#         expect = "Undeclared Identifier: j"
#         self.assertTrue(TestChecker.test(input, expect, 412))
    
#     def test413(self):
#         input = """
# func main()
# begin
#     number x <- readNumber()
#     if (x <= 10) writeString("Number is less than or equal to 10")
#     elif ((x > 10) and (x <= 20)) writeString("Number is between 11 and 20")
#     else writeString("Invalid number!")
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 413))
    
#     def test414(self):
#         input = """
# func isPrime(number x)

# func main()
# begin
#     number x <- readNumber()
#     if (isPrime(x)) writeString("x is a prime number")
#     else writeString("x is not a prime number")
# end

# func isPrime(number x)
# begin
#     if (x <= 1) return false
#     var i <- 2
#     for i until i > x / 2 by 1
#     begin
#         if (x % i = 0) return false
#     end
#     return true
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 414))
    
#     def test415(self):
#         input = """
# func areDivisors(number num1, number num2)
#     return ((num1 % num2 = 0) or (num2 % num1 = 0))

# func main()
# begin
#     var num1 <- readNumber()
#     var num2 <- readNumber()
#     if (areDivisors(num1, num2)) writeString("Yes")
#     else writeString("No")
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 415))
    
#     def test416(self):
#         input = """
# func f()
# begin
#     var i <- 0
#     for i until i > 10 by 1
#     begin

#     end
#     continue
# end

# func main()
# begin
#     f()
# end
# """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 416))
    
#     def test417(self):
#         input = """
# func findMax(number x[10], number n)
# begin
#     if (n = 1) return x[0]
#     number k <- findMax(x, n - 1)
#     if (k >= x[n]) return k
#     return x[n]
# end

# func main()
# begin
#     dynamic x <- [3, 4, 0, 1, 2, 7, 9, 8, 5, 6]
#     writeNumber(findMax(x, 10))
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 417))
    
#     def test418(self):
#         input = """
# func main()
# begin
#     number x <- 2 + true
#     writeNumber(x)
# end
# """
#         expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(2.0), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 418))
    
#     def test419(self):
#         input = """
# func main()
# begin
#     var x <- [[[[1, 2]], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
#     writeNumber(x)
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0))), ArrayLit(ArrayLit(NumLit(6.0), NumLit(7.0), NumLit(8.0)), ArrayLit(NumLit(9.0), NumLit(10.0), NumLit(11.0))))"
#         self.assertTrue(TestChecker.test(input, expect, 419))
    
#     def test420(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     number x[3, 3] <- [a, b, c]
#     a <- [1, 2, 3]
#     b <- [4, 5, 6]
#     c <- [7, 8, 9]
#     writeNumber(a[0] + b[0] + c[0])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 420))
    
#     def test421(self):
#         input = """
# func f(number x[3])
# begin
#     return
# end
    
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     f([a, b, c])
#     a <- 3
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 421))

#     def test422(self):
#         input = """
# func f(number x[2, 3])
    
# func main()
# begin
#     dynamic a
#     number x[2, 3] <- f(a)
#     a[0] <- [1, 2, 3]
# end

# func f(number x[2, 3])
#     return x
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 422))
    
#     def test423(self):
#         input = """
# func f(number x)
# begin
#     if (x = 0) return 0
#     elif (x = 1) return 1
#     else return f(x - 1) + f(x - 2)
# end
    
# func main()
# begin
#     dynamic a
#     number x <- f(a)
#     a[0] <- [1, 2, 3]
# end
# """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 423))
    
#     def test424(self):
#         input = """
# func max(number x, number y)
# begin
#     if (x <= y) return y
#     return x
# end

# func main()
# begin
#     number x <- readNumber()
#     number y <- readNumber()
#     number z <- readNumber()
#     writeNumber(max(max(x, y), z))
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 424))
    
#     def test425(self):
#         input = """
# func pow(number x, number y)

# func main()
# begin
#     number x <- readNumber()
#     number y <- readNumber()
#     writeNumber(pow(x, y))
# end

# func pow(number a, number b)
# begin
#     if (b = 0) return 1
#     number k <- pow(a, b / 2)
#     if (b % 2 = 0) return k * k
#     return a * k * k
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 425))
    
#     def test426(self):
#         input = """
# func add(number x, number x)

# func main()
# begin
#     number x <- readNumber()
#     number y <- readNumber()
#     writeNumber(add(x, y))
# end

# func add(number a, number b)
# begin
#     return a + b
# end
# """
#         expect = "Redeclared Parameter: x"
#         self.assertTrue(TestChecker.test(input, expect, 426))
    
#     def test427(self):
#         input = """
# func add(number x, number y)

# func main()
# begin
#     number x <- readNumber()
#     number y <- readNumber()
#     writeNumber(pow(x, y))
# end

# func add(number a, number b)
# begin
#     return a + b
# end
# """
#         expect = "Undeclared Function: pow"
#         self.assertTrue(TestChecker.test(input, expect, 427))
    
#     def test428(self):
#         input = """
# func add(number x, number y)

# func main()
# begin
#     var i <- 0
#     for i until i > 10 by 0
#     begin
#         i <- add(i, 1)
#         writeNumber(i)
#     end
# end

# func add(number a, number b)
# begin
#     number x <- a + b
#     return x
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 428))
    
#     def test429(self):
#         input = """
# func f(number x)

# func main()
# begin
#     number x <- 10
#     number y <- f(x)
#     writeNumber(y)
# end

# func f(string x)
# begin
#     return x == "Hello"
# end
# """
#         expect = "Redeclared Function: f"
#         self.assertTrue(TestChecker.test(input, expect, 429))
    
#     def test430(self):
#         input = """
# func main()
# begin
#     var i <- 0
#     for i until i < 0 by 1
#     begin
#         string x <- readString()
#         if (x == "Hello") 
#         begin
#             x <- x ... ", world!"
#             writeString(x)
#         end
#         else writeString("Try again")
#     end
#     break
# end
# """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 430))
    
#     def test431(self):
#         input = """
# func f(number arr[10], number n)
# begin
#     var i <- 0
#     for i until i >= n by 1
#         writeNumber(arr[i])
# end

# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 431))
    
#     def test432(self):
#         input = """
# func f(number arr[10], number n)
# begin
#     var i <- 0
#     for i until i >= n by 1
#         writeNumber(arr[i])
# end

# func main()
# begin
#     dynamic n
#     f([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n)
#     n <- 10
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 432))
    
#     def test433(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     number x[2, 2] <- [a, [b, 2]]
#     a <- 2
#     b <- 3
#     c <- true
# end
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(2.0))"
#         self.assertTrue(TestChecker.test(input, expect, 433))
    
#     def test434(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     number x[3, 2] <- [a, b, [c, 0]]
#     a <- [1]
#     b <- [3, 4]
#     c <- 0
# end
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(NumLit(1.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 434))
    
#     def test435(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic x <- [readNumber(), a, b, c]
#     a <- 3
#     b <- x[0]
#     c <- a + b
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 435))
    
#     def test436(self):
#         input = """
# func main()
# begin
#     dynamic x <- readBool()
#     dynamic y <- not readBool()
#     if (x and y) writeNumber(1)
#     else writeNumber(0)
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 436))
    
#     def test437(self):
#         input = """
# func main()
# begin
#     dynamic x
#     if (x) writeString("x is infer to true value")
#     else writeString("x is infer to false value")
#     x <- 1 + true
# end
# """
#         expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 437))
    
#     def test438(self):
#         input = """
# func main()
# begin
#     dynamic x
#     if (x) writeString("x is infer to true value")
#     else writeString("x is infer to false value")
#     x <- not (true and not false) and not (false and not true)
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 438))
    
#     def test439(self):
#         input = """
# func f(number x)
# begin
#     dynamic x <- (x - 2) * (x + true)
# end
# """
#         expect = "Undeclared Identifier: x"
#         self.assertTrue(TestChecker.test(input, expect, 439))
    
#     def test440(self):
#         input = """
# func f()
# begin
#     dynamic x
#     x <- (x - 2) * (x + true)
# end
# """
#         expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 440))
    
#     def test441(self):
#         input = """
# number a <- 1 + "Hello"
# func main()
#     return
# """
#         expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), StringLit(Hello))"
#         self.assertTrue(TestChecker.test(input, expect, 441))
    
#     def test442(self):
#         input = """
# func f()

# func main()
# begin
#     number x <- g(1, 2, 3)
# end
# """
#         expect = "Undeclared Function: g"
#         self.assertTrue(TestChecker.test(input, expect, 442))
    
#     def test443(self):
#         input = """
# number x
# number y
# func f()

# func main()
#     return
# """
#         expect = "No Function Definition: f"
#         self.assertTrue(TestChecker.test(input, expect, 443))
    
#     def test444(self):
#         input = """
# func f()

# number f
# dynamic x
# func main()
#     return
# """
#         expect = "Redeclared Variable: f"
#         self.assertTrue(TestChecker.test(input, expect, 444))
    
#     def test445(self):
#         input = """
# func f()
# begin

# end
# dynamic a
# number b
# bool c
# string d
# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 445))
    
#     def test446(self):
#         input = """
# func f(number x)
# begin
#     return f(x)
# end

# func main()
# begin
#     dynamic d <- f(10)
# end
# """
#         expect = "Type Cannot Be Inferred: Return(CallExpr(Id(f), [Id(x)]))"
#         self.assertTrue(TestChecker.test(input, expect, 446))
    
#     def test447(self):
#         input = """
# func f(number x)
# begin
#     return 1
# end

# func main()
# begin
#     f(2018)
# end
# """
#         expect = "Type Mismatch In Statement: CallStmt(Id(f), [NumLit(2018.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 447))
    
#     def test448(self):
#         input = """
# func main()
# begin
#     continue
# end
# """
#         expect = "Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 448))
    
#     def test449(self):
#         input = """
# func main()
# begin
#     break
# end
# """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 449))
    
#     def test450(self):
#         input = """
# number x
# number y
# func add()
#     return x + y

# func main()
# begin
#     x <- readNumber()
#     y <- readNumber()
#     writeNumber(add())
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 450))
    
#     def test451(self):
#         input = """
# func add(number x, number y)

# func main()
# begin
#     number x <- readNumber()
#     number y <- readNumber()
#     dynamic a <- add(x, y) + 1
# end

# func add(number x, number y)
#     return "Hello"
# """
#         expect = "Type Mismatch In Statement: Return(StringLit(Hello))"
#         self.assertTrue(TestChecker.test(input, expect, 451))
    
#     def test452(self):
#         input = """
# func add(number x, number y)

# func main()
# begin
#     dynamic a
#     a[0] <- [1, 2, 3]
# end

# func add(number x, number y)
#     return "Hello"
# """
#         expect = "Type Cannot Be Inferred: AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 452))
    
#     def test453(self):
#         input = """
# func main()
# begin
#     number arr[3, 2] <- [[1, 2], [3, 4], [5, 6]]
#     number b[2] <- arr[1]
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 453))
    
#     def test454(self):
#         input = """
# func f(number arr[10], number x)

# func main()
# begin
#     dynamic n
#     var i <- 0
#     number arr[10]
#     for i until true by 1
#     begin
#         n <- readNumber()
#         if ((n > 10) or (n <= 0)) writeString("Try again")
#         else break
#     end
    
#     for i until i >= n by 1
#         arr[i] <- readNumber()
    
#     f(arr, n)
# end

# func f(number a[5], number n)
#     return
# """
#         expect = "Redeclared Function: f"
#         self.assertTrue(TestChecker.test(input, expect, 454))
    
#     def test455(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     number arr[2, 2] <- [[a, b]]
#     number c[2, 2] <- arr
# end
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(a), Id(b))))"
#         self.assertTrue(TestChecker.test(input, expect, 455))
    
#     def test456(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     var arr <- [[a], [b], [c], [1]]
#     arr <- [[1], [2], [3], [4]]
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 456))
    
#     def test457(self):
#         input = """
# func main()
# begin
#     dynamic x <- "Hello"
#     if (x == "Hello") writeString(x)
#     else writeString("Something weird!")
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 457))
    
#     def test458(self):
#         input = """
# func main()
# begin
#     dynamic x <- [1, 2, 3]
#     dynamic a <- x
#     writeNumber(a[0])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 458))
    
#     def test459(self):
#         input = """
# func foo(number a)

# func main()
# begin
#     number a <- foo(1)
#     return
# end

# func foo(number a)
# begin
#     return
# end
# """
#         expect = "Type Mismatch In Statement: Return()"
#         self.assertTrue(TestChecker.test(input, expect, 459))
    
#     def test460(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     number c[2] <- [3, 4]
#     number arr[2,2] <- [[a], c]
# end
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(a)), Id(c)))"
#         self.assertTrue(TestChecker.test(input, expect, 460))
    
#     def test461(self):
#         input = """
# func f(number a[3], number b[3])
#     return

# func main()
# begin
#     f([1, 3, 2], [1, "Hello", 2])
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), StringLit(Hello), NumLit(2.0))"
#         self.assertTrue(TestChecker.test(input, expect, 461))
    
#     def test462(self):
#         input = """
# dynamic a <- [[3, 9, 2, 10, -1], [0, -10, 5, 3, 11], [10, 9, -27, 36, 4]]
# func sort(number a[5])
# begin
#     var i <- 0
#     var j <- 0
#     for i until i > 4 by 1
#         for j until j > 4 by 1
#             if (a[i] > a[j])
#             begin
#                 var temp <- a[i]
#                 a[i] <- a[j]
#                 a[j] <- temp
#             end
# end

# func main()
# begin
#     var i <- 0
#     for i until i > 2 by 1
#         sort(a[i])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 462))
    
#     def test463(self):
#         input = """
# number x <- 10
# func f(number x)
# begin
#     number x <- x + 20
#     writeNumber(x)
# end
# """
#         expect = "Undeclared Identifier: x"
#         self.assertTrue(TestChecker.test(input, expect, 463))
    
#     def test464(self):
#         input = """
# func f(number n)

# number a[2, 3] <- [[f(1), f(2), f(3)], [f(4), f(5), f(6)]]
# func main()
# begin
#     var i <- 0
#     dynamic j <- 0
#     for i until i > 1 by 1
#         for j until j > 2 by 1
#             writeNumber(a[i, j])
# end

# func f(number a)
#     return a
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 464))
    
#     def test465(self):
#         input = """
# func f(number x[2, 3])
#     return x[0]

# func main()
# begin
#     dynamic x <- f([[1, 2, 3], [4, 5, 6]])[2, 3]
#     writeNumber(x)
# end
# """
#         expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(f), [ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0)))]), [NumLit(2.0), NumLit(3.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 465))
    
#     def test466(self):
#         input = """
# func f(number n)

# func main()
# begin
#     var i <- f(2, 3)
# end

# func f(number a)
#     return a
# """
#         expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(2.0), NumLit(3.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 466))
    
#     def test467(self):
#         input = """
# func f(number x, number y)

# func main()
# begin
#     var i <- f(2)
# end

# func f(number a)
#     return a
# """
#         expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(2.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 467))
    
#     def test468(self):
#         input = """
# dynamic a
# func main()
# begin
#     var i <- a ... 2.75
# end
# """
#         expect = "Type Mismatch In Expression: BinaryOp(..., Id(a), NumLit(2.75))"
#         self.assertTrue(TestChecker.test(input, expect, 468))
    
#     def test469(self):
#         input = """
# dynamic a
# func main()
# begin
#     var i <- a[2] ... 2.75
# end
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(i), None, var, BinaryOp(..., ArrayCell(Id(a), [NumLit(2.0)]), NumLit(2.75)))"
#         self.assertTrue(TestChecker.test(input, expect, 469))
    
#     def test470(self):
#         input = """
# func main()
# begin
#     if (1) writeBool(true)
#     else writeBool(false)
# end
# """
#         expect = "Type Mismatch In Statement: If((NumLit(1.0), CallStmt(Id(writeBool), [BooleanLit(True)])), [], CallStmt(Id(writeBool), [BooleanLit(False)]))"
#         self.assertTrue(TestChecker.test(input, expect, 470))
    
#     def test471(self):
#         input = """
# func main()

# func main()

# func main()
# begin
#     if (1) writeBool(true)
#     else writeBool(false)
# end
# """
#         expect = "Redeclared Function: main"
#         self.assertTrue(TestChecker.test(input, expect, 471))
    
#     def test472(self):
#         input = """
# number a
# bool b
# string c
# dynamic d
# func main()
# begin
#     if (b) d <- 1 + a
#     else d <- a - 1.75
#     c <- "Hello, world!"
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 472))
    
#     def test473(self):
#         input = """
# func f(number arr[10], number n)
# begin
#     if ((n < 0) or (n >= 10)) return -999
#     number i <- 0
#     for i until i >= n by 1
#         if (arr[i] < 10) return i
    
#     return not (n < 20)
# end

# func main()
# begin
#     f([1, 9, 6, 5, 3, 8, 10, 28, 0, -10], 10)
# end
# """
#         expect = "Type Mismatch In Statement: Return(UnaryOp(not, BinaryOp(<, Id(n), NumLit(20.0))))"
#         self.assertTrue(TestChecker.test(input, expect, 473))
    
#     def test474(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     var arr <- [[a, 1], [b, true], [c, "Hello"]]
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(a), NumLit(1.0)), ArrayLit(Id(b), BooleanLit(True)), ArrayLit(Id(c), StringLit(Hello)))"
#         self.assertTrue(TestChecker.test(input, expect, 474))
    
#     def test475(self):
#         input = """
# dynamic x
# dynamic y
# func main()
# begin
#     dynamic z
#     dynamic arr <- [[1, x], [2, y], [3, z]]
#     x <- 20
#     y <- 30
#     z <- "Hi"
# end
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(z), StringLit(Hi))"
#         self.assertTrue(TestChecker.test(input, expect, 475))
    
#     def test476(self):
#         input = """
# func main()
# begin
#     var x <- [10, 20, 40]
#     var y <- [true, false, true]
#     number a[2, 3] <- [x, y]
#     writeNumber(a[0, 0])
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(Id(x), Id(y))"
#         self.assertTrue(TestChecker.test(input, expect, 476))
    
#     def test477(self):
#         input = """
# func main()
# begin
#     dynamic x
#     dynamic y
#     number a[2, 3] <- [x, y]
#     x <- [10, 20, 40]
#     y <- [true, false, true]
#     writeNumber(a[0, 0])
# end
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(y), ArrayLit(BooleanLit(True), BooleanLit(False), BooleanLit(True)))"
#         self.assertTrue(TestChecker.test(input, expect, 477))
    
#     def test478(self):
#         input = """
# func main()
# begin
#     dynamic x
#     dynamic y
#     number a[2, 3] <- [x, y]
#     y <- [y[1] + y[2], y[2] - y[0], y[0] + y[1] < y[2]]
#     x <- [1, 9, 6]
#     writeNumber(a[0, 0])
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(BinaryOp(+, ArrayCell(Id(y), [NumLit(1.0)]), ArrayCell(Id(y), [NumLit(2.0)])), BinaryOp(-, ArrayCell(Id(y), [NumLit(2.0)]), ArrayCell(Id(y), [NumLit(0.0)])), BinaryOp(<, BinaryOp(+, ArrayCell(Id(y), [NumLit(0.0)]), ArrayCell(Id(y), [NumLit(1.0)])), ArrayCell(Id(y), [NumLit(2.0)])))"
#         self.assertTrue(TestChecker.test(input, expect, 478))
    
#     def test479(self):
#         input = """
# func f(number x, bool y, string z)
#     return not y

# func main()
# begin
#     dynamic x
#     dynamic y
#     dynamic z
#     bool t <- f(x, y, z)
#     writeBool(y and not t)
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 479))
    
#     def test480(self):
#         input = """
# func main()
# begin
#     var x <- [[1, 2], [3, 4, 5]]
#     writeNumber(x[0, 2])
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 480))
    
#     def test481(self):
#         input = """
# func test(number x)
# begin
#     var y <- test
#     test(2018)
# end
# """
#         expect = "Undeclared Identifier: test"
#         self.assertTrue(TestChecker.test(input, expect, 481))
    
#     def test482(self):
#         input = """
# func test(number x)
# begin
#     var a <- x
#     var b <- -a
#     var c <- a + b
#     writeNumber(a + b + c)
# end

# func main()
# begin
#     test(2018)
#     return -1
# end
# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 482))
    
#     def test483(self):
#         input = """
# dynamic a
# func main()
# begin
#     number a[2, 3] <- [a, [10, 20, 30]]
#     a <- [1, 9, 6]
#     writeNumber(a[0])
# end
# """
#         expect = "Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input, expect, 483))
    
#     def test484(self):
#         input = """
# dynamic a
# func main()
# begin
#     var x <- [a, [1, 2, 3]]
#     a <- [1, 9, 6]
#     x <- [[3, 9, 6], [1, 3, 2]]
#     writeNumber(x[0, 0])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 484))
    
#     def test485(self):
#         input = """
# dynamic a
# func main()
# begin
#     dynamic b
#     dynamic c
#     dynamic d
#     var e <- 1
#     var x <- [a, [b], [[c]], [[[d, e]]]]
#     c <- [-10, 2 / 3 % 0.75]
#     b <- [c]
#     a <- [b]
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 485))

#     def test486(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic d
#     var x <- [a, b, c, [[1, 2, 3, 4], [5, 6, 7, 8]]]
#     c[0] <- d
#     d <- [0, 3, 1]
# end
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(d), ArrayLit(NumLit(0.0), NumLit(3.0), NumLit(1.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 486))
    
#     def test487(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c <- a ... ", world!"
#     a <- b
#     b <- [1, 2, 3]
# end
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(b), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 487))
    
#     def test488(self):
#         input = """
# func main()
# begin
#     number x
#     begin
#         number x <- (10 + x) * 2
#     end
# end
# """
#         expect = "Undeclared Identifier: x"
#         self.assertTrue(TestChecker.test(input, expect, 488))
    
#     def test489(self):
#         input = """
# func test(number x)

# func main()
# begin
#     number test
#     begin
#         number x <- test(2018) + 1
#     end
# end
# """
#         expect = "Type Mismatch In Expression: CallExpr(Id(test), [NumLit(2018.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 489))
    
#     def test490(self):
#         input = """
# func main()
# begin
#     dynamic x
#     number a <- [x]
# end
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, ArrayLit(Id(x)))"
#         self.assertTrue(TestChecker.test(input, expect, 490))
    
#     def test491(self):
#         input = """
# dynamic x
# number a[3] <- [1, [x, x]]
# func  main()
# begin
#     x <- 1
# end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), ArrayLit(Id(x), Id(x))))"
#         self.assertTrue(TestChecker.test(input, expect, 491))
    
#     def test492(self):
#         input = """
# func f(number x, number y)
# begin
#     if (y == 0) return x
#     return f(y, x % y)
# end

# func main()
# begin
#     number x <- readNumber()
#     number y <- readNumber()
#     dynamic res <- f(x, y)
#     writeString(res)
# end
# """
#         expect = "Type Mismatch In Expression: BinaryOp(==, Id(y), NumLit(0.0))"
#         self.assertTrue(TestChecker.test(input, expect, 492))
    
#     def test493(self):
#         input = """
# func f(number x, number y)
# begin
#     if (y = 0) return x
#     return f(y, x % y)
# end

# func main()
# begin
#     number x[10]
#     number y[10]
#     var i <- 0
#     for i until i >= 10 by 1
#         x[i] <- readNumber()
    
#     for i until i >= 10 by "Hello"
#         y[i] <- readNumber()
    
# end
# """
#         expect = "Type Mismatch In Statement: For(Id(i), BinaryOp(>=, Id(i), NumLit(10.0)), StringLit(Hello), AssignStmt(ArrayCell(Id(y), [Id(i)]), CallExpr(Id(readNumber), [])))"
#         self.assertTrue(TestChecker.test(input, expect, 493))
    
#     def test494(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic x <- [a, b, c]
# end
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, dynamic, ArrayLit(Id(a), Id(b), Id(c)))"
#         self.assertTrue(TestChecker.test(input, expect, 494))
    
#     def test495(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic x
#     x <- [a, b, [c]]
# end
# """
#         expect = "Type Cannot Be Inferred: AssignStmt(Id(x), ArrayLit(Id(a), Id(b), ArrayLit(Id(c))))"
#         self.assertTrue(TestChecker.test(input, expect, 495))
    
#     def test496(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic x <- (a ... b) ... c
#     writeString(x)
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 496))
    
#     def test497(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic x <- [a, [b, c], [2, 3]]
#     writeNumber(a[0] + a[1] + b + c)
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 497))
    
#     def test498(self):
#         input = """
# func main()
# begin
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic d
#     dynamic x <- [a, [b, c], [2, d]]
#     d <- x[0, 0] + x[0, 1]
#     writeNumber(a[0] + a[1] + b + c + d)
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 498))
    
#     def test499(self):
#         input = """
# func main()
# begin
#     number x
#     dynamic y
#     begin
#         number x <- (10 + y) * 2
#     end
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 499))
    
#     def test500(self):
#         input = """
# func main()
# begin
#     number arr[2, 2] <- [1, 2, 3, 4]
# end
# """
#         expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 500))

import unittest
from TestUtils import TestChecker

class CheckerSuite(unittest.TestCase):
    def test_001_test_1_No_entry_point(self):
        input = """
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test_002_test_1_No_entry_point(self):
        input = """
            func main()
            func main() begin
                number main
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    def test_003_test_1_No_entry_point(self):
        input = """
            func main(number a) begin
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 402))
        
    def test_004_test_1_No_entry_point(self):
        input = """
            func main() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 403))
        
    def test_005_test_1_No_entry_point(self):
        input = """
            number VoTien
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_006_test_2_NoDefinition(self):
        input = """
            func foo(number a)
            func foo(number a) return     
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_007_test_1_No_entry_point(self):
        input = """
            func foo(number a) return   
        
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))
        
    def test_008_test_1_No_entry_point(self):
        input = """
            func foo(number a) 
        
            func main() return
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 407))
        
    def test_009_test_3_Redeclared(self):
        input = """
            number a
            string a 
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test_010_test_1_No_entry_point(self):
        input = """
            func a()
            number a
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 409))
        
    def test_011_test_1_No_entry_point(self):
        input = """
            func foo() return
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test_012_test_1_No_entry_point(self):
        input = """
            func foo()
            func foo()
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 411))
        
    def test_013_test_1_No_entry_point(self):
        input = """
            func foo() return
            func foo() return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 412))
        
    def test_014_test_1_No_entry_point(self):
        input = """
            number foo
            func foo() return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 413))
        
    def test_015_test_1_No_entry_point(self):
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                number c
                string VoTien
                begin
                    number c
                    string VoTien
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 414))
        
    def test_016_test_1_No_entry_point(self):
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 415))
        
    def test_017_test_1_No_entry_point(self):
        input = """
            number a
            string a
            func VoTien() return
            func main()begin
                number a
                begin
                    number a
                end
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 416))
        
    def test_018_test_1_No_entry_point(self):
        input = """
            number a
            func VoTien() return
            func main()begin
                number a
                begin
                    number a
                    string a
                end
                
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 417))
        
    def test_019_test_1_No_entry_point(self):
        input = """
            number a
            func VoTien(number a, number VoTien, number a)
            begin
                string c
            end
            
            func main() return
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
    def test_020_test_1_No_entry_point(self):
        input = """
            number a
            func VoTien(number a, number VoTien, number c, string c)
            begin
            end
            
            func main() return
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 419))
        
    def test_021_test_1_No_entry_point(self):
        input = """
            number a
            func VoTien(number a, number VoTien, number c)
            begin
                begin
                    number a
                end
                number a
            end
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))
        
    def test_022_test_1_No_entry_point(self):
        input = """
            func foo(number a) 
            func foo(number b) return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 421))
        
    def test_023_test_1_No_entry_point(self):
        input = """
            func foo(number a) 
            func foo(string a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 422))
        
    def test_024_test_1_No_entry_point(self):
        input = """
            func foo(number a) 
            func foo(number a, string c) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 423))
        
    def test_025_test_1_No_entry_point(self):
        input = """
            func foo(number a, string c) 
            func foo(number a) return
            
            func main() return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 424))
        
    def test_026_test_3_Undeclared(self):
        input = """
            number a <- a
            func main() begin
                number b <- a
                number c <- e
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 425))
        
    def test_027_test_1_No_entry_point(self):
        input = """
            func a() return 1
            func main() begin
                number b <- a
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 426))
        
    def test_028_test_1_No_entry_point(self):
        input = """
            func a() return 1
            func main() begin
                number a
                begin 
                    number d
                end
                number b <- a
                number c <- d
            end
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 427))
        
    def test_029_test_1_No_entry_point(self):
        input = """
            func a() begin
                a()
            end
            func main() begin
                a()
                b()
            end
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 428))
        
    def test_030_test_1_No_entry_point(self):
        input = """
            func a() return
            func main() begin
                number a
                a()
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(a), [])"
        self.assertTrue(TestChecker.test(input, expect, 429))
        
    def test_031_test_1_No_entry_point(self):
        input = """
            func a()
            func main() begin
                a()
            end
            func a() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_032_test_4_MustInLoop(self):
        input = """
            func main() begin
                var i <- 2
                for i until true by 1
                begin
                    break
                    continue
                    begin
                        break
                        continue
                    end
                    
                    for i until true by 1
                    begin
                        break
                        continue
                    end
                    break
                    continue
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 431))
        
    def test_033_test_1_No_entry_point(self):
        input = """
            func main() begin
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 432))
        
    def test_034_test_1_No_entry_point(self):
        input = """
            func main() begin
                continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 433))
        
    def test_035_test_5_TypeCannotBeInferred(self):
        input = """
            dynamic VoTien
            var a <- VoTien

            func main() return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 434))
        
    def test_036_test_1_No_entry_point(self):
        input = """
            number VoTien
            var a <- VoTien
            number b <- a

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 435))
        
    def test_037_test_1_No_entry_point(self):
        input = """
            dynamic VoTien
            number a <- VoTien
            number b <- VoTien

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_038_test_1_No_entry_point(self):
        input = """
            func foo() begin
                dynamic a
                return a
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 437))
        
    def test_039_test_1_No_entry_point(self):
        input = """
            func foo() begin
                return 1
                dynamic a
                return a
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 438))
        
    def test_040_test_1_No_entry_point(self):
        input = """
            func foo() begin
                number a
                return a
                return 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))
        
    def test_041_test_1_No_entry_point(self):
        input = """
            func foo() begin
                dynamic a
                dynamic b
                a <- b
            end

            func main() return
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 440))
        
    def test_042_test_1_No_entry_point(self):
        input = """
            func foo() begin
                number a
                dynamic b
                a <- b
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 441))
        
    def test_043_test_1_No_entry_point(self):
        input = """
            func foo() begin
                number a
                dynamic b
                b <- a
                b <- 1
            end

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))
        
    def test_044_test_6_TypeMismatchInStatement(self):
        input = """
            number a <- "1"

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    def test_045_test_1_No_entry_point(self):
        input = """
            number a[1,2] <- [[1,2]]

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 444))
       
    def test_046_test_1_No_entry_point(self):
        input = """
            number a[1,2,3] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_047_test_1_No_entry_point(self):
        input = """
            number a[1] <- [[1,2]]

            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 446))       

    def test_048_test_1_No_entry_point(self):
        input = """
            func foo() return

            func main()begin
                foo()
                foo(1)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 447))    
        
    def test_049_test_1_No_entry_point(self):
        input = """
            func foo(number a) return

            func main()begin
                foo()
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 448))     
        
    def test_050_test_1_No_entry_point(self):
        input = """
            func foo(number a) return

            func main()begin
                foo("1")
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 449))    
        
    def test_051_test_1_No_entry_point(self):
        input = """
            func foo(number a) return

            func main()begin
                dynamic a
                foo(a)
                number c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 450))                

    def test_052_test_1_No_entry_point(self):
        input = """
            func main()begin
                dynamic a
                if (a) return
                a <- true
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 451))     
        
    def test_053_test_1_No_entry_point(self):
        input = """
            func main()begin
                dynamic a <- 1
                if (a) return
            end
        """
        # Type Mismatch In Statement: If(Id(a), Return()), [], None
        expect = "Type Mismatch In Statement: If((Id(a), Return()), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 452))                 

    def test_054_test_1_No_entry_point(self):
        input = """
            func main()begin
                dynamic a
                if (a) number a
                elif (a)  return
                else number a
                
                if(true) number a
                elif (1) number a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 453)) 
        
    def test_055_test_1_No_entry_point(self):
        input = """
            func foo() begin
                dynamic a
                dynamic b
                dynamic c
                for a until b by c return
                a <- 1
                b <- true
                c <- 1
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))   
        
    def test_056_test_1_No_entry_point(self):
        input = """
            func foo() begin
                dynamic a <- true
                dynamic b
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 455))    
        
    def test_057_test_1_No_entry_point(self):
        input = """
            func foo() begin
                dynamic a 
                dynamic b <- 2
                dynamic c
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 456))  

    def test_058_test_1_No_entry_point(self):
        input = """
            func foo() begin
                dynamic a 
                dynamic b
                dynamic c <- "1"
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 457))    
        
    def test_059_test_1_No_entry_point(self):
        input = """
            func foo() begin
                number a
                return 1
                return a
                return "!"
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 458))  
        
        
    def test_060_test_1_No_entry_point(self):
        input = """
            func foo() begin
                number a
                a <- 1
                a <- true
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 459))  

    def test_061_test_6_TypeMismatchInExpression(self):
        input = """
            func foo() return 1

            func main() begin
                var a <- foo()
                var b <- foo(1)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 460))
        
    def test_062_test_1_No_entry_point(self):
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 461))
        
    def test_063_test_1_No_entry_point(self):
        input = """
            func foo(number a) return 1

            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 462))
        
    def test_064_test_1_No_entry_point(self):
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 463))
        
    def test_065_test_1_No_entry_point(self):
        input = """
            func foo(number a) return
            
            func main() begin
                var a <- foo("1")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 464))
        
    def test_066_test_1_No_entry_point(self):
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 465))
        
    def test_067_test_1_No_entry_point(self):
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- left + 1
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 466))
        
    def test_068_test_1_No_entry_point(self):
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- 1 + right
                left <- 1
                right <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 467))
        

    def test_069_test_1_No_entry_point(self):
        input = """
            func main() begin
                dynamic left
                dynamic right
                
                var c <- - left
                left <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))
        
    def test_070_test_1_No_entry_point(self):
        input = """
            func main() begin
                number a[1,2]
                number b
                var c <- b[1]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 469))
        
    def test_071_test_1_No_entry_point(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- b[1]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, var, ArrayCell(Id(b), [NumLit(1.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 470))
        
    def test_072_test_1_No_entry_point(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[b, 1]
                b <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 471))
        
    def test_073_test_1_No_entry_point(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a["1"]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 472))
        
    def test_074_test_1_No_entry_point(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,2,3]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])"
        self.assertTrue(TestChecker.test(input, expect, 473))
        
    def test_075_test_1_No_entry_point(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1,3]
                c <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 474))
        
    def test_076_test_1_No_entry_point(self):
        input = """
            func main() begin
                number a[1,2]
                dynamic b
                var c <- a[1]
                c <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))
        
    def test_077_test_1_No_entry_point(self):
        input = """
            func VoTien()
            func main() begin
                number VoTien_ <- VoTien()
            end
            func VoTien() begin
            end
        """
        # expect = "???"
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))
        
    def test_078_test_1_No_entry_point(self):
        input = """
            dynamic VoTien
            var x <- VoTien and (VoTien > VoTien)
        """
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(VoTien), Id(VoTien))"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_079_test_1_No_entry_point(self):
        input = """
            dynamic VoTien
            var x <- VoTien + VoTien * VoTien
            number y <- VoTien
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 478))
        
    def test_080_test_1_No_entry_point(self):
        input = """
            dynamic VoTien
            var x <- VoTien > VoTien ... VoTien < VoTien
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., BinaryOp(>, Id(VoTien), Id(VoTien)), BinaryOp(<, Id(VoTien), Id(VoTien)))"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_081_test_7_full(self):
        input = """
            func areDivisors(number num1, number num2)
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
            func main()
            begin
            var num1 <- readNumber()
            var num2 <- readNumber()
            if (areDivisors(num1, num2)) writeString("Yes")
            else writeString("No")
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 480))
        
    def test_082_test_1_No_entry_point(self):
        input = """
func isPrime(number x)
func main()
begin
number x <- readNumber()
if (isPrime(x)) writeString("Yes")
else writeString("No")
end
func isPrime(number x)
begin
if (x <= 1) return false
var i <- 2
for i until i > x / 2 by 1
begin
if (x % i = 0) return false
end
return true
end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 481))
        
    def test_083_test_1_No_entry_point(self):
        input = """
            var VoTien <- VoTien
            func main() return
        """
        expect = "Undeclared Identifier: VoTien"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_084_test_1_No_entry_point(self):
        input = """
            func main() return main()
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(main), []))"
        self.assertTrue(TestChecker.test(input, expect, 483))
            
    def test_085_test_arraylit(self):
        input = """
            dynamic x
            number a <- [x]
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 484))        
        
    def test_086_test_1_No_entry_point(self):
        input = """
            dynamic x
            number a[3] <- [x]
            func f()
            begin
                x <- [1,2,3]
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 485))        
        
    def test_087_test_1_No_entry_point(self):
        input = """
            dynamic x
            number a[3] <- [x, 1, 2]
            func  main()
            begin
                x <- 1
            end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 486))     
        

    def test_088_test_1_No_entry_point(self):
        input = """
            dynamic x
            number a[3] <- [x, x, x]
            func  main()
            begin
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 487))   
        
    def test_089_test_1_No_entry_point(self):
        input = """
            dynamic x
            number a[3] <- [x, x, "1"]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x), Id(x), StringLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 488))   
        
    def test_090_test_1_No_entry_point(self):
        input = """
            dynamic x
            number a[3] <- [x, 1, "1"]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), NumLit(1.0), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 489))  
        
    def test_091_test_1_No_entry_point(self):
        input = """
            dynamic x
            number a[3] <- [x, [x,x], 1]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 490))  

    def test_092_test_1_No_entry_point(self):
        input = """
            dynamic x
            number a[3] <- [1, [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), ArrayLit(Id(x), Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_093_test_1_No_entry_point(self):
        input = """
            dynamic x
            number a[3] <- [[1,2,3], [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 492))     
        
    def test_094_test_1_No_entry_point(self):
        input = """
            dynamic x
            number a[3,3] <- [[1,2,3], x, x]
            func  main()
            begin
                x <- [1,2,3]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 493))     
        
    def test_095_test_1_No_entry_point(self):
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], [x,x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 494))  
        
    def test_096_test_1_No_entry_point(self):
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], 1]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 495)) 
        
    def test_097_test_1_No_entry_point(self):
        input = """
            dynamic x
            number a[2,3] <- [[1,2,3], [x,x]]
            func  main()
            begin
                x <- 1
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(x), Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 496)) 
        
    def test_098_test_1_No_entry_point(self):
        input = """
            dynamic x
            number a[1,1,1,1] <- [[[x]]]
            func  main()
            begin
                x <- [1]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 497)) 
        
        
    def test_099_test_1_No_entry_point(self):
        input = """
            dynamic x
            number a[1,1,2,2] <- [[[[1,2], x]]]
            func  main()
            begin
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 498)) 
        
    def test_100_test_1_No_entry_point(self):
        input = """
            dynamic x
            number a[1,1,2,2] <- [[[x, x]]]
            func  main()
            begin
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499)) 
  
    def test_101_test_1_No_entry_point(self):
        input = """
            dynamic x
            var a <- [x]
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 500))  
        
    def test_102_test_1_No_entry_point(self):
        input = """
            func foo() begin
                dynamic x
                return [x]                
            end
            func main() return 
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 501))  
        
    def test_103_test_1_No_entry_point(self):
        input = """
            func foo() begin
                dynamic x
                return [x, [1,2]]                
            end
            func main() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 502))  
        
    def test_104_test_1_No_entry_point(self):
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[y], [y]]
                return x
                return [[1], [2]]
            end
            func main() return 
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(ArrayLit(Id(y)), ArrayLit(Id(y))))"
        self.assertTrue(TestChecker.test(input, expect, 503))  
        
    def test_105_test_1_No_entry_point(self):
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[1], [2]]
                return [x, y]
                x <- [1]
                y <- x
            end
            func main() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 504)) 
        
        
    def test_106_test_1_No_entry_point(self):
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[1], [2]]
                return [x, [y]]
                x <- [1]
                y <- x
            end
            func main() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 505)) 
        
        
    def test_107_test_1_No_entry_point(self):
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo(x)
                x <- [[2,2], [2,3]]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 506)) 
        
    def test_108_test_1_No_entry_point(self):
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo([x])
                x <- [1]
            end
        """
        expect = "Type Cannot Be Inferred: CallStmt(Id(foo), [ArrayLit(Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 507)) 

    def test_109_test_1_No_entry_point(self):
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo([x, x])
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 508)) 
        
    def test_110_test_1_No_entry_point(self):
        input = """
            func foo(number a[2,2]) return 1
            func main() begin
                dynamic x
                var a <- foo([x, x])
                x <- [1,2]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 509)) 
        
    def test_111_test_1_No_entry_point(self):
        input = """
            func foo(number a[2,2]) return 1
            func main() begin
                dynamic x
                var a <- foo(x)
                x <- [1,2]
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), ArrayLit(NumLit(1.0), NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 510)) 

    def test_112_test_return(self):
        input = """
            func main() begin 
                return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 511))   

    def test_113_test_1_No_entry_point(self):
        input = """
            func main() begin 
                return 1
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 512))   

    def test_114_test_1_No_entry_point(self):
        input = """
            func main() begin 
                return 1
                begin
                    return "string"
                end
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 513))    
        
    def test_115_test_1_No_entry_point(self):
        input = """
            func main() begin 
                dynamic i
                return 1
                return i
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 514))  
        
    def test_116_test_1_No_entry_point(self):
        input = """
            func fun() begin
                return 
                return
                return 1
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 515))       
        
    def test_117_test_1_No_entry_point(self):
        input = """
            func fun() begin
                return 1
                return "string"
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 516))    
        
    def test_118_test_1_No_entry_point(self):
        input = """
            func fun() begin
                number a[3]
                return [1, 4, 3]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 517))   
        
    def test_119_test_1_No_entry_point(self):
        input = """
            func fun() begin
                number a[2,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 518))    
        
    def test_120_test_1_No_entry_point(self):
        input = """
            func fun() begin
                number a[3,2]
                return [[1,2], [3,4]]
                return a
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 519))  
        
    def test_121_test_1_No_entry_point(self):
        input = """
            func fun() begin
                number a[2,2]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 520))   
        
    def test_122_test_1_No_entry_point(self):
        input = """
            func fun() begin
                string a[2,2, 3]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 521))  
        
    def test_123_test_1_No_entry_point(self):
        input = """
            func fun() begin
                string a[2]
                return a
                return [["1","2"], ["3","4"]]
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 522))   
        
    def test_124_test_1_No_entry_point(self):
        input = """
            func fun() begin
                string a[1,1,1,1,1]
                return a
                return [[[[["1"]]]]]
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 523))     
        
    def test_125_test_1_No_entry_point(self):
        input = """
            func fun() begin
                return [1,2]
                return [3,4]
            end
            
            func fun1() begin
                return [[1,2], [3,4]]
                return [[1,5], [3,4]]
            end
            
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 524)) 
        
        
    def test_126_test_1_No_entry_point(self):
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               return fun3()
            end
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(fun3), []))"
        self.assertTrue(TestChecker.test(input, expect, 525)) 
        
    def test_127_test_1_No_entry_point(self):
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               return fun1()
            end
            func fun3() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 526)) 

    def test_128_test_1_No_entry_point(self):
        input = """
            func fun1() return 1
            func fun2() return
            func fun3()
            
            func main() begin 
               number a <- fun3()
            end
            func fun3() return "1"  
        """
        expect = "Type Mismatch In Statement: Return(StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 527)) 
        
                
    def test_129_test_1_No_entry_point(self):
        input = """
            func fun1() return [1,2]
            func fun2() return [3,4]
            func fun3()
            
            func main() begin 
               return fun1()
               return fun2()
               return fun3()
            end 
        """
        expect = "No Function Definition: fun3"
        self.assertTrue(TestChecker.test(input, expect, 528)) 
        

    def test_130_test_Assign(self):
        input = """
            func main() begin 
                number a
                dynamic b
                dynamic c
                b <- c
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 529)) 
        

    def test_131_test_1_No_entry_point(self):
        input = """
            func main() begin 
                number a
                dynamic b
                dynamic c
                a <- c
                b <- c
                return a
                return b
                return c
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 530))   
        
    def test_132_test_1_No_entry_point(self):
        input = """
            func main() begin 
                number a
                string b
                dynamic c
                a <- c
                c <- b

            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 531))   
        
    def test_133_test_1_No_entry_point(self):
        input = """
            func main() begin 
                number a
                string b
                dynamic c
                c <- a
                b <- c

            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 532))      
        
    def test_134_test_1_No_entry_point(self):
        input = """
            func main() begin 
                number a[1,3]
                dynamic c
                c <- [[1,2,3]]
                c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 533))   
        
    def test_135_test_1_No_entry_point(self):
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                c <- foo()
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(c), CallExpr(Id(foo), []))"
        self.assertTrue(TestChecker.test(input, expect, 534)) 
        
    def test_136_test_1_No_entry_point(self):
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                a <- foo()
            end
            func foo()
                return [[1,2,3]]
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 535))
        
    def test_137_test_1_No_entry_point(self):
        input = """
            func foo()
            func main() begin 
                number a[1,3]
                dynamic c
                a <- foo()
            end
            func foo()
                return [1,2,3]
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 536))

    def test_138_test_1_No_entry_point(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    number c[2] <- [3,4]
    number arr[2,2] <- [[a],c]
end
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(a)), Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 537))

    def test_139_test_1_No_entry_point(self):
        input = """
number a
func f(number a) begin
    number a <- a + a
    return a
end
"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 538))

    def test_140_test_1_No_entry_point(self):
        input = """
func foo()
            func foo2()
            func foo3()

            func main()
            begin
                dynamic i
                dynamic j
                dynamic k
                dynamic l
                for i until j >= k by l
                begin
                    continue
                end
                var a <- i + j + k + l

                for i until foo() by foo2()
                begin
                    foo3()
                end

                number b <- foo2()
                bool c <- foo()

            end

            func foo()
                return true
            func foo2()
                return 1
            func foo3()
                return 0
"""
        expect = "Type Mismatch In Statement: Return(NumLit(0.0))"
        self.assertTrue(TestChecker.test(input, expect, 539))

    def test_141_test_1_No_entry_point(self):
        input = """
func a()
begin
    return 1
end
func main()
begin
    number b <- a()
    return
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 540))

    def test_142_test_1_No_entry_point(self):
        input = """
            func main() return main()
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(main), []))"
        self.assertTrue(TestChecker.test(input, expect, 541))

    def test_143_test_1_No_entry_point(self):
        input = """
            func foo()
            func main() begin
                number foo_ <- foo()
            end
            func foo() begin
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 542))

    def test_144_test_1_No_entry_point(self):
        input = """
func main()
begin
    dynamic a
    dynamic b
    number c[2] <- [3,4]
    number arr[2,2] <- [[a],c]
end
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(a)), Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 543))

    def test_145_test_1_No_entry_point(self):
        input = """
func foo(number a)

func main()
begin
    number a <- foo(1)
    return
end

func foo(number a)
begin
    return
end
"""
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 544))