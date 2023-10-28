import PyComplexHeatmap as ch


def plot_heatmap(data,ax,leg=True,vmin=-.4, vmax=.4):
    plot_cm = ch.ClusterMapPlotter(
        data,
        col_dendrogram=True,
        row_dendrogram=True,
        # left_annotation=col_ha,
        vmin=vmin, vmax=vmax,
        # center = 0,
        # rasterized=True, 
        cmap = 'BlueYellow',
        verbose=False,
        legend=leg,legend_gap=1,
        plot=False
        # show_rownames=True,show_colnames=True
    )
    plot_cm.plot(ax=ax)
    plot_cm.plot_legends(ax=ax)

    return ax
