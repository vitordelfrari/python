import math

manufctured = int(input("Type the number of manufactured items: "))
item_box = int(input("Type the number of items that the user will pack per box: "))
boxes = math.ceil(manufctured / item_box)

print(f"For {manufctured} items, packing {item_box} items in each box, you will need {boxes} boxes.")



