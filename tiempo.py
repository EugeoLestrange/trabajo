def segundos_a_horas(segundos):
    return (segundos / 3600)

def horas_a_segundos(horas):
    return (horas * 3600)

if __name__ == "__main__":
    segundos = 678
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas} horas, tontin")

    horas = 50
    segundos = horas_a_segundos(horas)
    print(f"{horas} horas equivalen a {segundos} segundos, tontin")