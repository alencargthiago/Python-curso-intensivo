maior=None
menor=None
while True:
    num= input("Enter a number:")
    if num =="done":
        break
    try:
        num=int(num)
        if maior is None or num > maior:
            maior=num
        if menor is None or num < menor:
            menor= num
    except:
        print("Invalid input")
        
print("Maximum is", maior)
print("Minimum is", menor)