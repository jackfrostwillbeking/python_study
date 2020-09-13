for I in range(1,51):
    count = 0
    if I % 3 == 0:
        print('Fizz',end='')
        count += 1
    if I % 5 == 0:
        print('Buzz',end='')
        count += 1
    if count == 0:
        print(I,end='')
    print('',end=' ')