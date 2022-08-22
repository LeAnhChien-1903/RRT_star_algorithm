import cv2
import numpy as np
import os
import random
import math
import argparse

class Nodes:
    """Class to store the RRT graph"""
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.parent_x = []
        self.parent_y = []
class RRT_star:
    def __init__(self, image, start, goal):
        self.image = image
        self.grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        self.start = start
        self.goal = goal
    # return dist and angle between two point
    def dist_and_angle(self, x1, y1, x2, y2):
        dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        angle = math.atan2(y2-y1, x2-x1)
        return (dist, angle)
    # generate a random  point  in the image space
    def sample(self, h, l):
        new_y = random.randint(0, h)
        new_x = random.randint(0, l)

        return (new_x, new_y)