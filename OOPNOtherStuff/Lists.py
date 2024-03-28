from itertools import count

#hey this is just a sample change to demonstrate how python works


s = "eggs"
B = "EGGS"
list1 = ["naruto", "sasuke", "sakura"]
numList = [1,2,3,4]
mixedList = ["anime",42,"gym", 1]
anotherList = list(("dogs", "cats", 2, "cats", 2, 2, "cats"))         #important to have double paranthesis

print(list1)
print(numList)
print(mixedList)
print(anotherList)

#list functions#
print(s.upper()) #changes to upper case
print(B.lower()) #changes to lower case

#append() - attaches one or more elements to the end of a list
list1.append("neji")
print(list1)
list1.append(mixedList)
print(list1)

#copy() - copies a list
x = list1.copy()
print(x)
#clear() - clears a list
list1.clear()
print(list1) 
#count() - counts duplicates of an element in a list. works with all variable types
y = anotherList.count("cats")
print(y)
#extend() - adds one or more elements to the end of a list. Diff from append() is the new elements become just like any other element in the list(the same list gets extended), instead of being a seperat
#list inside the list(the two list APPEND together, so it's two lists in one)
mixedList.extend(numList)
print(mixedList)
#index() -  returns the index of an element
z = mixedList.index(3)
print(z) #returns 6
#insert() - inserts an element at an index
anotherList.insert(3, "sheeps")
print(anotherList)
#pop() - "pops" or removes an element from an index in the list
anotherList.pop(3)
print(anotherList)
#remove() - removes the first matching element
anotherList.remove("cats")
print(anotherList)
#reverse() - reverses the list
mixedList.reverse()
print(mixedList)
#sort() - sorts the list in ascending order. compares the first letter for strings. Uppercases are always prioritized!!!
yeet = ["lier","two","one","four", "a", "Seven"]
yeet.sort()
print(yeet) #OBS! Numbers and strings cannot mix or else it returns error
    #Question - what if the initial letter is the same?
sameLetters = ["one","oak","ola","oz"]
sameLetters.sort()
print(sameLetters) #Answer - compares the 2nd letters instead

    #sort(reverse=true) - sorts in a descending order
yeet.sort(reverse=True)
print(yeet)
    #you can make a function if you wanna make your own sorting rules. Function becomes the "key" for the sorting
    #example:
def sortFunc(e):
    return len(e) #returns length of a string

yeet.sort(key=sortFunc)
print(yeet)
yeet.sort(key=sortFunc, reverse=True)
print(yeet)
yeet.sort(key=str.upper) #removes sorting by uppercase, which it otherwise does by default
print(yeet)
#
#
#
#
#
#