import pickle

# 修改路径为自己文件夹即可
FILE_PATH = r'C:\Users\xuzhou123\Desktop\排序\generated_data.pkl'

def load_nums():
    with open(FILE_PATH, 'rb') as f:
        return pickle.load(f)


def file_path():
    return FILE_PATH
