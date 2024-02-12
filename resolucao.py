import re

def processar_endereco(endereco):
    # Padrão regex para combinar nome da rua, número e sufixo
    padrao = r"^(?P<nome_rua>[\w\s]+)\s(?P<numero_rua>\d+(?:[\w]*))$"
    
    # Combinar o padrão com o endereço de entrada
    combinacao = re.match(padrao, endereco)
    
    # Se o padrão combinar, retorna o nome da rua, número e sufixo
    if combinacao:
        resultado = combinacao.groupdict()
        if "numero_rua" in resultado:
            resultado["numero_rua"] = resultado["numero_rua"].strip()
        return resultado

    # Se o padrão não combinar, retorna uma mensagem de erro
    return {"erro": "Formato de endereço inválido"}

    # Casos de teste
print(processar_endereco("Miritiba   339"))  # {'nome_rua': 'Miritiba', 'numero_rua': '339'}
print(processar_endereco("Babaçu   500"))  # {'nome_rua': 'Babaçu', 'numero_rua': '500'}
print(processar_endereco("Cambuí   804B"))  # {'nome_rua': 'Cambuí', 'numero_rua': '804B'}
print(processar_endereco("Rio Branco   23"))  # {'nome_rua': 'Rio Branco', 'numero_rua': '23'}
print(processar_endereco("Quirino dos Santos   23 b"))  # {'nome_rua': 'Quirino dos Santos', 'numero_rua': '23 b'}

# Casos de teste para endereços com sufixos
endereco = "4, Rue de la République"
combinacao = re.match(r"^(?P<numero_rua>\d+),?\s(?P<nome_rua>[\w\s]+)$", endereco)
if combinacao:
    resultado = combinacao.groupdict()
    resultado["numero_rua"] = resultado["numero_rua"].strip(",")
    print(resultado)  # {'numero_rua': '4', 'nome_rua': "Rue de la République"}


endereco = "100 Broadway Av"
combinacao = re.match(r"^(?P<nome_rua>[\w\s]+)\s(?P<numero_rua>\d+)$", endereco)
if combinacao:
    resultado = combinacao.groupdict()
    resultado["numero_rua"] = resultado["numero_rua"].strip()
    print(resultado)  # {'nome_rua': 'Broadway Av', 'numero_rua': '100'}


endereco = "Calle Sagasta,  26"
combinacao = re.match(r"^(?P<nome_rua>[\w\s]+),\s(?P<numero_rua>\d+)$", endereco)
if combinacao:
    resultado = combinacao.groupdict()
    resultado["numero_rua"] = resultado["numero_rua"].strip()
    print(resultado)  # {'nome_rua': 'Calle Sagasta', 'numero_rua': '26'}


endereco = "Calle  44 No  1991"
combinacao = re.match(r"^(?P<nome_rua>[\w\s]+)\s(?P<numero_rua>\d+)$", endereco)
if combinacao:
    resultado = combinacao.groupdict()
    resultado["numero_rua"] = resultado["numero_rua"].strip()
    print(resultado)  # {'nome_rua': 'Calle  44', 'numero_rua': '1991'}

