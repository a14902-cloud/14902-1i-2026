
#B1
num = int(input("Diz um número: "))

if num >= 0:
    print("positivo")
else:
    print("negativo")
#B2
idade = int(input("Qual é a idade: "))
if idade >= 18:
    print("Maior de idade")
elif idade <=17:
    print("Menor de idade")
#B3
numero = int(input("diz o teu número: "))
if numero % 2 == 0:
    print("par")
else:
    print("impar")

#B4
num1 =int(input("digite o 1 valor:"))
num2 =int(input("digite o 2 valor:"))

if num1 >= num2 :
    print (f"O {num1} é o maior")
else:
    print(f"o {num2} é o maior")

#B5
passe = str (input("qual é o user:"))

password_correta = "python"

print (passe == password_correta )

#I1 

nota =int(input("Qual é a nota:"))

if nota >= 18:
   print("Excelente")

elif nota >= 14 :
   print("Bom")

elif nota >= 10:
   print("Suficiente")

else:
   print("Reprovado")

#I2
    
idade=int(input("Quantos anos tens:"))

if idade < 13:
   print("És criança")

elif idade <= 17:
   print("És jovem")

elif idade <= 64:
   print("És adulto")

elif idade <= 65:
   print("És Sénior")
   

#I3

I3 = int(input("Indique um número: "))


if I3 % 5 == 0 and I3 % 3 == 0:
    print("É múltiplo de de ambos")
elif I3 % 3 == 0:
    print("É múltiplo de 3")
elif I3 % 5 == 0:
    print("É múltiplo de 5")
else:
    print("É não é multiplo de nenhum")

#I4

user = str (input("qual é o user:"))
senha = int(input("qual é a senha:"))

user_correto = "admin"
senha_correta = 1234

print (user == user_correto and senha == senha_correta)

#I5
I5 = int(input("Indique um número: "))
if 10 <= I5 <= 20:
    print ("Esta dentro do intrevalo")
else:
    print ("não esta dentro do intrevalo")

#A1

Saldo=1000
retirar=int(input("quanto quer tirar: "))
Saldo_restante= Saldo - retirar

if Saldo >= retirar:
   print ("autorizado")
else:
  print("saldo insuficiente")

#A2
A1 =int(input("digite o 1 valor:"))
A2 =int(input("digite o 2 valor:"))
A3 =int(input("digite o 3 valor:"))
A4 =int(input("digite o 4 valor:"))

if A1 >= A2 and A1 >= A3 and A1 >= A4:
   print(A1)
elif A2 >= A1 and A2 >= A3 and A2 >= A4:
   print(A2)
   print(A1)
elif A3 >= A1 and A3 >= A2 and A3 >= A4:
   print(A3)
elif A1 == A2 == A3 == A4:
     print("rodos são iguais")
else:
   print(A4)
#A3
peso =int(input("digite o teu peso:"))
altura =float(input("digite a tua altura: "))

IMC = peso / (altura*altura)

if IMC < 18.5:
   print("Baixo peso")
elif  18.5 <= IMC <= 24.9 :
   print("Normal")
elif 25 <= IMC <= 29.9:
    print("Excesso de peso")
else:
   print("Obesidade")
#A4

desconto = 0
pagar =int(input("Quanto pagaste:"))

if pagar >= 100:
   desconto = pagar * 0.1
   valor_final = pagar - desconto
   print(f"O seu desconto é {desconto} e o valor finala pagar é {pagar}")

elif pagar >= 50:
   desconto = pagar * 0.05
   valor_final = pagar - desconto
   print(f"O seu desconto é {desconto} e o valor finala pagar é {pagar}")

else: print("")

#A5
ano = input("Digite um amo:")
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")



