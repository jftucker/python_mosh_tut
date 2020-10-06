import numpy as np

dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)

dimensions_inch = [1, 2, 3]
dimensions_cm = [x * 2.54 for x in dimensions_inch]

print(dimensions_cm)