#write functions here, don't add input('') statements here!


def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True