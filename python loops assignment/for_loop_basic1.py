for x in range (151):    #integers from 0 to 150 
    print(x)

for y in range (5,1001,5):  #multiple of 5
    print(y)

for z in range (1,101):       #coding dojo 
    if z % 10 == 0:
        print("coding dojo")
    elif z % 5 == 0:
        print("coding")
    else:
        print(z)


sum = 0       ## sum 
for o in range (1,500001,2):    
    sum += o
print("The sum of odd integers from 0 to 500,000 is:",sum)


number = 2018      #positive_numbers
while number > 0:
    print(number)
    number -= 4

    lowNum = 2
highNum = 9
mult = 3

for p in range(lowNum, highNum + 1):
    if p % mult == 0:
        print(p)

