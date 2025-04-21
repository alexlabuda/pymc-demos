import matplotlib.pyplot as plt

def apply_minimal_style():
    """
    Apply a minimal ggplot2-like style to matplotlib plots.
    This style features a clean white background with minimal chart elements.
    """
    # Start with seaborn whitegrid as a base
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # Define custom style parameters for a minimal look
    minimal_style = {
        # Figure
        'figure.facecolor': 'white',
        'figure.figsize': (10, 6),
        
        # Axes
        'axes.facecolor': 'white',
        'axes.grid': True,
        'axes.axisbelow': True,
        'axes.edgecolor': '#DDDDDD',
        'axes.linewidth': 0.8,
        'axes.titlesize': 14,
        'axes.labelsize': 12,
        'axes.spines.top': False,
        'axes.spines.right': False,
        
        # Grid
        'grid.color': '#DDDDDD',
        'grid.linestyle': '-',
        'grid.linewidth': 0.8,
        
        # Ticks
        'xtick.color': '#666666',
        'ytick.color': '#666666',
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'xtick.direction': 'out',
        'ytick.direction': 'out',
        
        # Lines and markers
        'lines.linewidth': 1.8,
        'lines.markersize': 6,
        'scatter.marker': 'o',
        'scatter.edgecolors': 'none',
        
        # Legend
        'legend.frameon': False,
        'legend.fontsize': 10
    }
    
    # Apply our custom style
    plt.rcParams.update(minimal_style)
    
    return "Minimal ggplot2-like style applied successfully!" 