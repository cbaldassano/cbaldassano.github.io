def GameOver(gamestate):
    if (gamestate[0] == 'X' and gamestate[3] == 'X' and gamestate[6] == 'X') or \
       (gamestate[1] == 'X' and gamestate[4] == 'X' and gamestate[7] == 'X') or \
       (gamestate[2] == 'X' and gamestate[5] == 'X' and gamestate[8] == 'X') or \
       (gamestate[0] == 'X' and gamestate[1] == 'X' and gamestate[2] == 'X') or \
       (gamestate[3] == 'X' and gamestate[4] == 'X' and gamestate[5] == 'X') or \
       (gamestate[6] == 'X' and gamestate[7] == 'X' and gamestate[8] == 'X') or \
       (gamestate[0] == 'X' and gamestate[4] == 'X' and gamestate[8] == 'X') or \
       (gamestate[2] == 'X' and gamestate[4] == 'X' and gamestate[6] == 'X'):
        return 1
    if (gamestate[0] == 'O' and gamestate[3] == 'O' and gamestate[6] == 'O') or \
       (gamestate[1] == 'O' and gamestate[4] == 'O' and gamestate[7] == 'O') or \
       (gamestate[2] == 'O' and gamestate[5] == 'O' and gamestate[8] == 'O') or \
       (gamestate[0] == 'O' and gamestate[1] == 'O' and gamestate[2] == 'O') or \
       (gamestate[3] == 'O' and gamestate[4] == 'O' and gamestate[5] == 'O') or \
       (gamestate[6] == 'O' and gamestate[7] == 'O' and gamestate[8] == 'O') or \
       (gamestate[0] == 'O' and gamestate[4] == 'O' and gamestate[8] == 'O') or \
       (gamestate[2] == 'O' and gamestate[4] == 'O' and gamestate[6] == 'O'):
        return -1

    if (gamestate.count('-') == 0):
        return 0
    else:
        return 'NotOver'

def StateValue(gamestate, movenumber):
    if GameOver(gamestate) != 'NotOver':
        return (GameOver(gamestate),-1)

    if movenumber % 2 == 0:
        bestval = -2
        for i in range(len(gamestate)):
            if gamestate[i] == '-':
                nextstate = list(gamestate)
                nextstate[i] = 'X'
                gameval = StateValue(''.join(nextstate), movenumber+1)[0]
                if gameval > bestval:
                    bestval = gameval
                    bestmove = i
    else:
        bestval = 2
        for i in range(len(gamestate)):
            if gamestate[i] == '-':
                nextstate = list(gamestate)
                nextstate[i] = 'O'
                gameval = StateValue(''.join(nextstate), movenumber+1)[0]

                if (movenumber == 1):
                    print(nextstate, gameval)
                if gameval < bestval:
                    bestval = gameval
                    bestmove = i

    return (bestval, bestmove)


print(StateValue('----X----',1))
