palavra_certa = ['C','H','A','V','E']
nova_palavra = ['X','X','X','X','X']
tentativas = 1

print('=-=-=-=-=-=-=-=-SEJA BEM-VINDO AO JOGO DE ADVINHAÇÃO=-=-=-=-=-=-=-=-\n')
print(f'VOCÊ PRECISA ACERTAR {len(palavra_certa)} PALAVRAS')

while True:
    chutes = input('Digite uma letra: ').upper().strip()

    if len(chutes) != 1:
        print('Ops!! Você só pode digitar uma letra de cada vez.')
        continue

    if chutes.isdigit():
        print('Eiita!! Não pode digitar números.')
        continue

    # if chutes.isspace():
    #     print('Eiita!! Cuidado, você só digitou espaço em branco')
    #     continue

    for index, i in enumerate(palavra_certa):
        # index = palavra_certa.index(i)
        if chutes == i:
            nova_palavra.pop(index)
            nova_palavra.insert(index, chutes)
            print('Ebaaa!! Você acerrtou.')
            print(nova_palavra)

    if nova_palavra == palavra_certa:
        print('Parabéns!! Você ganhou.')
        break

    print('Nossa! Você errou a palavra, tente de novo.')