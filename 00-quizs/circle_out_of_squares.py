import turtle

def draw_square(t):
    # Draw 4 edges to form a square and back to original position with same orientation
    for n in range(1, 5):
        t.forward(100)
        t.right(90)
    
def draw_art():
    
    # Create Canva
    window = turtle.Screen()
    window.bgcolor("red")
    
    # Create turtle object 
    t = turtle.Turtle()
    t.color('yellow')
    t.speed(10)

    # Draw 36 times, each time rotate 10 degree clockwisely
    for n in range(1, 36):
        draw_square(t)
        t.right(10)
    
    window.exitonclick()

if __name__ == "__main__":
    draw_art()