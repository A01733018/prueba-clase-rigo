print("Hola a todos, este es un repositorio local y se desplegara en Github")

print("Este archivo se estará modificando")

for i in range(10):
    print(int)

def suma(a,b):
    return a+b


print("La suma de los numerso es: ", suma(89,52))

def suma(a, b, c):
    print(a + b + c)
    suma()

def generar_datos_ventas():
    dias= ['Lun', 'Mar', 'Mie', 'Jue', 'Vie']
    ventas = [120, 500, 230, 289, 310]
    return dias, ventas 

def resumen_analitica():
    dias, ventas = generar_datos_ventas()
    total =sum(ventas)
    promedio = total /len(ventas)
    return {
        "días": dias, 
        "ventas": ventas, 
        "total":total,
        "promedio":promedio
    }

datos = resumen_analitica()
print("Total de ventas:", datos["total"])
print("Promedio diario:", datos["promedio"])