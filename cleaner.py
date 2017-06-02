import re

matchme = re.compile("<[Kk]aliu[mM]")
matchurl = re.compile("www|http|youtu\.be")

f = open("logs.txt","r")
stor = f.read()
stor = stor.split("\n")
w = open("out.txt","w")
f.close()
for k in stor:
    if matchme.search(k):
        trim = k[k.find(">")+2::]
        #I need to clean out URL's so I'm gonna destroy any words
        #starting with http or www or youtu.be
        for l in trim.split(" "):
            cleanarr = []
            print(l)
            if not matchurl.search(l):
                cleanarr.insert(0,l)
        
        trim = " ".join(cleanarr)

        w.write(trim+"\n")

w.close()
print("done!")
