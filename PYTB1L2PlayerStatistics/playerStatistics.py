player = 'player1'
playerHealth = 100
playerStamina = 50
playerMana = 120
playerStrength = 30
playerSpeed = 'slow'
playerMagic = 'light'
weapon = 'wand'
equipment = 'robe'
playerAlignment = 0
goodAlignment = 0


print('Hello my name is ' + player + ' and these are my statistics:\n' + 
'Health: ' + str(playerHealth) + '\nStamina: ' + str(playerStamina) + '\nMana: ' + str(playerMana) + '\nStrength: ' + str(playerStrength) + '\nSpeed: ' + playerSpeed + '\n\nAnd this is my magic type: ' + playerMagic + '\nAnd this i what I carry with me: ' + weapon + ', ' + equipment)

if playerAlignment == goodAlignment:
    print('And I am aligned with the forces of good')
elif playerAlignment == 1:
    print('And I am aligned with the forces of evil')
else:
    print('And I am not aligned with any faction')

print('\nIk heb een integer, string en een boolean')