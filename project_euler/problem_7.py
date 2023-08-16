# What is the 10,001st prime number ?

def is_prime(num):  # function to check if the given number is a prime
    if num <= 1:
        return False
    
    for i in range(2, int(num/2)): 
        if num%i == 0:
            return False
    
    return True


def n_prime(n):
    """
    This function finds the nth prime number
    """

    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
        if count == n:
            return num
        num += 1

print(n_prime(10001))
    