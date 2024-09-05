
def inverter(string):
    invercao = ''
    for char in string:
        invertida = char + invercao
    return invertida

palavra = input("Digite a string que deseja inverter: ")
print("String invertida:", inverter(palavra))
