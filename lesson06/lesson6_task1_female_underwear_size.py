def sizes(intern_size, country):

    underwear = {
        'XXS':  {'Ukraine': '42', 'Germany': '36', 'USA':  '8', 'France': '38', 'GB': '24'},
        'XS':   {'Ukraine': '44', 'Germany': '38', 'USA': '10', 'France': '40', 'GB': '26'},
        'S':    {'Ukraine': '46', 'Germany': '40', 'USA': '12', 'France': '42', 'GB': '28'},
        'M':    {'Ukraine': '48', 'Germany': '42', 'USA': '14', 'France': '44', 'GB': '30'},
        'L':    {'Ukraine': '50', 'Germany': '44', 'USA': '16', 'France': '46', 'GB': '32'},
        'XL':   {'Ukraine': '52', 'Germany': '46', 'USA': '18', 'France': '48', 'GB': '34'},
        'XXL':  {'Ukraine': '54', 'Germany': '48', 'USA': '20', 'France': '50', 'GB': '36'},
        'XXXL': {'Ukraine': '56', 'Germany': '50', 'USA': '22', 'France': '52', 'GB': '38'}
        }
    return None if intern_size not in underwear else underwear.get(intern_size).get(country)


print(sizes("XXXL", "Ukraine"))
