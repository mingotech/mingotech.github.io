#! /usr/bin/env python3

from datetime import datetime
import conf

def select_category():
    print("目前Blog可用分类选项如下(\033[33m如果要增删,请修改conf.py文件\033[0m): ")
    default_cat = ""
    for (cat_name, cat_info) in conf.categories.items():
        print("\033[32m%-12s\033[0m→ \033[34m%-s\033[0m" % (cat_name, cat_info["remark"]))
        if cat_info["default"]:
            default_cat = cat_name

    while True:
        category = input("\n请选择文章分类: ")
        if category.strip() == "" and default_cat != "":
            return default_cat
        elif category not in conf.categories:
            print("\033[31m✖ 文章分类 #%s# 不存在,请重新输入\033[0m" % category)
        else:
            return category

def select_tags():
    print("目前Blog可用标签选项如下(\033[33m如果要增删,请修改conf.py文件\033[0m): ")
    default_tag = ""
    for (tag_name, tag_info) in conf.tags.items():
        print("\033[32m%-12s\033[0m→ \033[34m%-s\033[0m" % (tag_name, tag_info["remark"]))
        if tag_info["default"]:
            default_tag = tag_name

    while True:
        _raw_tags = input("\n请选择文件标签, \033[33m多个标签请使用空格分隔\033[0m: ")
        if _raw_tags.strip() == "" and default_tag != "":
            return (default_tag)

        _tags = _raw_tags.split(" ")

        is_all_right = True
        for _tag in _tags:
            if _tag not in conf.tags:
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

tags = select_tags()
print("\033[33m✔ %s \033[0m\n" % (tags, ))

is_star = input("是否要加标[y/n]: ")
star = "true" if is_star == "Y" or is_star == "y" else "false"
print("\033[33m✔ %s \033[0m\n" % (star))

content = conf.post_tpl % {"title": post_title, "post_time": post_time, "category": category, "tag": tags, "star": star}
#print(content)

md = open("_posts/%s" % post_name, "w")
md.write(content)

md.close()
