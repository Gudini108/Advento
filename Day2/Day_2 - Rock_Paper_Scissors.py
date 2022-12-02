f = open('C:/Users/gudin/Desktop/Пограммки/Advento/Day2/input.txt')

rps = f.read()

games_total = rps.split('\n')[1:-1] # getting list of all individual R-P-S contests without empty spaces


elf_hand = {'A':1, 'B':2, 'C':3} # A - rock / B - paper / C - scissors
your_hand = {'X':1, 'Y':2, 'Z':3} # X - rock / Y - paper / Z - scissors


score = 0
for game in range(len(games_total)):
    
    elf = games_total[game][0]
    you = games_total[game][2]
    
    if (
        ((elf == 'A' and you == 'X')) # rock to rock
        or 
        ((elf == 'B' and you == 'Y')) # paper to paper
        or
        ((elf == 'C' and you == 'Z')) # scissors to scissors
        ):
        score += (3 + your_hand[you])
    
    elif (
        ((elf == 'A' and you == 'Z')) # rock to scissors
        or 
        ((elf == 'B' and you == 'X')) # paper to rock
        or
        ((elf == 'C' and you == 'Y')) # scissors to paper
        ):
        score += your_hand[you]
    
    else:
        score += (6 + your_hand[you])


real_score = 0
for game in range(len(games_total)):
    
    elf = games_total[game][0]
    you = games_total[game][2]
    
    if you == 'X':
        if elf == 'A':
            real_score += your_hand['Z']
        elif elf == 'B':
            real_score += your_hand['X']
        else:
            real_score += your_hand['Y']
    elif you == 'Y':
        real_score += 3
        if elf == 'A':
            real_score += your_hand['X']
        elif elf == 'B':
            real_score += your_hand['Y']
        else:
            real_score += your_hand['Z']
    else:
        real_score += 6
        if elf == 'A':
            real_score += your_hand['Y']
        elif elf == 'B':
            real_score += your_hand['Z']
        else:
            real_score += your_hand['X']


print(real_score)