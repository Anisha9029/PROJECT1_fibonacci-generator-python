# Fibonacci Generator

try:
    n = int(input("Enter how many Fibonacci numbers you want: "))
    if n > 0:
        a, b = 0, 1
        seq = []
        for _ in range(n):
            seq.append(a)   
            a, b = b, a + b 
        print(seq)
    else:
        print("Please enter a positive number.")
except ValueError:
    print("Invalid input. Please enter an integer.")
