#backend exercise to find how many repeating occurences 
# exist in given 2 lists(arrays)

arr = [2,3,4,3,2,1]
a=3

def some_function(arr, a):
    occurence = 0
    for i in arr:
        if i == a:
            occurence += 1
    print(occurence)
some_function(arr, a)
print(len(arr))
