import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / (3**0.5) / 2)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

    window.mainloop()


def main():
    try:
        recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    if recursion_level < 0:
        print("Рівень рекурсії повинен бути не менше 0.")
        return

    draw_koch_snowflake(recursion_level)


if __name__ == "__main__":
    main()
