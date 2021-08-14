import os
import pandas as pd
import json


def save_json_to_csv(index_path, csv_path):
    if os.path.exists(index_path):
        csv_data = pd.read_csv(index_path)
        csv_data_frame = pd.DataFrame(csv_data)
        n = len(csv_data)
        column_list = ['date_publish', 'title', 'description', 'main_text', 'url', 'image_url', 'language',
                       'source_domain', 'title_page']
        data_frame = pd.DataFrame(columns=column_list)
        for i in range(0, n):
            json_path = csv_data_frame.iloc[i, 2]
            with open(json_path, encoding='utf-8', errors='ignore') as f:
                line = f.readline()
                try:
                    json.loads(line)
                except json.decoder.JSONDecodeError:
                    line = line + '""}'
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
                    main_text = ''
                except KeyError:
                    main_text = ''

                data_list = [date_publish, title, description, main_text, url, image_url, language,
                             source_domain, title_page]
                data_dict = dict(zip(column_list, data_list))
                data_frame = data_frame.append(data_dict, ignore_index=True)
        data_frame.index.name = 'id'
        data_frame.to_csv(csv_path, encoding='utf-8')

    else:
        print("Index file does not exist, please generate index file first.")


if __name__ == '__main__':
    rootPath = r"D:\news_set\data\Europe\Italy\8-6"
    index_name_suffix = r'\index.csv'
    news_csv_suffix = r'\news.csv'
    save_index_path = rootPath + index_name_suffix
    save_news_path = rootPath + news_csv_suffix
    save_json_to_csv(save_index_path, save_news_path)
