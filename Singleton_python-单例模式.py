# coding=utf-8
######################
#
#   这个例子没有加锁，不能用于多线程模式，如果有需要请自行加上
#
#######################

import time


class Test(object):
    __instance_test = None
    flag = False

    def __init__(self):
        if not Test.flag:
            raise
        self.a = 1

    @staticmethod
    def get_instance():
        if Test.__instance_test is None:
            Test.flag = True
            Test.__instance_test = Test()
            Test.flag = False
        return Test.__instance_test

    def print_num(self):
        print self.a
        time.sleep(0.5)
        self.add_num()

    def add_num(self):
        self.a += 1


test = Test.get_instance()
