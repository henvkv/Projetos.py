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

def listagem(lista):
    print(f'\n{'No.':<5}{'Nome':<20}{'Idade':<10}{'Série':<10}')
    for a in range(0, len(lista)):
        print(f'''{a+1:<5}{lista[a]['nome']:<20}{lista[a]['idade']:<10}{lista[a]['serie']:<10}''')
    sleep(0.50)

def verificar_alunos(lista):
    if len(lista) == 0:
        print('Nenhum aluno cadastrado! Digite outra opção.')
        sleep(0.25)
        return False
    else:
        return True
    
def editar_lista(txt, lista):
    editar_variavel = int(input(f'\nEscolha o aluno para editar {txt} (1 a {len(lista)}): '))
    editar_variavel = validar_intervalo(editar_variavel, len(lista), 1, 'Digito incorreto. Digite novamente: ')

    if txt == 'idade':
        variavel_troca = int(input(f'''Qual a {txt} você deseja colocar no {lista[editar_variavel-1]['nome']}?
\nDigite aqui: '''))
        if variavel_troca < 15:
            print('Impossível editar. Idade abaixo do ensino médio!')
        
        elif variavel_troca > 18:
            print('O aluno deve se matricular na Educação de Jovens e Adultos (EJA).')
        
        else: 
            if txt == 'serie':
                variavel_troca = int(input(f'''Qual a {txt} você deseja colocar no {lista[editar_variavel-1]['nome']}?
\nDigite aqui: '''))
                variavel_troca = validar_intervalo(variavel_troca, 3, 1, 'Série inválida. Digite novamente: ')

            else:
                variavel_troca = str(input(f'''Qual {txt} você deseja colocar no {lista[editar_variavel-1]['nome']}?
            \nDigite aqui: ''')).upper()
            
            match txt:
                case 'idade': print(f'O {lista[editar_variavel-1]['nome']} agora tem {variavel_troca} anos de idade!')
                case 'nome': print(f'O {lista[editar_variavel-1]['nome']} foi alterado para {variavel_troca}!')
                case 'serie': print(f'O {lista[editar_variavel-1]['nome']} agora está na {variavel_troca}º Série!')

            lista[editar_variavel-1][txt] = variavel_troca