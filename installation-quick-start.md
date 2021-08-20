____
# Installation
____


Currently, spartan is available through PyPi:

```python
pip install spartan
```


____
# Quick Start
____

With spartan installed, you can import it with
```python
import spartan as sp
```
Although spartan has been loaded, you can continue to make default matplotlib plots until you are ready to swtich; to do that, use:
```python
sp.start()
```
This may be all that you need! For example, here is a simple plot done in matplotlib defaults and using only the import statement above.

* add two plots here

Note that spartan uses a lot less ink to convey the same information by highlighting the data and not the support structure.

Next, you may wish to customize your palette so that the color cycle of your plots matches your goals. Spartan provides many new palettes, which are described [here](palettes.md). This is how you see the available palettes
```python
sp.list_palettes()
```
and this is how you set a palette
```python
sp.change(palette = "MAC")
```

[Go back.](index.md)

