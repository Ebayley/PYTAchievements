player = 'player1'
playerHealth = 100
playerStamina = 50
playerMana = 120
playerStrength = 30
playerSpeed = 'slow'
playerMagic = 'light'
weapon = 'wand'
equipment = 'robe'
playerAlignment = True


print('Hello my name is ' + player + ' and these are my statistics:\n' + 
'Health: ' + str(playerHealth) + '\nStamina: ' + str(playerStamina) + '\nMana: ' + str(playerMana) + '\nStrength: ' + str(playerStrength) + '\nSpeed: ' + playerSpeed + '\nAnd this is my magic type: ' + playerMagic + '\nAnd this is what I carry with me: ' + weapon + ' & ' + equipment)

if playerAlignment == True:
    print('And I am aligned with the forces of good')
elif playerAlignment == False:
    print('And I am aligned with the forces of evil')
else:
    print('And I am not aligned with any faction')

print('\nIk heb een integer, string en een boolean')
