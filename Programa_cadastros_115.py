import os

from exerc115.dat import cadastros
from exerc115.dat import ler_cadastros
from exerc115.dat import Cores
from exerc115 import Opcao


select = 1

while select != 4:
   print('\033[0;31m=-\033[0m'*20)
   print('           \033[0;30mMENU DE CADASTRO\033[0m')
   print('\033[0;31m=-\033[0m'*20)

   Cores.amarelo('[1]Ver pessoas cadastradas.')
   Cores.verde('[2]Cadastrar novas pessoas.') 
   Cores.vermelho('[3]Apagar o cadastro.')    
   print('[4]Sair.')
   
   select = Opcao.options('Selecione uma opção: ')
   
   while select > 4 or select < 1:
         print('\033[0;31mError, selecione a opção correta.')
         select = Opcao.options('Selecione uma opção: ')
        

   if select == 1:
       print('~='*20)
       print('         PESSOAS CADASTRADAS:')
       print('~='*20)
       ler_cadastros.len_cadastro()
       print('~='*20)
   
   if select == 2:
       Nome = str(input('Digite o seu nome: '))
       Idade = Opcao.options('Digite a sua idade: ')
       cadastros.cadastro(Nome, Idade)
   
   if select == 3:
       os.remove('Pessoas_cadastradas.txt')
    