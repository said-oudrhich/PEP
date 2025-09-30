entero = 6
print("Valor:", entero, "Tipo:", type(entero))
otra_variable = entero
print("Valor:", otra_variable, "Tipo:", type(otra_variable))
print("¿Apuntan al mismo objeto?", entero is otra_variable)
print("¿No apuntan al mismo objeto?", entero is not otra_variable)
entero = "Hola"
print("Valor:", entero, "Tipo:", type(entero))
print("Valor:", otra_variable, "Tipo:", type(otra_variable))
print("¿La primera variable es de tipo int?", isinstance(entero, int))
print("¿La segunda variable es de tipo str?", isinstance(otra_variable, str))
