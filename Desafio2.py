entrada = input()

def descrever_pratica(pratica):
    if pratica == "Backup":
        return "Copia de seguranca dos dados"
    
    # TODO: complete as demais práticas
    elif pratica == "Atualizacao":
        return  "Correcao de falhas e melhorias no sistema"
    
    elif pratica == "Firewall":
        return  "Controle de trafego de rede"
    
    elif pratica == "Antivírus":
        return "Deteccao e remocao de softwares maliciosos"

print(descrever_pratica(entrada))
