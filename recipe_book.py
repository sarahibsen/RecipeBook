# recipe book 
class RecipeBook:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, name, ingredients, instructions):
        self.recipes[name] = {'ingredients': ingredients, 'instructions': instructions}

    def get_recipes_by_ingredient(self, ingredient):
        found = False
        for name, details in self.recipes.items():
            if any(ingredient.lower() in ing.lower() for ing in details['ingredients']):
                found = True
                print(f"\nRecipe for {name}:")
                print("Ingredients:")
                for ing in details['ingredients']:
                    print(f"- {ing}")
                print("\nInstructions:")
                for step, instruction in enumerate(details['instructions'], start=1):
                    print(f"Step {step}: {instruction}")
        if not found:
            print("No recipes found with that ingredient.")

# Create an instance of RecipeBook
my_recipe_book = RecipeBook()

# Add some recipes
my_recipe_book.add_recipe("Grilled Lemon Garlic Chicken",
                          ["2 chicken breasts", "2 cloves garlic, minced", "1 lemon, juiced and zested",
                           "2 tablespoons olive oil", "Salt and pepper to taste", "1 cup quinoa",
                           "1 cucumber, diced", "1 bell pepper, diced", "1/4 cup chopped fresh parsley",
                           "2 tablespoons red wine vinegar"],
                          ["Marinate the chicken with garlic, lemon juice and zest, olive oil, salt, and pepper for at least 30 minutes.",
                           "Cook quinoa as per package instructions and let cool.",
                           "Grill the chicken until fully cooked.",
                           "Toss quinoa with cucumber, bell pepper, parsley, red wine vinegar, and olive oil.",
                           "Serve the grilled chicken with the quinoa salad."])

my_recipe_book.add_recipe("Beef and Broccoli Stir-Fry",
                          ["300g beef strips", "2 cups broccoli florets", "1 onion, sliced", "2 tablespoons soy sauce (gluten-free)",
                           "1 tablespoon sesame oil", "1 teaspoon cornstarch", "1/4 cup water", "1 tablespoon ginger, grated"],
                          ["Mix soy sauce, sesame oil, cornstarch, and water in a bowl.",
                           "Stir-fry beef until browned then set aside.",
                           "In the same pan, add broccoli and onion, cooking until vegetables are tender.",
                           "Add ginger and the cooked beef back to the pan.",
                           "Pour the sauce mixture over and stir well to coat. Cook until the sauce thickens.",
                           "Serve hot."])

# User interaction
ingredient = input("Enter an ingredient to find recipes (e.g., chicken, beef): ")
my_recipe_book.get_recipes_by_ingredient(ingredient)
