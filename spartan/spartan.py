
import matplotlib as mpl
import matplotlib.pyplot as plt


def init():
    
    print("Setting default spartan style....")
    plt.style.use("../spartan.mplstyle")


def change(grid = "dont_change", labels = "dont_change", palette = "dont_change", context = "dont_change"):
    '''Allow the user to customize the base style, including:
       * grids,
       * labels,
       * palettes,
       * contexts,
       * more coming soon...
       '''
    
    # GRIDS
    
    print("Your grid is now set to:", grid)
    
    if grid != "dont_change":
        
        if grid == "vertical":
            mpl.rcParams['axes.grid.axis'] = 'x'
            
        elif grid == "horizontal":
            mpl.rcParams['axes.grid.axis'] = 'y'
            
        elif grid == "darker":
            mpl.rcParams['grid.linewidth'] = 0.9
            mpl.rcParams['grid.alpha'] = 0.9
            mpl.rcParams['grid.color'] = '#cccccc'
            mpl.rcParams['xtick.bottom'] = True
            mpl.rcParams['ytick.left'] = True
            
        elif grid == "default":
            mpl.rcParams['axes.grid.axis'] = 'both'
            mpl.rcParams['xtick.bottom'] = False
            mpl.rcParams['ytick.left'] = False

            
    # LABELS
    
    print("Your labels are now set to:", labels)
    
    if labels != "dont_change":
        
        if labels == "darker":
            mpl.rcParams['xtick.color'] = '222222'
            mpl.rcParams['ytick.color'] = '222222'
            
        elif labels == "default":
            mpl.rcParams['xtick.color'] = '555555'
            mpl.rcParams['ytick.color'] = '555555'
            
            
    # PALETTES
    
    
    # CONTEXTS
    
    print("Your context is now set to:", context)

    if context != "dont_change":
        if context == "poster":
            mpl.rcParams['xtick.labelsize'] = 24
            mpl.rcParams['ytick.labelsize'] = 24
            mpl.rcParams['grid.color'] = '#888888'
            mpl.rcParams['lines.linewidth'] = 3.8

        elif context == "projection":
            mpl.rcParams['xtick.labelsize'] = 20
            mpl.rcParams['ytick.labelsize'] = 20
            mpl.rcParams['lines.linewidth'] = 3.0

        elif context == "monitor":
            mpl.rcParams['xtick.labelsize'] = 12
            mpl.rcParams['ytick.labelsize'] = 12
            mpl.rcParams['lines.linewidth'] = 2.2

        elif context == "web_meeting":
            mpl.rcParams['xtick.labelsize'] = 16
            mpl.rcParams['ytick.labelsize'] = 16
            mpl.rcParams['lines.linewidth'] = 2.8

        elif context == "publication":
            mpl.rcParams['xtick.labelsize'] = 14
            mpl.rcParams['ytick.labelsize'] = 14
            mpl.rcParams['lines.linewidth'] = 2.0
            
        elif context == "default":
            mpl.rcParams['xtick.labelsize'] = 10
            mpl.rcParams['ytick.labelsize'] = 10
            mpl.rcParams['lines.linewidth'] = 2.2
