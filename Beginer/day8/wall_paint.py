import math

test_h = int(input("height of wall: "))
test_w = int(input("width of wall: "))


coverage = 5

def paint(height, width,coverage):
    number_of_can = (height*width)/coverage
    num_up = math.ceil(number_of_can)   #làm tròn lên
    print(f"You'll need{num_up} cans of paints")
