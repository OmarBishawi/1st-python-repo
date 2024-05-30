def a():
    return 5
print(a())           # prediction:none / output :5  incorrect

#2
def a():
    return 5
print(a() + a())     #prediction :10 / output :10 correct

#3 
#3
def a():
    return 5
    return 10
print(a())            #prediction : 5 /output :5 correct


#4
def a():
    return 5           #prediction : 10,5 /  putput:5 incorrect
    print(10)
print(a())


#5
def a():
    print(5)
x = a()
print(x)             #prediction :5,5  /output :5,none incorrect

#6
# def a(b,c):
 #   print(b+c)
#print(a(1,2) + a(2,3))   #prediction :error  / correct   none + none

#7
def a(b,c):
    return str(b)+str(c)   #prediction :25 /correct
print(a(2,5))

#8
def a():                 #prediction 100,10 correct
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#9
def a(b,c):           #prediction :7,14,21 correct
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#10                        #prediction :8 correct
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#11                      #prediction incorrect 
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#12           #prediction correct
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)


#13             #incorrect prediction
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#14               correct 
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)






























