import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase

print("Herzlich willkommen beim Caesar_chiffre.py-Programm.")
print("Viel Spaß beim \"Verschlüsseln\"")

def encrypt(string, n):
    encrypted_string = ""
    for c in string:
        if c in lower:
            index = lower.find(c)
            encrypted_string += lower[(index + n)%26]
        elif c in upper:
            index = upper.find(c)
            encrypted_string += upper[(index + n)%26]
        else:
            encrypted_string += c
    print(encrypted_string)

string = input("Satz: ")
n = int(input("Verschiebung: "))
encrypt(string, n)
