dict={'Name': 'Universitas Amikom Yogyakarta', 'Address': 'Jl. Ringroad Utara'}

print(dict['Name'])
print(dict['Address'])

buah={'b1': 'Mangga', 'b2': 'Jeruk', 'b3': 'Melon'}
harga={'h1': 8000, 'h2': 6000, 'h3': 9000}

print("Menu Buah")
print("1. ", buah['b1'], "=", harga['h1'])
print("2. ", buah['b2'], "=", harga['h2'])
print("3. ", buah['b3'], "=", harga['h3'])

def luas_segitiga(alas, tinggi):
    return((alas*tinggi) / 2)

luas_segitiga(4, 6)
print (luas_segitiga)