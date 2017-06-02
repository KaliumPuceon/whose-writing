import re

matchme = re.compile("<[Kk]aliu[mM]")
matchurl = re.compile("www|http|youtu\.be")

f = open("logs.txt","r")
stor = f.read()
stor = stor.split("\n")
w = open("out.txt","w")
f.close()
for k in stor:
    clearstring = ""
    if matchme.search(k):
        trim = k[k.find(">")+2::]
        
        #I need to clean out URL's so I'm gonna destroy any words
        #starting with http or www or youtu.be 
        clearstring=""
        
        for l in trim.split(" "): 
            
            if not matchurl.search(l):
                
                clearstring = clearstring + " " + l

        if not len(clearstring) == 0:
            w.write(clearstring[1::] + "\n")

w.close()
print("done!")
