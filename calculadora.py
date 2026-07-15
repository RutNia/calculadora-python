"""
Calculadora en Python
Responsable del proyecto: Ruth Benítez (Líder)
"""

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: no se puede dividir entre cero"

def main():
    print("*** BIENVENIDO A LA CALCULADORA ***")
    print("Selecciona una operación:")
    print("a) Sumar")
    print("b) Restar")
    print("c) Multiplicar")
    print("d) Dividir")
    opcion = input("Tu elección: ")
    print("Calculadora en construcción...")

if __name__ == "__main__":
    main()
