def main():
    # Escribe tu código abajo de esta línea
    c = int(input("Introduce los cm: "))
    if c<100:
        print(c,"cm")
    elif c<1000:
        x=c//100
        y=c-(x*100)
        print(x,"m")
        if y!=0:
            print(y,"cm")
    else:
        x=c//100000
        y=(c-(x*100000))//100
        z=(c-(x*100000)-(y*100))
        if x!=0:
            print(x,"km")
        if y!=0:
            print(y,"m")
        if z!=0:
            print(z,"cm")

if __name__ == '__main__':
    main()
