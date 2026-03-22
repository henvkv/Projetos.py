# IMPORT
from time import sleep 

# DEFININDO AS FUNÇÕES
def menu(*txt):
    for e, texto in enumerate(txt):
        print(f'[{e+1}] {texto}')
    
def validar_intervalo(editar_variavel, limite_maximo, limite_minimo, txt):
    while editar_variavel > limite_maximo or editar_variavel < limite_minimo:
        editar_variavel = int(input(txt))
    return editar_variavel

def listagem():
    print(f'\n{'No.':<5}{'Nome':<20}{'Idade':<10}{'Série'}')
    for a in range(0, len(lista_de_alunos)):
        print(f'''{a+1:<5}{lista_de_alunos[a]['nome']:<20}{lista_de_alunos[a]['idade']:<10}{lista_de_alunos[a]['serie']}º''')
    sleep(0.50)

def verificar_alunos():
    if len(lista_de_alunos) == 0:
        print('Nenhum aluno cadastrado! Digite outra opção.')
        sleep(0.25)
        return False
    else:
        return True
    
def editar_lista(txt):
    editar_variavel = int(input(f'\nEscolha o aluno para editar {txt} (1 a {len(lista_de_alunos)}): '))
    editar_variavel = validar_intervalo(editar_variavel, len(lista_de_alunos), 1, 'Digito incorreto. Digite novamente: ')

    if txt == 'idade':
        variavel_troca = int(input(f'''Qual a {txt} você deseja colocar no {lista_de_alunos[editar_variavel-1]['nome']}?
\nDigite aqui: '''))
        if variavel_troca < 15:
            print('Impossível editar. Idade abaixo do ensino médio!')
        
        elif variavel_troca > 18:
            print('O aluno deve se matricular na Educação de Jovens e Adultos (EJA).')
        
        else: 
            if txt == 'serie':
                variavel_troca = int(input(f'''Qual a {txt} você deseja colocar no {lista_de_alunos[editar_variavel-1]['nome']}?
\nDigite aqui: '''))
                variavel_troca = validar_intervalo(variavel_troca, 3, 1, 'Série inválida. Digite novamente: ')

            else:
                variavel_troca = str(input(f'''Qual {txt} você deseja colocar no {lista_de_alunos[editar_variavel-1]['nome']}?
            \nDigite aqui: ''')).upper()
            
            match txt:
                case 'idade': print(f'O {lista_de_alunos[editar_variavel-1]['nome']} agora tem {variavel_troca} anos de idade!')
                case 'nome': print(f'O {lista_de_alunos[editar_variavel-1]['nome']} foi alterado para {variavel_troca}!')
                case 'serie': print(f'O {lista_de_alunos[editar_variavel-1]['nome']} agora está na {variavel_troca}º Série!')

            lista_de_alunos[editar_variavel-1][txt] = variavel_troca

# DEFININDO A LISTA E DICIONÁRIOS
dados_de_alunos = dict()
lista_de_alunos = list()

# EXECUTANDO O CÓDIGO
while True:
    print()
    print('-'*30)
    print('SISTEMA DE ALUNOS'.center(30))
    print('-'*30)
    menu('Adicionar aluno', 'Listar alunos', 'Excluir aluno', 'Editar', 'Sair')

    escolha = int(input('Escolha a sua opção: '))

    escolha = validar_intervalo(escolha, 5, 1, 'Digito incorreto. Digite novamente: ')

    if escolha == 1:
        dados_de_alunos['nome'] = str(input('\nNome: ')).upper()
        
        idade_aluno = int(input('Idade: '))
        if idade_aluno < 15:
            print('Aluno não matriculado. Idade abaixo do ensino médio!')
        
        elif idade_aluno > 18:
            print('O aluno deve se matricular na Educação de Jovens e Adultos (EJA).')

        else:
            dados_de_alunos['idade'] = idade_aluno
            menu('1º Série (MÉDIO)', '2º Série (MÉDIO)', '3º Série (MÉDIO)')         
            
            serie = int(input('Digite sua opção: '))
            
            serie = validar_intervalo(serie, 3, 1, 'Digito incorreto. Digite novamente: ')

            dados_de_alunos['serie'] = serie

            print(f'{dados_de_alunos["nome"]} da {dados_de_alunos["serie"]}º Série adicionado!')

            lista_de_alunos.append(dados_de_alunos.copy())
            dados_de_alunos.clear()

    elif escolha == 2:
        if verificar_alunos() == True:
            listagem()
            print(f'Ao total temos {len(lista_de_alunos)} aluno(s).')

    elif escolha == 3:
        if verificar_alunos() == True:
            listagem()
            excluir_aluno = int(input('\nDigite o número do aluno para excluir: '))
            excluir_aluno = validar_intervalo(excluir_aluno, len(lista_de_alunos), 1, 'Digito incorreto. Digite novamente: ')

            print(f'{lista_de_alunos[excluir_aluno-1]['nome']} foi removido com sucesso!')
            del lista_de_alunos[excluir_aluno-1]

    elif escolha == 4:
        if verificar_alunos() == True:
            print('\nO que você deseja editar?')
            menu('Nome', 'Idade', 'Série')

            editar = int(input('Digite sua ação: '))
            editar = validar_intervalo(editar, 3, 1, 'Digito incorreto. Digite novamente: ')

            match editar:
                case 1: listagem(), editar_lista('nome')
                case 2: listagem(), editar_lista('idade')
                case 3: listagem(), editar_lista('serie')
    
    else:
        if len(lista_de_alunos) == 0:
            print('\n','<'*5,'VOLTE SEMPRE','>'*5)
            break
        else:
            print('\n','<'*5,'DADOS ATUALIZADOS COM SUCESSO!','>'*5)
            break