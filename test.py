import random
deg = '*****'
end = '_____'
print(deg * 5)
print('welcome to guessing the number ')
print(deg *5)


run = True
first = True
while run:
    num = random.randint(0,20)
    if first :
        cho = 'y'
        first = False
    else :
        cho = input("do you what to continue ? (y/n): ")
    if cho == 'y':
        while True:
            ch = int(input("guess the number: "))
            if ch > num:
                print("the number is too big")
            elif ch < num :
                print("the number is too small")
            elif ch == num:
                print(end*10)
                print("****  congratulation you have guessed to correct number  ****")
                print(end*10)
                break
    elif cho == 'n':
        print('thank you for playing..')
        break
    else:
        print('invalid input')