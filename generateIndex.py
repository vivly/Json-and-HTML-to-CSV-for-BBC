import os
import pandas as pd


def getIndexList(path, suffix):
    inputFileName = []
    inputFilePath = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if os.path.splitext(name)[1] == suffix:
                inputFileName.append(name)
                inputFilePath.append(os.path.join(root, name))
    return inputFileName, inputFilePath


def saveIndex(json_name_list, json_path_list, html_name_list, html_path_list, save_path):
    dataframe = pd.DataFrame({'Json Name List': json_name_list, 'Json Path List': json_path_list,
                              'HTML Name List': html_name_list, 'HTML Path List': html_path_list})
    dataframe.index.name = 'id'
    dataframe.to_csv(save_path, encoding='utf-8')


if __name__ == '__main__':
    root_path = r"D:\news_set\data\test"
    index_json_suffix = r'\index.csv'
    save_json_index_path = root_path + index_json_suffix
    jsonNameList, jsonPathList = getIndexList(root_path, '.json')
    htmlNameList, htmlPathList = getIndexList(root_path, '.html')
    saveIndex(jsonNameList, jsonPathList, htmlNameList, htmlPathList, save_json_index_path)

