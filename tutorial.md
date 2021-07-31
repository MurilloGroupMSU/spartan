____
# Tutorial
____

## Base Style

The simplest use of `spartan` is to instantiate it using

```import spartan as sp```.

This step customizes the default settings for `matplotlib`, which can then be used as usual. Changes to the style include:

* removal of unnecessary spines,
* a dim grid,
* a custom color palette,
* 16 point Arial font,
* fancy lengend,

and so on. This is implemented through the `spartan.mplstyle` file; all of the details can be found in that file. This may be most of what you need just to get a new look for your plots! 

In these example plots one sees the key differences. 


## Context Styles

Spartan's base style may be all that you need for most use cases. However, spartan has context styles to handle nuanced use cases that require small changes to the defaults. Spartan currently has five context styles for viewing on the screen, in a publication, at a poster presentation, during an online presentation and at an in-person talk. The context can be set when you initialize spartan using:
```python
sp.init_context("screen")
```


### Screen

The screen context applies when you have a high quality monitor and wish to examine the graphic in detail. Such a situation allows for less ink: thinner lines and smaller fonts. This context exploits the fact that our eyes are capable of easily resolving small details when needed, which allows us to minimize those details relative to the data in the graphic.

### Publication

### Poster

### Online Talk

Online talks are similar to viewing graphics on the screen; however, the quality of transmission is often poor and the viewing time is not controlled by the viewer. In this context, the font sizes and linewidths are increased.

### In Person Talk

Most projection systems have low resolution, poor color quality and lower contrast -- much less than your monitor. The in-person talk context accounts for these deficiencies with larger fonts, higher-contrast color palettes (with less reliance on green) and thicker lines. (If you are lucky enough to have access to a wide gamut HDR projector, consider using the screen context instead.)

___

