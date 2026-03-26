# IMPORT
from time import sleep 
from tools import menu, validar_intervalo, listagem, verificar_alunos, editar_lista


# DEFININDO A LISTA/DICIONÁRIOS/VARIAVEL SOMA
dados_de_alunos = dict()
lista_de_alunos = list()
soma = 0


# EXECUTANDO O CÓDIGO
while True:
    print()
    print('-'*30)
    print('SISTEMA DE ALUNOS'.center(30))
    print('-'*30)
    menu('Adicionar aluno', 'Listar alunos', 'Excluir aluno', 'Editar','Gerar boletim', 'Sair')

    escolha = int(input('Escolha a sua opção: '))
    escolha =   validar_intervalo(escolha, 5, 1, 'Digito incorreto. Digite novamente: ')

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
            dados_de_alunos['serie'] = f'{serie}º'

            for n in range(1,4):
                nota = float(input(f'\nDigite a nota do {dados_de_alunos["nome"]} no {n}º Trimestre (Digite 999 se não tiver): '))
                soma += nota
                if nota == 999:
                    print(f'{dados_de_alunos["nome"]} da {dados_de_alunos["serie"]} Série adicionado!')
                    break
            
            dados_de_alunos['media'] = soma/3
            soma = 0

            lista_de_alunos.append(dados_de_alunos.copy())
            dados_de_alunos.clear()

    elif escolha == 2:
        if  verificar_alunos(lista_de_alunos) == True:
            listagem(lista_de_alunos)
            print(f'Ao total temos {len(lista_de_alunos)} aluno(s).')

    elif escolha == 3:
        if  verificar_alunos(lista_de_alunos) == True:
            listagem(lista_de_alunos)
            excluir_aluno = int(input('\nDigite o número do aluno para excluir: '))
            excluir_aluno = validar_intervalo(excluir_aluno, len(lista_de_alunos), 1, 'Digito incorreto. Digite novamente: ')

            print(f'{lista_de_alunos[excluir_aluno-1]['nome']} foi removido com sucesso!')
            del lista_de_alunos[excluir_aluno-1]

    elif escolha == 4:
        if  verificar_alunos(lista_de_alunos) == True:
            print('\nO que você deseja editar?')
            menu('Nome', 'Idade', 'Série')

            editar = int(input('Digite sua ação: '))
            editar =    validar_intervalo(editar, 3, 1, 'Digito incorreto. Digite novamente: ')

            match editar:
                case 1: listagem(lista_de_alunos),  editar_lista('nome',lista_de_alunos)
                case 2: listagem(lista_de_alunos),  editar_lista('idade',lista_de_alunos)
                case 3: listagem(lista_de_alunos),  editar_lista('serie',lista_de_alunos)

    elif escolha == 5:
        if  verificar_alunos(lista_de_alunos) == True:
            print(f'\n{'No.':<5}{'Nome':<20}{'média':<10}{'Status':<10}')

            for a in range(0, len(lista_de_alunos)):
                if lista_de_alunos[a]['media'] >= 7:
                    status = 'Aprovado'
                    lista_de_alunos[a]['status'] = status
                else:
                    status = 'Reprovado'
                    lista_de_alunos[a]['status'] = status

            for b in range(0, len(lista_de_alunos)):
                print(f'''{b+1:<5}{lista_de_alunos[b]['nome']:<20}{lista_de_alunos[b]['media']:<10}{lista_de_alunos[b]['status']:<10}''')
            sleep(1)


    else:
        if len(lista_de_alunos) == 0:
            print('\n','<'*5,'VOLTE SEMPRE','>'*5)
            break
        else:
            print('\n','<'*5,'DADOS ATUALIZADOS COM SUCESSO!','>'*5)
            break