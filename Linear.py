from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt 

image = 'D:\OneDrive - BENNETT UNIVERSITY\BU\Reserach\Python Dev Work\PythonDataAnalysisWithPandasNumpySeabourn\Einstein.jpg'

pic = Image.open(image)

# plt.imshow(pic)
# plt.show()

pic = np.array(pic)
plt.imshow(pic,cmap='gray')
plt.show()

U,S,V = np.linalg.svd(pic)

print(U)