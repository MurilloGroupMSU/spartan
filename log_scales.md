# Logarithmic Scales

Nonlinear scales play an important role in compressing numerical data to mititgate extreme values from dominating the visualization. Logarithmic scales, or just "log scales" are the most common variant that allows us to see variations in the data at small values when there are very large values in the dataset. All plotting software comes with built-in log plots, including variants for each axes: linear-log, log-linear and log-log. Few things change from a visualization perspective other than:
* because the scale is less intutive, a grid or obvious ticks could be useful (but, not overwhelming the data),
* if possible, create the data uniformly on a log scale (e.g., use Numpy's `logspace` command).

