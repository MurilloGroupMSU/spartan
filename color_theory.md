____
# Color Theory for Spartan
____

This page summarizes some of the important aspects of color theory that are used to create color palettes in spartan. Much of this information can be found in other parts of the documentation, but this discussion is for the color nerds, those people who wish to dive a little bit more deeply into colors. 

To make the ideas concrete and applicable to your work, I'll consider the specific problem of creating a color palette. That is, imagine you wish to have a sequence of colors that starts at given color, ends at a given color and has $N-2$ colors in between; this defines the color cycle, which would then repeat if sampled more than $N$ times.

___
### User Facing RGB 

The first issue we have to deal with is how we specify the initial and final colors. There are many ways to do this, as we will see, but spartan (currently) makes the choice that the user (you!) will know your colors in the RGB color space. This space is fairly intuitive and common - we are typically taught to think this way in school and many of our electronic devices are specified this way. There are three common ways to make this specification:

1. The R, G, and B values are given in the range [0,1], where the value is a float (real number). 
2. Sometimes RGB values are given in percentages, as in (54%, 17%, 65%), rather than floats.
3. The R, G and B values are given by integers in the range [0, 255], a binary format that uses 8 bits (1 byte).  (You can get the first specification by dividing by 255.)
4. The RGB values are given as a hexadecimal number, usually denoted with a # in front of it, as in #ff12e1. Each pair of digits is the value from the second specification. In this example, #ff = 255, #12 = 18, #e1 = 225. 

Let's look at some examples... [1D plot of points....]

These are all equivalent and spartan assumes (for now) that you are working with specification 2. Internally, spartan makes various conversions as needed, but the user does not necessarily need to know these transformations. For example, if you use a spartan palette or make your own, you specify three RGB values in the range [0, 255] and spartan makes a list of hexadecimal values because that is what matplotlib uses. And, there is more.

Before we get to that, let's stick with color palettes built directly from user specified RGB. A new palette can be obtained by interpolating the numerical values from the two the user specified as the end points. Suppose you want to start with red and end with blue: you would specify RGB1 = (255, 0, 0) and RGB2 = (0, 0, 255). Then, given that you want a color cycle of length $N$, you can linearly interpolate each color channel; in this case, you would form three lines from $255 \to 0$, $0 \to 0$ (trivial for this example!) and $0 \to 255$.  

Let's look at some examples.... [more 1D plots...]


___
### Spartan's Custom Palettes and the HSB/HSV Color Space 

Many of the palettes in spartan were obtained by....

![HSV](HSV_color_solid_cylinder_saturation_gray.png)

____
### CIEXYZ and CIELAB Color Spaces

For almost all uses, the linear interpolation method works just fine. Chose your colors to have some meanings and you get a nicely spaced range of colors in between. The problem arises when you need to exert additional control over the colors in your bespoke palette. Are the colors generated kind to color blind people? Do they print well in black and white? And, so on. One of the most important issues is psychological: what colors does the brain see as "popping out", being "more important"? Related, are there colors in your palette that blend with the background because they are too light? In this important use case we need to take into account not how the eye works, but how the brain works. 


The XYZ color space is designed to isolate the luminance of a color from its chromaticity. The luminance is given by the Y value and thus the chromaticity is specified by the X and Z values.

____
### Creating Palettes

There are many ways to create palettes and many types of palettes you will want to create. 

Consider a situation in which you know the first and last color in the color cycle and the intermediate colors should transition smoothly between them. An example use case is having a single color that transitions from light to dark to put increasing emphasis on subsequent lines or points. Similarly, we may transition from gray to red. Another example is when there is a physical meaning to the color, such as a transition from hot to cold. 
