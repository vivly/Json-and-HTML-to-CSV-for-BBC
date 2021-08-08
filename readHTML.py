import pandas as pd
import bs4
import re


def readNews(news_path, index_path):
    csv_data = pd.read_csv(news_path)
    data_frame = pd.DataFrame(csv_data)
    column_list = list(data_frame)
    column_count = len(column_list)
    n = len(data_frame)
    for i in range(0, n):
        bs, data_frame = mainTextReader(i, index_path, data_frame)
        for k in range(1, column_count):
            try:
                block_content = data_frame.iloc[i, k]
                if pd.isnull(block_content):
                    raise NoContentException(i, column_list[k])
                else:
                    print("id为 " + str(i) + " 的 " + column_list[k] + " 列内容完整。")
            except NoContentException as e:
                print(e)
                data_frame = htmlReader(e.row, e.column, bs, data_frame)
    return data_frame

def mainTextReader(row, index_path,dataframe):
    index_csv_data = ''
    try:
        index_csv_data = pd.read_csv(index_path)
    except IOError as e:
        print("index文件不可用,程序退出。")
        quit()
    index_data_frame = pd.DataFrame(index_csv_data)
    html_path = index_data_frame.iloc[row, 4]
    html_file = open(html_path, 'rb').read()
    bs = bs4.BeautifulSoup(html_file, 'html.parser')
    main_text_list = []
    for x in bs.find_all(name='p'):
        main_text_string = x.get_text()
        main_text_list.append(main_text_string)
    main_text = ''.join(main_text_list)
    temp_dataframe = dataframe
    temp_dataframe.iloc[row, 4] = main_text
    return bs, temp_dataframe


def htmlReader(row, column, bs, dataframe):
    dict_for_keyword = {'title_page': titlePageModifier, 'title': titleModifier, 'description': descriptionModifier,
                        'url': urlModifier, 'image_url': imageUrlModifier, 'language': languageModifier,
                        'source_domain': sourceDomainModifier, 'date_publish':datePublishModifier}
    data_frame_modified = dict_for_keyword.get(column, defaultModifier)(bs, row, column, dataframe)
    return data_frame_modified


def titlePageModifier(bs, row, column, dataframe):
    temp_dataframe = dataframe
    temp_dataframe.iloc[row, 9] = bs.title.string
    printModifyResult(row, column)
    return temp_dataframe


def titleModifier(bs, row, column, dataframe):
    temp_dataframe = dataframe
    temp_dataframe.iloc[row, 2] = bs.h1.string
    printModifyResult(row, column)
    return temp_dataframe


def descriptionModifier(bs, row, column, dataframe):
    temp_dataframe = dataframe
    temp_dataframe.iloc[row, 3] = bs.b.string
    printModifyResult(row, column)
    return temp_dataframe


def urlModifier(bs, row, column, dataframe):
    url_formula = re.compile('(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')
    t_list = bs.find_all(name='meta', attrs={'data-rh': 'true', 'property': 'og:url'})
    url = url_formula.search(str(t_list[0])).group(0)
    temp_dataframe = dataframe
    temp_dataframe.iloc[row, 5] = url
    printModifyResult(row, column)
    return temp_dataframe


def imageUrlModifier(bs, row, column, dataframe):
    url_formula = re.compile('(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')
    t_list = bs.find_all(name='meta', attrs={'data-rh': 'true', 'property': 'og:image'})
    image_url = url_formula.search(str(t_list[0])).group(0)
    temp_dataframe = dataframe
    temp_dataframe.iloc[row, 6] = image_url
    printModifyResult(row, column)
    return temp_dataframe


def languageModifier(bs, row, column, dataframe):
    temp_dataframe = dataframe
    temp_dataframe.iloc[row, 7] = 'en'
    printModifyResult(row, column)
    return temp_dataframe


def sourceDomainModifier(bs, row, column, dataframe):
    temp_dataframe = dataframe
    temp_dataframe.iloc[row, 8] = 'bbc.com'
    printModifyResult(row, column)
    return temp_dataframe


def datePublishModifier(bs, row, column, dataframe):
    date_formula = re.compile(r'\d{4}-\d{1,2}-\d{1,2}T\d{1,2}:\d{1,2}:\d{1,2}')
    t_list = bs.find_all(name='time', attrs={'data-testid': 'timestamp'})
    date_time = date_formula.search(str(t_list[0])).group(0)
    temp = date_time.split("T")
    date_and_time = temp[0] + " " + temp[1]
    temp_dataframe = dataframe
    temp_dataframe.iloc[row, 1] = date_and_time
    printModifyResult(row, column)
    return temp_dataframe


def defaultModifier(bs, row, column, dataframe):
    return dataframe


def printModifyResult(row, column):
    print('修改完成！')


class NoContentException(Exception):
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __str__(self):
        return "id为 " + str(self.row) + " 的 " + self.column + " 列内容为空，正在修改..."


if __name__ == "__main__":
    rootPath = r"D:\news_set\data\test"
    news_csv_suffix = r'\news.csv'
    index_csv_suffix = r'\index.csv'
    news_path = rootPath + news_csv_suffix
    index_path = rootPath + index_csv_suffix
    dataframe = readNews(news_path, index_path)
    dataframe.to_csv(news_path, encoding='utf-8', index=False)
