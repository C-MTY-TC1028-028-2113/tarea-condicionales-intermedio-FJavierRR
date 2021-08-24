![Tec de Monterrey](../../images/logotecmty.png)
# Día siguiente - considera año Bisiesto

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python

def main():
    # Escribe el código adecuado para completar el programa
    y = int(input("Año: "))
    m = int(input("Mes: "))
    d = int(input("Día : "))

if __name__ == '__main__':
    main()
```

Recuerda, la línea `# Escribe el código adecuado para completar el programa` es un comentario, el programa la va a ignorar al ejecutarse.

## Definición del problema  

Escribe un programa que dada una fecha (año, mes y día), devuelva la fecha del día siguiente. Te recomiendo que antes de ponerte de codificar, verifiques todas las posibilidades que se pueden presentar.

Este problema debe considerar la verificación de año bisiesto. Recuerda que el siguiente algoritmo se puede usar para determinar si un año determinado es bisiesto:  
  * Los años bisiestos son cualquier año que es divisible por 4 (como 2012, 2016, etc).
  * Excepto si puede dividirse por 100, entonces no lo es (como 2100, 2200, etc).
  * A menos que pueda ser divisible por 400, como 2000, 2400.

Para este ejercicio, no validaremos las entradas, confiaremos que el usuario ingresará una fecha válida.

**Entradas**  
Año, día y mes (**enteros positivos**) en ese orden.

**Salidas**  
Año, día y mes (**enteros positivos**) en ese orden que corresponde al día siguiente ingresado como entrada.
 
## Ejemplos  

Ejemplo 1    

```plaintext
Año: 2015
Mes: 2
Día: 13
2015
2
14
```

Ejemplo 2

```plaintext
Año: 2016
Mes: 2
Día: 28
2016
2
29
```

Ejemplo 3

```plaintext
Año: 2016
Mes: 12
Día: 31
2017
1
1
```

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest --tb=short`,
subela a tu repositorio en GitHub, con el proceso de commit + push
