starting_num = 50
current_num  = starting_num
commands     = ""
count        = 0

with open( 'input.txt' ) as f:
    commands = f.readlines()

    for spin in commands:
        if spin[0] == 'L':
            current_num = current_num - int( spin[1:] ) % 100 
        else:
            current_num = current_num + int( spin[1:] ) % 100 

        if current_num > 99:
            current_num = current_num - 100
        elif current_num < 0:
            current_num = 100 + current_num

        if current_num == 0:
            count += 1
        print( current_num )

print( commands )
print( count )
