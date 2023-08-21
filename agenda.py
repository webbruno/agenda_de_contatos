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
        print(f'Nome: {contato}')
        print(f'Telefone: {AGENDA[contato]["telefone"]}')
        print(f'email: {AGENDA[contato]["email"]}')
        print(f'Endereço: {AGENDA[contato]["endereco"]}')
        print('--------------------')

mostrar_contatos()