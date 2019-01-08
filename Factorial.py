# factorial of the number is the product of the all the numbers from 1 to that number
# factorial of 0 is 1

num =7
factorial =1

if num < 0:
    print(" Negatives numbers will not have factorial!")
elif num==0:
    print("Factorial of 0 is 1!")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("Factorial of a " ,num ,"is" ,factorial)