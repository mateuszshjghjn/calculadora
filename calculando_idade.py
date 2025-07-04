#calculando a idade de uma pessoa 
print("******Qual a sua idade?******")
from datetime import datetime

# Função para calcular a idade
def calcular_idade(data_nascimento):
    hoje = datetime.today()
    idade = hoje.year - data_nascimento.year
    
    # Verificar se o aniversário já passou no ano atual
    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    
    return idade

# Entrada de dados
ano = int(input("Digite o ano de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
dia = int(input("Digite o dia de nascimento: "))

# Criando um objeto datetime com a data de nascimento
data_nascimento = datetime(ano, mes, dia)

# Calculando a idade
idade = calcular_idade(data_nascimento)

# Exibindo a idade
print(f"Sua idade é: {idade} anos")
 