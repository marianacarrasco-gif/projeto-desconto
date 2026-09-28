# Solicita o dado de entrada (valor total da compra) ao usuário e converte para decimal
valor_total = float(input("Digite o valor total da compra: "))
#Aplicação de Condicional
#Se valor total for > 200, calcular desconto de 5% e retorna desconto e valor total a pagar ao usuário
if valor_total < 200:
    desconto1 = valor_total * 0.05 # Calcula 5% sobre o valor total
    valor1 = valor_total - desconto1 # Subtrai o desconto para achar o valor final a pagar
    print(f"Você recebeu R$ {desconto1:.2f} de desconto") #Exibe o valor do desconto formatado. O 2.f determina duas casas decimais.
    print(f"Total a pagar: R$ {valor1:.2f}") #Exibe o valor final a pagar. O 2.f determina duas casas decimais.
 #Se valor total for >= 300, calcular desconto de 15% e retornar desconto e valor total a pagar ao usuário
elif valor_total >= 300:
    desconto3 = valor_total*0.15 # Calcula 15% sobre o valor total
    valor3 = valor_total - desconto3 # Subtrai o desconto para achar o valor final a pagar
    print(f"Você recebeu R$ {desconto3:.2f} de desconto") #Exibe o valor do desconto formatado. O 2.f determina duas casas decimais.
    print(f"Total a pagar: R$ {valor3:.2f}") #Exibe o valor final a pagar. O 2.f determina duas casas decimais.
# Senão,(200 = valor_total < 300), calcular desconto de 15% e retornar desconto e valor total a pagar ao u
else:
    desconto2 = valor_total*0.10 #calcula 10% sobre o valor total
    valor2 = valor_total - desconto2 #Calcula 10% sobre o valor total
    print(f"Você recebeu R$ {desconto2:.2f} de desconto") #Exibe o valor do desconto formatado. O 2.f determina duas casas decimais.
    print(f"Total a pagar: R$ {valor2:.2f}") #Exibe o valor final a pagar. O 2.f determina duas casas decimais.