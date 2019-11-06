#! /usr/bin/env python

from recipe import Recipe
from book import Book


tourte = Recipe(name='tourte a l`epinard', cooking_time=40, cooking_lvl=2, ingredients='patate, carotte', recipe_type='lunch', description='my top 3 recipe')

tiramissu = Recipe(name='tiramissu', cooking_time=30, cooking_lvl=4, ingredients='mascarponne, boudoirs', recipe_type='dessert')

soupe_oignons = Recipe(name='soupe oignons', cooking_time=25, cooking_lvl=1, ingredients='ouignons, h2o', recipe_type='starter')

to_string = str(tourte)
print(to_string)

book = Book(name="mybook", last_update="2012-11-12 22:12", creation_date="2013-01-23 22:12", recipe_list={'starter':soupe_oignons, 'lunch':tourte, 'dessert':tiramissu})

print(str(book.get_recipe_by_name('soupe oignons')))

print(str(book.get_recipe_by_type('dessert')))
