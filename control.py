#Write a function that uses while, if and continue statements to print
# all the even numbers between 0 and 50. 
def even_numbers():
    x = 1
    while x < 50:
        x+=1
        if x % 2 != 0:
            continue
        print(x)

#Write a function that takes an integer argument and prints "Prime" if 
# the number is prime, and "Not prime" if the number is not prime.
def prime_numbers(num):
    determiner = False
    for x in range (2,num):
        if num % x == 0:
            determiner = True
            break
    if determiner:
        print( num, "Not prime")
    else:
        print( num, "Prime number")

#Write a function that takes a list of integers as input and prints the 
# sum of all the even numbers in the list.
def even_numbers_listed(int_list):
    sum_even = 0
    for x in int_list:
        if x % 2 == 0:
            sum_even += x
    print(sum_even)

#Write a function that takes any two integers as input, and prints 
# the sum of all the numbers between the two integers (inclusive) that 
# are divisible by 3.
def two_Integers(integer1,integer2):
    sum_between = 0
    for x in range(integer1,integer2):
        if x % 3 == 0:
            sum_between += x
    print(sum_between)

    
    
