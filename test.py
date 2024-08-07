def sum_of_digits(n):
    return (n // 10) + (n % 10)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])  # Number of test cases
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        results.append(sum_of_digits(n))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
