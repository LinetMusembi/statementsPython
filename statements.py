#Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50.
def  even_num():
    x=0
    while x<=50:
        x+=1
        if x%2!=0:
            continue
        print(x)

#Write a function that takes an integer argument and prints "Prime" if the number 
# is prime, and "Not prime" if the number is not prime. 
def prime_num(b):
    if b<=1:
        print("is a prime number")
    elif b>1:
        for i in range (2,b):
            if b%i==0:
                print("not prime")
                break 
            else:
                print("prime")    

   

# Write a function that takes a list of integers as input and prints the sum of all 
# the even numbers in the list.    
        
def sum_odd():
    sum=0
    for i in range(15):
        if i%2==0:
            sum=sum+i
            print("sum=",sum)


#Write a function that takes any two integers as input, and prints the sum of all 
# the numbers between the two integers (inclusive) that are divisible by 3. 

def int_nums():
    n,m=3,10
    for i in range(1,m+1):
        sum1=0
        sum2=0
    if i %n==0:
        sum1+=i
    else:
        sum2+=i
        print(f"{sum1} {sum2}")        




