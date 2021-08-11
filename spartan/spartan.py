
import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

plt.style.use('default') # force matplotlib default for consistency in Jupyter

SPARTAN_PALETTES = dict(

                    base4 = ['#18453a', '#cc5a29', '#004372', '#6e005f'],
                    base6 = ['#18453a', '#cc5a29', '#00465e', '#ae1949', '#003b7c', '#6e005f'],
                    base8 = ['#18453a', '#cc5a29', '#004654' ,'#bc2e3f', '#004372', '#9c0252', '#23347c', '#6e005f'],
                    base10 = ['#18453a','#cc5a29','#00474d', '#c2393a', '#004567', '#ae1949', '#003f7a', '#920056',
                              '#382f79', '#6e005f'],
    
                    soft4 = ["#69bf77", "#6986bf", "#bf69b1", "#bfa369"],
                    soft6 = ["#69bf77", "#69b1bf", "#7769bf", "#bf69b1", "#bf7869", "#b1bf69"],
                    soft8 = ["#69bf77", "#69bfb8", "#6986bf", "#8d69bf", "#bf69b1", "#bf6970", "#bfa369", "#9bbf69"],
                    soft10 = ["#69bf77", "#69bfab", "#69a0bf", "#696cbf", "#9a69bf", "#bf69b1", "#bf697d", "#bf8969",
                              "#bfbc69", "#8ebf69"],

                    earth4 = ["#5b8c63", "#5b6c8c", "#8c5b84", "#8c7c5b"],
                    earth6 = ["#5b8c63", "#5b848c", "#635b8c", "#8c5b84", "#8c635b", "#848c5b"],
                    earth8 = ["#5b8c63", "#5b8c88", "#5b6c8c", "#705b8c", "#8c5b84", "#8c5b5f", "#8c7c5b", "#788c5b"],
                    earth10 = ["#5b8c63", "#5b8c81", "#5b7a8c", "#5b5d8c", "#7a5b8c", "#8c5b84", "#8c5b67", "#8c6d5b",
                               "#8c8b5b", "#708c5b"],

                    vivid4 = ["#22e643", "#2263e6", "#e622c5", "#e6a422"],
                    vivid6 = ["#22e643", "#22c5e6", "#4322e6", "#e622c5", "#e64322", "#c5e622"],
                    vivid8 = ["#22e643", "#22e6d6", "#2263e6", "#7422e6", "#e622c5", "#e62232", "#e6a422", "#94e622"],
                    vivid10 = ["#22e643", "#22e6b8", "#229ee6", "#2229e6", "#9122e6", "#e622c5", "#e62250", "#e66a22",
                               "#e6df22", "#77e622"],

                    neutral4 = ["#adccb3", "#adb8cc", "#ccadc7", "#ccc2ad"],
                    neutral6 = ["#adccb3", "#adc7cc", "#b3adcc", "#ccadc7", "#ccb3ad", "#c7ccad"],
                    neutral8 = ["#adccb3", "#adccc9", "#adb8cc", "#baadcc", "#ccadc7", "#ccadb0", "#ccc2ad", "#bfccad"],
                    neutral10 = ["#adccb3", "#adccc5", "#adc1cc", "#adaecc", "#bfadcc", "#ccadc7", "#ccadb5", "#ccb9ad",
                                 "#cccbad", "#bbccad"],

                    pastel4 = ["#b8e6bf", "#b8c7e6", "#e6b8de", "#e6d6b8"],
                    pastel6 = ["#b8e6bf", "#b8dee6", "#bfb8e6", "#e6b8de", "#e6bfb8", "#dee6b8"],
                    pastel8 = ["#b8e6bf", "#b8e6e2", "#b8c7e6", "#cbb8e6", "#e6b8de", "#e6b8bb", "#e6d6b8", "#d2e6b8"],
                    pastel10 = ["#b8e6bf", "#b8e6db", "#b8d5e6", "#b8b9e6", "#d2b8e6", "#e6b8de", "#e6b8c2", "#e6c8b8",
                                "#e6e4b8", "#cbe6b8"],        

                    cool4 = ["#338076", "#007188", "#005d90", "#4b4080"],
                    cool6 = ["#338076", "#007881", "#006d8b", "#006190", "#22528d", "#4b4080"],
                    cool8 = ["#338076", "#067a7d", "#007385", "#006c8c", "#006390", "#005990", "#304d8b", "#4b4080"],
                    cool10 = ["#338076", "#157c7c", "#007782", "#007188", "#006b8c", "#006490", "#005d90", "#1b548e",
                              "#374b89", "#4b4080"],

                    warm4 = ["#ccb129", "#dd7631", "#cd3d52", "#991f70"],
                    warm6 = ["#ccb129", "#da8e27", "#dc6a37", "#d3474b", "#bc2b5f", "#991f70"],
                    warm8 = ["#ccb129", "#d79825", "#dc7e2d", "#dc653a", "#d54c48", "#c73657", "#b32564", "#991f70"],
                    warm10 = ["#ccb129", "#d59e24", "#db8a28", "#dd7631", "#db623b", "#d64f47", "#cd3d52", "#bf2e5d", 
                              "#ae2367", "#991f70"],

                    blue_gradient4 = ["#82b8d9", "#3487c9", "#0053b2", "#16168c"],
                    blue_gradient6 = ["#82b8d9", "#539bd0", "#237dc5", "#005eb8", "#003ea5", "#16168c"],
                    blue_gradient8 = ["#82b8d9", "#61a3d2", "#3f8ecc", "#1a79c4", "#0063ba", "#004cae", "#00349e", "#16168c"],
                    blue_gradient10 = ["#82b8d9", "#68a8d4", "#4e98cf", "#3487c9", "#1576c3", "#0065bb", "#0053b2",
                                       "#0041a7", "#002e9b", "#16168c"],

                    green_gradient4 = ["#ace6b6", "#75ad8c", "#447763", "#18453a"],
                    green_gradient6 = ["#ace6b6", "#8ac49d", "#6aa284", "#4d826b", "#326352", "#18453a"],
                    green_gradient8 = ["#ace6b6", "#93cda4", "#7cb592", "#669e80", "#51866e", "#3d705d", "#2a5a4b", "#18453a"],
                    green_gradient10 = ["#ace6b6", "#99d3a8", "#86c09a", "#75ad8c", "#649b7e", "#538970", "#447763",
                                        "#356655", "#265547", "#18453a"],

                    MAC4 = ["#18453a", "#395a28", "#7a6505", "#cc5a29"],
                    MAC6 = ["#18453a", "#265332", "#445e21", "#6b640b", "#9a6406", "#cc5a29"],
                    MAC8 = ["#18453a", "#204f35", "#31582c", "#495f1e", "#65640e", "#866503", "#a8620e", "#cc5a29"],
                    MAC10 = ["#18453a", "#1d4d37", "#295431", "#395a28", "#4c5f1d", "#626310", "#7a6505", "#956404",
                             "#b06114", "#cc5a29"],

                    clay4 = ["#cc9600", "#e1593f", "#c43175", "#703d99"],
                    clay6 = ["#cc9600", "#de7229", "#e04e4b", "#ce356b", "#a93287", "#703d99"],
                    clay8 = ["#cc9600", "#db7c1e", "#e16237", "#de494f", "#d23767", "#bb317c", "#9b358e", "#703d99"],
                    clay10 = ["#cc9600", "#d88218", "#df6e2c", "#e1593f", "#dd4752", "#d43964", "#c43175", "#ae3285",
                              "#923791", "#703d99"],


                    # gray based palettes

                    cyan_gray = ["#26b2bf", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", 
                                 "#b3b3b3", "#b3b3b3", "#b3b3b3"],

                    green_gray = ["#26bf66", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", 
                                 "#b3b3b3", "#b3b3b3", "#b3b3b3"],

                    blue_gray = ["#2633bf", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", 
                                 "#b3b3b3", "#b3b3b3", "#b3b3b3"],

                    red_gray = ["#bf2626", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", 
                                 "#b3b3b3", "#b3b3b3", "#b3b3b3"],

                    purple_gray = ["#7f26bf", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", 
                                 "#b3b3b3", "#b3b3b3", "#b3b3b3"],

                    orange_gray = ["#f28b24", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", "#b3b3b3", 
                                 "#b3b3b3", "#b3b3b3", "#b3b3b3"],

                    # graydients

                        # fine

                    cyan_graydient_fine = ["#26b2bf", "#4d4d4d", "#595959", "#666666", "#737373", "#808080", "#8c8c8c", 
                                           "#999999", "#a6a6a6", "#b3b3b3", "#bfbfbf", "#cccccc"],

                    green_graydient_fine = ["#26bf66", "#4d4d4d", "#595959", "#666666", "#737373", "#808080", "#8c8c8c", 
                                           "#999999", "#a6a6a6", "#b3b3b3", "#bfbfbf", "#cccccc"],

                    blue_graydient_fine = ["#2633bf", "#4d4d4d", "#595959", "#666666", "#737373", "#808080", "#8c8c8c", 
                                           "#999999", "#a6a6a6", "#b3b3b3", "#bfbfbf", "#cccccc"],

                    red_graydient_fine = ["#bf2626", "#4d4d4d", "#595959", "#666666", "#737373", "#808080", "#8c8c8c", 
                                           "#999999", "#a6a6a6", "#b3b3b3", "#bfbfbf", "#cccccc"],

                    purple_graydient_fine = ["#7f26bf", "#4d4d4d", "#595959", "#666666", "#737373", "#808080", "#8c8c8c", 
                                           "#999999", "#a6a6a6", "#b3b3b3", "#bfbfbf", "#cccccc"],

                    orange_graydient_fine = ["#f28b24", "#4d4d4d", "#595959", "#666666", "#737373", "#808080", "#8c8c8c", 
                                           "#999999", "#a6a6a6", "#b3b3b3", "#bfbfbf", "#cccccc"],

                        # coarse

                    cyan_graydient_coarse = ["#26b2bf", "#4d4d4d", "#666666", "#808080", "#999999", "#b3b3b3", "#cccccc"],

                    green_graydient_coarse = ["#26bf66", "#4d4d4d", "#666666", "#808080", "#999999", "#b3b3b3", "#cccccc"],

                    blue_graydient_coarse = ["#2633bf", "#4d4d4d", "#666666", "#808080", "#999999", "#b3b3b3", "#cccccc"],

                    red_graydient_coarse = ["#bf2626", "#4d4d4d", "#666666", "#808080", "#999999", "#b3b3b3", "#cccccc"],

                    purple_graydient_coarse = ["#7f26bf", "#4d4d4d", "#666666", "#808080", "#999999", "#b3b3b3", "#cccccc"],

                    orange_graydient_coarse = ["#f28b24", "#4d4d4d", "#666666", "#808080", "#999999", "#b3b3b3", "#cccccc"]

)


def start():
    
    print("Setting default spartan style....")
    plt.style.use("../spartan.mplstyle")


def change(grid = "dont_change", labels = "dont_change", palette = "dont_change", context = "dont_change", reset = "dont_change"):
    '''Allow the user to customize the base style, including:
       * grids,
       * labels,
       * palettes,
       * contexts,
       * more coming soon...
       '''

    
    # RESET
    
    if reset != "dont_change":
        
        # user wants matplotlib defaults
        if reset == "mpl_default":
            plt.style.use('default')
    
        elif reset == "spartan_default":
            plt.style.use("../spartan.mplstyle")
    
    
    # GRIDS
    
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
    
    if labels != "dont_change":
        
        if labels == "darker":
            mpl.rcParams['xtick.color'] = '222222'
            mpl.rcParams['ytick.color'] = '222222'
            
        elif labels == "default":
            mpl.rcParams['xtick.color'] = '555555'
            mpl.rcParams['ytick.color'] = '555555'
            
            
    # PALETTES
    
    if palette != "dont_change":
            
        palette_keys = list(SPARTAN_PALETTES.keys())
        
        if palette in palette_keys:
            print("You want", palette, "and it exists!")
            colors_for_palette = SPARTAN_PALETTES[palette]
            print("The colors are:", colors_for_palette)
            mpl.rcParams['axes.prop_cycle'] = cycler(color = colors_for_palette)
        else:
            print("Try a different palette name; can't find that one.")
            
    
    # CONTEXTS

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
