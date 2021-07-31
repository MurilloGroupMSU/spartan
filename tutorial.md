____
____
# Tutorial
____

## Base Style

The simplest use of `spartan` is to instantiate it using

```python
import spartan as sp```.

This step customizes the default settings for `matplotlib`, which can then be used as usual. Changes to the style include:

* removal of unnecessary spines,
* a dim grid,
* a custom color palette,
* 16 point Arial font,
* fancy legend,

and so on. This is implemented through the `spartan.mplstyle` file; all of the details can be found in that file. This may be most of what you need just to get a new look for your plots! 

In these example plots one sees the key differences. 

____
## Context Styles

Spartan's base style may be all that you need for most use cases. However, spartan has context styles to handle nuanced use cases that require small changes to the defaults. Spartan currently has five context styles for viewing on the screen, in a publication, at a poster presentation, during an online presentation and at an in-person talk. The context can be set when you initialize spartan using:
```python
sp.init_context("screen")
```


### Screen

The screen context applies when you have a high quality monitor and wish to examine the graphic in detail. Such a situation allows for less ink: thinner lines and smaller fonts. This context exploits the fact that our eyes are capable of easily resolving small details when needed, which allows us to minimize those details relative to the data in the graphic.

### Publication

Publications are often viewed on paper or on a screen, in principle allowing for smaller fonts, thinner lines and nuanced colors. However, many journals have specific requirements that include minimum font sizes, colors that can be viewed in black and white, varying linestyles and lack of a colored background. Spartan makes a conservative estimate for such use cases; each journal has its specific set of choices, of course, and you may need to tweak the defaults for a specific journal. 


### Poster

Posters are typically viewed from a wide range of distances and spartan uses the largest fonts sizes and linewidth for this context. 


### Online Talk

Online talks are similar to viewing graphics on the screen; however, the quality of transmission is often poor and the viewing time is not controlled by the viewer. In this context, the font sizes and linewidths are increased.

### In Person Talk

Most projection systems have low resolution, poor color quality and lower contrast -- much less than your monitor. The in-person talk context accounts for these deficiencies with larger fonts, higher-contrast color palettes (with less reliance on green) and thicker lines. (If you are lucky enough to have access to a wide gamut HDR projector, consider using the screen context instead.)


____
## Plot Types

Spartan currently supports seven plot types (not including plots you make using the basic spartan style and palettes). 

### Minimal

One of Tufte's principles is to maximize the ratio of data to ink, the so-called data-ink ratio. Spartan's basic style captures most of this spirit, whereas the minimal plot types removes all axes and grids as well.


### Scatter

Minimal scatter plots are also available with options for rug or kde along the axes, and/or with a range frame.

### Range Frame

Range frames are similar to minimal plots but inlude partial frames that indicate the range of the data. See Tufte [Tufte] page 130. Options are available for both line and scatter plots.


### 1D Plots

1D plots are used when you have a set of numbers and you wish to see how they are distributed.


### Mixolinian

It is often the case that our data varies over many orders of magnitude and, for these cases, we employ log plots. While convenient, log plots can distort the data with values very close to zero. In fact, often our data has both zero values and we desire a log scale. Worse, often our data has negative values as the data range passes from positive values through zero. Numpy and Matplotlib partially rescue us with [logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html), creating a uniform grid on our log plot, and [symlog](https://matplotlib.org/3.1.0/gallery/scales/symlog_demo.html), which allows us to have both positive and negative log scales. Values close to zero remain an issue. Spartan provides a plot type that mixes linear with logarithmic by employing a linear scale around zero, thereby not distorting smalle values and allowing for values close to or equal to zero; outside of this linear region, the scale is logarithmic. 


### Sparklines

Spartan provides sparklines, which are typically very small line plots without axes or the usual labels. (This is more minimal than the minimal plot.) Spartan's sparklines can be used with no labels, with the minimum, maximum and final values labeled, with a zero value line or with a band reflecting the mean and variance.


### Parallel Plot

Data most often lives in dimensions higher than 1D, minimal and scatter plots can handle. Spartan provides parallel plots for these cases. The minimal style and options are borrowed from the minimal and range frame styles.

___

