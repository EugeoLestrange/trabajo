def gramos_a_toneladas(gramos):
    return (gramos/1000000)

def toneladas_a_gramos(toneladas):
    return (toneladas * 1000000)

if __name__ == "__main__":
    gramos = 1000
    toneladas = gramos_a_toneladas(gramos)
    print(f"{gramos} gramos de pan equivalen a {toneladas} toneladas de pan, tontin")

    toneladas = 4
    gramos = toneladas_a_gramos(toneladas)
    print(f"{toneladas} toneladas de pan equivalen a {gramos} gramos de pan, tontin")
