from flask import Flask, request, render_template, redirect
from ice_cream_app import (
    add_seasonal_flavor, add_ingredient, add_customer_suggestion, add_allergen, 
    add_to_cart, get_seasonal_flavors, get_ingredients, get_customer_suggestions, 
    get_allergens, get_user_cart
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_seasonal_flavor', methods=['POST'])
def add_seasonal_flavor_route():
    name = request.form['name']
    season = request.form['season']
    add_seasonal_flavor(name, season)
    return redirect('/')

@app.route('/add_ingredient', methods=['POST'])
def add_ingredient_route():
    name = request.form['name']
    stock = request.form['stock']
    add_ingredient(name, stock)
    return redirect('/')

@app.route('/add_customer_suggestion', methods=['POST'])
def add_customer_suggestion_route():
    flavor = request.form['flavor']
    allergens = request.form['allergens']
    add_customer_suggestion(flavor, allergens)
    return redirect('/')

@app.route('/add_allergen', methods=['POST'])
def add_allergen_route():
    name = request.form['name']
    add_allergen(name)
    return redirect('/')

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart_route():
    flavor_id = request.form['flavor_id']
    add_to_cart(flavor_id)
    return redirect('/')

@app.route('/view_seasonal_flavors')
def view_seasonal_flavors():
    flavors = get_seasonal_flavors()
    return render_template('view_seasonal_flavors.html', flavors=flavors)

@app.route('/view_ingredients')
def view_ingredients():
    ingredients = get_ingredients()
    return render_template('view_ingredients.html', ingredients=ingredients)

@app.route('/view_customer_suggestions')
def view_customer_suggestions():
    suggestions = get_customer_suggestions()
    return render_template('view_customer_suggestions.html', suggestions=suggestions)

@app.route('/view_allergens')
def view_allergens():
    allergens = get_allergens()
    return render_template('view_allergens.html', allergens=allergens)

@app.route('/view_cart')
def view_cart():
    cart = get_user_cart()
    return render_template('view_cart.html', cart=cart)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)