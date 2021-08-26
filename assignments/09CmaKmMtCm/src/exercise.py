def main():
    # Escribe tu código abajo de esta línea
    C = int(input("Introduce los cm: "))
    if C<100:
        print(C,"cm")
    elif C<1000:
        x=C//100
        y=C-(x*100)
        print(x,"m")
        if y!=0:
            print(y,"cm")
    else:
        x=C//100000
        y=(C-(x*100000))//100
        z=(C-(x*100000)-(y*100))
        if x!=0:
            print(x,"km")
        if y!=0:
            print(y,"m")
        if z!=0:
            print(z,"cm")

if __name__ == '__main__':
    main()
