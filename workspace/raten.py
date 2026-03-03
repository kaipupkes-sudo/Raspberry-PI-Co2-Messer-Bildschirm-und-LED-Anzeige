import random
random_number = random.randint(1, 100)
print(random_number)
i=0
geratene_zahl = int(input(f"Geben Sie die erste Schätzung ein"))
go_on = True
while go_on:
    i +=1
    if geratene_zahl > random_number:
        print("zu hoch")
        geratene_zahl = int(input(f"Geben Sie die Schätzung Nummer {i} ein"))
    
    elif geratene_zahl < random_number:
        print("zu niedrig")
        geratene_zahl = int(input(f"Geben Sie die Schätzung Nummer {i} ein"))
    
    else:
        go_on = True
        print(f"Richtig. Du hast {None} Versuche gebraucht")
     