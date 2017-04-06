#!/usr/bin/python
# -*- coding: utf-8 -*-

class Ant(object):
    def __init__(self, ID):
        self.ID = ID
        self.__clean_data()

    #初始化数据
    def __clean_data(self):
        #蚂蚁走过的路径集合
        self.path = []
        #蚂蚁走过的路径总长度
        self.total_distance = 0.0
        #蚂蚁走过的城市数
        self.steps = 0
        #蚂蚁当前所在城市,初始化为-1
        self.current_city = -1
        #range返回的是一个包含所有元素的列表，xrange返回的是一个生成器，生成器是一个可迭代对象，在对生成器进行迭代时，
        #元素是逐个被创建的。一般来看，在对大序列进行迭代的时候，因为xrange的特性，所以它会比较节约内存。
