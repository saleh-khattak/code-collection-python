def greaterNum(n1,n2,n3):
    if(n1>n2 and n1>n3):
        greater=n1
    elif(n2>n1 and n2>n3):
        greater=n2
    elif(n3>n1 and n3>n2):
        greater=n3
    return greater

n1=int(input("Enter a number "))
n2=int(input("Enter a number "))
n3=int(input("Enter a number "))
print(f"The greater number is :  {greaterNum(n1,n2,n3)}")
