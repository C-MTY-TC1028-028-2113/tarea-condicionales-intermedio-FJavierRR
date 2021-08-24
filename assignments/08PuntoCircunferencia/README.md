![Tec de Monterrey](../../images/logotecmty.png)
# Punto con respecto a la circunferencia
**Decisiones - Posición de un punto con respecto a la circunferencia**

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

Escriba un programa que pida el radio y las coordenadas del centro de una circunferencia, así como las coordenadas de un punto. El programa deberá indicar si el punto está sobre la circunferencia, dentro o fuera de ella. Investiga o recuerda la fórmula del calculo de distancia entre dos puntos porque la vas a necesitar.

**Entradas**
- radio (flotante)
- x1 Coordenada x del centro de la circunferencia (flotante)
- y1 Coordenada y del centro de la circunferencia (flotante)
- x2 Coordenada x del punto (flotante)
- y2 Coordenada y del punto (flotante)
- NOTA: Los datos deberán ser ingresados estrictamente en este orden.

**Salida**
- Un string que representa la posición del punto con respecto a la circunferencia: `"DENTRO"`, `"FUERA"`, `"SOBRE"`.

Estos son algunos ejemplos de ejecución del programa. La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Introduce el radio: 5
Introduce x1: 0
Introduce y1: 0
Introduce x2: 0
Introduce y2: 6
FUERA

Introduce el radio: 5
Introduce x1: 0
Introduce y1: 0
Introduce x2: 0
Introduce y2: 5
SOBRE

Introduce el radio: 5
Introduce x1: 0
Introduce y1: 0
Introduce x2: 0
Introduce y2: 3
DENTRO
```
**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest` o `pytest --tb=short`,
subela a tu repositorio en GitHub, con el proceso de commit + push.
