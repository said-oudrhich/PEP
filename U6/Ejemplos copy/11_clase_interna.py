class Externa:
  def __init__(self):
    self.nombre = "Clase Externa"

  class Interna:
    def __init__(self):
      self.nombre = "Clase Interna"

    def mostrar(self):
      print("Esta es la clase interna")

externa = Externa()
interna = externa.Interna()
interna.mostrar()