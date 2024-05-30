x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x)
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']}

sports_directory['basketball'][1]='bryant'
sports_directory['soccer'][0]='andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)

#2
def iterateDictionary(some_list):
    for dictionary in some_list:
        output = ""
        for key, value in dictionary.items():
            output += f"{key} - {value}, "
        print(output[:-2])  # Remove the trailing comma and space

# Given list of dictionaries
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
iterateDictionary(students)

#3
def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])
        else:
            print(f"The key '{key_name}' is not present in one of the dictionaries.")

# Example usage with 'first_name' key:
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

print("Output for 'first_name':")
iterateDictionary2('first_name', students)

# Example usage with 'last_name' key:
print("\nOutput for 'last_name':")
iterateDictionary2('last_name', students)

#4
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key.upper()}")
        for item in value:
            print(item)
        print()

# Example usage:
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)







