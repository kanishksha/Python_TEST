import math

num=[1,2,3,4,5]

sqrr=[math.sqrt(x) for x in num] 

print(sqrr)

listt=[1,2,[3,4,'hello']]

listt[2][2]='goodbye'

print(listt)

# PYTHON statments test 

st='sam printS only the word that starts with s in the sentence'

for word in st.split():
    if word[0].lower() == 's':
        print(word)

print(st.split())

#use range() to print even numbers 0 to 10

for num in range(0,11,2):
    print(num)
    
#
for num in range(0,51):
    if num%3==0:
        print(num)
#
list=[numm for numm in range(0,51) if numm%3==0]
print(list)

# go through the string below and length of word is even print even

sttt='go through the string below and length of word is even print even'

for w in sttt.split():
    if len(w)%2==0:
        print(w, "word is even")

#buzz and fizz ques if multiple of 3 fizz, if 5 buzz if both fizzbuzz

for intt in range(1,101):
    if intt%3==0:
        print("fizz")
    elif intt%5==0:
        print("buzz")
    elif intt%3==0 and intt%5==0:
        print("fizzbuzz")
    else:
        print(intt)
        
#first letter of every in the string by using list comprehension

stringg='first letter of every in the string by using list comprehension'

k=[wrd[0] for wrd in stringg.split()]
print(k)
print(stringg.split())

        