import numpy as np

magni = 0

def angle_between_vectors(vector, other):
    theta = np.arccos(np.abs(np.dot(vector, other))/ (mag(vector) * mag(other)))
    theta = np.rad2deg(theta)
    return theta

def unit_vec(vector):
    vector = np.array(vector)
    mag = np.linalg.norm(vector)
    vector = vector * (1/mag)
    return vector 

def unit2Org(vector):
    print(vector)
    print(mag)
    return vector * magni  

def mag(vector):
    return np.abs(np.linalg.norm(vector))

def find_ortho_vec(vector):
    theta = 0
    other_vec = np.random.randn(len(vector))
    vector = unit_vec(vector)  
    while not (89.9999 < theta < 90.0001):
        other_vec = np.round(np.random.randn(len(vector)) * 10)
        other_vec = unit_vec(other_vec)
        theta = angle_between_vectors(vector, other_vec)
        # print(theta)
    print(magni)    
    print(other_vec)
    unit2Org(other_vec)


if __name__ == "__main__":
    vector = np.array([1,2,3,4,5,6,7,8,9,10])
    print(find_ortho_vec(vector))
    # print(angle_between_vectors(vector, other_vec))
        