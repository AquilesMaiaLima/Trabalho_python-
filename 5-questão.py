hora = int(input("digite a hora: "))
if 0<= hora<=23:
    if 0<= hora <12:
        p = 'manhã'
    elif 12 <= hora < 18:
        p = "tarde"
    else:
        p = "noite"
    print(f'È de {p}')
else:
    print("horario invalido")