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

    #imprime información de todos los eventos
    for evento in data:
        evento.info()

    eleccion = input('Escoja un evento\n===>Nombre de evento: ')

    asientos_cantidad = int(input('-->Cantidad de asientos a comprar: '))

    clear()
    for evento in data:
        #busca el evento escogido por el usuario
        if evento.nombre.lower() == eleccion.lower():
            clear()
            crearMapa(evento.mapa, evento.sillasOcupadas)
            print('Escoja 1 por 1 los asientos: ')

            i = 1
            #el usuario escoge sus asientos aquí
            while i <= asientos_cantidad:
                silla = input(f'{i}-->').upper()
                if silla in evento.sillasOcupadas or silla not in evento.mapa or silla == '-' or silla in asientos:
                    print('Asiento no válido')
                    continue
                else:
                    #si el asiento es válido los agrega a los asientos por comprar y suma el precio al monto
                    asientos.append(silla)
                    monto += evento.precios[silla[0]]
                    i += 1
            
            #calcular descuentos, IVA y monto total
            descuento = 0
            iva = monto * 0.16
            if vampiro(ci, ci[:len(ci)//2], ci[len(ci)//2:], ci[:len(ci)//2], ci[len(ci)//2:]):
                descuento += (monto * 0.5)
    
            total = monto + iva - descuento

            print(f"-Subtotal: {monto}$")
            print(f"-Descuento: {descuento}$")
            print(f"-IVA: {iva}$")
            print(f"\n-Total: {total}")

            comprar = input('Desea continuar con la compra?\n-->Si (1)\n-->no (2)\n===>Opción: ')
            #ocupa silla selccionadas y agrega el cliente a la base de datos
            if comprar == "1":
                for i in asientos:
                    evento.sillasOcupadas.append(i)
                    evento.ingresoGenerado += total
                    
                file = open('clientes.txt', 'a')
                file.write(f'{nombre}|{ci}|{edad}|{evento.nombre}|{total}|0\n')
                lista = ''
                for i in asientos:
                    lista = lista + i + '|'
                file.write(f'{lista}\n')
                file.close()

                evento.ingresoGenerado += total

                return Cliente(nombre, ci, edad, evento.nombre, asientos, total, 0)
            break