import masa 
import temperatura
import tiempo

def convertir_temperatura(valor, unidad, unit_destino):
    if unidad == "celsius" and unit_destino == "fahrenheit":
        return temperatura.celsius_a_fahrenheit(valor)
    

def convertir_masa(valor, unidad, unit_destino):
    if unidad == "gramos" and unit_destino == "toneladas":
        return masa.gramos_a_toneladas(valor)
    

def convertir_tiempo(valor, unidad, unit_destino):
    if unidad == "segundos" and unit_destino == "horas":
        return tiempo.segundos_a_horas(valor)   
    
if __name__ == "__main__":
    valor = float(input("Por favor,ingresa un numero a convertir: "))
    unidad = "celsius"
    unit_destino = "fahrenheit"
    resultado = convertir_temperatura(valor, unidad, unit_destino)
    print(f"{valor} de grados {unidad} son igual a {resultado} {unit_destino}")