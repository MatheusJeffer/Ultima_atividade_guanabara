def options(txt):
   while True: 
         try:
              selection = int(input(f'\033[0.33m{txt}\033[0m'))
         except (ValueError):
              print('\033[0;31mError, digite um número inteiro válido.\033[0m')
         else:
              return selection
