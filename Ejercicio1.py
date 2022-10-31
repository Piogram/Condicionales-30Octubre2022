lista_dias = ["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]
dia = input("Ingrese el día: ").lower() #lunes
codigo = input("Ingrese el código: ") #"45251"
monto = float(input("Ingrese el monto: ")) # 300
acum_desc = 0
#Descuento 1: Ultimo dígito
num_dia = lista_dias.index(dia) + 1 # 1
num_dia_tarj = int(codigo[-1]) #1
if num_dia == num_dia_tarj:
    print("Descuento 1")
    acum_desc += 5
    
#Descuento 2: Penúltimo dígito
penult_digito = int(codigo[-2]) #5
if monto >300:
    print("Descuento 2")
    acum_desc += penult_digito
    
#Descuento 3: Antepenúltimo dígito 
antpenult_digito = int(codigo[-3])
if 400 < monto <= 500: #monto > 400 and monto <=500
    print("Descuento 3")
    acum_desc += antpenult_digito 
    
#Descuento 4: Compra mayor a 500
if monto > 500:
    print("Descuento 4")
    acum_desc += 10
    
print('acum_desc: ', acum_desc) 
monto_total = monto - (monto * acum_desc/100)
print('El monto con descuentos es: ', monto_total)
    

    
    
    



    






