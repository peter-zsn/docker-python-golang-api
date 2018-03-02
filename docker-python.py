#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: docker-test.py
@time: 2018/3/2 10:17
"""

import docker

d = docker.Client(base_url="192.168.42.133:2375", version='auto', timeout=20)
print d.version()    # 查看docker的版本
print d.images()    # 查看docker 所有的镜像
old_test = d.containers(all=True, filters={'name': "test"})         # 遍历所有容器得到当前镜像的状态
if old_test:
    old_test_1 = d.inspect_container("test")  # 得到当前容器的状态
    print old_test_1['State']['Status']                             # 得到该容器目前的状态
    # d.remove_container("test")    # 删除某个容器
    d.start("test")                 # 运行某个容器
    d.stop("test")                  # 停止某个容器
else:
    d.create_container("15294627382/baseos:1.0", command="/bin/sh", name="test")    # 创建容器


