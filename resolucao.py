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