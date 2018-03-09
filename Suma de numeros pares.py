#Programa que suma los 20 primeros numeros naturales pares
#Se define la variable en la cual se almacenaran los valores de la suma 
s=0
#Se define la variable c, la cual tomara valores de uno en uno hasta 20
c=1
#mientras "c" no sea mayor que 20 
while c<=20:
#se considerara "c" cuando sea par para sumarse
    while c%2==0:

        s=s+c

        c+=1
#si "c" no es par, no se sumara y "c" tomara el siguiente valor
    c+=1    
#Cuando "c" sea igual a 20, el proceso se detiene y se imprime "s"
print(s)
