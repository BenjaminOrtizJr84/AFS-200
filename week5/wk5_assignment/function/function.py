def maxNumber (a,b,c):
    if a > b and a > c :
        print("Biggest Number=", a)
    elif b > a and b > c:
        print("Biggest Number=", b)
    elif a == b:
        print("a = b") 
    elif a == c: 
         print("a = c")
    elif b == c:
        print("b = c")
    
    print("Biggest Number=",c)   

maxNumber(10, 20, 30)