def segundos_a_horas(segundos):
    return (segundos / 3600)

def horas_a_segundos(horas):
    return (horas * 3600)

if __name__ == "__main__":
    segundos = 678
    horas = segundos_a_horas(segundos)
    print(f"{celsius} grados celsius equivalen a {fahrenheit} grados, tontin")

    fahrenheit = 50
    celsius = fahrenheit_a_celsius(fahrenheit)
    print(f"{fahrenheit} grados celsius equivalen a {celsius} grados, tontin")