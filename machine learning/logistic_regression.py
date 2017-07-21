#coding=utf-8

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression

def logistic_regression():
    x = list()
    #用于训练
    x.append("fuck you")
    x.append("fuck you all")
    x.append("hello body")

    #用于测试
    x.append("fuck")
    x.append("hello")

    y = [1,1,0]
    ve = TfidfVectorizer()
    x_train = ve.fit_transform(x[:-2])
    x_test = ve.transform(x[-2:])

    lr = LogisticRegression()
    print lr.fit(x_train, y)

    print lr.predict(x_test)


if __name__ == '__main__':
    logistic_regression()
