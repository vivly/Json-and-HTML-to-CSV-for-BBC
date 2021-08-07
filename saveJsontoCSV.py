import os
import pandas as pd
import json


def savejsontocsv(index_path, csv_path):
    if(os.path.exists(index_path)):
        csv_data = pd.read_csv(index_path)
        csv_data_frame = pd.DataFrame(csv_data)
        for i in range(0, 1):
            json_path = csv_data_frame.iloc[0,2]
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
                try:
                    main_text = d['maintext']
                except KeyError:
                    main_text = ''

                if(os.path.exists(csv_path)):
                    pass
                else:
                    column_list = ['date_publish', 'title', 'description', 'main_text', 'url', 'image_url', 'language',
                                   'source_domain', 'title_page']
                    data_list = [date_publish, title, description, main_text, url, image_url, language,
                                 source_domain, title_page]
                    data_dict = dict(zip(column_list, data_list))
                    print(date_publish)
                    data_frame = pd.DataFrame(columns=column_list)
                    data_frame = data_frame.append(data_dict, ignore_index=True)
                    data_frame.to_csv(csv_path, encoding='utf-8')



    else:
        print("Index file does not exist, please generate index file first.")

if __name__ == '__main__':
    rootPath = r"D:\news_set\data\test"
    index_name_suffix = r'\index.csv'
    news_csv_suffix = r'\news.csv'
    string_list_1 = [rootPath, index_name_suffix]
    string_list_2 = [rootPath, news_csv_suffix]
    temp = ''
    save_index_path = temp.join(string_list_1)
    save_news_path = temp.join(string_list_2)
    savejsontocsv(save_index_path, save_news_path)