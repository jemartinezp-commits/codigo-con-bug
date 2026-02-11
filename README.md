## Bug original
El programa solicitaba la edad con input(), pero input() devuelve un string.
Se estaba comparando directamente con un número entero (18), lo que provocaba un error de tipo.

edad = input("Ingresa tu edad: ")
if edad >= 18:

## Problema
No se puede comparar un string con un entero.

## Corrección
Se convirtió la entrada a entero usando int().

edad = int(input("Ingresa tu edad: "))

Con esto la comparación funciona correctamente.
