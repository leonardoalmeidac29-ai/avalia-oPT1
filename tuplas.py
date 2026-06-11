meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
num_mes = int(input("Digite o número do mês (1 a 12): "))
if 1 <= num_mes <= 12:
    print(f"O mês correspondente é: {meses[num_mes - 1]}\n")
else:
    print("Número inválido!\n")
