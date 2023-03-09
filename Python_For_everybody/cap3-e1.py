#qual sua pontuação?
note= float(input("Insira sua nota"))
if note <0 or note >1:
    print("Sua nota não é válida, insira um valor entre 0 e 1")
    quit()
elif note == 0.9:
    print("A")
elif note >0.8 and note < 0.9:
    print("B")
elif note >0.7 and note <0.8:
    print("C")
elif note >6 and note < 0.7:
    print ("D")
elif note < 0.6:
    print ("F")
