myfile = "myfile.txt"

with open(myfile,"w") as file:
    file.write("Hello file world\n")

with open(myfile,"r+") as file:
    content = file.read()
    print(content)

content = content.replace("Hello file ", "Hello my file ")

with open(myfile, "w") as file:
    file.write(content)
    file.flush()
