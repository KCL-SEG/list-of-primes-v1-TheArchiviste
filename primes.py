"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 2
    while len(list) < number_of_primes:
        for i in range(2, count // 2):
            if count % i != 0:
                list.append(count)
    return list
