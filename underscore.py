class Underscore:
    def map(self, iterable, callback):
        return[callback(item) for item in iterable]
    def find(self, iterable, callback):
        for item in iterable:
            if callback(item):
                return item
            
    def filter(self, iterable, callback):
        return [item for item in iterable if callback(item)]
    def reject(self, iterable, callback):
        return[item for item in iterable if not callback(item)]
# you just created a library with 4 methods!
# let's create an instance of our class
_= Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above

print(_.map([1,2,3,],lambda x :x*2))
print(_.find([1,2,3,4,5,6],lambda x : x>4))#return first value greater than 4
print(_.filter([1,2,3,4,5,6],lambda X : X%2==0)) #[2,4,6]
print(_.reject([1,2,3,4,5,6],lambda X: X%2 ==0))
#We can say instead of lamba for example _..ap ([1,2,3],function(num){return num*3;})