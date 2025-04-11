
# #------------------------------
# 5.select opciones
# 6.Ingresar por teclado 2 numeros verifique que tipo de dato
# 7.Validar que el segundo numero no sea cero
# 8.Realizar la operacion seleccionada
# 9.Mostrar el resultado
# 10.Validar que la opcion seleccionada sea correcta
# 11.Mostrar un mensaje de error si la opcion no es correcta

print(""" Menu de opciones
1.Sumar
2.Restar
3.Multiplicar
4.Dividir
""")

a=int(input("Ingrese un opcion: "))
if a< 0 or a>4:
    print("Ingrese una opcion valida")
    a=int(input("Ingrese un opcion valida: "))

if a==1:
    num1=float(input("Ingrese el primer numero: "))
    num2=float(input("Ingrese el sugundo numero: "))
    suma=num1+num2
    print("El resultado es: ", suma)

if a==2:
    num1=float(input("Ingrese el primer numero: "))
    num2=float(input("Ingrese el sugundo numero: "))
    resta=num1-num2
    print("El resultado es: " ,resta)

if a==3:
    num1=float(input("Ingrese el primer numero: "))
    num2=float(input("Ingrese el sugundo numero: "))
    multi=num1*num2
    print("El resultado es: ", multi)

if a==4:
    num1=float(input("Ingrese el primer numero: "))
    num2=float(input("Ingrese el sugundo numero: "))
    if num2==0:
        print("Error: Division para cero no es posible")
        num2=float(input("Ingrese el segundo numero: "))
        div=num1/num2
    else:
        div=num1/num2
    print("El resultado es: ", div)
