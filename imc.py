altura = float(input("Altura: "))
peso = float(input("Peso: "))

imc = peso / (altura * altura)

if imc <= 18.9:
    print("Abaixo do peso")
elif imc >= 19 and imc <= 24.9:
    print("Peso normal")

elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")

elif imc >= 30 and imc <= 34.9:
    print("Obesidade grau 1")

elif imc >= 35 and imc <= 39.9:
    print("obesidade garu 2")
else:
    print("Obesidade garu 3")

print("o seu IMC atual é de ", imc)
