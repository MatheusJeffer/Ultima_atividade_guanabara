def len_cadastro():
    try:
        arquivo = open('Pessoas_cadastradas.txt', 'r')
        conteudo = arquivo.read()
        print(conteudo)
        arquivo.close()        

    except:
        print('não foi possivel ler o arquivo.')
        