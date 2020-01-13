

def annotate_points(points_to_annotate, ax, **kwargs):
    '''
    Annotate points with corresponding text.
    
    Parameters
    ----------
    points_to_annoate : dict
        Dictionary with desired annotation text as keys and the (x, y)-
        coordinates of the annotation as values.
    ax : matplotlib axis object
        Axis object on which to plot the annotations. 
    **kwargs : keyword arguments
        Arguments to be forwarded to the ax.annotate call.    
    '''
    
    # Loop through x- and y-coordinates of all points
    for text, (xp, yp) in points_to_annotate.items():

        # Annotate point
        ax.annotate(s=text, xy=(xp, yp), **kwargs)