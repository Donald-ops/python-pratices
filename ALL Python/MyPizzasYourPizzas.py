pizzas = ['chicken', 'pepperoni','cheese','margherita']
friend_pizzas = pizzas[:]
print(friend_pizzas)

pizzas.append('new york-style')
friend_pizzas.append('neapolitan')

print("\nMy favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are: ")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
