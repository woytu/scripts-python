#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author : bajins www.bajins.com
# @File : ObjectUtil.py
# @Version: 1.0.0
# @Time : 2019/8/22 9:11
# @Project: windows-wallpaper-python
# @Package: 
# @Software: PyCharm
import inspect
import re


def get_object_method(genus):
    """
    获取类中所有方法
    :param genus:类
    :return:
    """
    func_list = []
    for m in genus.__all__:
        _class = getattr(genus, m)
        for name, value in inspect.getmembers(_class):
            if not name.startswith("_"):
                func_list.append(name)
    return func_list


def dict_to_str(dictionary):
    """
    将字典转成字符串
    :param dictionary:字典
    :return:
    """
    s = ''
    for i in dictionary:
        val = ''
        if dictionary[i] is not None:
            val = dictionary[i]
        s = s + i + ': ' + val + '\r\n'
    return s


def array_to_str(array):
    """
    数组转字符串
    :param array: 数组
    :return:
    """
    # eval(array)
    return ''.join(array)


def typeof(variate):
    """
    判断变量类型
    isinstance() 与 type() 区别：
        type() 不会认为子类是一种父类类型，不考虑继承关系。
        isinstance() 会认为子类是一种父类类型，考虑继承关系。
        如果要判断两个类型是否相同推荐使用 isinstance()。
    :param variate:
    :return:
    """
    this_type = None
    if isinstance(variate, int):
        this_type = "int"
    elif isinstance(variate, str):
        this_type = "str"
    elif isinstance(variate, float):
        this_type = "float"
    elif isinstance(variate, list):
        this_type = "list"
    elif isinstance(variate, tuple):
        this_type = "tuple"
    elif isinstance(variate, dict):
        this_type = "dict"
    elif isinstance(variate, set):
        this_type = "set"
    return this_type


def remove_array_repeat(array):
    """
    去除数组中重复的元素
    :param array:
    :return:
    """
    array2 = []
    for i in array:
        if i not in array2:
            array2.append(i)
    # list(set(s))
    return array2


def remove_child_in_array(array, child_array):
    """
    移除数组在子数组中的元素
    :param array: 数组
    :param child_array: 子数组
    :return:
    """
    for a in array:
        for child in child_array:
            if child in a:
                array.remove(a)


def is_in_array(arg, array):
    """
    判断元素是否存在数组中
    :param arg:元素
    :param array:数组
    :return:
    """
    for a in array:
        if re.match("^.*" + a + ".*", arg):
            return True
    return False
