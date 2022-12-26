import requests
print('\n')
print('Welcome to a recipe search.'+ '\n'+'You can find recipes here based on ingredients'+'\n')

def recipe_search(ingredients):
    app_id ='3f62d545'
    app_key ='3f7787f2f28188a35f6e6e91fbaf65fa'
    result = requests.get(
'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredients,app_id,app_key))
    data = result.json()
    return data['hits']

def run():
   ingredient = input('Enter an ingredient: ')
   results = recipe_search(ingredient)
   print('\n')
   vegetarian = input('are you vegetarian? y/n ')
   is_vegetarian = vegetarian == 'y'
   recipe_list = []
   for result in results:
       recipe = result['recipe']
       label = recipe['label']
       if is_vegetarian:
           if 'Vegetarian' in recipe['healthLabels']:
               recipe_list.append(label)
       else:
           recipe_list.append(label)
   print('\n')
   print('The recipes you can choose from are:')
   print('\n')
   print(*recipe_list,sep='\n')
   print('\n')
   weight = input('would you like the weight order -in grams - of the recipes? y/n ')
   list ={}
   if weight == 'y':
       for result in results:
           recipe = result['recipe']
           label = recipe['label']
           weight = recipe['totalWeight']
           list.update({str(label): weight})

       # order dictionary by value
       order = dict(sorted(list.items(), key=lambda item: item[1]))

       print('\n')
       print(order)
       print('\n')
   else:
       print('okay, thank u')
       print('\n')

   choice=input('Enter your recipe choice for more details: ')
   for result in results:
       recipe = result['recipe']
       label = recipe['label']
       ingredientslines = recipe['ingredientLines']
       if str(label).lower() == choice.lower():
           print('\n')
           print('here is what you will need to make your recipe:')
           print('\n')
           print(ingredientslines)
           print('\n')
           print('Read more here on how to make your recipe via this link:')
           print(recipe['url'])
           print('\n')

   recipe_save_choice = input('would you like to save all the recipes from your search before you leave? y/n ')
   if recipe_save_choice == 'y' and is_vegetarian:
       results = recipe_search(ingredient)
       for result in results:
           recipe = result['recipe']
           with open('ingredient.txt', 'a+') as ingredient_file:
               ingredient_file.write(recipe['label'])
               ingredient_file.write('\n')
               ingredient_file.write(recipe['url'])
               ingredient_file.write('\n')
               ingredient_file.write('\n')
   else:
       print('\n')
       print('thank you for using our search app, see you soon!')
   print('\n')
   print('bye!')
run()