import re

matchme = re.compile("<[Kk]aliu[mM]")

f = open("logs.txt","r")
stor = f.read()
stor = stor.split("\n")
w = open("out.txt","w")

for k in stor:
    if matchme.search(k):
        trim = k[k.find(">")+2::]
        w.write(trim+"\n")

print("done!")
