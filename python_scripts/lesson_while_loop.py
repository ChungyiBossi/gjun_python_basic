# Fibonacci num < 10000
def find_fibonacci(constraint):
    F0 = 0
    F1 = 1
    # F2 = F0 + F1
    list_fib = [F0, F1]
    while list_fib[-1] < constraint:
        list_fib.append(list_fib[-2] + list_fib[-1])
    return list_fib

if __name__ == '__main__':
    fibs = find_fibonacci(10000)
    print(fibs, len(fibs))