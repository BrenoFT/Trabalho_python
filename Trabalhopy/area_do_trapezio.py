print("-------------Calcule a área do trapézio-------------")

baseMaior = float(input("Digite a base maior: "))
baseMenor = float(input("Digite a base menor: "))
altura = float(input("Digite a altura: "))

def areadoTrapezio():
    area = ((baseMaior + baseMenor) * altura) / 2
    input(f"A área do trapezio é: {area}")

areadoTrapezio()




