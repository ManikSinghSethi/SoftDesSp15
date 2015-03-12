import numpy as np
import pygame
pygame.init()


import cv2
import numpy as np

#general functions
def avg(lis):
    """ average """
    return sum(lis)/len(lis)

def w_avg(lis, weights):
    """ weighted average """
    avg_w = avg(weights)
    w_lis = [lis[i] * weights[i] / avg_w for i in range(len(lis))]
    return avg(w_lis)

#openCv stuff
class Ball(object):
    def __init__(self, min_color, max_color):
        """
            initialize ball class by starting a video Capture
            and setting initial values
            Take in a min and max HSV type color
            for the ball's color threshold
        """
        self.min_color = min_color
        self.max_color = max_color
        self.cap = cv2.VideoCapture(0)
        ret, self.frame = self.cap.read()
        self.filterd = self.frame
        self.x = 0
        self.y = 500 #initialize y at 500 for 0 volume

    def filter(self):
        """
            Filter out the desired Colors
            Resets frame to a greyscale image
            with only black and the desired color
        """
        HSV = cv2.COLOR_BGR2HSV
        kernel = np.ones((15, 15), 'uint8')

        gray_image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY, 3) #convert to gray

        hsv_pic = cv2.cvtColor(self.frame, HSV) #convert to hsv
        inRange_pic = cv2.inRange(hsv_pic, self.min_color, self.max_color) #get purple
        eroded_pic = cv2.erode(inRange_pic, kernel)
        dilated_pic = cv2.dilate(eroded_pic, kernel)
        blured_pic = cv2.medianBlur(dilated_pic,5)
        #show gray_image in purple areas and black everywhere else
        self.filtered = cv2.bitwise_and(gray_image, gray_image, mask = blured_pic)

    def find_center(self):
        """
            Uses HoughCircles on the filtered frame to fit circles into the ball
            averages the center of the circles, weighted by their radii
            Sets self.x and self.y to the calculated position
        """
        circles = cv2.HoughCircles(self.filtered, cv2.cv.CV_HOUGH_GRADIENT, 1,
                                   20, param1=30,param2=15,minRadius=0,maxRadius=0)
        if circles == None:
            self.y = 500 #makes volume 0
        else:
            circles = np.uint16(np.around(circles))
            #get coordinates for all circles
            allx = [i[0] for i in circles[0,:]]
            ally = [i[1] for i in circles[0,:]]
            weights = [i[2] for i in circles[0,:]] #radii of circles
            #take weighted average
            self.x = w_avg(allx, weights)
            self.y = w_avg(ally, weights)

    def position(self):
        """ Finds the position of the ball """
        ret, self.frame = self.cap.read()
        self.filter()
        self.find_center()

    def print_pos(self):
        """
            For Testing -
                prints positon (x, y) of ball
        """
        print (self.x, self.y)

    def draw(self):
        """ draws frame with ball """
        np.set_printoptions(threshold=np.inf)
        cv2.imshow('frame', cv2.flip(self.filtered, 1))


class Note(object):
    def __init__(self):
        """ make filenames of notes into a list """
        self.sound = ["blues_note%02d.wav" % i for i in range(19)]

    #conversion functions
    def get_pitch(self, x):
        """ get pitch associated with ball's x """
        max_x = 600.
        min_note = 0
        note_range = 18
        scaled_x = 1 - x / max_x
        return int(min_note + (note_range * scaled_x))

    def get_vol(self, y):
        """ get volume associated with ball's y """
        max_y = 500.
        min_vol = 0
        vol_range = 1
        scaled_y = 1 - y / max_y
        return min_vol + (vol_range * scaled_y)

    def playanote(self, pitch, vol):
        """ play note with input pitch and volume """
        pygame.mixer.music.set_volume(vol) #adjusts volume to user input based on y position
        pygame.mixer.music.load(self.sound[pitch]) #plays pitch file based on user input for x position

        pygame.mixer.music.play()


if __name__ == "__main__":
    #purple
    min_HSV_color = (100, 0, 0)
    max_HSV_color = (150, 255, 255)


    ball = Ball(min_HSV_color, max_HSV_color)
    note = Note()

    while True:
        ball.position()
        pitch = note.get_pitch(ball.x)
        vol = note.get_vol(ball.y)
        note.playanote(pitch, vol)
        ball.draw()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break #kill if q is pressed


    #release Capture
    ball.cap.release()
    cv2.destroyAllWindows()