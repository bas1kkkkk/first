from random import randint

nameuser = str(input( 'Введите своё имя : '))

print( 'Здравствуйте {0}'.format(nameuser) + ' вы гей на ' + str(randint(0,100)) + '%')