##Chaine Mudalige
##integration project
##This program solves Linear Systems of Equations with -1 as one of the coefficients.
##Each equation has two variables with one of the coefficients being -1.
##Should be able to figure out where the -1 coefficient is located and choose the appropriae steps to solve for the two vairables and shows the steps to get there.
##I used POGLE 7 (Python Activity 7: Nested IF-ELSE Statements [Word Document] ,Python Activity 7: Nested IF-ELSE Statements. Microsoft Corpiration.Python Activity 07 Nested IF-ELSE Statements - POGIL.docxPreview the document) and  (Repl.it - https://repl.it/student/submissions/10782948) to help me with my integration project
a = int(input("Enter a positive or negative number for the constant of x in the first equaltion: "))
c = int(input("Enter a positive or negative number for the constant of y in the first equaltion: "))
d = int(input("Enter what the frist equation equals: "))
e = int(input("Enter a  positive or negative number for the constant of x in the second equaltion: "))
g = int(input("Enter a positive or negative number for the constant of y in the second equaltion: "))
h = int(input("Enter what the frist equation equals: "))
print(a, c, d, e, g, h)
print(a, "* x", "+", c, "* y", "=", d)
print(e, "* x", "+", g, "* y", "=", h)
if -1 == a and abs(a * e) == abs(e):
    print((a*e), "x", "+", (c*e), "y", "=", (d*e))
    print(e, "x", "+", g, "y", "=", h)
    print(((a*e) + e), "x", "+", ((c*e) + g), "y", "=", ((d*e) + h))
    print((((c*e) + g) / ((c*e) + g)), "y", "=", (((d*e) + h) / ((c*e) + g)))
    y = (((d*e) + h) / ((c*e) + g))
    print(a, "* x", "+", (c * y), "=", d)
    print(a, "* x", "+", ((c * y) - (c * y)), "=", (d - (c * y)))
    print((a / a), "* x", "+", ((c * y) - (c * y)), "=", ((d - (c * y)) / a))
    x = ((d - (c * y)) / a)
    print("x =", x, "y =", y)
elif -1 == c and abs(c * g) == abs(g):
    print((a*g), "x", "+", (c*g), "y", "=", (d*g))
    print(e, "x", "+", g, "y", "=", h)
    print(((a*g) + e), "x", "+", ((c*g) + g), "y", "=", ((d*g) + h))
    print((((a*g) + e) / ((a*g) + e)), "x", "=", (((d*g) + h) / ((a*g) + e)))
    x = (((d*g) + h) / ((a*g) + e))
    print((a * x), "+", c, "* y", "=", d)
    print(((a * x) - (a * x)), "+", c, "* y", "=", (d - (a * x)))
    print(((a * x) - (a * x)), "+", (c / c), "* y", "=", ((d - (a * x)) / c))
    y = ((d - (a * x)) / c)
    print("x =", x, "y =", y)
elif -1 == e and abs(e * a) == abs(a):
    print(a, "x", "+", c, "y", "=", d)
    print((e*a), "x", "+", (g*a), "y", "=", (h*a))
    print(((e*a) + a), "x", "+", ((g*a) + c), "y", "=", ((h*a) + d))
    print((((g*a) + c) / ((g*a) + c)), "y", "=", (((h*a) + d) / ((g*a) + c)))
    y = (((h*a) + d) / ((g*a) + c))
    print(a, "* x", "+", (c * y), "=", d)
    print(a, "* x", "+", ((c * y) - (c * y)), "=", (d - (c * y))) 
    print((a / a), "* x", "+", ((c * y) - (c * y)), "=", ((d - (c * y)) / a))
    x = ((d - (c * y)) / a)
    print("x =", x, "y =", y)
elif -1 == g and abs(g * c) == abs(c):
     print(a, "x", "+", c, "y", "=", d)
     print((e*c), "x", "+", (g*c), "y", "=", (h*c))
     print(((e*c) + a), "x", "+", ((g*c) + c), "y", "=", ((h*c) + d))
     print((((e*c) + a) / ((e*c) + a)), "x", "=", (((h*c) + d) / ((e*c) + a)))
     x = (((h*c) + d) / ((e*c) + a))
     print((a * x), "+", c, "* y", "=", d)
     print(((a * x) - (a * x)), "+", c, "* y", "=", (d - (a * x)))
     print(((a * x) - (a * x)), "+", (c / c), "* y", "=", ((d - (a * x)) / c))
     y = ((d - (a * x)) / c)
     print("x =", x, "y =", y)


#Other examples
print(2 ** 2)
num2 = 100
print(num2)
num2 = 100 + 2
print(num2)

    
    
    
    
### paart 2 ###


b = input(int())
i = input()
j = input(int())
k = input()
l = input()
m = input()
n = input()
o = input()


print(bgh)

# countinuously add, subtract, multil]ply, and divide until you want to finish.
# Finish when number: None
#part 2
def getadda(num):
    h = 0
    h += num
    return h

def getequation(j,k):
    a = str("add")
    b = str("subtract")
    c = str("multiply")
    d = str("divide")
    e = str("done")
    g = str(input("Enter a word add, subtract, multiply, or divide: "))
    i = 0
    while i == 0:
        if a == g:
            k += j
            return k
            
        elif b == g:
            k -= j
            return k
        elif c == g:
            k *= j
            return k
        elif d == g:
            k /= j
            return k
        elif e == g:
            print(k)
            return k
            break
        else:
            print("pi")
            break
            
    
    




def main():
    a = "add"
    b = "subtract"
    c = "multiply"
    d = "divide"
    e = "done"
    i = 0
    f = int(input("Ehter a number: "))
    answerAdda = getadda(f)
    print("The smaller of the two numbers is", answerAdda)
    while i == 0:
        a = "add"
        b = "subtract"
        c = "multiply"
        d = "divide"
        e = "done"
        i = 0
        j = int(input("Enter a number: "))
        k = answerAdda
        answerEquation = getequation(j,k)
        answerAdda = answerEquation
        print("number: ", answerAdda)
        
### call to main ###
main()


