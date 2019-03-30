def addChar(charWeight, jaywalking):
    try: num = int(input('Add a character or press 0 if there are no more characters > '))
    except ValueError:
        print('Invalid entry')
        addChar(charWeight, jaywalking)
    if num:
        try: char = numChar[num]
        except ValueError:
            print('Invalid entry')
            addChar(charWeight, jaywalking)
        weight = charWeight[char]
        if jaywalking == 'Y' and char not in ['Dog', 'Cat']: n += 0.291920196*weight
        else: n += weight
def getWeight(side, charWeight):
    print('Deaths on ' + side + ' side')
    passenger, jaywalking = False, False
    while passenger not in ['Y', 'N']: passenger = input('Passenger? (Y/N) > ').upper()
    if passenger == 'N':
        while jaywalking not in ['Y', 'N']: jaywalking = input('Jaywalking? (Y/N) > ').upper()
    for key, value in numChar.items(): print(key, value)
    num, n = True, 0
    while num:
        try: num = int(input('Add a character or press 0 if there are no more characters > '))
        except ValueError:
            print('Invalid entry')
            continue
        if not num: break
        try: char = numChar[num]
        except KeyError:
            print('Invalid entry')
            continue
        i = charWeight[char]
        if jaywalking == 'Y' and char not in ['Dog', 'Cat']: n += 0.291920196*i
        else: n += i
    if passenger == 'Y': n *= 5.976440283
    return n
def choose(side): print('Continue with ' + side + ' scenario')
charWeight = {'Man': 1, 'Woman': 1, 'Pregnant Woman': 1, 'Baby': 2.255379727, 'Elderly Man': 0.09317147, 'Elderly Woman': 0.09317147, 'Boy': 5.660293394, 'Girl': 5.660293394, 'Homeless Person': 0.561489098, 'Large Woman': 0.106958749, 'Large Man': 0.106958749, 'Criminal': 0.211613543, 'Male Executive': 1.117429247, 'Female Executive': 1.117429247, 'Female Athlete': 50.03391293, 'Male Athlete': 50.03391293, 'Female Doctor': 11.1128903, 'Male Doctor': 11.1128903, 'Dog': 0.432911022, 'Cat': 0.300093252}
numChar, i = dict(), 1
for key in charWeight:
    numChar[i] = key
    i += 1
for j in range(13):
    left, right, swerve = getWeight('left', charWeight), getWeight('right', charWeight), False
    if left < right: choose('left')
    elif left > right: choose('right')
    else:
        while swerve not in ['L', 'R']:
            print('L Left\nR Right')
            swerve = input('In which scenario would the self-driving car swerve? (L/R) > ').upper()
            if swerve == 'L': choose('right')
            elif swerve == 'R': choose('left')
            else: print('Invalid entry')
    print()
