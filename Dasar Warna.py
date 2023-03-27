import turtle

# Membuat layar
wn = turtle.Screen()

# Menentukan warna layar
wn.bgcolor("white")

# Membuat turtle
t = turtle.Turtle()

# Menentukan warna turtle
t.color("red")

# Menggambar kotak
for i in range(4):
    t.forward(100)
    t.right(90)

# Menutup layar saat di-klik
wn.exitonclick()
