AGENDA = {}

AGENDA['Bruno'] = {
    'telefone': '11959552414',
    'email': 'devpythonbruno@gmail.com',
    'endereco': 'Avenida Mogiana',
}

AGENDA['Andre'] = {
    'telefone': '11962076476',
    'email': 'bdasilvacosta@gmail.com',
    'endereco': 'Rua Paulo de Proença',
}


def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)
        print('--------------------')


def buscar_contato(contato):
    print(f'Nome: {contato}')
    print(f'Telefone: {AGENDA[contato]["telefone"]}')
    print(f'email: {AGENDA[contato]["email"]}')
    print(f'Endereço: {AGENDA[contato]["endereco"]}')
    print('--------------------')


def incluir_editar_contato(nome, telefone, email, endereco):
    AGENDA[nome] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print(f'>>>>Contato {nome} adicionado/editado com sucesso\n')


def excluir_contato(contato):
    AGENDA.pop(contato)
    print(f'>>>>Contato {contato} excluido com sucesso')


def imprimir_menu():
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('0 - Fechar o programa')


if __name__ == '__main__':
    while True:
        imprimir_menu()
        print('--------------------')
        opcao = input('Escolha uma opção: ')
        print('--------------------')
        if opcao == '1':
            mostrar_contatos()
        elif opcao == '2':
            contato = input('Digite o nome do contato: ')
            print('--------------------')
            buscar_contato(contato)
        elif opcao == '3' or opcao == '4':
            contato = input('Digite o nome do contato: ')
            telefone = input('Digite o telefone: ')
            email = input('Digite o email: ')
            endereco = input('Digite o endereço: ')
            incluir_editar_contato(contato, telefone, email, endereco)
        elif opcao == '5':
            contato = input('Digite o nome do contato: ')
            excluir_contato(contato)
        elif opcao == '0':
            print('Fechando o programa')
            break
        else:
            print('Opção inválida')

