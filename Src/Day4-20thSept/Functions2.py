def make_pizza(*toppings,base):
    for topping in toppings:
        print(topping)
    print(base)

indra = make_pizza('pepper','extra cheese','milk',base= 'bread')