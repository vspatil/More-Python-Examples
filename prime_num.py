# checking the number is prime or not
# 1 is not a prime number
# prime number is a positive number greater than > 1 and will be divisible by 1 and itself i.e. 2,3,5,7,11,13,17,19,23


num = int(input("Enter the number: "))

if num > 1: #number is grater than 1
    for i in range(2,num): # starts from 2 and excludes num
        if(num % i)== 0:
            print(num,"is not a prime number!")
            print(i, "times" ,num//i ,"is",num)
            break
    else:
            print(num , "is a prime number")
            print(num,"times",num//i,"is",num)
else:
    print(num," is not a prime number")
