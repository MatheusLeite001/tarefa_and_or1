idade = int(input("Digite sua idade: "))
categoria = input("Digite sua categoria (estudante, aposentado, etc.): ")
dia_semana = input("Digite o dia da semana (segunda, terça, etc.): ")

desconto = 0

if idade >= 60:
    desconto = 0.3
elif categoria == "estudante" and (dia_semana == "segunda" or dia_semana == "terça"):
    desconto = 0.2
elif categoria == "aposentado":
    desconto = 0.15
elif categoria == "professor" and dia_semana == "quarta":
    desconto = 0.25

if desconto > 0:
    print("Você tem direito a um desconto de {:.0%}.".format(desconto))
else:
    print("Você não tem direito a nenhum desconto.")
