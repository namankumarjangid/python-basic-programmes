guess_count=0
secret_number=7
guess_limit=3
while guess_count<guess_limit:
    guess=int(input('Guess number:'))
    guess_count +=1
    if guess==secret_number:
        print('you won the prize')
        break
else:
    print('sorry try again!')