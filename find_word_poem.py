f=open("poem.txt","r")
content=f.read()
if("twinkle" in content):
    print("The word twinkle is present in file")
else:
    print("The word twinkle is not presen in file")