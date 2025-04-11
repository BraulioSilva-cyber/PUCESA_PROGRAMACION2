# for i in range(5):
#     print(i)

# for i in range(1,11): #llega hasta el 10
#     print(i)

# for i in range(1,10+1,2):#llega hasta 10 y salta de dos en dos
#     print(i)

# for i in range(0,5+1):
#     print("tabla del", i)
#     for j in range(0,11):
#         print(i,"*", j, "=", i*j)
#-----------------------------------------------------
# for i in range(0,10,2):
#     print("Emeneses" ,i)

# for i in [2,4,8]:
#     print("el valor de",i, "y su valor cuadrado es " ,i**2)

# for i in ["Edison", 20, "Ecuador", True]:
#     print("El valor de i es ",i)
#-----------------------------------------------------------
# for i in [1,2,3,4,5]:
#     print("tabla del", i)
#     for j in[1,2,3,4,5]:
#         print(i,"*",j,"=",i*j)
#------------------------------------------------------------
# resto=5%2
# print("El resto de 5 entre 2 es ", resto)
# if resto==0:
#     print("El numero es par")
# else:
#     print("El numero es impar")
for i in range(0,11):
    resto= i%2
    if resto ==0:
        print(i, "Es par")
    else:
        print(i, "Es impar")
#-------------------------------------------------------------
for i in range (0,11):
    if i%2==0:
        print(i, "Es par ")

for i in range(1,11):
    if i%2!=0:
        print(i, "Es impar")