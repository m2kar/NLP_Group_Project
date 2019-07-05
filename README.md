NLP小组作业
===============
# 研究内容：
文本分类

## 依赖项
* sudo apt install python3.7 python3.7-pip
* pip3 install https://download.pytorch.org/whl/cu100/torch-1.1.0-cp37-cp37m-linux_x86_64.whl
* pip3 install https://download.pytorch.org/whl/cu100/torchvision-0.3.0-cp37-cp37m-linux_x86_64.whl
* pip3 install jieba

## 词向量
https://github.com/Embedding/Chinese-Word-Vectors<br>
（这里用的是Zhihu_QA 知乎问答训练出来的word Word2vec）

## 用法
```bash
python3 main.py -h
python3 main.py -static=true -non-static=true -multichannel=true
```

## 准确率

|    数据集    | 随机初始化词向量    | 使用预训练的静态词向量 | 微调预训练的词向量  | 微调加静态          |
|:------------:|---------------------|------------------------|---------------------|---------------------|
| 开发用二分类 | 94.0000%(6616/7000) | 95.0000%(6679/7000)    | 96.0000%(6729/7000) | 96.0000%(6744/7000) |
| 课程提供     |                     |                        |                     |                     |
|              |                     |                        |                     |                     |

# 作者：

 - 孙旭 (实验)
 - 杨爽 (实验)
 - 芮志清 (报告+PPT)
 - 王丽敏 (PPT+报告)
 

**单位:** 中国科学院大学人工智能学院

# 参考：
 - https://github.com/bigboNed3/chinese_text_cnn
 - [Convolutional Neural Networks for Sentence Classification](https://arxiv.org/abs/1408.5882)

