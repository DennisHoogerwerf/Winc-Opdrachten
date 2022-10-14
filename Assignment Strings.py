# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

"""Part 1; Assignment: Strings"""

#Who scored in the Euro88 Final
scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'

#In what minute did the goal happen
goal_0 = 32
goal_1 = 54

#Who scored when
scorers = scorer_0 +' ' +str(goal_0) + ', '+ scorer_1 +' ' +str(goal_1)
print(scorers)

#Reporting
report = f"{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute"


"""Part 2; Assignement: Strings"""

#Spelernaam
player = 'Ruud Gullit'
first_name = player[:player.find(' ')]
last_name = player[player.find(' '):]
print(first_name)

last_name_len = len(last_name)
print(last_name_len)

name_short = player[0] +'. ' + last_name


#Chant
cheer = (first_name + '! ')
yell = (first_name + '!')
chant = (cheer * 3 + yell)
good_chant = (chant[-1] != " ")
print(chant)
print(good_chant)
