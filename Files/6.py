f1=open("demo1.txt","r")
line=f1.readlines()
f1.close()

f2=open("demo1.txt","w")
for lines in line:
    if lines.strip("\n") != "Nihad":
        f2.write(lines)

f2.close()
