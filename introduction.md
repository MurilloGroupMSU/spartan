

[like this](https://seaborn.pydata.org/introduction.html)

# Introduction to spartan


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

Let's examine what changes spartan brings at this level. Following the philosophy of emphasizing the data and hiding the style, note that there are no spines (the box that surrounds the plot - see above), the fonts are not large, the supporting structure is some level of grey and there is a dim grid that you only notice if you need it.

## Customizations




## Exploring palettes
