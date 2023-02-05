import numpy as np

clouds_rgb_a = np.empty((0,2),int)

r = 5.0
g = 5

clouds_rgb_a = np.append(clouds_rgb_a, np.array([[r, g]]), axis = 0)
print(clouds_rgb_a)