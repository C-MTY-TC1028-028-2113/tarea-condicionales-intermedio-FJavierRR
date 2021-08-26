import math

def main():
    # Escribe tu código abajo de esta línea
    A=int(input("Da el valor de a: "))
    b=int(input("Da el valor de b: "))
    c=int(input("Da el valor de c: "))
    if (A==0) and (b==0):
        print("No tiene solucion")
    elif (A==0):
        raiz=-c/b
        print(raiz)
    else:
        discrim=b**2-4*A*c
        if (discrim)>0:
            x1=(-b+math.sqrt(discrim))/(2*A)
            x2=(-b-math.sqrt(discrim))/(2*A)
            print(x1)
            print(x2)
        elif (discrim < 0):
            print("Raices complejas")
        else:
            x=-b/(2*A)
            print(x)

if __name__ == '__main__':
    main()
