import os


class ListaDeCompras:
    def __init__(self):
        self.lista = []

    def inserir_item(self):
        item = input('Digite o item que deseja listar: ')
        self.lista.append(item)
        print('Item adicionado com sucesso!')

    def apagar_item(self):
        while True:
            resp_apagar = input('Digite o índice: ')
            try:
                resp_apagar = int(resp_apagar)
                break
            except ValueError:
                print('Digite um valor válido. Digite novamente')
                continue
        if len(self.lista) >= resp_apagar >= 0 and self.lista:
            item_removido = self.lista.pop(resp_apagar)
            print(f'{item_removido} removido com sucesso!')
        else:
            print('Índice inexistente.')

    def listar_itens(self):
        if self.lista:
            for indice, nome in enumerate(self.lista):
                print(indice, nome)
        else:
            print('Lista vazia. Adicione itens para acionar esta função.')


lista_de_compras = ListaDeCompras()

while True:

    print('Selecione uma opção:')
    resp = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()
    if (len(resp) != 1 or not resp.isalpha()) and resp not in ['i', 'a', 'l', 's']:
        print('Resposta incorreta. Digite novamente')
        continue
    elif resp == 'i':
        os.system('cls' if os.name == 'nt' else 'clear')
        lista_de_compras.inserir_item()
        continue
    elif resp == 'a':
        os.system('cls' if os.name == 'nt' else 'clear')
        lista_de_compras.apagar_item()
    elif resp == 'l':
        os.system('cls' if os.name == 'nt' else 'clear')
        lista_de_compras.listar_itens()
    elif resp == "s":
        break
    else:
        print('Por favor, selecione uma das opções.')
        continue
