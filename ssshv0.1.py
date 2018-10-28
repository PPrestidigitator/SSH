
import sys


print("podaj partycje")
x=input()
path=x+":/ssh"
print("Ścieżka to: ", path)

try:
    open(path,"a").close()
    print ("ssh utworzony")
except Exception as e:
    print("blad: ", e)
    

sys.exit()
