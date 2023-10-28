from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
# import matplotlib.font_manager
# [f.name for f in matplotlib.font_manager.fontManager.ttflist]


size=6

params = {'font.family': 'DejaVu Sans',
          'legend.fontsize': size,
          'legend.handlelength': 2,
          'figure.figsize': (20,8),
          'axes.labelsize': size,
          'axes.titlesize': size,
          'xtick.labelsize': size*0.75,
          'ytick.labelsize': size*0.75,
          'axes.titlepad': 25,
          'figure.dpi': 300
         }

cdict = {'red':((0.0,0.125,0.125),
                (0.5,0.0,0.0),
                (1.0,0.957,0.957)),
        'green':((0.0,0.713,0.713),
                (0.5,0.0,0.0),
                (1.0,0.918,0.918)),
        'blue': ((0.0,0.886,0.886),
                (0.5,0.0,0.0),
                (1.0,0.094,0.094))}
blue_yellow = LinearSegmentedColormap('BlueYellow',cdict)
blue_yellow.set_bad((.9, .9, .9, 1.0))

plt.register_cmap(cmap=blue_yellow)
plt.rcParams.update(params)
