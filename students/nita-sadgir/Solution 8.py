def print_triangle(height):
    for row in range(1, height + 1):
        stars = ""
        for col in range(row):
            stars += "*"
        print(stars)

print_triangle(5) 
