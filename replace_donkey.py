word="donkey"

with open("file_donkey.txt","r") as f:
    content=f.read()
newcontent=content.replace(word,"######")

with open("file_donkey.txt","w") as f:
    f.write(newcontent)