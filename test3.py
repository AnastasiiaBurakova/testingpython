def solve_quadratic(a,b,c):
    determinant = b**2 - 4*a*c
    if (determinant == 0):
        return -b / 2*a
    if (determinant < 0):
        return None 
    answer1 = (-b + determinant**0.5) / 2*a 
    answer2 = (-b - determinant**0.5) / 2*a
    return (answer1, answer2)
    
         
