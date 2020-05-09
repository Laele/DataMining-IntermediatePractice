# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:48:00 2020

@author: luiss
"""

#Universidad de Guanajuato
#Practica Intermedia Mineria de Datos 
#Luis Gonzalo Soriano Crespo

import math as mt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def percentil(lista, perc):
    pm = (len(lista)-1)*perc
    pl = mt.floor(pm)
    pu = mt.ceil(pm)
    return lista[pl]+(lista[pu]-lista[pl])*perc

def fiveNumSummaryMediaDesvEstBloxplot(lista,name):
    mini = lista[0]
    maxi = lista[-1]
    mediana = percentil(lista,0.5)
    fq = percentil(lista,0.25)
    tq = percentil(lista,0.75)
    
    media = sum(lista)/len(lista)
    covar = sum([(i-media)**2 for i in lista])/(len(lista)-1)
    desvEst = covar**(1/2)
    
    print("\n" + name + "\n")
    print("Minimo: ", mini)
    print("Maximo: ", maxi)
    print("Mediana: ", mediana)
    print("1er Cuartil: ", fq)
    print("3er Cuartil: ", tq)
    print("Media: ", media)
    print("Desviacion Estandar: ", desvEst)
    
    plt.boxplot(lista,sym='')
    plt.show()

def binsHistogram(bins,lista,name):

    lista.sort()
   
    print("\n" + name)
    plt.hist(lista, bins)
    plt.show()

def correlation(lista1, lista2):
    x = sum(lista1)/len(lista1)
    y = sum(lista2)/len(lista2)
    
    suma1 = 0
    suma2 = 0
    suma3 = 0
    
    for i in range(0, len(lista1)):
        suma1 += (lista1[i]-x)*(lista2[i]-y)
        suma2 += (lista1[i]-x)**2
        suma3 += (lista2[i]-y)**2
        
    suma2 = mt.sqrt(suma2)
    suma3 = mt.sqrt(suma3)
    raiz = suma2 * suma3
    correlacion = suma1/raiz
    
    return correlacion



def menu():
    print("\nPractica Intermedia Mineria de Datos")
    print("Luis Gonzalo Soriano Crespo")
    print("Seleccione un punto (1 - 13) de la practica para continuar, 0 para salir: ")
    
    

def pointOne(data):
    print("\nPunto Numero Uno\n")
    
    anualSalary = data["ConvertedComp"].tolist()
    gender = data["Gender"].tolist()
    
    hombres = []
    mujeres = []
    nonBinary = []
    
    for (i,j) in zip(gender,anualSalary):
        isnan = mt.isnan(j)
        if (type(i) == str and isnan == False):
            tipo = i.split(';')
            for t in tipo:
                if t == 'Man':
                    hombres.append(j)
                elif t == 'Woman':
                    mujeres.append(j)
                elif t == 'Non-binary, genderqueer, or gender non-conforming':
                    nonBinary.append(j)

    #Ordenamiento para cada lista de salarios anuales
    hombres.sort()
    mujeres.sort()
    nonBinary.sort()
    
   
    #five-number sumamary para cada lista de salarios anuales
    fiveNumSummaryMediaDesvEstBloxplot(hombres,"Salario Anual Hombres:")
    fiveNumSummaryMediaDesvEstBloxplot(mujeres,"Salario Anual Mujeres:")
    fiveNumSummaryMediaDesvEstBloxplot(nonBinary,"Salario Anual Genero no Confirmado:")
    

def pointTwo(data):
    print("\nPunto Numero Dos\n")
    
    ethnicity = data["Ethnicity"].tolist()
    anualSalary = data["ConvertedComp"].tolist()
     
    difethni = []
     
    for i in ethnicity:
        if (type(i) == str):
            tipo = i.split(';')
            for t in tipo:            
                if (t not in difethni):
                    difethni.append(t)
                    
    l = 0
    while(l <= len(difethni)):
        lista = []
        for (i,j) in zip(ethnicity,anualSalary):
            isnan = mt.isnan(j)
            if (type(i) == str and isnan == False):
                tipo = i.split(';')
                for t in tipo:    
                    if t == difethni[l]: 
                        lista.append(j)
        lista.sort()
        fiveNumSummaryMediaDesvEstBloxplot(lista,"Salario Anual para Genero: " + difethni[l])
        l += 1
        if (l == len(difethni)):
            break
    

def pointThree(data):
    print("\nPunto Numero Tres\n")
    
    devtype = data["DevType"].tolist()
    anualSalary = data["ConvertedComp"].tolist()
     
    difdevtype = []
     
    for i in devtype:
        if (type(i) == str):
            tipo = i.split(';')
            for t in tipo:            
                if (t not in difdevtype):
                    difdevtype.append(t)
    
    l = 0
    while(l <= len(difdevtype)):
        lista = []
        for (i,j) in zip(devtype,anualSalary):
            isnan = mt.isnan(j)
            if (type(i) == str and isnan == False):
                tipo = i.split(';')
                for t in tipo:    
                    if t == difdevtype[l]: 
                        lista.append(j)
        lista.sort()
        fiveNumSummaryMediaDesvEstBloxplot(lista,"Salario Anual para Tipo de Desarrollador: " + difdevtype[l])
        l += 1
        if (l == len(difdevtype)):
            break
        

def pointFour(data):
    print("\nPunto Numero Cuatro\n")
    
    country = data["Country"].tolist()
    anualSalary = data["ConvertedComp"].tolist()
    
    difcountry = []
    
    for i in country:
        if (type(i) == str):
            tipo = i.split(';')
            for t in tipo:            
                if (t not in difcountry):
                    difcountry.append(t)
                 
    l = 0
    while(l <= len(difcountry)):
        lista = []
        for (i,j) in zip(country,anualSalary):
            isnan = mt.isnan(j)
            if (type(i) == str and isnan == False):
                tipo = i.split(';')
                for t in tipo:
                    if t == difcountry[l]: 
                        lista.append(j)
        lista.sort()
        
        if(len(lista) > 1 ):
            
            mediana = percentil(lista,0.5)
            media = sum(lista)/len(lista)
            covar = sum([(i-media)**2 for i in lista])/(len(lista)-1)
            desvEst = covar**(1/2)
            
            print("\nSalario Anual para Pais: " + difcountry[l])
            print("Mediana: ", mediana)
            print("Media: ", media)
            print("Desviacion Estandar: ", desvEst)
        else:
            print("\nSalario Anual para Pais: " + difcountry[l])
            print("No hay datos suficientes para hacer los calculos" )
            
        l += 1
        if (l == len(difcountry)):
            break
    

def pointFive(data):
    print("\nPunto Numero Cinco\n")
    print("Frecuencias de los diferentes tipos de Desarrolladores: ")
    devtype = data["DevType"].tolist()
    
    difdevtype = []
    
    for i in devtype:
        if (type(i) == str):
            tipo = i.split(';')
            for t in tipo:            
                if (t not in difdevtype):
                    difdevtype.append(t)
    
    frec = []
    
    l = 0
    while(l <= len(difdevtype)):
        count = 0
        for i in devtype:
            if (type(i) == str):
                tipo = i.split(';')
                for t in tipo:
                    if t == difdevtype[l]: 
                        count += 1
        frec.append(count)
            
        l += 1
        if (l == len(difdevtype)):
            break
        
    #print(frec)
        
    plt.barh(difdevtype,frec)
    plt.show()
                    
    

def pointSix(data):
    print("\nPunto Numero Seis\n")
    
    gender = data["Gender"].tolist()
    yearscode = data["YearsCode"].tolist()
    
    hombres = []
    mujeres = []
    nonBinary = []
    
    for (i,j) in zip(gender,yearscode):
        if type(j) != str: 
            isnan = mt.isnan(j)
        if type(j) == str and j != '':
            isnan = False   
        if (type(i) == str and isnan == False):
            tipo = i.split(';')
            for t in tipo:
                if j == 'Less than 1 year':
                    continue
                elif j == 'More than 50 years':
                    continue
                if t == 'Man':
                    hombres.append(int(j))
                elif t == 'Woman':
                    mujeres.append(int(j))
                elif t == 'Non-binary, genderqueer, or gender non-conforming':
                    nonBinary.append(int(j))
  
    binsHistogram(10,hombres,"Histograma para 10 bins Años de Experiencia coding por Genero: Hombres")
    binsHistogram(10,mujeres,"Histograma para 10 bins Años de Experiencia coding por Genero: Mujeres")
    binsHistogram(10,nonBinary,"Histograma para 10 bins Años de Experiencia coding por Genero: No Confirmado")
    
    

def pointSeven(data):
    print("\nPunto Numero Siete\n")
    
    devtype = data["DevType"].tolist()
    workweekhrs = data["WorkWeekHrs"].tolist()
     
    difdevtype = []
    
    for i in devtype:
        if (type(i) == str):
            tipo = i.split(';')
            for t in tipo:            
                if (t not in difdevtype):
                    difdevtype.append(t)
    
                    
    l = 0
    while(l <= len(difdevtype)):
        lista = []
        for (i,j) in zip(devtype,workweekhrs):
            isnan = mt.isnan(j)
            if (type(i) == str and isnan == False and j<112):
                tipo = i.split(';')
                for t in tipo:    
                    if t == difdevtype[l]: 
                        lista.append(j)
                        
        
        binsHistogram(10,lista,"Histograma para 10 bins Promedio de Horas/Semana por Tipo de Desarrollador: " + difdevtype[l])
        
        l += 1
        if (l == len(difdevtype)):
            break
    

def pointEight(data):
    print("\nPunto Numero Ocho\n")
    
    gender = data["Gender"].tolist()
    age = data["Age"].tolist()
    
    hombres = []
    mujeres = []
    nonBinary = []
    
    for (i,j) in zip(gender,age):
        if type(j) != str: 
            isnan = mt.isnan(j)
        if type(j) == str and j != '':
            isnan = False   
        if (type(i) == str and isnan == False):
            tipo = i.split(';')
            for t in tipo:
                if t == 'Man':
                    hombres.append(int(j))
                elif t == 'Woman':
                    mujeres.append(int(j))
                elif t == 'Non-binary, genderqueer, or gender non-conforming':
                    nonBinary.append(int(j))
  
    binsHistogram(10,hombres,"Histograma para 10 bins Edad por Genero: Hombres")
    binsHistogram(10,mujeres,"Histograma para 10 bins Edad por Genero: Mujeres")
    binsHistogram(10,nonBinary,"Histograma para 10 bins Edad Genero: No Confirmado")

def pointNine(data):
    print("\nPunto Numero Nueve\n")
    
    age = data["Age"].tolist()
    language = data["LanguageWorkedWith"].tolist()
    
    diflanguage = []
    
    for i in language:
        if (type(i) == str):
            tipo = i.split(';')
            for t in tipo:            
                if (t not in diflanguage):
                    diflanguage.append(t)
    
    #print(diflanguage)        
    l = 0
    
    while(l <= len(diflanguage)):
        lista = []
        for (i,j) in zip(language,age):
            isnan = mt.isnan(j)
            if (type(i) == str and isnan == False):
                tipo = i.split(';')
                for t in tipo:
                    if t == diflanguage[l]: 
                        lista.append(j)
        lista.sort()
        
        if(len(lista) > 1 ):
            
            mediana = percentil(lista,0.5)
            media = sum(lista)/len(lista)
            covar = sum([(i-media)**2 for i in lista])/(len(lista)-1)
            desvEst = covar**(1/2)
            
            print("\nSalario Anual para Pais: " + diflanguage[l])
            print("Mediana: ", mediana)
            print("Media: ", media)
            print("Desviacion Estandar: ", desvEst)
        else:
            print("\nSalario Anual para Pais: " + diflanguage[l])
            print("No hay datos suficientes para hacer los calculos" )
            
        l += 1
        if (l == len(diflanguage)):
            break

def pointTen(data):
    print("\nPunto Numero Diez\n")
    
    yearscode = data["YearsCode"].tolist()
    anualsalary = data["ConvertedComp"].tolist()
    
    lyearscode = []
    lanualsalary = []
     
    for (i,j) in zip(anualsalary,yearscode):
        if j == 'Less than 1 year':
            continue
        elif j == 'More than 50 years':
            continue
        if(type(i) == str):
            continue
        isnan = mt.isnan(float(j))
        isnan2 = mt.isnan(i)
        if (isnan == False and isnan2 == False):
            lyearscode.append(float(j))
            lanualsalary.append(i)

    print("Correlacion entre Años de experiencia coding y Salario Anual: ")    
    print(correlation(lyearscode,lanualsalary))
    


def pointEleven(data):
    print("\nPunto Numero Once\n")
    
    age = data["Age"].tolist()
    anualsalary = data["ConvertedComp"].tolist()
    
    lage = []
    lanualsalary = []
     
    for (i,j) in zip(anualsalary,age):
        if(type(i) == str or type(j) == str):
            continue
        isnan = mt.isnan(float(j))
        isnan2 = mt.isnan(i)
        if (isnan == False and isnan2 == False):
            lage.append(j)
            lanualsalary.append(i)
    print("Correlacion entre Edad y Salario Anual: ")
    print(correlation(lage,lanualsalary))
    

def pointTwelve(data):
    print("\nPunto Numero Doce\n")
    
    edlevel = data["EdLevel"].tolist()
    anualsalary = data["ConvertedComp"].tolist()
    
    d = {'I never completed any formal education': 0, 'Primary/elementary school': 1, 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)': 2,  'Some college/university study without earning a degree': 3, 'Bachelor’s degree (BA, BS, B.Eng., etc.)': 4, 'Professional degree (JD, MD, etc.)': 5, 'Master’s degree (MA, MS, M.Eng., MBA, etc.)': 6, 'Other doctoral degree (Ph.D, Ed.D., etc.)': 7, 'Associate degree':8}
    
    ledlevel = []
    lanualsalary = []
     
    for (i,j) in zip(anualsalary,edlevel):
        if(type(i) == str or type(j) != str):
            continue
        isnan2 = mt.isnan(i)
        if (isnan2 == False):
            for k in d:
                if j == k: 
                    ledlevel.append(d[k])
                    lanualsalary.append(i)
            
    print("Correlacion entre Nivel de Educacion y Salario Anual: ")
    print(correlation(ledlevel,lanualsalary))

      

def pointThirTeen(data):
    print("\nPunto Numero Trece\n")
    print("Frecuencias de los diferentes tipos de Desarrolladores: ")
    
    language = data["LanguageWorkedWith"].tolist()
    
    diflanguage = []
    
    for i in language:
        if (type(i) == str):
            tipo = i.split(';')
            for t in tipo:            
                if (t not in diflanguage):
                    diflanguage.append(t)
    
    frec = []
    
    l = 0
    while(l <= len(diflanguage)):
        count = 0
        for i in language:
            if (type(i) == str):
                tipo = i.split(';')
                for t in tipo:
                    if t == diflanguage[l]: 
                        count += 1
        frec.append(count)
            
        l += 1
        if (l == len(diflanguage)):
            break
        
    plt.barh(diflanguage,frec)
    plt.show()

# Remplazar ruta donde se encuentre el archivo survey_results_public
w_d = 'C:/Users/luiss/OneDrive/Documentos/Materias/Mineria de Datos/Data/survey_results_public.csv'
data = pd.read_csv(w_d,encoding = 'utf-8')


op = ''
while op != '0':
    menu()
    op = input()
    if(op == '1'):
        pointOne(data)
    elif(op == '2'):
        pointTwo(data)
    elif(op == '3'):
        pointThree(data)
    elif(op == '4'):
        pointFour(data)
    elif(op == '5'):
        pointFive(data)
    elif(op == '6'):
        pointSix(data)
    elif(op == '7'):
        pointSeven(data)
    elif(op == '8'):
        pointEight(data)
    elif(op == '9'):
        pointNine(data)
    elif(op == '10'):
        pointTen(data)
    elif(op == '11'):
        pointEleven(data)
    elif(op == '12'):
        pointTwelve(data)
    elif(op == '13'):
        pointThirTeen(data)
    elif(op == '0'):
        print("Nos vemos!\n")
    else:
        print("Vuelve a introducir un punto valido\n")
    
