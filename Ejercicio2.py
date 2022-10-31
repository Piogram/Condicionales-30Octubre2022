devolver = int(input("Ingrese el valor a devolver: ")) # 25
cant10 = int(input("Ingrese los billetes de $10 disponibles: ")) #1
cant5 = int(input("Ingrese los billetes de $5 disponibles: ")) #2
cant1 = int(input("Ingrese los billetes de $1 disponibles: ")) #3

dev10 = devolver // 10  #2 
if dev10 <= cant10:
    devolver = devolver % 10 
else:
    dev10 = cant10
    devolver = devolver - (cant10*10)
    
print('dev10: ', dev10) #1
print('devolver: ', devolver) #15

dev5 = devolver // 5 # 3
if dev5 <= cant5:
    devolver = devolver % 5 
else:
    dev5 = cant5 #2
    devolver = devolver - (cant5*5) # 5

print('dev5: ', dev5) #2
print('devolver: ', devolver) #5

dev1 = devolver // 1
if dev1 <= cant1:
    devolver = devolver % 1
else:
    dev1 = cant1
    devolver = devolver - (cant1*1)

print('dev1: ', dev1) #2
print('devolver: ', devolver) #5

if devolver > 0:
    print("No se puede dar vuelto")
else:
    print("Se entregó {} billetes de $10, {} billetes de $5 y {} billetes de $1".format(dev10,dev5,dev1))
    
    
    




    
    
    
    



