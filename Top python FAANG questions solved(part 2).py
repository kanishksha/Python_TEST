
#1. Write a Python Program to print Prime Numbers between 2 numbers
#2. Write a Sort function to sort the elements in a list
#3. Write a sorting function without using the list.sort function
#4. Write a Python program to print Fibonacci Series
#5. Write a Python program to print a list in reverse
#6. Write a Python program to check whether a string is a Palindrome or not 
#7. Write a Python program to print set of duplicates in a list
#8. Write a Python program to print number of words in a given sentence
#9. Given an array arr[] of n elements, write a Python function to search a given element x in arr[].
#10. Write a Python program to implement a Binary Search
#11. Write a Python program to plot a simple bar chart
#12. Write a Python program to join two strings (Hint: using join())
#13. Write a Python program to extract digits from given string
#14. Write a Python program to split strings using newline delimiter
#15. Given a string as your input, delete any reoccurring character, and return the new string.


#1
lower=100
upper=200

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
         
#2
l1=[12,4,6,3,2,88,90,5678,7]
l1.sort( reverse =True)
print(l1)

#3

def sor(ll):
    
    newlist=[]
    
    while ll:
        minimum=ll[0]
        for x in ll:
            if x<minimum:
                minimum=x
        newlist.append(minimum)
        ll.remove(minimum)
    return newlist
    
ll=[12,4,6,3,2,88,90,5678,7]
print(sor(ll))

#4

def F(n):
    listt=[]
    if n== 0:
        return 0
    elif n==1:
        return 1
    else:
        return F(n-1)+F(n-2)
        
for i in range(0,12):
    var= F(i)
    print(var)
    
#5
def rev(k):
    return k[::-1]
    
k=[1,2,3,4,5,6,7]
l=rev(k)
print(l)

#6
def palindrome(s):
    if s == s[::-1]:
        return True
        
s='malayalam'
p=palindrome(s)
print(p)

#7
ll=[1,1,1,2,3,4,5,5,6,7,8,9,9]
def h(ll):
    a=set([x for x in ll if ll.count(x)>1])
    return a

ll=[1,1,1,2,3,4,5,5,6,7,8,9,9]
g=h(ll)
print(g)

#8
def m(k):
    o=len(k.split())
    return o

k='hi how are you, i am fine'
p=m(k)
print(p)

#9

def search(arr,x):
    
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return 'not present in number'

arr=[1,2,3,4,5,6,7,8,9,0]
x=1
print(search(arr,x))

#10

def binarysearch(sequence, item):
    
    begin_index=0
    end_index=len(sequence)-1
    
    while begin_index <= end_index:
        
        mid_point= begin_index + (end_index - begin_index) //2
        mid_pointvalue = sequence[mid_point]
        if mid_pointvalue == item:
            return mid_point
        elif item<mid_pointvalue:
            end_index= mid_point-1
        else:
            begin_index=mid_point + 1
    return None        
    
sequence=[1,2,3,4,5,6,7,8,9,10]
item=5
print(binarysearch(sequence, item))


#12
str1='hi how are you'
str2='i am good'

str3=' '.join((str1,str2))

print(str3)

#13
strd='hfsgefy3hejhtl4tglkwh'

d=','.join(filter(lambda x: x.isdigit(), strd))

print(str(d))

#15

def delreccur(string):
    outputstring=''
    for char in string:
        if char not in outputstring:
            outputstring += char
    return ' '.join(str(e) for e in outputstring)
s='missiippi'
h=delreccur(s)
print(h)


###extras

fruits = ["Apple", "Pear", "Peach", "Banana"]
prices = [0.35, 0.40, 0.40, 0.28]

fruit_dictionary = dict(zip(fruits, prices))

print(fruit_dictionary)
            

