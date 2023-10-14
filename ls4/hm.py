from random import randint

score = 0
for i in range(5):
    action = randint(0, 2)

    match action:
        case 0:
            x, y = randint(1, 1000), randint(1, 1000)
            right_answer = x + y
            answer = input(f'{x} + {y} = ?: ')
        case 1:
            x, y = randint(1, 600), randint(1, 100)
            right_answer = x - y
            answer = input(f'{x} - {y} = ?: ')
        case 2:
            x, y = randint(1, 100), randint(1, 100)
            right_answer = x * y
            answer = input(f'{x} * {y} = ?: ')

    try:
        answer = int(answer)
    except ValueError:
        print("Error data: skip")
        score -= 10
        break

    if answer == right_answer:
        print("correct")
        score += 5
    else:
        score -= 5

if (score > 20):
    print('U win')
else:
    print('U lose')
