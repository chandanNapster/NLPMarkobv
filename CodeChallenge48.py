import numpy as np 
import matplotlib.pyplot as plt


vec1 = [2,6]

def dotProduct(vector1, vector2):
    return np.dot(vector1,vector2)

def length_of_vector(vector):
    return np.sqrt(dotProduct(vector,vector))    

def angle_between_vectors(vector1, vector2):    
    angle = np.abs(dotProduct(vector1,vector2)) / np.abs(length_of_vector(vector1) * length_of_vector(vector2))
    angle = np.arccos(angle)
    return angle
   

def orthoVector(vector):
    angle = 0
    while not (89.99999 < angle < 90.00001):
        orthoVec = np.array(np.round(np.random.randn(len(vector)) * 10)) 
        angle = np.rad2deg(angle_between_vectors(orthoVec, vector))
    return orthoVec

def showPlot(x,y):
    # Scatter plot with day against tip
    plt.plot(x)
    plt.plot(y)
    # Adding Title to the Plot
    plt.title("Scatter Plot")
    # Setting the X and Y labels
    plt.xlabel('Orthogonal Vector')
    plt.ylabel('Nprmal Vector')
    plt.show()


if __name__ == '__main__':
    multi_factor = 1.5
    angle = 0
    len_of_o_vec = []
    len_of_vec = []
    while angle != 360:
        deg = np.deg2rad(angle)
        thetha = deg
        rot_mat = np.array([[(multi_factor*np.cos(thetha)), -np.sin(thetha)],[np.sin(thetha),  np.cos(thetha)]])
        vec2 = np.array(vec1)
        o_Vec = vec2 @ rot_mat
        len_of_o_vec.append(length_of_vector(o_Vec))
        len_of_vec.append(length_of_vector(vec2))
        angle += 1 

    showPlot(len_of_o_vec, len_of_vec)


# # importing the modules
# from bokeh.plotting import figure, output_file, show
# from bokeh.palettes import magma
# import pandas as pd
 
 
# # instantiating the figure object
# graph = figure(title = "Bokeh Scatter Graph")
 
# # reading the database
# data = pd.read_csv("tips.csv")
 
# color = magma(256)
 
# # plotting the graph
# graph.scatter(data['total_bill'], data['tip'], color=color)
 
# # displaying the model
# show(graph)