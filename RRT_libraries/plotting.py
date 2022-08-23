"""
    Plotting tools for Sampling-based algorithms
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sys

sys.path.insert(0, 'RRT_libraries')
import env

class Plotting:
    def __init__(self, x_start, x_goal):
        self.xI, self.xG = x_start, x_goal
        self.env = env.Env()
        self.obs_bound = self.env.obs_boundary
        self.obs_circle = self.env.obs_circle
        self.obs_rectangle = self.env.obs_rectangle
    
    def animation(self, nodelist, path, name, animation = False):
        self.plot_grid(name)
        self.plot_visited(nodelist)
        self.plot_path(path)
    
    def animation_connect(self, V1, V2, path, name):
        self.plot_grid(name)
        self.plot_visited_connect(V1, V2)
        self.plot_path(path)
    def plot_grid(self, name):
        fig, ax = plt.subplot()
        
        for (ox, oy, w, h) in self.obs_bound:
            ax.add_patch(
                patches.Rectangle( (ox, oy), w, h,
                    edgecolor = 'black',
                    facecolor = 'black',
                    fill = True
                )
            )
