from Cliente import Cliente
from functions import crearMapa, clear, vampiro

def ventaTickets(data):
    clear()
    print('******************************')
    print('        VENDER TICKETS')
    print('******************************\n')
    #añadir cliente
    nombre = input('-->Nombre: ')
    ci = input('-->Cédula: ')
    edad = input('-->Edad: ')
    clear()

    asientos = []
    monto = 0

    for evento in data:
        evento.info()

    eleccion = input('Escoja un evento\n===>Nombre de evento: ')

    asientos_cantidad = int(input('-->Cantidad de asientos a comprar: '))
    clear()
    for evento in data:
        if evento.nombre.lower() == eleccion.lower():
            clear()
            crearMapa(evento.mapa, evento.sillasOcupadas)
            print('Escoja 1 por 1 los asientos: ')

            i = 1

            while i <= asientos_cantidad:
                silla = input(f'{i}-->').upper()
                if silla in evento.sillasOcupadas or silla not in evento.mapa or silla == '-':
                    print('Asiento no válido')
                    continue
                else:
                    asientos.append(silla)
                    monto += evento.precios[silla[0]]
                    i += 1
            
            descuento = 0
            iva = monto * 0.16
            if vampiro(ci):
                descuento += (monto * 0.5)
    
            total = monto + iva - descuento

            print(f"-Subtotal: {monto}$")
            print(f"-Descuento: {descuento}$")
            print(f"-IVA: {iva}$")
            print(f"\n-Total: {total}")

            comprar = input('Desea continuar con la compra?\n-->Si (1)\n-->no (2)\n===>Opción: ')

            if comprar == "1":
                for i in asientos:
                    evento.sillasOcupadas.append(i)
                    evento.ingresoGenerado += total
                return Cliente(nombre, ci, edad, evento.nombre, asientos, total)
            input()
            break