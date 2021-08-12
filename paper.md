---
title: 'spartan: potent visualizations'
tags:
  - Python
  - visualization
authors:
  - name: Michael S. Murillo
    orchid: XYZ-XYZ
    affiliation: 1
affiliations:
  - name: Department of Computational Mathematics, Science and Engineering, Michigan State University
    index: 1
date: 8 August 2021
bibliography: paper.bib
---


# Summary

Good visualization practices allow us to communicate powerful ideas quickly and efficiently. Spartan is a Python library, built on matplotlib, for creating visualizations based on modern practices such as those of Tufte and others. In its simplest use, Spartan provides for a parsimonious style that highlights the data while minimizing the design. Context variations for talks, posters, publications and posters are included. Spartan provides new color palettes that deepen diverse narratives. Users can build custom color palettes in lab space (for perceptual uniformity) or in rgb space. Plotting tools are provided for 1D plots, range frames, scatter plots with rug and KDE accents, sparklines, parallel plots and a new mixed linear-log plot. All tools are built as close to the matplotlib API as possible for a seamless integration into current workflows.



# Statement of need

Communicating through visualization is central to the scientific process [@Tukey]. The production of scientific graphs is now guided by rules and heuristics that increase the efficiency of communication while mitigating miscommunication. Tufte [@Tufte:2001], and many others [@Wilkinson:2005],[@Knaflic:2015],[@Knaflic:2020], have documented rules that increase our ability to communicate well. 


Some of the most important rules are:
* reduce non-data ink,
* allow the narrative/conclusion to guide color choices,
* choose graph types that don't mislead,

All of these issues increase in importance in the "Big Data" age. Python, through its matplotlib library [@Hunter], provides a powerful tool set for building custom visualizations. However, the average user may not be knowledgeable or have the time to code at a lower level that exposes matplotlib's most powerful capablities. This need has been addressed by libraries, such as seaborn [@Waskom:2021], that provide a higher-level interface to the user while providing extremely rich visualizations. However, none of these libraries directly incorporate many of the best practices into the base Matplotlib workflow. For example, the sparkline and range frame popularized by Tufte [cite] can be made in matplotlib with effort but is not part of the standard library. 




# Example

* standard mpl versus spartan for line plot with gradient palette



# Overview

* interface
* plot types
	* minimal
	* range frame
	* spark-line
	* rug
	* KDE
	* linlog
	* 1D
	* parallel
* palettes
* themes for use cases

# Citation Practice



* https://github.com/ahupp/etframes
* https://github.com/juanshishido/tufte
* Hunter, matplotlib
* Waskom, seaborn
* Tukey, EDA
* storytelling with data
* Tufte in R website


# References
