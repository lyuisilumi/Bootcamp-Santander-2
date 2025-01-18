def verificar_phishing(mensagem):

    palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click",  "promoção"]
    palavras_confirmacao = ['Seguro','Phishing']
   
    for palavra in mensagem:
       
        palavra = ''.join(letra for letra in palavra if letra.isalnum()).lower() # remover caracteres especiais
       
        if palavra in palavras_suspeitas: # letras minúsculas
            
            analise = palavras_confirmacao[1]
            
            break
        
        else: analise = palavras_confirmacao[0] 
    
    return analise
        
email_usuario = input().split() # Definir uma lista de palavras

print('Classificação:', verificar_phishing(email_usuario) )