"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
print("\033c")

paises1=("Mexico","Canada","EUA")
paises3=["Mexico","Canada","EUA"]
varios=("Hola",True,33,3.1416)

print(paises1)
print(paises3)

print(varios)
paises3[1]="Brazil"
print(paises3)

for i in paises1:
  print(i)
for i in range(0,len(paises1)):
  print(paises1[i])
i=0
while i<len(paises1):
  print(paises1[i])
  i+=1
print(f"El paise que ignagura la copa del mundo 2026 es: {paises1[0]}")

edades=(23,24,18,20,20,23,24,19,24)
num=int(input("Imgrese un numero").strip())
posicion=edades.index(num)
print(f"El numero {num} se encontro en la posicion {posicion}")

# print(edades)

# cuantos=edades.count(24)
# print(cuantos)

num=int(input("Ingrese un numero").strip())
posiciones={}
posiciones.clear()
for i in range(0,len(edades)):
  # posicion=edades.index(num)
  if edades[i]==num:
    posiciones.add(i)
posiciones=tuple(posiciones)   
for i in posiciones:
  print(f"El numero {num} se encontro en la posicion {i}")