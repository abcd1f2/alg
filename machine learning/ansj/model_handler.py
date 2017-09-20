#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re

class ModelHandler(object):
    def __init__(self, model_file):
        self.modelfile_ = model_file
        self.unigram = {}
        self.bigram = {}
        self.trigram = {}

    def Init(self):
        flag = 0
        with open(self.modelfile_, "rb") as f:
            for line in f.xreadlines():
                line = line.strip()
                if flag == 0:
                    if line.endswith("1-grams:"):
                        flag = 1
                        continue
                elif flag == 1:
                    if line.endswith("2-grams:"):
                        flag = 2
                        continue
                    result = re.split(" |\t", line)
                    if len(result) == 3:
                        self.unigram[result[1]] = result[0]
                elif flag == 2:
                    if line.endswith("3-grams:"):
                        flag = 3
                        continue
                    result = re.split(" |\t", line)
                    if len(result) == 4:
                        self.bigram[result[1]] = {result[2]:result[0]}
                elif flag == 3:
                    result = re.split(" |\t", line)
                    if len(result) == 4:
                        self.trigram[result[1]] = {result[2]:{result[3]:result[0]}}
