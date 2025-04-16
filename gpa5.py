import matplotlib.pyplot as plt 

def draw_colored_shapes(): 
    fig, ax = plt.subplots(figsize=(8, 8)) 
    
    # Draw and color a rectangle 
    rectangle = plt.Rectangle((1, 1), 4, 3, color='blue', ec= 'black', lw=2, label="Rectangle") 
    ax.add_patch(rectangle) 
    
    # Draw and color a circle 
    circle = plt.Circle((6, 6), 2, color='green',ec= 'black', lw=2,  label="Circle") 
    ax.add_patch(circle) 
    
    # Draw and color a triangle 
    triangle = plt.Polygon([[2, 7], [3.5, 10], [5, 7]], color='red',ec= 'black', lw=2,  label="Triangle") 
    ax.add_patch(triangle) 
    
    # Draw and color a polygon 
    polygon = plt.Polygon([[7, 1], [8.5, 3], [10, 1], [8.5, -1]], color='yellow',ec= 'black', lw=2,  label="Polygon") 
    ax.add_patch(polygon) 
    
    # Configure plot 
    ax.set_xlim(0, 12) 
    ax.set_ylim(-2, 12) 
    plt.axhline(0, color='black', linewidth=0.5) 
    plt.axvline(0, color='black', linewidth=0.5) 
    ax.set_aspect('equal', adjustable='box')
    plt.grid(color='gray', linestyle='--', linewidth=0.5) 
    plt.title("Colored Shapes") 
    plt.legend(loc="best") 
    plt.show()

draw_colored_shapes()
