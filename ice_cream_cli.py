from ice_cream_app import *

def display_menu():
    print("Welcome to the Ice Cream Parlor!")
    print("1. Add Seasonal Flavor")
    print("2. Add Ingredient to Inventory")
    print("3. Add Customer Suggestion")
    print("4. View Seasonal Flavors")
    print("5. View Ingredients")
    print("6. View Customer Suggestions")
    print("7. Add Allergen")
    print("8. View Allergens")
    print("9. Add Flavor to Cart")
    print("10. View Cart")
    print("11. Exit")

def get_user_choice():
    return input("Enter your choice: ")

def main():
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == '1':
            name = input("Enter flavor name: ")
            season = input("Enter season: ")
            add_seasonal_flavor(name, season)
        elif choice == '2':
            name = input("Enter ingredient name: ")
            stock = int(input("Enter stock quantity: "))
            add_ingredient(name, stock)
        elif choice == '3':
            flavor = input("Enter suggested flavor: ")
            allergens = input("Enter allergens (comma-separated): ")
            add_customer_suggestion(flavor, allergens)
        elif choice == '4':
            flavors = get_seasonal_flavors()
            print("Seasonal Flavors:")
            for flavor in flavors:
                print(flavor)
        elif choice == '5':
            ingredients = get_ingredients()
            print("Ingredients Inventory:")
            for ingredient in ingredients:
                print(ingredient)
        elif choice == '6':
            suggestions = get_customer_suggestions()
            print("Customer Suggestions:")
            for suggestion in suggestions:
                print(suggestion)
        elif choice == '7':
            allergen = input("Enter allergen name: ")
            add_allergen(allergen)
        elif choice == '8':
            allergens = get_allergens()
            print("Allergens:")
            for allergen in allergens:
                print(allergen)
        elif choice == '9':
            flavor_id = input("Enter flavor ID to add to cart: ")
            add_to_cart(flavor_id)
        elif choice == '10':
            cart = get_user_cart()
            print("Your Cart:")
            for item in cart:
                print(item)
        elif choice == '11':
            close_connection()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
 
