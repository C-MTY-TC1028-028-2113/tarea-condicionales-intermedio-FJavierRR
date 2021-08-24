![Tec de Monterrey](../../images/logotecmty.png)
# Cuadrática
**Decisiones - Calcula los valores de una ecuación cuadrática**

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
  # Escribe tu código abajo de esta línea
  pass

if __name__ == '__main__':
    main()
```

La línea `#Escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

Realiza un programa para calcular los valores de la ecuación cuadrática `ax^2+bx+c` usando la fórmula cuadrática.
El programa debe leer tres valores enteros a, b y c, y encontrar los valores de x, considerando las siguientes restricciones:
- Si a = 0 y b = 0 se debe desplegar el mensaje `"No tiene solucion”`.
- Si a = 0 y b != 0 se debe despejar el valor de x = –c/b y mostrar este valor.
- Si a != 0 y b != 0 se debe calcular el discriminante.
      * Si el valor del discriminante es negativo debe mostrar el mensaje `"Raices complejas"`.
      * Si el valor del discriminante es positivo debe calcular y mostrar los dos valores de x, una en cada renglón.
      * En caso de que el discriminante sea cero se debe mostrar sólo un valor de x = -b/(2a).

**Entradas**
- Los tres valores enteros a, b, c uno en cada renglón y en ese orden.

**Salidas**
- El valor de la o las raices (si es el caso) uno en cada renglón, o alguno de los mensajes `"No tiene solucion"` o `"Raices complejas"`.

Estos son algunos ejemplos de ejecución del programa. La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Da el valor de a: 1
Da el valor de b: 2
Da el valor de c: 3
Raices complejas

Da el valor de a: 0
Da el valor de b: 1
Da el valor de c: 2
-2.0

Da el valor de a: 1
Da el valor de b: 5
Da el valor de c: 6
-2.0
-3.0

Da el valor de a: 0
Da el valor de b: 0
Da el valor de c: 2
No tiene solucion

NOTA: Para mostrar la salida solamente muestra las variables en las que tienes el 
resultado de los cálculos, no le apliques ningún formato.
```

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest` o `pytest --tb=short`,
súbela a tu repositorio en GitHub, con el proceso de `commit + push`.
