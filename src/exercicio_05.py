def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida


texto = input("Digite uma string para inverter: ")
string_invertida = inverter_string(texto)
print(f"String invertida: {string_invertida}")
