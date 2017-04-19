# Fuzzy Logic Evaluator

## Sinopsis
Este proyecto implementa una herramienta escrita en *Python 3* que permite al usuario:
* Definir un sistema de inferencia difusa:
  - Definir las variables de entrada y salida, con sus respectivos valores lingüísticos y funciones de membresía
  - Definir las reglas de inferencia
  - Especificar el método a emplear
  - Definir el tamaño de paso a utilizar en la discretización de los valores de las variables de salida
* Utilizar el sistema de inferencia definido, para obtener los valores de las variables de salida para diferentes juegos de datos

## Entrada
El programa se ejecuta mediante el comando:

```bash
python main.py <data>.json <rules>.fuz [--step <step_size>]
```

`<data>.json`: fichero en formato JSON con las especificaciones de las variables de entrada y sus respectivos valores, así como las funciones de membresía. Un ejemplo de una variable y una función sería:
```json
{
    "variables": {
        "input1": 5.3
    }
    "functions": {
        "membership_func1": [
            "Trapezoid", 10, 15, 20, 25
        ]
    }
}
```
Como se puede deducir del ejemplo, las funciones se especifican mediante una lista, cuyo primer elemento es el tipo de la función y los restantes son los parámetros que caracterizan su comportamiento; siendo estos últimos específicos de cada tipo.
Los tipos de funciones soportados son:
* __Trapezoid__:
  - `a`: Punto donde la monotonía de la función pasa a ser creciente, por tanto, `f(a)==0`. Si `a==null` se asume que para cualquier `x<=a` se cumple que `f(x)==1`.
  - `b`: Menor (mayor si `a==null`) valor de `x` para el que `f(x)==1`.
  - `c`: Mayor valor de `x` para el que `f(x)==1`, si no existe tal `x` finita, entonces `c==null`. Si `a==null`, entonces es el menor valor de `x` para el que `f(x)==0`.
  - `d`: Punto donde la monotonía deja de ser decreciente. Si no existe, o `a==null`, entonces `c==null`.
* __Triangle__: Caso particular de trapezoide, con tres parámetros `a`, `b` y `c` representando las `x` de sus 3 vértices.
* __Sigmoid__:
  - `k`: Ancho del sigmoide
  - `x0`: Valor central
* __Gaussian__:
  - `b`: Centro de la campana
  - `c`: Ancho de la campana

`<rules>.fuz`: fichero con la especificación de las reglas y el modelo de inferencia; sigue el siguiente formato:
```
[model] (Mamdani | Sugeno | Tsukamoto)
[t-norm] (min | product)
[t-conorm] (max | sum)
([defuzzy] (Centroid | Bisecter | Mean_max))?

input1 is val1 or input2 is val2 then output1 is val3
```
Todas las variables definidas a la izquierda de los `then` deben tener un valor asociado en el fichero de datos (.json). Asimismo ha de ocurrir con los valores lingüísticos usados en las reglas.
En el caso de usar el modelo *Sugeno*, el valor la parte derecha de los `then` será una expresión aritmética que puede usar valores numéricos y variables de entrada. Los operadores permitidos en este caso son `+`, `-`, `*`, `/` y `**` (potencia).

En los campos `t-norm` y `t-conorm` se indicarán las operaciones para evaluar las expresiones `and` y `or` respectivamente.

## Salida
El programa reporta el resultado de evaluar el sistema especificado. Los valores calculados para cada una de las variables de salidas son reportados por la salida estándar, siguiendo el formato: `output1: #.000\n`
