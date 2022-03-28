

def to_hex(n):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    left_digit = digits[n // 16]
    right_digit = digits[n % 16]
    if left_digit == '0':
        return right_digit
    return left_digit + right_digit


def hex_color(red,green,blue):
    hex_red = to_hex(red) 
    hex_green = to_hex(green)
    hex_blue = to_hex(blue)

    if len(hex_green) == 1:
        hex_green = '0' + hex_green
    if len(hex_red) == 1:
        hex_red = '0' + hex_red
    if len(hex_blue) == 1:
        hex_blue = '0' + hex_blue

    return '#' + hex_red + hex_green + hex_blue           


    

