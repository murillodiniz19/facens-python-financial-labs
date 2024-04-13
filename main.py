class Initialize():
    def __init__(self):
        self.__transaction = []
    
    def show_menu(menu):
        print(50 * '-')
        print('Bem vindo ao Controle Financeiro')
        print(50 * '-')

        print('1 - Adicionar transação')
        print('2 - Visualizar transações')
        print('3 - Sair')

    def choose_options(self):
        option = input('\nEscolha uma das opções: ')

        if option != '1' and option != '2' and option != '3':
            print('\nOpção Invalida')
        
        return option
    
    def to_add(self):
        operation = input('\nInforme o tipo de operação: ')
        value = input('\nInforme o valor: ')
        description = input('\nInforme a descrição: ')

        self.__transaction.append(
            (operation, value, description)
        )
    
    def to_view(self):
        for transaction in  self.__transaction:
            print(f'Operation: {transaction[0]} - Value: {transaction[1]} - description : {transaction[2]}')

    def to_go_out(self):
        print('\nObrigado, volte sempre')

if __name__ == '__main__':
    init = Initialize()
    option = ''

    while True:
        init.show_menu()
        option = init.choose_options()

        if option == '1':
            init.to_add()
        elif option == '2':
            init.to_view()
        else:
            init.to_go_out()
            break