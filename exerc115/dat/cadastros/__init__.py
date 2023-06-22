def cadastro(nome, idade):

   dados = []
   dados1 = []
   dados1.append(nome)
   dados1.append(idade)
   dados.append(dados1[:])
   dados1.clear()
   
   try:
       arquivo = open('Pessoas_cadastradas.txt', 'a+')
       for  pessoas in dados: 
             arquivo.write(f'{pessoas[0]: <20}              {pessoas[1]} anos\n')
       arquivo.close()
   except:
      print('Erro ao cadastrar.')
      