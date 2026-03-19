entrada = input()

def descrever_autenticacao(tipo):
    if tipo == "Senha":
        return "Combinacao secreta usada para acessar sistemas"
    
    # TODO: complete as demais condições
    elif tipo == "MFA":
        return "Uso de dois ou mais fatores de verificacao"
    
    elif tipo == "Biometria":
        return "Identificacao baseada em caracteristicas fisicas"
    
    elif tipo == "Token":
        return "Codigo temporario para validacao de acesso"

print(descrever_autenticacao(entrada))
