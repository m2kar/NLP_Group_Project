import pandas as pd
import numpy as np

# devdata = pd.read_csv('devdata.txt', sep=" ", header=None)
# print(devdata[0])


def txt_to_csv(name):
    label_list = []
    content_list = []
    with open(f'{name}data.txt', 'r') as f:
        for line in f:
            label, content = line.split('	')
            word_list = content.split()
            label_list.append(label)
            content_list.append(''.join(word_list))

    df = pd.DataFrame({'label': label_list,
                    'content': content_list})
    df.to_csv(f'{name}.csv')

txt_to_csv('dev')
txt_to_csv('test')


txt_to_csv('train')
