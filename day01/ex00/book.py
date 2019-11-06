# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: igarbuz <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 18:03:53 by igarbuz           #+#    #+#              #
#    Updated: 2019/11/04 18:46:22 by igarbuz          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime

class Book:
    def __init__(self, name, last_update, creation_date, recipe_list):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipe_list = recipe_list

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        if not isinstance(v, str): raise Exception('name must be string')
        self._name = v

    @property
    def last_update(self):
        return self._last_update

    @last_update.setter
    def last_update(self, v):
        try:
            date_format = datetime.fromisoformat(v)
        except Exception:
            print("last_update format must be YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]")
        self._last_update = date_format

    @property
    def creation_date(self):
        return self._creation_date

    @creation_date.setter
    def creation_date(self, v):
        try:
            date_format = datetime.fromisoformat(v)
        except Exception:
            print("creation_date format must be YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]")
        self._creation_date = date_format

    @property
    def recipe_list(self):
        return self._recipe_list

    @recipe_list.setter
    def recipe_list(self, v):
        types_list = ['starter', 'lunch', 'dessert']
        if not isinstance(v, dict): raise Exception('recipes_list must be a dictionary')
        for key in v:
            if key not in types_list: raise Exception('recipe type must be in [starter, lunch, dessert]')
        self._recipe_list = v

    def get_recipe_by_name(self, name):
        """print a recipe with the name `name` and return its instance"""
        for key, recipe in self.recipe_list.items():
            if name == recipe.name:
                return recipe

    def get_recipe_by_type(self, _type):
        """print a recipe with the name `name` and return its instance"""
        for key, recipe in self.recipe_list.items():
            if _type == recipe.recipe_type:
                return recipe

    def add_recipe(self, recipe):
        """
        Add a recipe to the book and update last_update
        """
        self.recipe_list[recipe.recipe_type] = recipe
