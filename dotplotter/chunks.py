'''
functions for calculating which portion of a line is with the points (chunks)
thanks to Simon Shaw
    functions:
        get_gradient(x: tuple[float, float], y: tuple[float, float]) -> float
        get_y_intercept_from_coordinate(gradient: float, x: float, y: float) -> float
        get_height_at_position(position: float, y: float, gradient: float) -> float
        get_chunks_inside_area(x_pairs: list[tuple[int, int]], y_pairs: list[tuple[int, int]],
                           area_start: float, area_end: float,
                           ) -> tuple[list[tuple[float, float]], list[tuple[float, float]]]
'''

def get_gradient(x: tuple[float, float], y: tuple[float, float]) -> float:
    '''
    gets the gradient of a line between two coordinates
        arguments:
            x: the x values of both coordinates
            y: the y values of both coordinates
        returns: 
            gradient: the gradient of the line
    '''
    return (y[1] - y[0]) / (x[1] - x[0])


def get_y_intercept_from_coordinate(gradient: float, x: float, y: float) -> float:
    '''
    gets the y-vaule intercept of the line based on the gradient and the start coordinate
        arguments:
            gradient: gradient of the line (m)
            x: x-value of the coordiante
            y: y-value of the coordinate
        returns: y-intercept
    '''
    return y - x * gradient


def get_height_at_position(position: float, y: float, gradient: float) -> float:
    '''
    gets the y-vaule of a line at a certain x value
        arguments:
            position: x-value
            y: y-value
            gradient: grandient of the line
        returns: y-vaule of a line at a certain x value
    '''
    return gradient * position + y


def get_chunks(x_pairs: list[tuple[int, int]], y_pairs: list[tuple[int, int]],
                           area_start: float, area_end: float,
                           ) -> tuple[list[tuple[float, float]], list[tuple[float, float]]]:
    '''
    returns the coordinates of the origional line between two boundaries
        arguments:
            x_pairs: start and stop location of the x-axis hit,
            y_pairs: start and stop location of the y-axis hit,
            area_start: the upstream boundary
            area_end: the downstream boundary
        returns:
            new_x_pairs: the x values of the new line between the boundaries
            new_x_pairs: the y values of the new line between the boundaries
    '''
    assert len(x_pairs) == len(y_pairs)
    assert area_start < area_end
    new_x_pairs = []
    new_y_pairs = []
    for x, y in zip(x_pairs, y_pairs):
        assert x[0] < x[1]  # at least these need to be ordered, for y it's not important
        # outside the area completely
        if x[1] <= area_start or x[0] >= area_end:
            continue
        gradient = get_gradient(x, y)
        y_inter = get_y_intercept_from_coordinate(gradient, x[0], y[0])
        truncate_left = x[0] < area_start
        truncate_right = area_end < x[1]
        if truncate_left and truncate_right:
            new_x_pairs.append((area_start, area_end))
            new_y_pairs.append((get_height_at_position(area_start, y_inter, gradient),
                                get_height_at_position(area_end, y_inter, gradient)))
        elif truncate_left:
            new_x_pairs.append((area_start, x[1]))
            new_y_pairs.append((get_height_at_position(area_start, y_inter, gradient), y[1]))
        elif truncate_right:
            new_x_pairs.append((x[0], area_end))
            new_y_pairs.append((y[0], get_height_at_position(area_end, y_inter, gradient)))
        else:
            new_x_pairs.append(x)
            new_y_pairs.append(y)

    return new_x_pairs, new_y_pairs
    