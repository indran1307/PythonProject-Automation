# def make_pizza(*toppings):
#     for topping in toppings:
#         print(topping)
#
#
# indra = make_pizza('pizza', 'cheese')
# sai = make_pizza('mushrooms', 'cheese', 'panner')


def make_pizza(*toppings,base):
    for topping in toppings:
        print(topping)
    print(base)
divya = make_pizza('pizza', 'cheese', 'mushrooms', base='soft')


