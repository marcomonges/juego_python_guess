import random

guessesTaken = 0
minNumber = 1
maxNumber = 20

print("Hola, cual es tu nombre?: ")
username = input()

number = random.randint(minNumber, maxNumber)
print("Bueno, " + username + ". Elige un numero del " + str(minNumber) + " al " + str(maxNumber))

#Bucle del Juego
while guessesTaken < 6:
    print("Elige un Numero: ")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1
    
    if guess < number:
        print("Tu numero es muy bajo.")
    if guess > number:
        print("Tu numero es muy alto.")
    if guess == number:
        break

if guess == number:
    print("Buen trabajo " + username + ", adivinaste mi numero en " + str(guessesTaken) + " intentos.")

if guess != number:
    print("No, el numero que estaba pensando era: " + str(number))

