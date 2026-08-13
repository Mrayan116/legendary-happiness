import tkinter as tk  # Import the Tkinter library for GUI
from PIL import Image, ImageTk  # Import Image and ImageTk from the PIL library for image handling
import time  # Import the time module for animation delays

# Function to draw a tree on the canvas
def draw_tree(canvas, x, trunk_width, leaves_width):
    # Define coordinates for the trunk
    trunk_left = x - trunk_width/2
    trunk_top = 300
    trunk_right = x + trunk_width/2
    trunk_bottom = 400
    # Draw the trunk rectangle
    canvas.create_rectangle(trunk_left, trunk_top, trunk_right, trunk_bottom, fill='brown')

    # Define coordinates for the leaves (triangle shape)
    leaves_left = x - leaves_width/2
    leaves_top = 300
    leaves_middle = 200
    leaves_right = x + leaves_width/2
    # Draw the triangular leaves on top of the trunk
    canvas.create_polygon(leaves_left, leaves_top, x, leaves_middle, leaves_right, leaves_top, fill='green')

# Function to draw a pond on the canvas
def draw_pond(canvas):
    # Draw a blue oval to represent a pond
    canvas.create_oval(400, 420, 500, 520, fill='blue')

# Function to draw clouds on the canvas
def draw_clouds(canvas):
    # Draw two oval-shaped clouds
    cloud1 = canvas.create_oval(50, 50, 150, 100, fill='white')
    cloud2 = canvas.create_oval(200, 80, 300, 130, fill='white')
    # Return the cloud IDs for later movement
    return [cloud1, cloud2]

# Function to draw a bird on the canvas
def draw_bird(canvas, x, y, bird_image):
    # Draw a bird image on the canvas and return its ID
    bird_id = canvas.create_image(x, y, anchor=tk.NW, image=bird_image)
    return bird_id

# Function to animate the bird's movement on the canvas
def animate_bird(canvas, bird_id):
    # Move the bird diagonally upward for a short distance
    for _ in range(50):
        canvas.move(bird_id, 3, -1)
        canvas.update()
        time.sleep(0.05)

# Function to move clouds horizontally on the canvas
def move_clouds(canvas, cloud_ids):
    # Move each cloud horizontally for a certain number of iterations
    for _ in range(100):
        for cloud_id in cloud_ids:
            canvas.move(cloud_id, 2, 0)
        canvas.update()
        time.sleep(0.05)

# Function to draw a grassy land on the canvas
def draw_grassy_land(canvas):
    # Draw a green rectangle to represent the ground/grassy land
    canvas.create_rectangle(0, 400, 600, 500, fill='green')

# Main function to set up the Tkinter window and draw elements
def main():
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("flying bird")

    # Create a canvas within the window
    canvas = tk.Canvas(root, width=600, height=500, bg='skyblue')
    canvas.pack()

    # Load and resize the bird image
    bird_image_path = "bird.png"
    original_bird_image = Image.open(bird_image_path)
    resized_bird_image = ImageTk.PhotoImage(original_bird_image.resize((40, 30)))

    # Draw elements on the canvas
    draw_grassy_land(canvas)
    draw_tree(canvas, 150, 20, 40)
    draw_tree(canvas, 450, 30, 50)
    draw_tree(canvas, 50, 25, 45)
    draw_pond(canvas)
    cloud_ids = draw_clouds(canvas)
    bird_id = draw_bird(canvas, 50, 50, resized_bird_image)

    # Animate the bird and move the clouds
    animate_bird(canvas, bird_id)
    move_clouds(canvas, cloud_ids)

    # Return the Tkinter window and canvas for mainloop
    return root, canvas

# Run the main function and start the Tkinter mainloop
root, canvas = main()
root.mainloop()
