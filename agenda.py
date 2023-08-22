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


mostrar_contatos()
incluir_editar_contato('Sandra','11965102064','sandra.pcosta@gmail.com','Teodoro Bernardo do Nascimento')
mostrar_contatos()
excluir_contato('Bruno')
mostrar_contatos()