def f_to_c(f):
    c=(5*(f-32))/9
    return c

f=int(input("Enter fahrenhiet :"))
celsius=f_to_c(f)
print(f"The temperature in Celsius is :{round(celsius,2)} C")