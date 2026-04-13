# pattern_solutions.py

# 1. Right Triangle Star Pattern
def right_triangle_star(n):
    for i in range(n):
        print('*' * (i + 1))

# 2. Pyramid Star Pattern
def pyramid_star(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# 3. Diamond Star Pattern
def diamond_star(n):
    pyramid_star(n)
    for i in range(n-1):
        print(' ' * (i + 1) + '*' * (2 * (n - i - 1) - 1))

# Example usage
if __name__ == "__main__":
    print("Right Triangle Star Pattern:")
    right_triangle_star(5)
    print("\nPyramid Star Pattern:")
    pyramid_star(5)
    print("\nDiamond Star Pattern:")
    diamond_star(5)