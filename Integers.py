def find_sum(n):
    if n == 0:
        return 0
    else:
        return n + find_sum(n-1)

n = int(input("Enter a number: "))

result = find_sum(n)
print(f"The sum of the first {n} integers is {result}.")