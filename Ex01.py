def area_trapezio(B,b,h):
    media = (B+b)*h/2

    return media

B = float(input("Digite a Base Maior do Trapézio:"))
b = float(input("Digite a Base Menor do Trapézio: "))
h = float(input("Digite a Altura do Trapézio: "))
valor = area_trapezio(B,b,h)
print(valor)