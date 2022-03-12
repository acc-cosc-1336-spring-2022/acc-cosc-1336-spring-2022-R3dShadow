#add import
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
        if num == False:
            return isprime(num)
        else:
            str(input("Would you like to continue Y/N?"))
            if "Y":
                return isprime(num)
            else:
                "Thank you for running the program"

num1 = int(input("Please enter a number"))
num2 = isprime(num1)
print(num2)