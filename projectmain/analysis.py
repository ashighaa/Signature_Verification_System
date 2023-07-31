import pandas as pd
import cv2
import seaborn as sns
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import csv
from tkinter import messagebox
df = pd.read_csv('analysis.csv')
filename = "analysis.csv"
def analysis():
    df = pd.read_csv('analysis.csv')
    val0= np.array(df['accuracy'] == 0)
    val1= np.array(df['accuracy'] == 1)
    val00=df[val0]
    val11 = df[val1]
    size1= val11.size
    size0 = val00.size
    sns.set()
    sns.barplot(x=['correct','wrong'], y=[size1,size0])
    plt.title('Analysis of system efficiency')
    plt.show()

def record():
    res = messagebox.askquestion(
        'Analysis', 'Select yes if result is satisfactory else no')
    if res == 'yes':
        rows = ['1']
        with open(filename, 'a') as csvfile:

            csvwriter = csv.writer(csvfile)

            csvwriter.writerows(rows)
    elif res == 'no':
        rows = ['0']
        with open(filename, 'a') as csvfile:

            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(rows)
