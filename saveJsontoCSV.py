import os
import pandas as pd
import json


def savejsontocsv(index_path):
    if(os.path.exists(index_path)):
        csv_data = pd.read_csv(index_path)
        data_frame = pd.DataFrame(csv_data)
        for i in range(0, len(data_frame)):
            json_path = data_frame.iloc[0,2]
            with open(json_path, encoding='utf-8') as f:
                line = f.readline()
                try:
                    json.loads(line)
                except json.decoder.JSONDecodeError:
                    string_list = [line, '""}']
                    temp = ''
                    line = temp.join(string_list)
                d = json.loads(line)

                try:
                    date_publish = d['date_publish']
                except KeyError:
                    date_publish = ''
                try:
                    description = d['description']
                except KeyError:
                    description = ''
                try:
                    image_url = d['image_url']
                except KeyError:
                    image_url = ''
                try:
                    language = d['language']
                except KeyError:
                    language = ''
                try:
                    title = d['title']
                except KeyError:
                    title = ''
                try:
                    title_page = d['title_page']
                except KeyError:
                    title_page = ''
                try:
                    url = d['url']
                except KeyError:
                    url = ''
                try:
                    source_domain = d['source_domain']
                except KeyError:
                    source_domain = ''
                print(date_publish, title, url, source_domain)



    else:
        print("Index file does not exist, please generate index file first.")

if __name__ == '__main__':
    rootPath = r"D:\news_set\data\test"
    index_name_suffix = r'\index.csv'
    string_list = [rootPath, index_name_suffix]
    temp = ''
    save_index_path = temp.join(string_list)
    savejsontocsv(save_index_path)