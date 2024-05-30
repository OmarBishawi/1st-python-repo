#1
def positive(lst):
    for i in range (len(lst)):
        if lst[i] > 0:
            lst[i] = "big"
        else :
            lst[i] = lst[i]
    return lst

result = positive([-1,3,5,-5])
print(result)

#2  counting positives
def replace(lst) :
    positive_value = 0
    for num in lst:
        if num >0 :
            positive_value +=1
    lst[-1] = positive_value
    return lst
#example 
positiveresult = replace([-1,1,1,1])
print(positiveresult)
    

#3 
def calculatesum(lst):
    return sum(lst)
my_list = [1, 2, 3, 4, 5]
total_sum = calculatesum(my_list)
print("The sum of the values in the list is:", total_sum)



#4 average
def average(lst):
    if not lst:
        return 0
    average = sum(lst)/len(lst)
    return average 
newaverage =average([1,2,3,4])
print(newaverage)

#5 list
def getlistlength(lst):
    return len(lst)
randomlist=([37,2,1,-9])
finallength = getlistlength(randomlist)

print (finallength)


#6
def minimum(lst):
    if not lst :
        return False 
    return min(lst)
my_list = [5, 2, 8, 1, 4]
min_value=minimum(my_list)
print(min_value)
    
#7
def maximum(lst):
    if not lst :
        return False
    return max(lst)
my_list = ([37,2,1,-9])
max_value = maximum(my_list)
print(max_value)

#8
def calculate_statistics(lst):
    if not lst:
        return {}
    stats = {
        "sumTotal": sum(lst),
        "average": sum(lst) / len(lst),
        "minimum": min(lst),
        "maximum": max(lst),
        "length": len(lst)
    }
    return stats
my_list = [5, 2, 8, 1, 4]
result = calculate_statistics(my_list)
print(result)

#9 
def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        # Swap elements at left and right indices
        lst[left], lst[right] = lst[right], lst[left]
        # Move the left pointer to the right
        left += 1
        # Move the right pointer to the left
        right -= 1

# Example usage:
my_list = [1, 2, 3, 4, 5]
reverse_list(my_list)
print("Reversed list:", my_list)




