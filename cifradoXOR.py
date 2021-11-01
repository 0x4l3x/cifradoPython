import sys
if sys.argv[2]=="cifra":
    fich1=open("text.txt","r")
    fich2=open("cifra.txt","w")
elif sys.argv[2]=="descifra":
    fich1=open("cifra.txt","r")
    fich2=open("text.txt","w")
else:
    print("Error argumento incorrecto")
    exit()

clave=sys.argv[1]
lenClave=len(clave)
encoded=""
plaintxt=""
n=0

for line in fich1:
    for charac in line:
        plaintxt+=charac
        encoded+=chr(ord(charac.encode("utf8"))^ord(clave[n].encode("utf8")))
        n=(n+1)%lenClave

# TESTING
decoded=""
n=0
for i in encoded:
    decoded+=chr(ord(i.encode("utf8"))^ord(clave[n].encode("utf8")))
    n=(n+1)%lenClave

if decoded==plaintxt :
    print("El funcionamiento es correcto")

fich2.write(encoded)
fich1.close()
fich2.close()
