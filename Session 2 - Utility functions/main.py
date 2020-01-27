
# Third party imports
import matplotlib.pyplot as plt
import numpy as np

# Project specific imports
import utils
import plotting

# Create a graph
x = np.linspace(1, 20, 40)
y = np.sin(x) * 3 * np.cos(x**2)

# Define the interval in which to annotate extreme values
interval = (7.0, 15)

# Extract indices for values inside interval
interval_idx = utils.extract_interval(x, interval)

# Extract only values inside interval for both arrays
xx = x[interval_idx]
yy = y[interval_idx]

# Find indices of the extreme values in the interval
idx_extr = utils.extrema_indices(yy)

# Create a dict of x- and y-coords for extreme values using the found indices 
extreme_dict = utils.arrays_todict(xx[idx_extr], yy[idx_extr])

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(10, 7))

# Plot original line graph (entire graph)
ax.plot(x, y)

# Annotate peaks inside the defined interval
plotting.annotate_points(extreme_dict, ax, color='green', size=10)

plt.show()


