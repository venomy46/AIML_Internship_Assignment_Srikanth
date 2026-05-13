import time
import numpy as np

# Create 1 million numbers using Python list
python_list = list(range(1000000))

# Create 1 million numbers using NumPy array
numpy_array = np.arange(1000000)

# Python list operation timing
start = time.time()
python_result = [x * 2 for x in python_list]
end = time.time()
python_time = end - start

# NumPy array operation timing
start = time.time()
numpy_result = numpy_array * 2
end = time.time()
numpy_time = end - start

print("Python List Time:", python_time)
print("NumPy Array Time:", numpy_time)