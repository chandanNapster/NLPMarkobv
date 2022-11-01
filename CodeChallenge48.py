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


if __name__ == '__main__':

    angle = 0
    len_of_o_vec = []
    len_of_vec = []
    while angle != 360:
    
        deg = np.deg2rad(angle)
        thetha = deg
        
        rot_mat = np.array([[4*np.cos(thetha), -np.sin(thetha)],[np.sin(thetha), np.cos(thetha)]])
        vec2 = np.array(vec1)
        print('The angle is-->', angle)
        # print(rot_mat)
        # print(vec1)

        o_Vec = vec2 @ rot_mat
        # print('')
        # print(length_of_vector(o_Vec))
        # print(length_of_vector(vec2))
        print('ratio -->', length_of_vector(o_Vec)/length_of_vector(vec2))
        print('################')
        len_of_o_vec.append(length_of_vector(o_Vec * 10))
        len_of_vec.append(length_of_vector(vec2))
        angle += 1 

  
    # print(np.rad2deg(angle_between_vectors(o_Vec, vec1)))

    # orth_vec = orthoVector(vec1)

    # print('Othro')
    # print(orth_vec)


    # print(vec2.T @ rot_mat)

    # print(orthoVector(vec1))
    # print(np.rad2deg(angle_between_vectors(vec1, orthoVector(vec1))))

    # angle_between_vectors(vec1, vec1)