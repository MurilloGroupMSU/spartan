
# Introduction to spartan


The first few sections below describe spartan capabilities provided through matplotlib customizations. This means that you are able to use matplotlib just as you always have once youe have used spartan's customizations. When we get to the sections on plots, spartan provides new plots types not part of matplotlib.


## Basic style

Let's begin by comparing with `matplotlib`:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 12, 100)

for c in range(8):
  y = np.sin(x*np.sqrt(c))
  plt.plot(x, y)
```

Next, let's compare with `spartan`:

```python
import numpy as np
import matplotlib.pyplot as plt

# this time import spartan
import spartan as sp
# you need to start spartan first
sp.start()

x = np.linspace(0, 12, 100)

for c in range(8):
  y = np.sin(x*np.sqrt(c))
  plt.plot(x, y)
```

Let's examine what changes spartan brings at this level. Following the philosophy of emphasizing the data and hiding the style, note that there are no spines (the box that surrounds the plot - see above), the fonts are not large, the supporting structure is some level of grey and there is a dim grid that you only notice if you need it. The data is the focus.


## Contexts

Perhaps for your everyday work, that is all you need. For scientific work however, you will find your self in several settings:

* working long hours in front of the monitor that is sitting motionless with a high resolution a fixed distance from your eyes,
* you are giving a Zoom talk in which the quality of transmission is less certain and the viewer needs to grasp the plots more quickly,
* we return to giving presentations in person and our audience is spread across many distances in the large, very crowded room,
* you didn't get the invited talk this time, but you have a poster that is surrounded by people reading from a large range of distances,
* it's all done and you need a high quality visualization that your journal will accept.

Let's re-examine the plots above in each of these contexts. 

#### screen
```python
import spartan as sp
```

#### online presentation
```python
import spartan as sp
```

#### in person presentation
```python
import spartan as sp
```

#### poster
```python
import spartan as sp
```

#### publication
```python
import spartan as sp
```






## Other Customizations

The spartan style is motivated by the minimalist school that minimizes clutter, color and other chartjunk that competes with your data. This style is most often associated with [Tufte](https://en.wikipedia.org/wiki/Edward_Tufte), but you can find such guidance from most sources these days. That doesn't mean that all plots need to look the same - far from it.  Let's look at some common use cases.

Suppose that the story we wish to tell heavily relies on quantitative comparisons. We really need the grids in this case. Here is how spartan handles that case:

```python
import spartan as sp
```

Another use case is that the abscissa (x axis) is very obvious and the focus of the story is the ordinate (y axis). For example, we have something important and detailed varying over time. In this case, we can remove the useless "vertical ink" from the plot to obtain:

```python
import spartan as sp
```

Conversely, your story focus on exactly when something happened, not how much happened. In this case, we can remove the useless "horizontal ink" from the plot to obtain:

```python
import spartan as sp
```


## Exploring palettes

Once we have taken control of the ink levels in our plots, we can focus on the data. The story your data conveys will highly depend on how you use color. 

[Go back.](index.md)

