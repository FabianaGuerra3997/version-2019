from generador import generador,generador_mejor

buscado=generador(1,1000)
nadie_adivino=True
lista_numero=[]
while nadie_adivino:
    print("Ingrese un numero")
    numero=int(input())
    if numero==buscado:
        print("Adivinaste!!!")
        nadie_adivino=False
    if numero<buscado:
        print("Ingresa un numero mas grande") 
    if numero>buscado:
        print("Ingresa un numero mas chico")
    

    if nadie_adivino==True:
        numero2=generador_mejor(1,1000,lista_numero)
        lista_numero.append(numero2)
        print("Juega la computadora")
        print(str(numero))
        if numero2==buscado:
            print("Adivinaste!!!")
            nadie_adivino=False
        if numero2<buscado:
            print("Ingresa un numero mas grande")
        if numero2>buscado:
            print("Ingresa un numero mas chico")
