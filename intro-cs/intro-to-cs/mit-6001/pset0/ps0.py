import pylab
x = int(input("Enter number x: "))
y = int(input("Enter number y: "))
powerResult = x**y
logResult = pylab.log2(x)
print("x**y = ", powerResult)
print("log(x) =", logResult)