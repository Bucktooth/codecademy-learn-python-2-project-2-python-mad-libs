"""
This program generates passages that are generated in mad-lib format
Author: Joey 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print "Mad Libs has started!"
name = raw_input("Enter a name: ")
first_adjective = raw_input("Enter an adjective: ")
second_adjective = raw_input("Enter an adjective: ")
third_adjective = raw_input("Enter an adjective: ")
verb = raw_input("Enter a verb: ")
first_noun = raw_input("Enter a noun: ")
second_noun = raw_input("Enter a noun: ")
animal = raw_input("Enter an animal: ")
food = raw_input("Enter a food: ")
fruit = raw_input("Enter a fruit: ")
superhero = raw_input("Enter a superhero: ")
country = raw_input("Enter a country: ")
dessert = raw_input("Enter a dessert: ")
year = raw_input("Enter a year: ")

print STORY % (name, first_adjective, second_adjective, animal, food, verb, first_noun, fruit, third_adjective, name, superhero, name, country, name, dessert, name, year, second_noun)
