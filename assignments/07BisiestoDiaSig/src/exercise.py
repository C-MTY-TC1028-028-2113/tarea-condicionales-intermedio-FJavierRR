def main():
    #escribe tu código abajo de esta línea
    y = int(input("Año: "))
    m = int(input("Mes: "))
    d = int(input("Día: "))
    # Meses con 31 dias: 1, 3, 5, 7, 8, 10, 12
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if d == 31:
            d = 1
            if m == 12:
                m = 1
                y = y + 1
            else:
                m = m + 1
        else:
            d = d + 1
    # Meses con 30 dias: 4, 6, 9, 11
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if d == 30:
            d = 1
            m =m + 1
        else:
            d = d + 1
    # Mes 2 puede tener 28 o 29 dias
    else:
        if d == 29 and y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            d = 1
            m = m + 1
        elif d == 28:
            if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
                d = d + 1
            else:
                d = 1
                m = m + 1
        else:
            d = d + 1
    print(y)
    print(m)
    print(d)

if __name__=='__main__':
    main()
