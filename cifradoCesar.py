import sys
cifra=False
if sys.argv[2]=="cifra":
    cifra=True
    fich1=open("text.txt","r")
    fich2=open("cifra.txt","w")
elif sys.argv[2]=="descifra":
    fich1=open("cifra.txt","r")
    fich2=open("text.txt","w")
else:
    print("Error argumento incorrecto")
    exit()

alfa= " ABCDEFGHIJKLMNOPQRSTUVWXYZÑ"
clave=int(sys.argv[1])
x=""

for line in fich1:
    for charac in line:
        numberCharac=alfa.find(charac.upper())
        if cifra:
            x+=alfa[(numberCharac+clave)%28]
        else:
            x+=alfa[(numberCharac-clave)%28]
fich2.write(x)
fich1.close()
fich2.close()
