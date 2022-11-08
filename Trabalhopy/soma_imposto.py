import string


print("-----------------Soma de imposto-----------------")
print("Para finalizar a operação digite '-1' no campo de imposto !!")

cont_produtos = 0
i = 0
x = 0
taxa_impostos = []
taxa_imposto = 0
custos = []
somas = []
while(x < 10): 
    taxa_imposto = float(input("Quantos porcento será taxado de imposto por venda: "))
    if taxa_imposto == -1:
        break
    taxa_imposto = taxa_imposto / 100 + 1
    
    custo = float(input("Custo do produto: "))
    taxa_impostos.append(taxa_imposto)
    custos.append(custo)
    cont_produtos += 1

print(f"Porcentagens de imposto: {taxa_impostos}")
print(f"Produtos sem imposto: {custos}")

def soma_imposto():
    for i in range(cont_produtos):
        soma = custos[i] * taxa_impostos[i]
        somas.append(soma)
    
    print(f"Produtos com impostos: {somas}")

soma_imposto()


    