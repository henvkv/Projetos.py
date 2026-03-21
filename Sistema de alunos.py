def menu(*txt):
    for e, texto in enumerate(txt):
        print(f'[{e+1}] {texto}')
    
def loop(variavel, limite_maximo, limite_minimo, txt):
    while variavel > limite_maximo or variavel < limite_minimo:
        variavel = int(input(txt))
    return variavel

def listagem():
    print(f'\n{'No.':<5}{'Nome':<20}{'Idade':<10}{'Série'}')
    for a in range(0, len(lista_de_alunos)):
        print(f'''{a+1:<5}{lista_de_alunos[a]['nome']:<20}{lista_de_alunos[a]['idade']:<10}{lista_de_alunos[a]['serie']}º''')

def verificar_alunos():
    if len(lista_de_alunos) == 0:
        print('Nenhum aluno cadastrado! Digite outra opção.')
        return False
    else:
        return True

dados_de_alunos = dict()
lista_de_alunos = list()
qnt_de_alunos = 0

while True:
    print()
    print('-'*30)
    print('SISTEMA DE ALUNOS'.center(30))
    print('-'*30)
    menu('Adicionar aluno', 'Listar alunos', 'Excluir aluno', 'Editar', 'Sair')

    escolha = int(input('Escolha a sua opção: '))

    escolha = loop(escolha, 5, 1, 'Digito incorreto. Digite novamente: ')

    if escolha == 1:
        dados_de_alunos['nome'] = str(input('\nNome: ')).upper()
        qnt_de_alunos += 1
        
        dados_de_alunos['idade'] = int(input('Idade: '))

        menu('1º Série (MÉDIO)', '2º Série (MÉDIO)', '3º Série (MÉDIO)')         
        
        serie = int(input('Digite sua opção: '))
        
        serie = loop(serie, 3, 1, 'Digito incorreto. Digite novamente: ')

        match serie:
            case 1: dados_de_alunos['serie'] = serie
            case 2: dados_de_alunos['serie'] = serie
            case 3: dados_de_alunos['serie'] = serie

        print(f'{dados_de_alunos["nome"]} da {dados_de_alunos["serie"]}º Série adicionado!')

        lista_de_alunos.append(dados_de_alunos.copy())
        dados_de_alunos.clear()

    elif escolha == 2:
        verificar_alunos()
        
        if verificar_alunos() == True:
            listagem()

    elif escolha == 3:
        verificar_alunos()
        
        if verificar_alunos() == True:
            listagem()
            excluir_aluno = int(input('\nDigite o número do aluno para excluir: '))
            excluir_aluno = loop(excluir_aluno, len(lista_de_alunos), 1, 'Digito incorreto. Digite novamente: ')

            print(f'{lista_de_alunos[excluir_aluno-1]['nome']} foi removido com sucesso!')
            del lista_de_alunos[excluir_aluno-1]

    elif escolha == 4:
        verificar_alunos()

        if verificar_alunos() == True:
            print('\nO que você deseja editar?')
            menu('Nome', 'Idade', 'Série')

            editar = int(input('\nDigite sua ação: '))
            editar = loop(editar, 3, 1, 'Digito incorreto. Digite novamente: ')