import os
import pandas as pd
import json


def getJsonList(path, suffix):
    inputFileName = []
    inputFilePath = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if os.path.splitext(name)[1] == suffix:
                inputFileName.append(name)
                inputFilePath.append(os.path.join(root, name))
    return inputFileName, inputFilePath


def saveindex(nameList, pathList, save_path):
    dataframe = pd.DataFrame({'Name List': nameList, 'Path List': pathList})
    dataframe.to_csv(save_path, encoding='utf-8')

if __name__ == '__main__':
    rootPath = r"D:\news_set\data\test"
    index_name_suffix = r'\index.csv'
    string_list = [rootPath,index_name_suffix]
    temp = ''
    save_index_path = temp.join(string_list)
    jsonNameList, jsonPathList = getJsonList(rootPath, '.json')
    saveindex(jsonNameList, jsonPathList, save_index_path)

