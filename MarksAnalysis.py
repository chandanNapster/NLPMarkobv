import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np
from scipy.stats import pearsonr 


class MarksAnalysis:

  def __init__(self, file):
    self.dataset = file
    self.dataframe = None

  def readData(self):
    # print(self.dataset)
    dataframe = pd.read_csv(self.dataset)
    print(dataframe.columns)
    
    d_total = dataframe[['Student Name','Batch','Presentation Marks','Participation Marks','TOTAL']]
    # d_total = dataframe[['Student Name','Batch','TOTAL']]
    
    # d_total = d_total.iloc[:]
    self.dataframe = d_total 
    print("******************")
    print(self.dataframe.describe())
    print("********************")
    
    # print(d_total.describe())
    return self.dataframe 

  def visualizeData(self):
    df = self.readData()
    # print(df)
    # self.histogram(df)
    self.distPlot(df)
    self.boxplot(df)
    # self.jointPlots(df)
    

  def distPlot(self, df):
    sns.set_style('whitegrid')
    ax= sns.displot(x=df['TOTAL'], kde = True, color ='blue', bins = 20, height=4.75, kind='hist')
    ax.set(xlabel='Total Marks', ylabel='Total Number of Students')
    plt.show()
   

  def histogram(self, df):
    plt.figure(figsize=(5,4))
    plt.subplot(1,2,1)
    df['Presentation Marks'].hist()
    plt.title("Presentation Marks")

    plt.subplot(1,2,2)
    df['Participation Marks'].hist()
    plt.title("Participation Marks")
    # df['TOTAL'].hist()
    
    # df['Participation Marks'].hist()
    # plt.subplot(1,2,1)
    # sns.scatterplot(x=df['Presentation Marks'], y=df['Participation Marks'])
    # plt.title("Participation Marks")
    
    # plt.title("TOTAL MARKS")
    plt.show()
    # print(df)
  
  def boxplot(self, df):
    plt.figure(figsize = (5,4))
    sns.boxplot(x=df['Batch'], y=df['TOTAL'])
    # print(df.decribe())
    # sns.violinplot(x = df['TOTAL'], scale= 'count')
    # sns.violinplot(x = df['Batch'],y = df['TOTAL'])
    plt.title("Five Point Summary")
    plt.show()

  def jointPlots(self,df):
    sns.jointplot(data = df, x='Participation Marks', y='Presentation Marks', height=4.5, kind= 'reg')
    print(self.correlationValue(df['Participation Marks'], df['Presentation Marks']))
    plt.show()

  def correlationValue(self, df1, df2):
    vec1 = np.array(list(df1))
    vec2 = np.array(list(df2))
    return self.corr(vec1, vec2)

  def unit_vec(self,vector):
    vector = np.array(vector)
    mag = np.linalg.norm(vector)
    vector = vector * (1/mag)
    return vector            

  def corr(self,vec1, vec2):
    vec1,vec2 = np.array(vec1), np.array(vec2)
    vec1, vec2 = self.unit_vec(vec1), self.unit_vec(vec2)
    avg_vec1, avg_vec2 = np.average(vec1), np.average(vec2)
    vec1,vec2 = vec1 - avg_vec1, vec2 - avg_vec2
    r_value = np.abs(np.dot(vec1, vec2)) / np.abs((np.linalg.norm(vec1)) * np.abs(np.linalg.norm(vec2)))
    # print(r_value)
    # if  r_value > 1:
    #     r_value = 0.99999999999
    theta = np.arccos(r_value)
    theta = np.rad2deg(theta)
    # corr, _ = pearsonr(vec1, vec2)
    # print(corr)
    return r_value, theta  
    
    