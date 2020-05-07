# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:35:46 2020

@author: diego
"""
import math as mt
import matplotlib.pyplot as plt
import pandas as pd

def quartile(l, quartile):
    l.sort()
    n_elem = len(l)-1
    pl = mt.floor(n_elem*quartile)
    pu = mt.ceil(n_elem*quartile)
    q = l[pl] + (l[pu] - l[pl])*quartile
    return q
    
def fiveNumberSummary(l):
    l.sort()
    print("Min: ",l[0])
    print("Max: ",l[-1])
    # First quartile
    print("First quartile: ",quartile(l,0.25))
    # median
    print("Median: ",quartile(l,0.5))
    # 3rd quartile
    print("Third quartile: ",quartile(l,0.75))
    print("")
    
def mean(l):
    # mean
    total = 0
    for x in l:
        total += x
    mean = total/len(l)
    print("Mean: ",mean)
    return total
    
def stdDev(l):
    media = sum(l)/len(l)
    varianza = sum([(i - media)**2 for i in l]) / (len(l) - 1)
    print("Standard deviation",varianza**(1/2))
    return varianza**(1/2)
    



directory = 'P:/UG/8°/Mineria/data/'
path = directory + 'survey_results_public.csv'

data = pd.read_csv(path, encoding = 'utf-8')



# 1
# Compute the five-number summary, the boxplot, the mean, and the standard deviation
# for the annual salary per gender.
def genderAnalysis():
    print("Man analysis")
    df_filter = data['Gender'] == 'Man'
    df_filter2 = data['ConvertedComp'] > 0
    
#    data[df_filter].boxplot(column='ConvertedComp')
    l = data[df_filter][df_filter2]['ConvertedComp'].tolist()
    print("Anual salary per gender:")
    print("Five number summary:")
    fiveNumberSummary(l)
    mean(l)
    stdDev(l)
    plt.boxplot(l)
    
    print("\n-----------------------------------------------\n")
    print("Woman analysis")
    df_filter = data['Gender'] == 'Woman'
    df_filter2 = data['ConvertedComp'] > 0
#    data[df_filter].boxplot(column='ConvertedComp')
    l = data[df_filter][df_filter2]['ConvertedComp'].tolist()
    print("Anual salary per gender:")
    print("Five number summary:")
    fiveNumberSummary(l)
    mean(l)
    stdDev(l)
    plt.boxplot(l)
    
    
#genderAnalysis()

# 2
# Compute the five-number summary, the boxplot, the mean, and the standard deviation
#for the annual salary per ethnicity.
def ethnicityAnalysis():
    l = data['Ethnicity']
    print(data['Ethnicity'].head())
    print("Anual salary per gender:")
    print("Five number summary:")
#    fiveNumberSummary(l)
#    mean(l)
#    plt.boxplot(l)
#    stdDev(l)
    
ethnicityAnalysis()
"""
# 3
# Compute the five-number summary, the boxplot, the mean, and the standard deviation
# for the annual salary per developer type.
def developerTypeAnalysis():
    l = data['DevType']
    print("Anual salary per gender:")
    print("Five number summary:")
    fiveNumberSummary(l)
    mean(l)
    plt.boxplot(l)
    stdDev(l)

# 4
# Compute the median, mean and standard deviation of the annual salary per country.
def salaryCountryAnalysis():
    # median
    print("Median: ",quartile(l,0.5))
    mean(l)
    stdDev(l)


# 5
# Obtain a bar plot with the frequencies of responses for each developer type.
def developerTypePlot():
    
#6
# Plot histograms with 10 bins for the years of experience with coding per gender.
def experiencePerGenderPlot():
    
#7
# Plot histograms with 10 bins for the average number of working hours per week, per
developer type.
def developerHoursPlot():
    
#8
# Plot histograms with 10 bins for the age per gender.
def agePerGenderPlot():
    
#9
# Compute the median, mean and standard deviation of the age per programming
language.
def languageAnalysis():

#10
# Compute the correlation between years of experience and annual salary.
def experienceSalaryCorrelation():    

#11
# Compute the correlation between the age and the annual salary.
def ageSalaryCorrelation():
    
#12
# Compute the correlation between educational level and annual salary.
def educationSalaryCorrelation():
    
#13
# Obtain a bar plot with the frequencies of the different programming languages.
def languagesPlot():
"""
