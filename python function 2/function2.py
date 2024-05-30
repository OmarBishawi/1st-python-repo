def countdown(n) :
    return list (range(n,-1,-1))

#example 
number  = 5
result = countdown(number)
print(result)   #[5,4,3,2,1,0]

#2
def printandreturn(numbers) :
    print("first value:", numbers[0])
    return numbers [1]
#example
my_list = [10,20]
result =printandreturn(my_list)
print ("returned value:", result)


#3
def pluslength(lst):
    sum = lst[0] + len(lst) 
    return sum 

finallist = [1,2,3,4,5]
finalresult =pluslength(finallist)
print(finalresult)


#3 another solution :
def sum_first_and_length(lst):
    # Check if the list is not empty
    if lst:
        # Calculate the sum of the first value and the length of the list
        return lst[0] + len(lst)
    else:
        # Return 0 if the list is empty
        return 0

# Example usage:
my_list = [1, 2, 3, 4, 5]
result = sum_first_and_length(my_list)
print("Result:", result)

#4
def greaterthansecond(lst):
    if len(lst) < 2:
        return False 
    second_value = lst[1]
    newlist = []
    for i in lst:
        if i > second_value:
            newlist.append(i)
    print(len(newlist))
    return newlist

print(greaterthansecond([1, 3, 2, 4, 5])) 
print(greaterthansecond([3]) )     #example

#5
def intfunction(size,value):
    return [value] * size
   #example 
size = 5
value = 10
result = intfunction(size, value)
print(result)

