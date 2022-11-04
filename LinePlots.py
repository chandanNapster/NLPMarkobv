import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr 

num_rows = 14

file = "D:\\NLPMarkov\\NLPMarkobv\\Burndown.csv"
data = pd.read_csv(file)

days = list(data['Days'])
estimated = list(data['Estimated'])
actual = list(data['Actual'])

data_preproc = pd.DataFrame({
    'DAYS': days, 
    'ESTIMATED': estimated,
    'ACTUAL': actual})


def showLinePlot():
    ax = sns.lineplot(x='DAYS', y='value', hue='variable', data=pd.melt(data_preproc, ['DAYS']))    
    ax.set(ylabel='User Story Points', xlabel='Number of Days')
    plt.show()     


def showJointPlot(val1,val2,choice):
    # kind{ “scatter” | “kde” | “hist” | “hex” | “reg” | “resid” }
    knd = kind_type(choice)
    if choice == 4:
        r_value, angle = corr(val1, val2)
        if 1 > r_value > .9:
            print("Very High Positive Correlation = {0} and angle between two vectors is = {1} degrees".format(r_value, angle))
        elif .9 > r_value > .7:
            print("High Positive Correlation = {0} and angle between two vectors is = {1} degrees".format(r_value, angle))
        elif .7 > r_value > .5:
            print("Moderate Positive Correlation = {0} and angle between two vectors is = {1} degrees".format(r_value, angle))
        elif .5 > r_value > .3:
            print("Weak Positive Correlation = {0} and angle between two vectors is = {1} degrees".format(r_value, angle))    
        elif .3 > r_value > -.3:
            print("Negligible Correlation = {0} and angle between two vectors is = {1} degrees".format(r_value, angle))
        elif -.3 > r_value > -.5:
            print("Weak Negative Correlation = {0} and angle between two vectors is = {1} degrees".format(r_value, angle)) 
        elif -.5 > r_value > -.7:
            print("Moderate Negative Correlation = {0} and angle between two vectors is = {1} degrees".format(r_value, angle))
        elif -.7 > r_value > -.9:
            print("High Negative Correlation = {0} and angle between two vectors is = {1} degrees".format(r_value, angle))
        elif -.9 > r_value > -1:
            print("Very High Negative Correlation = {0} and angle between two vectors is = {1} degrees".format(r_value, angle))

        if val1 == actual:           
            sns.jointplot(data=data_preproc, x='ACTUAL', y='ESTIMATED', kind=knd)
        elif val1 == estimated:
            sns.jointplot(data=data_preproc, x='ESTIMATED', y='ACTUAL', kind=knd)
        elif val1 == days and val2 == actual:
            sns.jointplot(data=data_preproc, x='DAYS', y='ACTUAL', kind=knd)
        elif val1 == days and val2 == estimated:
            sns.jointplot(data=data_preproc, x='DAYS', y='ESTIMATED', kind=knd)
        
    else:
        if val1 == actual:           
            sns.jointplot(data=data_preproc, x='ACTUAL', y='ESTIMATED', kind=knd)
        elif val1 == estimated:
            sns.jointplot(data=data_preproc, x='ESTIMATED', y='ACTUAL', kind=knd)
        elif val1 == days and val2 == actual:
            sns.jointplot(data=data_preproc, x='DAYS', y='ACTUAL', kind=knd)
        elif val1 == days and val2 == estimated:
            sns.jointplot(data=data_preproc, x='DAYS', y='ESTIMATED', kind=knd)

    plt.show()

def kind_type(argument):
    match argument:
        case 0:
            return "scatter"
        case 1:
            return "kde"
        case 2:
            return "hist"
        case 3:
            return "hex"
        case 4:
            return "reg"        
        case 5:
            return "resid"

def unit_vec(vector):
    vector = np.array(vector)
    mag = np.linalg.norm(vector)
    vector = vector * (1/mag)
    return vector            

def corr(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    avg_vec1 = np.average(vec1)
    avg_vec2 = np.average(vec2)
    vec1 = vec1 - avg_vec1
    vec2 = vec2 - avg_vec2
    r_value = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    theta = np.arccos(r_value)
    theta = np.rad2deg(theta)
    return r_value, theta


if __name__ == "__main__":
    # showLinePlot() 
    plot_type_choice = 4
    plot_between_choices = 2

    if plot_between_choices == 0:
        parameter1, parameter2 = days, actual
    elif plot_between_choices == 1:
        parameter1, parameter2 = days, estimated    
    elif plot_between_choices == 2:
        parameter1, parameter2 = estimated, actual
    elif plot_between_choices == 3:
        parameter1, parameter2 = actual, estimated        

    showLinePlot()
    showJointPlot(parameter1,parameter2, plot_type_choice)
    corr, _ = pearsonr(parameter1, parameter2)
    print(corr)
    