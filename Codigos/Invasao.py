def detectar_invasao(registros):
    
    usuario_atual = None
    tentativas_consecutivas = 0
    invasor_detectado = None
    
    invasor_detectado = 'Nenhum invasor detectado'
    
    for registro in registros:

        usuario, status = registro.split(":")
        
        if usuario_atual != usuario:
            usuario_atual = usuario
            
        tentativas_consecutivas = (tentativas_consecutivas+1) * (status == "falha")
    
        if tentativas_consecutivas > 3: 
            invasor_detectado = usuario
    
    return invasor_detectado

def main():
    
    registros = [registro for registro in input().split(",")]

    print( detectar_invasao(registros) )

if __name__ == "__main__":
    main()    