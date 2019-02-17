# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 13:16:51 2019

@author: PC USER
"""
import csv
import pandas as pd




def hello():
    print("Hello")
    
def printfile():   
    with open('Pokemon_all.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count < 100:
                print(f'{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]} | {row[8]} | {row[9]} | {row[10]} | {row[12]} | {row[13]}')
                line_count += 1
            
        print(f'Processed {line_count} lines.')
    
def dictionarylist():
    with open('Pokemon_all.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        pokedex = []
        for row in csv_reader:
            if line_count <= 0:
                line_count += 1
            else:
                pokedex.append({'id':row[0], 'name':row[1], 'type1':row[2], 'type2':row[3], 'total':row[4], 'hp':row[5], 'attack':row[6], 'defense':row[7], 'spatk':row[8], 'spdef':row[9], 'speed':row[10], 'generation':row[11], 'legendary':row[12], 'mega':row[13]})
                line_count += 1
        

dictionarylist()
for p in pokedex:
    print(str(p) + '\n')



    