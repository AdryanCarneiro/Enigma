entrada= "AAAAABABABABABABABABA"
armada = "ABA"
cont =0
cont2=0
for i in range (len(entrada)-(len(armada))):
    cont=0
    for p in range (len(armada)):
        if entrada[i+p] != armada[p]:
            cont+=1

        else:
            break

    if cont == (len(armada)):
        cont2+=1

print(cont2)
