primeiro = int(input("Primeiro elemento: ") )
razao = int(input("Razao: ") )

ultimo = primeiro + (10 - 1) * razao

for var in range(primeiro, ultimo + razao, razao):
    print(var, end=' -> ')
print('Fim')
