# Logarithmic Scales

Nonlinear scales play an important role in compressing numerical data to mititgate extreme values from dominating the visualization. Logarithmic scales, or just "log scales" are the most common variant that allows us to see variations in the data at small values when there are very large values in the dataset. All plotting software comes with built-in log plots, including variants for each axes: linear-log, log-linear and log-log. Few things change from a visualization perspective other than:
* because the scale is less intutive, a grid or obvious ticks could be useful (but, not overwhelming the data),
* if possible, create the data uniformly on a log scale (e.g., use Numpy's `logspace` command).

It is often said that the problem with log scales is that you can't use them with negative numbers because the logarithm of zero is infinite and what does the log of a negative number mean? Strictly speaking, this is true. However, nothing prevents us from simply taking the absolute value of our data so that everything is positive. This flips the negative portion up into the postive and we only need to keep track of which parts of the graph have been flipped. But, we can do beetter than that by using the absolute value but still plotting the data on the negative axis, which is much easier to interpret. So, in fact, making log plots with negative values in the data is fairly easy.

A problem arises, however, when the data literally goes through zero; you may literally have values of zero in your data. To handle this situation, we can make the axis linear very close to zero and logarithmic everywhere else. In fact, this capability already exists in matplotlib through its `symlog` capability. The challenge is only that we need to develop and understand the nonlinear transformation, and this is not unique; spartan provides three options, each of which is documented here. 

Before we discuss the three plot types, let's first understand the mathematics behind the transformations used. The first plot type mixes linear with logarithmic in a very literal way, and this is referred to as the mixolinean log plot (mixo is Greek for "mixed"). A portion of the axis, which can be either or both of the axes, is strictly linear. This allows the data to be represented without distortion for small values near zero, while still retaining the larger values on a log scale outside of that user-defined region. Why would you use this? As an example, consider how two atoms interact - we often assume the energy of that interaction as a function of the separation _r_ between the atoms goes like 1/r^12  - 1/r^6. This function tends to infinity as _r_ becomes very small, but has interesting and import structure near _r=1_. We could like to see that structure without simply chopping off the larger values we care a bit less about. The mixolean log does not need a mathematical transformation because the rule is very simple: linear in this range, and log outside of that. 

What if we don't care about being strictly linear around zero and we don't want the discontinuity that arise at the linear-to-log boundary? Let's first review how normal log scales work. 

_T(x) = log(x)_

### Mixolinean Log

_T(x) = x,      |x| < C_
_T(x) = log(x), |x| > C_

### Symlog

The symlog capability mirrors what is currently in matplotlib, with three goals:
* provide the spartan style to this plot type,
* document the transformation that it uses, which has been the [source of some confusion](https://stackoverflow.com/questions/39988048/what-is-the-origin-of-matplotlibs-symlog-a-k-a-symmetrical-log-scale),
* and, allow this algorithm to be easily compared with the other two option. 

### Cinch

_T(x) = sinh^{-1}(x)_
