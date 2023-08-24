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
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print()
        print('>>>> Agenda vazia')
        print()


def buscar_contato(contato):
    try:
        print(f'Nome: {contato}')
        print(f'Telefone: {AGENDA[contato]["telefone"]}')
        print(f'email: {AGENDA[contato]["email"]}')
        print(f'Endereço: {AGENDA[contato]["endereco"]}')
        print('----------------------------------------')
    except KeyError:
        print()
        print(f'>>>> Contato {contato} inexistente')
        print()
    except Exception as error:
        print()
        print('>>>> Um erro inesperado ocorreu')
        print(error)
        print()


def incluir_editar_contato(contato):
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    endereco = input('Digite o endereço: ')
    
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print()
    print(f'>>>> Contato {contato} adicionado/editado com sucesso\n')
    print()


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        print()
        print(f'>>>> Contato {contato} excluido com sucesso')
        print()
    except KeyError:
        print()
        print(f'>>>> Contato {contato} inexistente')
        print()
    except Exception as error:
        print()
        print('>>>> Um erro inesperado ocorreu')
        print(error)
        print()


def exportar_contatos():
    try:
        with open('agenda.csv','w',encoding='utf-8') as arquivo:
            arquivo.write('nome,telefone,email,endereco\n')
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato},{telefone},{email},{endereco}\n')
        print('>>>> Agenda exportada com sucesso')
    except:
        print('>>>> Algum erro ocorreu ao exportar contatos')


def imprimir_menu():
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos para CSV')
    print('0 - Fechar o programa')


if __name__ == '__main__':
    while True:
        imprimir_menu()
        print('----------------------------------------')
        opcao = input('Escolha uma opção: ')
        print('----------------------------------------')
        if opcao == '1':
            mostrar_contatos()
        elif opcao == '2':
            contato = input('Digite o nome do contato: ')
            print('----------------------------------------')
            buscar_contato(contato)
        elif opcao == '3':
            contato = input('Digite o nome do contato: ')
            
            try:
                AGENDA[contato]
                print()
                print(f'>>>> Ccontato {contato} já existente')
                print()
            except KeyError:
                incluir_editar_contato(contato)
        elif opcao == '4':
            contato = input('Digite o nome do contato: ')

            try:
                AGENDA[contato]
                print()
                print(f'>>>> Editando contato: {contato}')
                print()
                incluir_editar_contato(contato)
            except KeyError:
                print()
                print('>>>> Contato inexistente')
                print()
        elif opcao == '5':
            contato = input('Digite o nome do contato: ')
            excluir_contato(contato)
        elif opcao == '6':
            exportar_contatos()
        elif opcao == '0':
            print('Fechando o programa')
            break
        else:
            print('Opção inválida')

