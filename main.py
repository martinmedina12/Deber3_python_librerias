import qrcode as pd
def menu():
    print("==== GENERADOR DE QR ====")
    print("1. Crear QR de texto")
    print("2. Crear QR de enlace")
    print("3. Salir")
opcion=""
while opcion !=3:
    menu()
    opcion=int(input("Ingrese una opcion:"))
    if opcion==1:
        texto=input("Ingrese el texto:")
        img=pd.make(texto)
        img.save("qr_texto.png")
        print("QR guardado como qr_texto.png")
    elif opcion==2:
        link=input("Ingrese el enlace:")
        img=pd.make(link)
        img.save("qr_link.png")
        print("QR guardado como qr_link.png")
    elif opcion==3:
        print("Fin del programa")
    else:
        print("Ingrese una opción válida")