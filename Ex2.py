def soma_imposto(taxa_imposto,custo):
    return (1 + taxa_imposto/100)*custo

t = float(input("Digite a taxa de imposto do produto: "))
c = float(input("Digite o custo do produto: "))
print("Valor do produto com o imposto: ",soma_imposto(t,c))
