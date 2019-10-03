# create 脚本所需要常量定义

# 标签树
# level1: category
# level2: tag
label_tree = [
    {
        "category": "mysql",
        "remark": "MySQL相关",
        "tags": [
            {"tag": "Innodb", "remark": "Innodb索引说明"},
            {"tag": "事务", "remark": "事务相关"},
            {"tag": "mysql", "remark": "mysql通用相关", "default": True},
        ]
    },

    {
        "category": "cache",
        "remark": "Cache相关",
        "tags": [
            {"tag": "redis", "remark": "redis使用相关", "default": True},
            {"tag": "memcache", "remark": "memcache相关"},
        ]
    },

    {
        "category": "mq",
        "remark": "MessageQueue相关",
        "tags": [
            {"tag": "kafaka", "remark": "kafaka使用相关", "default": True},
            {"tag": "RocketMQ", "remark": "RocketMQ使用相关"},
        ]
    },

    {
        "category": "zk",
        "remark": "Zookeeper相关",
        "tags": [
            {"tag": "zk算法", "remark": "zk使用算法,理论"},
            {"tag": "zk", "remark": "zk通用相关", "default": True},
        ]
    },

    {
        "category": "lib",
        "remark": "各种库的使用说明, 源码分析",
        "tags": [
            {"tag": "RxJava", "remark": "RxJava框架"},
            {"tag": "Spring", "remark": "Spring框架", "default": True},
        ]
    },

    {
        "category": "test",
        "remark": "测试相关,性能测试,安全测试",
        "tags": [
            {"tag": "ab", "remark": "ab测试", "default": True},
        ]
    },

    {
        "category": "tool",
        "remark": "软件开发工具类",
        "tags": [
            {"tag": "fiddler", "remark": "fiddler网络抓包工具"},
            {"tag": "awk", "remark": "awk使用技巧", "default": True},
            {"tag": "tcpdump", "remark": "tcpdump网络抓包工具"},
            {"tag": "strace", "remark": "strace工具说明"},
        ]
    },

    {
        "category": "python",
        "remark": "Python相关的总结",
        "tags": [
            {"tag": "python", "remark": "python常用点说明", "default": True},
        ]
    },

    {
        "category": "java",
        "remark": "Java相关的心得体会",
        "tags": [
            {"tag": "jvm", "remark": "jvm总结"},
            {"tag": "gc", "remark": "gc总结"},
            {"tag": "java", "remark": "java常用点说明", "default": True},
        ]
    },

    {
        "category": "golang",
        "remark": "Golang相关的心得体会",
        "tags": [
            {"tag": "golang", "remark": "golang常用点说明", "default": True},
        ]
    },

    {
        "category": "unix",
        "remark": "unix服务器使用,配置,调优相关",
        "tags": [
            {"tag": "shell", "remark": "shell说明", "default": True},
            {"tag": "bash", "remark": "bash编程"},
            {"tag": "net", "remark": "网络编程"},
        ]
    },

    {
        "category": "net",
        "remark": "网络相关",
        "tags": [
            {"tag": "tcp/udp", "remark": "tcp/udp编程"},
            {"tag": "net", "remark": "net常用点总结", "default": True},
        ]
    },

    {
        "category": "perf",
        "remark": "性能调优相关",
        "tags": [
            {"tag": "perf", "remark": "perf常用点总结"},
        ]
    },

    {
        "category": "cloud",
        "remark": "云应用相关",
        "tags": [
            {"tag": "docker", "remark": "docker常用点总结"},
            {"tag": "k8s", "remark": "k8s常用点总结", "default": True},
        ]
    },

    {
        "category": "arch",
        "remark": "架构相关",
        "tags": [
            {"tag": "arch", "remark": "arch常用点总结", "default": True},
        ]
    },

    {
        "category": "design-patterns",
        "remark": "设计模式",
        "tags": [
            {"tag": "design-patterns", "remark": "design-patterns常用点总结", "default": True},
        ]
    },

    {
        "category": "other",
        "remark": "文章暂时还没想好归类的",
        "default": True,
        "tags": [
            {"tag": "other", "remark": "other常用点总结", "default": True},
        ]
    },
]
       
post_tpl = """---
title       : "%(title)s"
author      : "mingo"
date        : "%(post_time)s"

layout      : post
category    : %(category)s
tag         : [%(tag)s]
blog        : true
star        : %(star)s
---

## 概述

写这文章的背景, 是为了记录什么心得, 还是宣传什么库/产品

读这文章的好处, 能有何收获, 从利人利已角度都可以

## What 

什么是XX

## Why

为什么要用XX

## How 

XX怎么用

## 进阶

XX实现原理, 架构设计, 指导理论, 精妙算法

## 其它

- 使用过程中有没有遇到坑
- 使用技巧, 骚操作
- 八卦,趣闻

## 参考
- [引用链接1](http://ref.post.com/)

"""

