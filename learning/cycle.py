# cycles (how many times to repeat and with condition on start)

# how many times to repeat: range using (start, stop, step)

for x in range(5,0,-1):
    print(x)

quit()

# radrange using (start, stop, step)
from random import randrange

while True:
    if (randrange(1, 100000, 1)) == 10:
        break
    print('MATCHING')
print('DONE')

quit()

#while True:
#    if (randrange(10000)) == 50:
#        print('DONE')
#        break
#    else:
#        print('MATCHING')
