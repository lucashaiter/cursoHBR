# Ex 1
product_list = [
    {'name': 'Teclado Mecânico', 'price': 350.00, 'in_stock': True},
    {'name': 'Mouse Gamer', 'price': 120.50, 'in_stock': False},
    {'name': 'Monitor 4K', 'price': 1800.00, 'in_stock': True},
    {'name': 'Webcam Full HD', 'price': 450.00, 'in_stock': True},
    {'name': 'Headset Pro', 'price': 550.00, 'in_stock': True}
]

new_list = []

for p in product_list:
    if p['price'] < 500 and p['in_stock'] == True:
        new_list.append(p)

for i in range(len(new_list)):
    print(f"Produto {i + 1}")
    print(f"Nome: {new_list[i]['name']}")
    print(f"Preço: {new_list[i]['price']}")
    print(f"Em estoque: {new_list[i]['in_stock']}\n")


# Ex2
post_slugs = ['como-aprender-django', 'guia-de-python-para-iniciantes', 'otimizando-queries-sql']
full_urls = []

for i in range(len(post_slugs)):
    full_urls.append("/blog/" + post_slugs[i] + "/")

for i in range(len(full_urls)):
    print(f"{i + 1}º URL: {full_urls[i]}")


# Ex3
tag_names = ['Python', 'Django', 'Desenvolvimento Web', 'Banco de Dados']
form_choices = []

for tag in tag_names:
    form_choices.append((tag, tag))

for i in range(len(form_choices)):
    print(f"{form_choices[i]}")


# Ex4
users_to_deactivate = [
    {'username': 'ana.souza', 'email': 'ana@example.com', 'is_active': True},
    {'username': 'bruno.lima', 'email': 'bruno@example.com', 'is_active': True},
    {'username': 'carla.reis', 'email': 'carla@example.com', 'is_active': True}
]

for i in range(len(users_to_deactivate)):
    users_to_deactivate[i]['is_active'] = False
    print(f"Nome de usuário: {users_to_deactivate[i]['username']}, Email: {users_to_deactivate[i]['email']}, Ta ativo: {users_to_deactivate[i]['is_active']}")


# Ex5
cart_items = [
    {'product': 'Cadeira Gamer', 'price': 1200.00, 'quantity': 1},
    {'product': 'Mousepad', 'price': 80.00, 'quantity': 2},
    {'product': 'Cabo USB-C', 'price': 50.00, 'quantity': 3}
]

total_price = 0.0

for i in range(len(cart_items)):
    total_price += cart_items[i]['price'] * cart_items[i]['quantity']

print(f"O valor total do carrinho é: R$ {total_price:.2f}")