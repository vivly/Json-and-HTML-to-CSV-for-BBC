import pandas as pd
import numpy as np


def readCsv(newspath):
    csv_data = pd.read_csv(newspath)
    data_frame = pd.DataFrame(csv_data)
    print("新闻数据集中是否存在空值：" + str(np.any(data_frame.isnull())))


if __name__ == "__main__":
    rootPath = r"D:\news_set\data\Europe\Italy\8-6"
    news_csv_suffix = r'\news.csv'
    index_csv_suffix = r'\index.csv'
    news_path = rootPath + news_csv_suffix
    index_path = rootPath + index_csv_suffix
    readCsv(news_path)
