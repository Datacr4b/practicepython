
# create all possible board combinations

def isValidchessboard(argument):
    validcolors = ['w','b']
    validpieces = ['pawn','rook','bishop','king','queen','knight']
    chessboard = []
    validboard = []
    count_bpawn=0
    count_wpawn=0
    count_wpieces=0
    count_bpieces=0
    count_king={}

    for y in range(1,9):
        for x in ['a','b','c','d','e','f','g','h']:
            chessboard.append(str(y)+x)

    for vc in validcolors:
        for vp in validpieces:
            validboard.append(vc+vp)

    for k in argument.keys():
        if k not in chessboard:
            print('Spaces error')
            return False
    for v in argument.values():
        if v == 'wpawn':
            count_wpawn+=1
        if v == 'bpawn':
            count_bpawn+=1
        if v.startswith('w'):
            count_wpieces+=1
        if v.startswith('b'):
            count_bpieces+=1
        count_king.setdefault('bking',0)
        count_king.setdefault('wking',0)
        if v in count_king:
            if v == 'wking':
                count_king['wking'] = count_king['wking']+1
            else:
                count_king['bking'] = count_king['bking']+1
        if v not in validboard:
            print('Piece error')
            return False
    if count_bpawn>8:
        print('Black Pawn Count Error')
        return False
    if count_wpawn>8:
        print('White Pawn Count Error')
        return False
    if count_wpieces>16:
        print('White Pieces Count Error')
        return False
    if count_bpieces>16:
        print('White Pieces Count Error')
        return False
    if count_king['wking'] != 1:
        print('White King Count Error')
        return False
    if count_king['bking'] != 1:
        print('Black King Count Error')
        return False
    print('Valid')
    return True

isValidchessboard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '4h': 'wrook'})

