![Tec de Monterrey](../../images/logotecmty.png)
# De Centímetros a Kilómetros, Metros y Centímetros
**Decisiones - Conversión de centímetros a kilómetros, metros y centímetros**

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

Escribe un programa que pida una distancia en centímetros y que escriba esa distancia en su equivalente en kilómetros, metros y centímetros (escribiendo solamente las unidades necesarias).

**Entrada**
- Un número entero que representa la distancia en centímetros.

**Salidas**
- El número de km, m y cm equivalente a la cantidad de centímetros dada por el usuario.

Estos son algunos ejemplos de ejecución del programa. La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Introduce los cm: 100
1 m

Introduce los cm: 240005
2 km
400 m
5 cm

Introduce los cm: 67
67 cm

Introduce los cm: 300004
3 km
4 cm

Introduce los cm: 1200500
12 km
5 m
```
El resultado se debe mostrar como se indica con cada valor en un renglón por separado, indicando las unidades correspondientes (km, m y cm en minúscula) y en el orden indicado. Si no hay valor para alguna de las tres unidades, no debe mostrar dicho renglón.   

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest` o `pytest --tb=short`,
subela a tu repositorio en GitHub, con el proceso de commit + push.
