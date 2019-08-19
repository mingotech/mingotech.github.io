#! /usr/bin/env python3

from datetime import datetime
import conf
import os

# cat_name -> tags {"tag": "remark"}
cats = {}

def select_category():
    print("目前Blog可用分类选项如下(\033[33m如果要增删,请修改conf.py文件\033[0m): ")
    default_cat = ""
    global cats

    for label_info in conf.label_tree:
        cat_name = label_info["category"]
        cat_remark = label_info["remark"]
        cats[cat_name] = label_info["tags"]
        print("\033[32m%-18s\033[0m→ \033[34m%-s\033[0m" % (cat_name, cat_remark))
        if "default" in label_info and label_info["default"]:
            default_cat = cat_name

    while True:
        category = input("\n请选择文章分类: ")
        if category.strip() == "" and default_cat != "":
            return default_cat
        elif category not in cats:
            print("\033[31m✖ 文章分类 #%s# 不存在,请重新输入\033[0m" % category)
        else:
            return category

def select_tags(cate):
    print("目前Blog可用标签选项如下(\033[33m如果要增删,请修改conf.py文件\033[0m): ")
    default_tag = ""
    global cats
    tags = {}
    for tag_info in cats[cate]:
        tag_name = tag_info["tag"]
        tag_remark = tag_info["remark"]
        tags[tag_name] = tag_remark
        print("\033[32m%-12s\033[0m→ \033[34m%-s\033[0m" % (tag_name, tag_remark))
        if "default" in tag_info and  tag_info["default"]:
            default_tag = tag_name

    while True:
        _raw_tags = input("\n请选择文件标签, \033[33m多个标签请使用空格分隔\033[0m: ")
        if _raw_tags.strip() == "" and default_tag != "":
            return [default_tag]

        _tags = _raw_tags.split(" ")

        is_all_right = True
        for _tag in _tags:
            if _tag not in tags:
                print("\033[31m✖ 文章标签 #%s# 不存在,请重新输入\033[0m" % _tag )
                is_all_right = False

        if is_all_right:
            return _tags

post_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

post_title = input("请输入文章标题: ")
print("\033[33m✔ %s \033[0m\n" % post_title)

file_name = input("请输入文件名: ")
post_name = "%s-%s.md" % (post_time.split(" ")[0], "-".join(file_name.split(" ")))
print("\033[33m✔ %s \033[0m\n" % (post_name))

category = select_category()
print("\033[33m✔ %s \033[0m\n" % (category, ))

tags = []
tags = tags + select_tags(category)
print("\033[33m✔ %s \033[0m\n" % (tags, ))

is_original = input("是否原创(1: original, 2: note): ")
a_tag = "original" if is_original == "1" else "note"
print("\033[33m✔ %s \033[0m\n" % (a_tag, ))
tags.append(a_tag)

final_tag = ",".join("\"%s\"" % wrap for wrap in tags)

is_star = input("是否要加标[y/n]: ")
star = "true" if is_star == "Y" or is_star == "y" else "false"
print("\033[33m✔ %s \033[0m\n" % (star))

content = conf.post_tpl % {"title": post_title, "post_time": post_time, "category": category, "tag": final_tag, "star": star}
#print(content)

final_path = "_posts/%s%s" % (category + "/" if category != "other" else "", post_name)
final_path = "_posts"
if category != "other":
    final_path = "_posts/" + category
    if not os.path.exists(final_path):
        os.makedirs(final_path)

md = open("%s/%s" % (final_path, post_name), "w")
md.write(content)

md.close()
print("\033[33m✔ 初始化文章完成 \033[0m\n")
