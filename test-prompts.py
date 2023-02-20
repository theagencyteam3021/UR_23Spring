A1 = 'Lower Left Corner'
A8 = 'Lower Right Corner'
H1 = 'Upper Left Corner'
H8 = 'Upper Right Corner'

startPos = input('Enter Starting Position: ')
endPos = input('Enter Ending Position: ')

print ('{} {}'.format(startPos, eval(endPos)))

import board
print(board.A1)