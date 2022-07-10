#1. Sherlock Holmes is solving a case, and he is trying to find out if a Ransom Note belongs to a magazine
#2. Help the Merchant to count the number of pair of socks 
#3. Stacking up empty boxes: Amazon workers are trying to stack up empty boxes at the end
#4. Factory workers fill in missing time entries
#5. Given a string as your input, delete any recurring character, and return the new string.
#6. Essay Exam Competition: Average Word Length in a statement
#7. Analyze if a stock price has always gone up or always gone down
#8. how many toys boy can buy

#2
from collections import Counter

def socks(arr):
    count=0
    dic={x:arr.count(x) for x in arr}
    
    for val in dic.values():
        inc=int(val/2)
        count= count + inc
    return count
    
arr1=[1,2,3,3,2,1,5]
arr2=[9,9,8,7,7,6]


print(socks(arr1))
print(socks(arr2))


#1
def chose(m,n):
    
    a=(Counter(n)-Counter(m))
    if a==[]:
        return True
    else:
        return False
        
m1=['a','aa','c']
n1=['cc','b','a']

m2=['u','i','o']
n2=['u','r','o']

print('is n1 is m1: ', chose(m1,n1))
print('is n2 is m1: ', chose(m2,n2))

 
#3        
def putzeroinend(arr):
    
    for x in arr:
        if 0 in arr:
            arr.remove(0)
            arr.append(0)
    return arr
            
arr1=[1,0,2,0,2,7,0,12,15]
#result:[1,2,2,7,12,15,0,0,0]
print(putzeroinend(arr1))


#4
def mi(arr):
    result=[]
    isvalid=0
    for items in arr:
        if items is not None:
            result.append(items)
            isvalid= items
        else:
            result.append(isvalid)
    return(result)
    
arr1=[1,2,3,None,4,5,6,None]
print(mi(arr1))
        
        
#5
def str(s):
    
    seenchar=set()
    outputstring=''
    
    for char in s:
        if char not in seenchar:
            seenchar.add(char)
            outputstring+=char
    return outputstring
    
s='missiippi'
print(str(s))
        
        
#6# average word length in a statement

def stat(s):
    for p in ":?."";":
        s=s.replace(p,' ')
    
    words=s.split()
    w=sum(len(word) for word in words)/len(words)
    return round(w,2)    
s='hi how are you i am fine'
print(stat(s))


#7#define a function determine monotonic array

def monotonic(arr):
    
    r=range(len(arr)-1)
    
    for i in r:
        if arr[i]<=arr[i+1] or arr[i]>=arr[i+1]:
            return True
        else:
            return False
        
        
arr=[100,90,80,80,70,6,40,10]
print('array is monotonic', monotonic(arr) )

           


#8#how many toys boy can buy 
import math

def maxtoys(prices, k):
    prices.sort()
    cost=0
    i=0
    while cost<k:
        if cost+prices[i]<k:
            cost+=prices[i]
        else:
            break
        i+=1
    return i    

dollars=90
prices=[10,20,40,70,88,999]
print('can buy toys', maxtoys(prices,dollars))




#extra

print(Counter(list(("mississippi"))))
print(Counter(list(("Mary had a little lamb"))))   
    
print('Mary had a little lamb'.count('a'))   

def cn(s='Mary had a little lamb'):
    for x in s:
        print(s.count(x))
        
def c(s):
    c1='Mary hoeeee'
    counter=Counter(c1)
    print(counter)
    #both u can use
    counter.pop('M', None)
    del counter["M"]
    del counter[' ']
    print(counter)
            
        
def f(listt,num):
    newlist=[]
    for x in list:
        if x!=num:
            newlist.append(x)
        
    return newlist        

listt=[1,2,3,4,56,666,7]
num=2
print(newlist)    

    
    

        
