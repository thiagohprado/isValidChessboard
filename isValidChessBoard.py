def isValidChessBoard(dict):
    bcount = 0
    wcount = 0
    bpawncount=0
    wpawncount=0
    colors=['b', 'w']
    pieces=['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    allpieces=[]
    letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    allspaces=[]

    #Monta todas as peças válidas possíveis
    for color in colors:
        for p in pieces:
            allpieces.append(color + p)

    #Monta todos os espaços válidos possíveis
    for n in range(1,9):
        for l in letras:
            allspaces.append(str(n) + l)

    #Verifica se possui ao menos um rei de cada cor
    if 'bking' and 'wking' in dict.values():
        for i in dict.values():
            tmp=str(i)
            if tmp[0] == colors[0]:
                bcount=bcount+1
                if tmp == 'bpawn':
                    bpawncount+=1
            elif tmp[0] == colors[1]:
                wcount=wcount+1 
                if tmp == 'wpawn':
                    wpawncount+=1
            else:
                print('Erro, alguma peça não inicia com a letra w ou b')
                return False
            
            #verifica se alguma peça não é válida
            if tmp not in allpieces:
                print('Erro, alguma peça não é válida.')
                return False

        #verifica a quantidade de peças brancas, pretas e peões.    
        if bcount <= 16 and bpawncount <= 8 and wcount <=16 and wpawncount <=8:
            #Verifica se os espaços são válidos
            for k in dict.keys():
                if k not in allspaces:
                    print('Erro - Espaço inválido.')
                    return False
            print('Chessboard validado com sucesso.')
            print('Possui ' + str(wcount) + ' peças brancas.')
            print('Possui ' + str(bcount) + ' peças pretas.')
            return True
        else:
            print('Erro - A quantidade de peças não é válida.')
    else:
        print('Erro - Não tem pelo menos um rei válido de cada cor.')
        return False
        
           

board={'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

print(isValidChessBoard(board))