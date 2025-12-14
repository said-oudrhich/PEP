class Persona:
    pass

persona= Persona()
print(type(persona)) # <__main__.Person object at 0x7fe70c878c10>
print(isinstance(persona, Persona)) # True
print(isinstance(persona, object)) # True