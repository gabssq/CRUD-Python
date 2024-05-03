def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Gabriel Quadros                                             |')
    print('|                                                             |')
    print('| Versão 1.0 de 30/abril/2024                                 |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt = input(solicitacao)

        if txt not in valido:
            print(mensagem, '- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print ()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio <= final:
        meio = ( inicio + final ) // 2
        
        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final = meio - 1
        else: # nom.upper()>agd[meio][0].upper()
            inicio = meio + 1
                        
    return [False,inicio]

def incluir (agd):
    digitouDireito = False
    while not digitouDireito:
        nome     = input('\nNome.......: ')
        resposta = ondeEsta(nome,agd)
        achou    = resposta[0]
        posicao  = resposta[1]

        if achou:
            print('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito = True
            
    aniversario = input('Aniversário: ')
    endereco    = input('Endereço...: ')
    telefone    = input('Telefone...: ')
    celular     = input('Celular....: ')
    email       = input('e-mail.....: ')
    print('\n')
    
    contato     = [nome,aniversario,endereco,telefone,celular,email]
    
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!\n')
    
def procurar (agd):
    digitouDireito = False
    while not digitouDireito:
        nome     = input('Nome.......: ')            
        resposta = ondeEsta(nome,agd)
        achou    = resposta[0]
        posicao  = resposta[1]
        print(nome.upper)
        if not achou:
            print ('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito = True
            print('\nCONTATO', nome.upper,'ENCONTRADO!')
            print('\nAniversario:',agd[posicao][1])
            print('Endereco...:',agd[posicao][2])
            print('Telefone...:',agd[posicao][3])
            print('Celular....:',agd[posicao][4])
            print('e-mail.....:',agd[posicao][5], '\n')
            
# função para atualizar agenda 
def att(agd,att_usuario,txt,pos):
    nome     = input('Digite o nome de quem deseja atualizar.......: ')
    resposta = ondeEsta(nome,agd)
    achou    = resposta[0]
    posicao  = resposta[1]
    if not achou:
        print ('Pessoa inexistente - Favor redigitar...')
    else:
        att_usuario = input(txt)
        agd[posicao][pos] = att_usuario
        
def atualizar (agd):
    while True:
         submenu=['1. Atualizar nome',\
                 '2. Atualizar aniversário',\
                 '3. Atualizar endereço',\
                 '4. Atualizar telefone',\
                 '5. Atualizar celular',\
                 '6. Atualizar e-mail',\
                 '7. Finalizar atualizações']
         escolha=int(opcaoEscolhida(submenu))  
         att_usuario=0 
         if escolha==1:
             
             att(agd,att_usuario, 'Nome...:', 0)
         if escolha==2: 
             att(agd,att_usuario , 'Aniversario...: ', 1)
         if escolha==3:
             att(agd,att_usuario, 'Endereco...:', 2)
         if escolha==4:
             att(agd,att_usuario, 'Telefone...:', 3)
         if escolha==5:
             att(agd,att_usuario, 'Celular...:', 4)
         if escolha==6:
             att(agd,att_usuario, 'E-mail...:', 5)
         if escolha==7:
             print('Atualizações finalizadas')
             break


def listar(agd):
    if not agd:
        print('Não há contatos cadastrados.')
    else:
        print('\nLISTA DE CONTATOS:')
        #print(agd)
        for c in agd:
            print('Nome:', c[0])
            print('Aniversário:', c[1])
            print('Endereço:', c[2])
            print('telefone:', c[3])
            print('Celular:', c[4])
            print('Email:', c[5], '\n')


def excluir (agd):
    print()
    
    digitouDireito=False
    while not digitouDireito:
        nome        = input('Nome.......: ')        
        resposta    = ondeEsta(nome,agd)
        achou       = resposta[0]
        posicao     = resposta[1]
        
        if not achou:
            print('Pessoa inexistente - Favor redigitar...\n')
        else:
            digitouDireito=True
    
    print('Aniversario:',agd[posicao][1])
    print('Endereco...:',agd[posicao][2])
    print('Telefone...:',agd[posicao][3])
    print('Celular....:',agd[posicao][4])
    print('e-mail.....:',agd[posicao][5])

    resposta    =   umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
    else:
        print('Remoção não realizada!')

apresenteSe()

agenda=[]

menu=['Incluir Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

opcao=69
while opcao != 6:
    opcao = int(opcaoEscolhida(menu))

    if opcao    ==  1:
        incluir(agenda)
    elif opcao  ==  2:
        procurar(agenda)
    elif opcao  ==  3:
        atualizar(agenda)
    elif opcao  ==  4:
        listar(agenda)
    elif opcao  ==  5:
        excluir(agenda)
        
print('OBRIGADO POR USAR ESTE PROGRAMA!')
