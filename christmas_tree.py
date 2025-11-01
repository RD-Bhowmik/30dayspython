import random

height = 10
base_width = 2*height - 1

palette  = ['*', '=', 'o', '+']
weights  = [0.65, 0.2, 0.1, 0.05] 

for i in range(1, height + 1):
    k = 2*i - 1
    row = ''.join(random.choices(palette, weights=weights, k=k))
    print(row.center(base_width))

trunk_height = 4
trunk_width  = 4
trunk = "#" * trunk_width
for _ in range(trunk_height):
    print(trunk.center(base_width))
