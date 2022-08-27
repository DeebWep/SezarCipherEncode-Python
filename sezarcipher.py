ciphercharsen_A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciphercharsen_a = "abcdefghijklmnopqrstuvwxyz"
badchars = " "
text = input("Enter Text:\n")
key = int(input("Enter Key Number: "))
textready = []
cipher_text = ""
for i in text:
    textready.append(i)

for j in textready:
    if j.isalpha():
        if j.isupper():
            k = ciphercharsen_A.index(j)
            k+=key
            if k >=26:
                k=k%26
            cipher_text += ciphercharsen_A[k]
        if j.islower():
            k = ciphercharsen_a.index(j)
            k+=key
            if k>=26:
                k=k%26
            cipher_text +=ciphercharsen_a[k]
    else:
        cipher_text += j
print("Cipher Text: ",cipher_text)

