# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 13:16:51 2019

@author: PC USER
"""
import csv
import json
import sys
from operator import itemgetter

print(sys.argv[0])
pokedex = []
sortedList = []
    
def createPokedex():
    with open('Pokemon_all.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count <= 0:
                line_count += 1
            else:
                pokedex.append({'id':row[0], 'name':row[1], 'type1':row[2], 'type2':row[3], 'total':row[4], 'hp':row[5], 'attack':row[6], 'defense':row[7], 'spatk':row[8], 'spdef':row[9], 'speed':row[10], 'generation':row[11], 'legendary':row[12], 'mega':row[13], 'coeff':0})
                line_count += 1
    return pokedex
    print(f'Processed {line_count} lines.')
    
def pokeSort():
    sortedList = pokedex
    sorter = input("Enter what you would like to sort by:")
    if sorter not in pokedex[0].keys():
        raise ValueError("BAD KEY NAME")
    else:
        sortedList = sorted(pokedex, key=lambda item: int(item[str(sorter)]))
        return sortedList

def coeffSort():
    sortedList = pokedex
    sortedList = sorted(pokedex, key=lambda item: int(item[str('coeff')]))
    legendary = input("Do you want to filter out legendaries?")
    mega = input("Do you want to filter out megas?")
    tempList = []
    for p in sortedList:
        if legendary == 'no' and mega == 'no':
            tempList.append(p)
        elif legendary == 'yes' and mega == 'yes':
            if p['legendary'] == 'FALSE' and p['mega'] == 'FALSE':
                tempList.append(p)
        elif legendary == 'yes' and mega == 'no':
            if p['legendary'] == 'FALSE':
                tempList.append(p)
        elif legendary == 'no' and mega == 'yes':
            if p['mega'] == 'FALSE':
                tempList.append(p)
    output = ""            
    for p in tempList:
        for k, v in p.items():
          output += str(k) +" : " + str(v) + "\n" 
        output += "\n-----------------------\n"
    print(output)
    return tempList

def priorityVal():
    print("Enter priority values for hp,att,def,spatk,spdef,speed: (seperated by spaces")
    prio = [int(x) for x in input().split()]
    for p in pokedex:
        p['coeff'] = int(p['hp'])/prio[0] + int(p['attack'])/prio[1] + int(p['defense'])/prio[2] + int(p['spatk'])/prio[3] + int(p['spdef'])/prio[4] + int(p['speed'])/prio[5]
    coeffSort()


createPokedex()    
priorityVal()

    