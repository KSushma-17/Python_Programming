#1. Use map() with a lambda to add 5 to every element of the following nested list [[1, 2], [3, 4], [5, 6]]

nums = [[1, 2], [3, 4], [5, 6]]
result = list(map(lambda sub: list(map(lambda x: x + 5, sub)), nums))
print(result)


#2. Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use filter() to keep only the keys whose values are greater than 50.

d = {"apple": 100, "banana": 40, "cherry": 150}
result = dict(filter(lambda item: item[1] > 50, d.items()))
print(result)


#3. Use functools.reduce() with a lambda to find the largest number from a given list Dynamically.

from functools import reduce
nums = [12, 45, 7, 89, 23]
largest = reduce(lambda a, b: a if a > b else b, nums)
print(largest)


#4. What happens if the lambda passed to reduce() accepts only one parameter or three parameters? Explain the output or error.
#case-1:one parameter
from functools import reduce
nums = [1, 2, 3]
reduce(lambda x: x + 1, nums)
#case-2:three parameters
from functools import reduce
nums = [1, 2, 3]
reduce(lambda a, b, c: a + b + c, nums)


#5. Use map() on a string to convert each character into its ASCII value (using ord()). Print the result list.

text = "Python"
result = list(map(ord, text))
print(result)


#6. Use filter() to remove all vowels from a string and print the final string.

text = "Functional Programming"
vowels = "aeiouAEIOU"
result = ''.join(filter(lambda ch: ch not in vowels, text))
print(result)


#7. Use reduce() to concatenate a list of characters into a single string. Example input: ['P', 'y', 't', 'h', 'o', 'n'].

from functools import reduce
chars = ['P', 'y', 't', 'h', 'o', 'n']
result = reduce(lambda a, b: a + b, chars)
print(result)


#8. Given a list of integers, use map() with id() to print the memory address of each element. Example: [10, 350, 10, 350, 20] — explain why some addresses repeat.

nums = [10, 350, 10, 350, 20]
addresses = list(map(id, nums))
print(addresses)


#9. Explain the difference between: map(str, [1, 2, 3]) map(lambda x: str(x), [1, 2, 3]) Which one is faster and why?

map(str, [1, 2, 3])
#directly uses built-in str
#cleaner and faster

map(lambda x: str(x), [1, 2, 3])
#creates an extra lambda function call
#unnecessary wrapper

map(str, [1, 2, 3])
#built-in functions are optimized in C
#avoids extra Python-level lambda execution


#10. Given a list of numbers: [5, 10, 15, 20, 25, 30] Perform the following in a single pipeline: • Use map() to square each number • Use filter() to keep only numbers divisible by 5 • Use reduce() to calculate the sum of remaining numbers.

from functools import reduce
nums = [5, 10, 15, 20, 25, 30]
result = reduce(
    lambda a, b: a + b,
    filter(
        lambda x: x % 5 == 0,
        map(lambda x: x ** 2, nums)
    )
)
print(result)


#11. Explain the difference between map(), filter(), and reduce() in Python. • What does each function return? • When should you prefer lambda functions over normal functions?

#Function	Purpose	                                  Returns
#map()	    Transform elements	                      map object
#filter()	Select elements based on condition	      filter object
#reduce()	Reduce sequence to single value	          single value

#map()
list(map(lambda x: x * 2, [1,2,3]))

#filter()
list(filter(lambda x: x % 2 == 0, [1,2,3,4]))

#reduce()
from functools import reduce
reduce(lambda a,b: a+b, [1,2,3,4])

"""
When to prefer lambda?

Use lambda:

for short, one-time logic
when function is simple

Use normal functions:

when logic is complex
reused multiple times
needs readability/debugging

Overusing lambda makes code harder to maintain."""


#12. Given two lists: a = [1, 2, 3, 4] b = [10, 20, 30, 40] Use map() with a lambda to create a new list containing the sum of corresponding elements.

#equal length
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
result = list(map(lambda x, y: x + y, a, b))
print(result)

#unequal length
a = [1, 2, 3]
b = [10, 20, 30, 40]
result = list(map(lambda x, y: x + y, a, b))
print(result)


#13. Given a list: nums = [12, 15, 7, 18, 20, 21, 25] Use filter() and lambda to keep numbers that are divisible by 3 OR divisible by 5 but NOT divisible by both. Explain how the logical condition works.

nums = [12, 15, 7, 18, 20, 21, 25]
result = list(filter(
    lambda x: (x % 3 == 0 or x % 5 == 0) and not (x % 3 == 0 and x % 5 == 0),
    nums
))
print(result)


#14. Given a list: nums = [1, 2, 3, 4] Use reduce() with a lambda to compute the sum, but start with an initial value of 10. Explain how the initial value affects the reduction process.

from functools import reduce
nums = [1, 2, 3, 4]
result = reduce(lambda a, b: a + b, nums, 10)
print(result)


#15. Consider the code below: nums = [[1, 2], [3, 4], [5, 6]] result = list(map(lambda x: x.append(10), nums)) print("Result:", result) print("Nums:", nums) Questions • What will be the output of result? • What will be the output of nums? • Why does map() behave this way with list.append()? • How can you modify the lambda so that nums is not changed?

nums = [[1, 2], [3, 4], [5, 6]]
result = list(map(lambda x: x.append(10), nums))
print("Result:", result)
print("Nums:", nums)

#how to avoid modifying nums?
nums = [[1, 2], [3, 4], [5, 6]]
result = list(map(lambda x: x + [10], nums))
print("Result:", result)
print("Nums:", nums)


