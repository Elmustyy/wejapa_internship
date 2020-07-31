#1. number of  tiles are needed
first_part = 9*7
print('tiles needed for the first part:{}'.format(first_part))
second_part = 5*7
print('tiles needed for the second part:{}'.format(second_part))
#2. after buying  17 packages of tiles containing 6 tiles each. below are the number of left over tiles?
total_num_of_tiles = 17*6
num_tiles_left = total_num_of_tiles -(first_part + second_part)

# expression that calculates the amount of tiles needed.
print('total number of tiles needed:{}\t'.format(first_part + second_part))

#expression that calculates how many tiles will be left over.
print('total number of tiles left over:{}'.format(num_tiles_left))