
#from pandas import factorize
from math import sqrt, floor,ceil
from random import random
from itertools import product

def list_range(a,b,exclude = []):
    out = []
    for i in range(a,b):
        if i not in exclude:
            out.append(str(i))
    return out

def factorize(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


prime1 = [str(_) for _ in[2,3,5,7]]
prime2 = [str(_) for _ in[11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]]
prime3 = [str(_) for _ in[101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,
                        211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,
                        307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,
                        401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,
                        503,509,521,523,541,547,557,563,569,571,577,587,593,599,
                        601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,
                        701,709,719,727,733,739,743,751,757,761,769,773,787,797,
                        809,811,821, 823, 827,829,839,853,857,859,863,877,881,883,887,
                        907,911,919,929,937,941,947,953,967,971,977,983,991,997]]
square2 =[str(_)for _ in [16,25,36,49,64,81]]
square3 = [str(_)for _ in [100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,900,961]]
cube2 = [str(_)for _ in [27,64]]
cube3 = [str(_)for _ in [125,216,343,512,729]]
#cube4  = [str(_)for _ in [1000,1296,1728,2197,2744,3375,4096,4913,5832,6859,8000,9261]]
#cube5 = [str(_)for _ in [10000,14641,19683,25921,32768,40960,50653,614125,74088,88573]]
complete = []

def is_triangular(n):
    x = (sqrt(8*n + 1) - 1)/2
    return x.is_integer()

def generate_triangular(length):
    out = []
    lower = 10**(length-1)
    if length ==1:
        lower = 0
    for i in range(lower,10**length):
        if is_triangular(i):
            out.append(str(i))
    return out

def is_prime12(x):
    if x in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]:
        return True

def is_length(numbers,n):
    out = []
    for i in numbers:
        if len(i) == n:
            out.append(i)
    return out

def is_palindrome(x):
    return x == x[::-1]
def reverse(possibilities):
    return [_.reverse() for _ in possibilities]


def multiple_of(n,l):
    return [_*n for _ in range(1+ceil(10**(l-1)/n),1+floor(10**l/n))]

def generate(length,test):
    out = []
    lower = 10**(length-1)
    if length ==1:
        lower = 0
    for i in range(lower,10**length):
        if test(i):
            out.append(str(i))
    return out

def generate2(numbers, test):
    out = []
    for i in numbers:
        if test(int(i)):
            out.append(i)
    return out

def digit_product(x):
    out = 1
    for i in str(x):
        out *= int(i)
    return out
def digit_sum(x):
    out = 0
    for i in str(x):
        out += int(i)
    return out
def digit_occurence(numbers):
    digits = set()
    for i in numbers:
        for j in i[0]:
            digits.add(j)
    return len(digits) == 9

def check_repeat(numbers):
    seen = set()
    for i in numbers:
        for j in i[0]:
            if j in seen:
                return False
            seen.add(j)
    return True

def conditon_P(numbers): # condition to check when solution has been reached
    return digit_occurence(numbers) and check_repeat(numbers)

def conditon_N(numbers): # condition to check whilst searching for solution
    return True


across2 = lambda x: True if (sqrt(digit_product(x))).is_integer() else False

numbers =[
generate_triangular(4),
generate_triangular(3),
prime2.copy(),
list_range(20,100,exclude = prime2),
list_range(11,100),
generate_triangular(2),
generate_triangular(3),
generate_triangular(4),
list_range(200,1000,exclude = prime3),#down 1
generate_triangular(3),
generate_triangular(3),
generate_triangular(2),
generate_triangular(3),
generate_triangular(3),
prime3.copy(),
generate_triangular(2)

]

# enable if numbers have to be from a specific set such as a function of the clues
"""
for i2,i in enumerate(numbers):
    for j2,j in enumerate(numbers):
        if j not in complete:
            numbers[i2].pop(j2)
"""




link2020 = [(0,0,3,0),
        (0,1,4,0),
        (1,0,4,1),
        (1,1,5,0),
        (2,0,5,1),
        (2,1,3,2)
        ] # links for testing
#numbers[0].remove("77")
#format: number, digit, number, digit
links= [(0, 0, 9, 0), (0, 1, 10, 0), (0, 3, 11, 0), (1, 0, 12, 0), (1, 1, 13, 0), (1, 2, 14, 0), (2, 0, 8, 1), (2, 1, 9, 1), (3, 0, 10, 1), (3, 1, 15, 0), (4, 0, 11, 1), (4, 1, 12, 1), (5, 0, 13, 1), (5, 1, 14, 1), (6, 0, 8, 2), (6, 1, 9, 2), (6, 2, 10, 2), (7, 0, 15, 1), (7, 2, 12, 2), (7, 3, 13, 2)] 

same_digit_sum = lambda x,y: digit_sum(x) == digit_sum(y)
across3= lambda x,y: y-digit_sum(y) == x

constants = []
#format: number, constant_index, function
variables = [] 
conditions = [] #format: function,n0,(input numbers)
#condtions2 = [] #format: function,n0,(input numbers) 2 inputs only

decisions = []
tree = []

reduced = True
unsolved =True

iterations =100000

while unsolved:
    iterations -= 1
    if iterations ==0:
        print("iteration cap reached")
        break
    #reduce using number crossover
    while reduced:
        reduced = False
        for link in links:  
            a_number, a_digit, b_number, b_digit = link
            for i in numbers[a_number]:
                digit = i[a_digit]
                possible = False
                for j2,j in enumerate(numbers[b_number]):
                    if digit == j[b_digit]:
                        possible = True
                        break
                if not possible:
                    numbers[a_number].remove(i)
                    reduced = True
        for link in links: 
            b_number, b_digit, a_number, a_digit = link
            for i in numbers[a_number]:
                digit = i[a_digit]
                possible = False
                for j2,j in enumerate(numbers[b_number]):
                    if digit == j[b_digit]:
                        possible = True
                        break
                if not possible:
                    numbers[a_number].remove(i)
                    reduced = True
        
        for i in variables:
            number, constant, func = i
            for j in numbers[number]:
                value = int(j)
                possible = False
                for k in constants[constant]:
                    if value == func(k):
                        possible = True
                        break
                if not possible:
                    numbers[number].remove(j)
                    reduced = True
        for i in variables:
            number, constant, func = i
            for j2,j in enumerate(constants[constant]):
                if str(func(j)) not in numbers[number]:
                    constants[constant].pop(j2)
                    reduced = True


    
    for condition in conditions:
        func, n0, inputs = condition
        for number2, number in enumerate(numbers[n0]):
            possible = False
            for i in product(*[numbers[_] for _ in inputs]):
                if func(number,*i):
                    possible = True
                    break
            if not possible:
                numbers[n0].pop(number2)
                reduced = True
    
    if reduced: continue
    possible = True
    changed = False

    for i in numbers: # check if solved
        if len(i) != 1:
            possible = False
        if len(i) == 0 or conditon_N(numbers) == False: #update tree
            changed = True
            if len(tree) == 0:
                print("No solution")
                exit()
            loop = True
            while loop:
                loop = False
                if decisions[-1][1] < len(tree[-1][decisions[-1][0]]):
                    decisions[-1][1] += 1
                    numbers = tree[-1][0]
                    constants = tree[-1][1]
                else:
                    tree.pop()
                    decisions.pop()
                    loop = True
                    #add recursive
    if possible == True:
        if conditon_P(numbers): break
        else: 
            changed = True
            if len(tree) == 0:
                print("No solution")
                exit()
            loop = True
            while loop:
                loop = False
                if decisions[-1][1] < len(tree[-1][decisions[-1][0]]):
                    decisions[-1][1] += 1
                    numbers = tree[-1][0]
                    constants = tree[-1][1]
                else:
                    tree.pop()
                    decisions.pop()
                    loop = True
                    #add recursive
    
    if not changed: 
        lowest = len(numbers[0])
        shortest = 0
        for i,number in enumerate(numbers):
            if len(numbers) < lowest:
                lowest = len(numbers)
                shortest = i
            #elif len(numbers) == lowest:
            #    if random() <0.5:
            #        shortest = i

        

            

print(numbers)
print(constants)
print(decisions )