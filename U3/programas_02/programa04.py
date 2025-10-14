import turtle

# Configuración de la ventana
turtle.title("Cuadrado y círculo con Turtle")

# --- Dibujar cuadrado rojo sin relleno ---
turtle.penup()
turtle.goto(-100, 0)  # Posición inicial para el cuadrado
turtle.pendown()
turtle.color("red")    # Color del borde
turtle.pensize(3)      # Grosor del borde

for _ in range(4):
    turtle.forward(100)  # Longitud del lado
    turtle.right(90)     # Giro 90 grados

# --- Dibujar círculo verde relleno ---
turtle.penup()
turtle.goto(100, 0)    # Posición inicial para el círculo
turtle.pendown()
turtle.color("green")      # Color del borde
turtle.fillcolor("green")  # Color de relleno

turtle.begin_fill()
turtle.circle(50)  # Radio del círculo
turtle.end_fill()

# Mantener la ventana abierta
turtle.done() # 