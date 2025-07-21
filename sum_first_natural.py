def sumOf(n):
    if(n==1):
        return 1
    return sumOf(n-1)+n

num=int(input("Enter a number:"))
ans=sumOf(num)
print(f"The sum of first {num} nutual number is: {ans}")