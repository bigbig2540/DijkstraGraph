# -*- coding: utf-8 -*-
#"""
#Created on Wed Oct  4 19:52:19 2017
#
#@author: MSR
#"""
import pandas as pd
import numpy as np
graphMatrix = dict()
#graphMatrix = { 'a' : {'b':3,'c':2,'g':4,'k':2},
#                'b' : {'a':3,'d':5,'e':4,'g':1},
#                'c' : {'a':2,'e':3},
#                'd' : {'b':5,'f':2,'j':3,'z':2},
#                'e' : {'b':4,'c':3,'f':1},
#                'f' : {'d':2,'e':1,'z':5},
#                'g' : {'a':4,'b':1,'j':7,'k':6},
#                'h' : {'i':7,'k':4},
#                'i' : {'h':7,'j':4,'z':3},
#                'j' : {'d':3,'g':7,'i':4},
#                'k' : {'a':2,'g':6,'h':4},
#                'z' : {'d':2,'f':5,'i':3} }


def genGraphMatrix():
    df = pd.read_csv('matrix2.csv')
    graphMatrix = dict()
   
    for x in range (0 , df.shape[0]):
        ind = str(df['NaN'].values[x])
        #print(df['NaN'].values[x])
        graphMatrix[ind] = dict()
        for y in range (0 , df.shape[0]):
            if df[ind][y] != 0:
                indY = str(df['NaN'].values[y])
                graphMatrix[ind][indY] = df[ind][y]
                #print(df['NaN'].values[y] , ' ' ,df[df['NaN'].values[x]][y])
    return graphMatrix


#def genGraphMatrix():
#    df = pd.read_csv('matrix.csv')
#    graphMatrix = dict()
#   
#    for x in range (0 , df.shape[0]):
#        index = str(df['NaN'].values[x])
#        #print(df['NaN'].values[x])
#        graphMatrix[df['NaN'].values[x]] = dict()
#        for y in range (0 , df.shape[0]):
#            if df[df['NaN'].values[x]][y] != 0:
#                graphMatrix[df['NaN'].values[x]][df['NaN'].values[y]] = df[df['NaN'].values[x]][y]
#                #print(df['NaN'].values[y] , ' ' ,df[df['NaN'].values[x]][y])
#    return graphMatrix
                       
def findLeastCost(result):
    leastNode = ''
    leastValue = 99999
    for node , value in result.items():
        if value[0] == 'F' :
            if value[1] < leastValue : 
                leastNode = node
                leastValue = value[1]
    return leastNode
        
def adjNodeUpdate(currentNode , result, startNodeMatrix):
    result[currentNode][0] = 'T'
    for adjNode , distance in startNodeMatrix.items():
#      print(adjNode , ' distace ' , distance)
      if result[adjNode][0]=='F' :
#          print('in 1 if ' , result[adjNode])
          if result[adjNode][1] > (result[currentNode][1] + distance) :
#              print('in 2 if ' , result[adjNode])
              result[adjNode][1] = result[currentNode][1] + distance
              result[adjNode][2] = currentNode
    return result
#   main prog
def genResultMatrix():
    result = dict()
    for node , adjNode in graphMatrix.items():
        result[node] = ['F',99999,-1]
    return result

def printPath(result, destinationNode , startNode):
    if destinationNode == startNode:
        print(destinationNode )     
        return
    printPath(result, result[destinationNode][2] , startNode)
    print(destinationNode, ' ' , result[destinationNode][1])
    

currentNode = ""
graphMatrix = genGraphMatrix()
result = genResultMatrix()


print(graphMatrix)

startNode = input("input Start Node : ")

destinationNode = input("input Destination Node : ")

result[startNode] = ['T',0,-1]

currentNode = startNode

if len(graphMatrix[destinationNode])==0 :
    print("No Path Found Destination Node is Isolate")
    
else:
    while True :
#        print(result , currentNode)
        if result[destinationNode][0] == 'T':
            break
    
        result=adjNodeUpdate(currentNode , result , graphMatrix[currentNode] )
         
        currentNode = findLeastCost(result)
    
    print('Total Distance : ',result[destinationNode][1])
    printPath(result,destinationNode,startNode)
#    

