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
    
def getAllTypes(l):
    t = []
    for x in l:
        temp = x.split(';')
        for i in temp:
            if not i in t:
                t.append(i)
    return t

#def bins(l, n):
#    l.sort()
#    intervalo = (l[-1]-l[0])/n
#    li = l[0]
#    ls = li + intervalo
#    r = []
#    bn = []
#    for n, i in enumerate(l):
#        if i < ls:
#            bn.append(i)
#        elif i == l[-1] and n != len(l)-1: # the last ones
#            bn.append(i)
#            r.append([])
#            li = ls
#            ls += intervalo
#        elif n == len(l)-1: # last one
#            bn.append(i)
#            r.append(bn)    
#        else:
#            r.append(bn)
#            li = ls
#            ls += intervalo
#            ls = round(ls, 5)
#            bn = []
#    return r
    
def bins(l, n):
    l.sort()
#    print(l)
    intervalo = (l[-1]-l[0])/n
    li = l[0]
    ls = li + intervalo
    r = []
    bn = []
    for n, i in enumerate(l):
#        print("i",i)
        if i >= li and i < ls:
            bn.append(i)
        else:
            if ls < l[-1]:
#                print("\nli",li,"ls",ls)
                li = ls
                ls += intervalo
                ls = round(ls, 5)
#                print(bn)
                r.append(bn)
                bn = []
            elif ls == l[-1]:
#                print("ls == l[-1]")
                if n < len(l)-1:
                    bn.append(i)
                elif n == len(l)-1:
#                    print(bn)
                    r.append(bn)
            while i > ls:
#                print([])
                r.append([])
                li = ls
                ls += intervalo
#                print("\nli",li,"ls",ls)
#                print("special i",i)
                ls = round(ls, 5)
            bn.append(i)
                
    return r

def correlation(l1, l2):
    mediax = 0
    for i in l1:
        mediax += i
    mediax /= len(l1)
    
    mediay = 0
    for i in l2:
        mediay += i
    mediay /= len(l2)
    
    aa = 0
    sumapow2 = 0
    sumbpow2 = 0
    for x in range(len(l1)):
        a = (l1[x] - mediax)*(l2[x] - mediay)
        aa += a
        
        apow2 = (l1[x] - mediax) ** 2
        bpow2 = (l2[x] - mediay) ** 2 
        sumapow2 += apow2
        sumbpow2 += bpow2
    
    r = aa / (mt.sqrt(sumapow2) * mt.sqrt(sumbpow2))
    return(r)

directory = 'P:/UG/8°/Mineria/data/'
path = directory + 'survey_results_public.csv'

data = pd.read_csv(path, encoding = 'utf-8')



# 1
# Compute the five-number summary, the boxplot, the mean, and the standard deviation
# for the annual salary per gender.
def genderAnalysis():
    df_filter = data['Gender'].isnull()
    devTypes = data[~df_filter]['Gender'].tolist()
    types = getAllTypes(devTypes)
    
    df_filter2 = data['ConvertedComp'].isnull()
    
    for t in types:
        print('\n-----------------------------------------------------\n')
        print(t)
        df_filter = data['Gender'].str.contains(t, na = False)
        l = data[df_filter & ~df_filter2]['ConvertedComp'].tolist()
        print("Anual salary per gender:")
        print("Five number summary:")
        fiveNumberSummary(l)
        mean(l)
        stdDev(l)
        plt.boxplot(l,  notch=False, sym = '')
        plt.show()
#genderAnalysis()

# 2
# Compute the five-number summary, the boxplot, the mean, and the standard deviation
#for the annual salary per ethnicity.
def ethnicityAnalysis():
    
    ethnicities = ['White or of European descent', 'East Asian', 'Multiracial', 'Black or of African descent', 'Hispanic or Latino/Latinal', 'Middle Eastern', 'Native American', 'Pacific Islander, or Indigenous Australian', 'South Asian', 'Biracial']
    df_filter2 = data['ConvertedComp'] > 0
    for e in ethnicities: 
        print('\n-----------------------------------------------------\n')
        print(e)
        df_filter = data['Ethnicity'] == e
        l = data[df_filter & df_filter2]['ConvertedComp'].tolist()
        # print(data[df_filter][df_filter2]['ConvertedComp'].head())
        print("Anual salary per gender:")
        print("Five number summary:")
        fiveNumberSummary(l)
        mean(l)
        plt.boxplot(l, notch=False, sym = '')
        plt.show()
        stdDev(l)
   
#ethnicityAnalysis()

# 3
# Compute the five-number summary, the boxplot, the mean, and the standard deviation
# for the annual salary per developer type.
def developerTypeAnalysis():
    
    df_filter = data['DevType'].isnull()
    df_filter2 = data['ConvertedComp'] > 0
    devTypes = data[~df_filter]['DevType'].tolist()
    types = getAllTypes(devTypes)
    
    for t in types:
        print('\n-----------------------------------------------------\n')
        print(t)
        df_filter = data['DevType'].str.contains(t, na = False)
        l = data[df_filter & df_filter2]['ConvertedComp'].tolist()
        fiveNumberSummary(l)
        mean(l)
        plt.boxplot(l, notch=False, sym = '')
        plt.show()
        stdDev(l)
    
#developerTypeAnalysis()

# 4
# Compute the median, mean and standard deviation of the annual salary per country.
def salaryCountryAnalysis():
    df_filter = data['Country'].isnull()
    df_filter2 = data['ConvertedComp'] > 0
    devTypes = data[~df_filter]['Country'].tolist()
    types = getAllTypes(devTypes)
    
    for t in types:
        print('\n-----------------------------------------------------\n')
        print(t)
        df_filter = data['Country'].str.contains(t, na = False)
        l = data[df_filter & df_filter2]['ConvertedComp'].tolist()
        if len(l) > 1:
            print("median: ",quartile(l, 0.5))
            mean(l)
            stdDev(l)
        elif len(l) == 1:
            print("median: ",quartile(l, 0.5))
            mean(l)
            print("Standard deviation no possible because single value is given")
        else:
            print("No given information for this country")
        

# salaryCountryAnalysis()

# 5
# Obtain a bar plot with the frequencies of responses for each developer type.
def developerTypePlot():
    df_filter = data['DevType'].isnull()
    l = data[~df_filter]['DevType']
    
    mydict = {}
    devTypes = []
    responses = []

    for t in l:
        temp = t.split(';')
        for i in temp:
            if i not in mydict:
                mydict[i] = 0
            else:
                mydict[i] += 1
    
    for e in mydict:
        devTypes.append(e)
        responses.append(mydict[e])
    
    plt.barh(devTypes,responses)
    
#developerTypePlot()
    

#6
# Plot histograms with 10 bins for the years of experience with coding per gender.
def experiencePerGenderPlot():
    df_filter = data['Gender'].isnull()
    devTypes = data[~df_filter]['Gender'].tolist()
    types = getAllTypes(devTypes)
    
    df_filter2 = data['YearsCode'].isnull()
    
    for t in types:
        print('\n-----------------------------------------------------\n')
        print(t)
        df_filter = data['Gender'].str.contains(t, na = False)
        l = data[df_filter & ~df_filter2]['YearsCode'].tolist()
        for n, i in enumerate(l):
            if i == 'Less than 1 year':
                l[n] = 0
            if i == 'More than 50 years':
                l[n] = 51
            l[n] = int(l[n])
        l.sort()
        print('\n----------------------------------------------------------\n')
        b = bins(l, 10)
        repetitions = []
        labels = []
        for i in b:
            repetitions.append(len(i))
            labels.append(str(i[0])+ "-" + str(i[-1]))
        plt.bar(labels, repetitions)
        plt.show()
            
#experiencePerGenderPlot()

#7
# Plot histograms with 10 bins for the average number of working hours per week, per
# developer type.
def developerHoursPlot():
    df_filter = data['DevType'].isnull()
    devTypes = data[~df_filter]['DevType'].tolist()
    types = getAllTypes(devTypes)
    
    df_filter2 = data['WorkWeekHrs'] > 0
    
    for t in types:
        print('\n-----------------------------------------------------\n')
        print(t)
        df_filter = data['DevType'].str.contains(t, na = False)
        l = data[df_filter & df_filter2]['WorkWeekHrs'].tolist()
        l.sort()
#        print(l)
        b = bins(l, 10)
        repetitions = []
        labels = []
#        print(b)
        for i in b:
            repetitions.append(len(i))
            if len(i) > 0:
                labels.append(str(i[0]))
            else:
                labels.append("0")
#        print(repetitions)
#        for i in b:
#            repetitions.append(len(i))
#            labels.append(str(i[0])+ "-" + str(i[len(b)]))
        print(repetitions)
        print(labels)
        plt.bar(labels, repetitions)
        plt.show()
    
developerHoursPlot()


#8
# Plot histograms with 10 bins for the age per gender.
def agePerGenderPlot():
    df_filter = data['Gender'].isnull()
    devTypes = data[~df_filter]['Gender'].tolist()
    types = getAllTypes(devTypes)
    
    df_filter2 = data['Age'] > 0
    
    for t in types:
        print('\n-----------------------------------------------------\n')
        print(t)
        df_filter = data['Gender'].str.contains(t, na = False)
        l = data[df_filter & df_filter2]['Age'].tolist()
        l.sort()
        b = bins(l, 10)
        repetitions = []
        labels = []
        for i in b:
            repetitions.append(len(i))
            if len(i) > 0:
                labels.append(str(i[0]))
            else:
                labels.append("0")
        plt.bar(labels, repetitions)
        plt.show()

#agePerGenderPlot()

#9
# Compute the median, mean and standard deviation of the age per programming
#language.
def languageAnalysis():
    df_filter = data['LanguageWorkedWith'].isnull()
    devTypes = data[~df_filter]['LanguageWorkedWith'].tolist()
    types = getAllTypes(devTypes)
    
    df_filter2 = data['Age'] > 0
    
    for t in types:
        print('\n-----------------------------------------------------\n')
        print(t)
        if t == 'C++':
            df_filter = data['LanguageWorkedWith'].str.contains('C+', na = False)
        else:
            df_filter = data['LanguageWorkedWith'].str.contains(t, na = False)
        l = data[df_filter & df_filter2]['Age'].tolist()
        if len(l) > 1:
            print("median: ",quartile(l, 0.5))
            mean(l)
            stdDev(l)
        elif len(l) == 1:
            print("median: ",quartile(l, 0.5))
            mean(l)
            print("Standard deviation no possible because single value is given")
        else:
            print("No given information for this language")
        
#languageAnalysis()
    

#10
# Compute the correlation between years of experience and annual salary.
def experienceSalaryCorrelation():
    df_filter = data['YearsCode'].isnull()
    df_filter2 = data['ConvertedComp'].isnull()
    l1 = data[~df_filter & df_filter2]['YearsCode'].tolist()
    
    for n, i in enumerate(l1):
            if i == 'Less than 1 year':
                l1[n] = 0
            if i == 'More than 50 years':
                l1[n] = 51
            l1[n] = int(l1[n])
    l1.sort()
    
    
    l2 = data[~df_filter2 & ~df_filter2]['ConvertedComp'].tolist()
    l2.sort()
    
    print("Correlation between years of experience and annual salary:")
    print(correlation(l1, l2))
    
#experienceSalaryCorrelation()

#11
# Compute the correlation between the age and the annual salary.
def ageSalaryCorrelation():
    df_filter = data['Age'].isnull()
    df_filter2 = data['ConvertedComp'].isnull()
    l1 = data[~df_filter & df_filter2]['Age'].tolist()
    l1.sort()
    l2 = data[~df_filter2 & ~df_filter2]['ConvertedComp'].tolist()
    l2.sort()
    
    print("Correlation between the age and the annual salary:")
    print(correlation(l1, l2))

#ageSalaryCorrelation()

#12
# Compute the correlation between educational level and annual salary.
def educationSalaryCorrelation(): 
     educationLevels = {
             'Primary/elementary school': 1,
             'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)': 2,
             'Bachelor’s degree (BA, BS, B.Eng., etc.)': 4,
             'Some college/university study without earning a degree': 3,
             'Master’s degree (MA, MS, M.Eng., MBA, etc.)': 5, 
             'Other doctoral degree (Ph.D, Ed.D., etc.)': 6,
             'Associate degree': 4,
             'Professional degree (JD, MD, etc.)': 4,
             'I never completed any formal education': 0
             }
     
     df_filter = data['EdLevel'].isnull()
     df_filter2 = data['ConvertedComp'].isnull()
     l1 = data[~df_filter & df_filter2]['EdLevel'].tolist()
     edValues = []
     for i, x in enumerate(l1):
         edValues.append(educationLevels[x])
        
     edValues.sort()
     l2 = data[~df_filter2 & ~df_filter2]['ConvertedComp'].tolist()
     l2.sort()

     print("Correlation between the age and the annual salary:")
     print(correlation(edValues, l2))

#educationSalaryCorrelation()

#13
# Obtain a bar plot with the frequencies of the different programming languages.
def languagesPlot():
    df_filter = data['LanguageWorkedWith'].isnull()
    l = data[~df_filter]['LanguageWorkedWith'].tolist()
    frec = {}

    for x in l:
        temp = x.split(';')
        for i in temp:
            if i not in frec:
                frec[i] = 0
            else:
                frec[i] += 1
    languages = []
    responses = []
    for f in frec:
        languages.append(f)
        responses.append(frec[f])

    plt.barh(languages, responses)
    plt.show()
    
#languagesPlot()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
