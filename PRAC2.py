
##### FUNCTION PRACTICE EXCERCISE #####

import math

def myfunc(string):
    new_string=[]
    
    for x in range(len(string)):
        if x%2==0:
            new_string += string[x].upper()
        else:
            new_string += string[x].lower()
    return new_string        

# lesser of two evens-if no. are even return lesser else return greater if odd

def lesser_even(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
        
# animal crackers- to write a function that takes in a two word string and then returns true if both words begin with the same letter.

def animal_cracker(text):
    word=text.split()
    print(word)
    
    return word[0][0]==word[1][0]
    
# makes twenty- given two integers return true if the sum of the integers is 20, or if one of the integers themselves is 20, if neither of these is true, go ahead and return false. 

def makes_twenty(n1,n2):
    return n1+n2==20 or n1==20 or n2==20
        
        
## LEVEL ONE PROBLEM ##

# wanted you to write a function that capitalizes the first and fourth letters of a name.

def cap(name):
    first_letter=name[0]
    in_btw=name[1:3]
    fourth_letter=name[3]
    rest=name[4:]
    
    return first_letter.upper() + in_btw + fourth_letter.upper() + rest
        
        
            
# master yoda- given sentence, return the sentence with word reversed

def rev(sentence):
    sen=sentence.split()
    print(sen)
    senrev=sen[::-1]
    print(senrev)
    return ' '.join(senrev)
    
# ALMOST THERE- given an integer n, return true if n is within 10 of either 100 or 200    

def almostthere(n):
    
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)
    
    
## LEVEL TWO PROBLEM ## 

## LEVEL TWO PROBLEM ## 

# return true If this list or array contains a three next to a three somewhere.

def has_33(nums):
    
    for i in range(len(nums)-1):
        
        if nums[i] == 3 and nums[i+1] == 3:
            return True
        return False    





    
