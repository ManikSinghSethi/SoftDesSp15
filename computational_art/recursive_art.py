""" TODO: Put your header comment here """

import random
<<<<<<< HEAD
from math import cos, sin, pi
=======
>>>>>>> 68b2965c9c5fa90bd2433f3b7f672e6b29c1bbbb
from PIL import Image


def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
    """
<<<<<<< HEAD

    randdepth = random.randint(min_depth, max_depth)
    fn = randmaker(randdepth)
    return fn


def randmaker(depth):

    if depth == 1:
        randxy = random.randint(0,1)
        return ["x", "y"][randxy]

    else:
        randnumber = random.randint(1,6)

        if randnumber ==  1:
            # prod = a*b
            return ["prod", randmaker(depth-1), randmaker(depth-1)]

        elif randnumber ==  2:
            # avg = 0.5*(a+b)
            return ["avg", randmaker(depth-1), randmaker(depth-1)]

        elif randnumber ==  3:
            # cospi = cos(pi*a)
            return ["cospi", randmaker(depth-1)] 

        elif randnumber ==  4:
            # sinpi = sin(pi*a)
            return ["sinpi", randmaker(depth-1)]

        elif randnumber ==  5:
            return ["cube", randmaker(depth-1)] 

        elif randnumber ==  6:
            return ["ex", randmaker(depth-1)]  
    
    # TODO: implement this
    # pass
=======
    # TODO: implement this
    pass

>>>>>>> 68b2965c9c5fa90bd2433f3b7f672e6b29c1bbbb

def evaluate_random_function(f, x, y):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02
    """
<<<<<<< HEAD

    if f[0] == "x":
        return x
    elif f[0] == "y":
        return y
    elif f[0] == "prod":
        return evaluate_random_function(f[1], x, y)*evaluate_random_function(f[2], x, y)
    elif f[0] == "avg":
        return (evaluate_random_function(f[1], x, y)+evaluate_random_function(f[2], x, y))*0.5
    elif f[0] == "cospi":
        return cos(pi*evaluate_random_function(f[1], x, y))
    elif f[0] == "sinpi":
        return sin(pi*evaluate_random_function(f[1], x, y)) 
    elif f[0] == "cube":
        return (evaluate_random_function(f[1], x, y))**3
    elif f[0] == "ex":
        return abs(evaluate_random_function(f[1], x, y))**0.5
=======
    # TODO: implement this
    pass
>>>>>>> 68b2965c9c5fa90bd2433f3b7f672e6b29c1bbbb


def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
<<<<<<< HEAD
    # val = (output_interval_end-output_interval_start)/(input_interval_end-input_interval_start)
    val = float(val - input_interval_start)/(input_interval_end - input_interval_start)*(output_interval_end-output_interval_start)+output_interval_start

    # (input_interval_end - val)/(input_interval_start - input_interval_end)*(output_interval_start + output_interval_end)
    # return output_interval_start+float((output_interval_end-output_interval_start))/(input_interval_end-input_interval_start)*(val-input_interval_start)
    return val
    # TODO: implement this
    # pass
=======
    # TODO: implement this
    pass
>>>>>>> 68b2965c9c5fa90bd2433f3b7f672e6b29c1bbbb


def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """ Generate test image with random pixels and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


def generate_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
<<<<<<< HEAD
    red_function = build_random_function(10, 12)
    green_function = build_random_function(9, 12)
    blue_function = build_random_function(10, 12)
    print red_function
    print green_function
    print blue_function
=======
    red_function = ["x"]
    green_function = ["y"]
    blue_function = ["x"]
>>>>>>> 68b2965c9c5fa90bd2433f3b7f672e6b29c1bbbb

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(evaluate_random_function(red_function, x, y)),
                    color_map(evaluate_random_function(green_function, x, y)),
                    color_map(evaluate_random_function(blue_function, x, y))
                    )

    im.save(filename)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #       implement remap_interval and evaluate_random_function
<<<<<<< HEAD
    generate_art("myart.png")

    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
    # test_image("noise.png")
=======
    #generate_art("myart.png")

    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
    test_image("noise.png")
>>>>>>> 68b2965c9c5fa90bd2433f3b7f672e6b29c1bbbb
