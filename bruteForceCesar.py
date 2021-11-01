fich1=open("cifra.txt","r")
fich2=open("text.txt","w")

alfa= " ABCDEFGHIJKLMNOPQRSTUVWXYZÑ"
x=[]
for line in fich1:
    for charac in line:
        numberCharac=alfa.find(charac.upper())
        x+=[numberCharac]

for key in range(1,len(alfa)):
    fich2.write("Clave:"+str(key)+"->")
    for char in x:
        fich2.write(str(alfa[(char+key)%28]))
    fich2.write("\n")

fich1.close()
fich2.close()
