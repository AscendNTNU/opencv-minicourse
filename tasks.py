import numpy as np
import cv2

def task1():
    """
    Load an image and show it to the screen!
    Image file: images/brick-wall.jpg

    Useful OpenCV functions:
        - imread
        - imshow
        - waitKey
    """

    # TODO: Implement

    """
    What if you want to load it in grayscale?
    """

    """
    What is the shape of the image? What does shape mean?
    """

def task2():
    """
    OpenCV uses BGR coloring. 
    However, the file images/jungle.jpg is saved as RGB! Can you display it normally?
    
    Useful OpenCV functions:
        - cvtColor

    Hint: Try to view the image normally. What is wrong?
    """
    # TODO: Implement

def task3():
    """
    The image images/jungle.jpg contains a lot of green. 
    However, there are a lot of impostors among the beautiful green colors.
    Can you mask out only the truly green colors in the image?
    For an example you can look at ./sample-solutions/jungle-green-example.png

    Useful OpenCV functions:
        - cvtColor
        - inRange
        - bitwise_and

    Hint  : Look up HSV color space
    Hint 2: https://docs.opencv.org/4.9.0/df/d9d/tutorial_py_colorspaces.html

    """
    # TODO: Implement

def task4():
    """
    The image ./images/fruit.jpg contains a lot of irrelevant fruits.
    Can you produce a cropped version containing only the lemon?

    For an example you can look at ./sample-solutions/lemon.png

    Useful functions:
        array slicing
    """
    # TODO: Implement

    """
    Could we have automatically calculated the crop region?
    """

def task5():
    """
    The file ./images/mysterious_animal.bin contains an image buffer representing some animal. 
    Can you recover the image and find out what animal it is?

    About the data:
        The pixel values are represented using uint8
        The format is BGR8. That is, each pixel is represented using three bytes, Blue, Green, Red.
        Width: 2048
        Height: 1366
        The files contains the raw pixel data only. No metadata is stored in the file.
        The axis order is Height x Width x Channel (HWC)

    Useful functions:
        open()
        np.frombuffer
        np.reshape
    """
    # TODO: Implement

def task6():
    """
    ./images/city.jpg contains some straight edges. 
    Can you apply a filter to detect the edges? 
    What if we want the really crisp ones?

    Note: you can decide how far you want to go with it. Look at
    - ./sample-solutions/edges-basic.png
    - ./sample-solutions/edges-crisp.png

    Useful functions:
        cv2.Sobel
        cv2.convertScaleAbs
        cv2.addWeighted
        cv2.GaussianBlur

    More or less useful:
        cv2.threshold
        cv2.connectedComponentsWithStats

    Hint: https://docs.opencv.org/4.9.0/d2/d2c/tutorial_sobel_derivatives.html

    What happens with different kernel sizes?

    """
    # TODO: Implement

def task7():
    """
    HARDER!

    Roger Federer is about to hit a tennis ball in ./images/tennis.jpg
    Can you detect the ball and draw a rectangle around it?
    - Note: no machine learning is required.

    Sample output is in ./sample-solutions/tennis-detected.jpg

    Useful functions:
        Functions from task3
        np.argmax
        ndarray.nonzero() (image.nonzero)
        np.min, np.max
        cv2.rectangle
    """
    # TODO: Implement

def task8():
    """
    'Optional'
    Implement all the previous tasks in C++.
    """

if __name__ == "__main__":
    for func in [
        task1,
        task2,
        task3,
        task4,
        task5,
        task6,
        task7
    ]:
        print(f"Running task: {func.__name__}")
        func()
