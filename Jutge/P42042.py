letra=input()
if letra.isupper():
    print("majuscula")
if letra.islower():
    print("minuscula")
if letra in "AEIOUaeiou":
    print("vocal")
else:
    print("consonant")