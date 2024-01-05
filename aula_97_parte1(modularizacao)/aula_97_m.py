
if __name__ == '__main__':
    print('Este módulo se chama',__name__)


import sys


caminho = sys.path

print(*caminho, sep='\n')