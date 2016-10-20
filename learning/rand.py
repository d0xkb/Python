from random import randrange
import time

start = time.perf_counter()

while True:
    if (randrange(100000)) == 50:
        break
#    print('MATCHING')
end = time.perf_counter()

t = '{:f}'.format(end-start)

print('DONE IN', t, 'seconds')

#print('DONE IN ', end - start, 'seconds')
#while True:
#    if (randrange(10000)) == 50:
#        print('DONE')
#        break
#    else:
#        print('MATCHING')
