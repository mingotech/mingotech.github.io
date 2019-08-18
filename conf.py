# create 脚本所需要常量定义

tags = {
        "MySQL": {"default": False, "remark": "MySQL相关"},
        "other": {"default": True, "remark": "文章暂时不好分类可使用此tag"}
}

categories = {
        "public": {"default": "true", "remark": "是否是公开的"}

}

post_tpl = """---
title       : "%(title)s"
author      : "mingo"
date        : "%(post_time)s"

layout      : post
category    : %(category)s
tag         : %(tag)s
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

