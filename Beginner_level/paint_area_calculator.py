import math
def paint_calc (height,width,cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"Number of cans that will be required are {number_of_cans}.")
     

test_h = int(input("Height of the wall :  "))
test_w = int(input("Width of the wall :  "))
coverage = 5
paint_calc(height=test_h , width = test_w , cover = coverage)

