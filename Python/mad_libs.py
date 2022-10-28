from random import randint
import copy


#welcome and play
playing = input("Hello, want to build a story with me? ")
if playing.lower() == "yes":
    print("Yay, lets go!")
else:
    print("okay, bye!")
    quit()
    

#input
adjective1 = input("Please enter an adjective: ")
noun1 = input("Please enter a noun: ")
plural_noun1 = input("Please enter a plural noun: ")
noun2 = input("Please enter a noun: ")
noun3 = input("Please enter a noun: ")
body1 = input("Please enter a body part: ")
adjective2 = input("Please enter a adjective: ")
plural_noun2 = input("Please enter a plural noun: ")

#story
story_1 = (
    "The Force is a mystical " + adjective1 + " power." '\n'
    "The Force is what gives a " + noun1 + " his(her) power" '\n'
    "It's an energy field created by all living " + plural_noun1 + ". It surrounds us and it penetrates us." '\n'
    "It binds the " + noun2 + " together." '\n'
    "Using the Force, a Jedi can do many " + noun3 + " things, like" '\n'
    "using the Force to exercise " + body1 + " control over " + adjective2 + "-minded" '\n'
    + plural_noun2 + "."
)

print(story_1)