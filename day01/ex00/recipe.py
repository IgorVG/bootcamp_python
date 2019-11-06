
class Recipe:

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=None):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    @property
    def cooking_lvl(self):
        return self._cooking_lvl

    @cooking_lvl.setter
    def cooking_lvl(self, v):
        if not (v >= 0 and v <= 5): raise Exception('Cooking_lvl must be in the range [0; 5]')
        self._cooking_lvl = v
    
    @property
    def cooking_time(self):
        return self._cooking_time
    
    @cooking_time.setter
    def cooking_time(self, v):
        if not (v >= 0): raise Exception('Cooking_time must be non negative')
        self._cooking_time = v
    
    @property
    def recipe_type(self):
        return self._recipe_type

    @recipe_type.setter
    def recipe_type(self, v):
        types_list = ['starter', 'lunch', 'dessert']
        if not (v in types_list): raise Exception('Recipe type must be in [starter, lunch, dessert]')
        self._recipe_type = v

    def __str__(self):
        format_str = ("To prepare %s, you must plan %s min; Cooking level"
                      "is %s; Prepare following ingredients: %s"
                      )
        data = (self.name, self.cooking_time, self.cooking_lvl, self.ingredients)
        format_str = ("To prepare {}, you must plan {} min; Cooking level"
                      "is {}; Prepare following ingredients: {}"
                      )
        #to_return = format(format_str2 % data)
        to_return = format_str.format(*data)
        if self.description:
            to_return += "\nDescription: \n{}". format(self.description)
        return to_return


