# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 19:37:37 2025

@author: Hi
"""

#Exercise 2: Prime Number Generator 

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_number_generator():
    try:
        # 1. Take two positive integers as input
        start = input("Enter the start of the range: ")
        end = input("Enter the end of the range: ")

        # 2. Validate input (must be positive integers)
        if not (start.isdigit() and end.isdigit()):
            print("Invalid input! Please enter only positive integers.")
            return
        
        start = int(start)
        end = int(end)

        if start <= 0 or end <= 0:
            print("Numbers must be positive!")
            return
        
        if start > end:
            print("Start of the range cannot be greater than the end.")
            return

        # 3. Find all primes in the range
        primes = [num for num in range(start, end + 1) if is_prime(num)]

        # 4. Display primes (10 numbers per line)
        print("\nPrime Numbers:")
        for i, prime in enumerate(primes, start=1):
            print(f"{prime:5}", end=" ")
            if i % 10 == 0:   # new line after 10 numbers
                print()
        
        if len(primes) % 10 != 0:  # final newline
            print()

        if not primes:
            print("No prime numbers found in this range.")

    except Exception as e:
        # 5. Handle unexpected errors
        print(f" An unexpected error occurred: {e}")


# Run the program
prime_number_generator()