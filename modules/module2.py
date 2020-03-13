#!/usr/bin/env python
# coding: utf-8

def getMeanValue(valueList):
    """
    Calculate the mean (average) value from a list of values.
    Input: list of integers/floats
    Output: mean value
    """
    valueTotal = 0.0
 
    for value in valueList:
        valueTotal += value
    numberValues = len(valueList)
    
    return (valueTotal/numberValues)
 
def compareMeanValueOfLists(valueList1,valueList2):
 
    """
    Compare the mean values of two lists of values.
    Input: valueList1, valueList2
    Output: Text describing which of the valueLists has the highest average value
    """
 
    meanValueList1 = getMeanValue(valueList1)
    meanValueList2 = getMeanValue(valueList2)
 
    if meanValueList1 == meanValueList2:
        outputText = "The mean values are the same ({:.2f}).".format(meanValueList1)
    elif meanValueList1 > meanValueList2:
        outputText = "List1 has a higher average ({:.2f}) than list2 ({:.2f}).".format(meanValueList1,meanValueList2)
    else:
        # No need to compare again, only possibility left
        outputText = "List2 has a higher average ({:.2f}) than list1 ({:.2f}).".format(meanValueList2,meanValueList1)
 
    return outputText
 




