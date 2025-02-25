---
title: "Python 系列 - 1. 命令行解析器 argparse"
summary: Learn About argparse in Python
date: 2025-02-13
weight: 1
aliases: ["/python-argparse"]
tags: ["argparse"]
categories: ["Python"]
author: ["Yongliang Yang"]
cover:
  image: images/papermod-cover.png
---




## 1.什么是 argparse

`argparse` 是一个强大的命令行参数解析工具，用于构建命令行脚本或程序时，可以非常方便地对传入的参数进行解释和处理。

在编写命令行工具或脚本时，往往需要接收来自命令行的参数或选项，以实现配置。

`argparse` 则能让你以更高层次、更结构化的方式来定义程序期望的参数形式，以及如何处理这些参数，从而自动生成帮助信息、错误信息等。

## 2.基本用法



```python
import argparse

def main():
    '''第一步：创建一个解析器对象，可以给出程序的简单描述'''
    parser = argparse.ArgumentParser(description="这是一个示例命令行工具")

    '''第二步：添加命令行参数和选项'''
    # 添加必选参数: 在命令中不需要特意写 -x 或者 --xx ，是脚本必须要获取的数据。
    parser.add_argument("filename", help="输入文件的路径")
    # 添加可选参数1：一般以短选项（如 -v）或长选项（如 --verbose）的形式出现。
    parser.add_argument("-v", "--verbose", 
                        action="store_true", 
                        help="是否输出详细信息（布尔开关）"
                        )
    # 添加可选参数2：一般以短选项（如 -v）或长选项（如 --verbose）的形式出现。
    parser.add_argument("-n", "--number",
                        type=int,
                        default=1,
                        help="重复操作次数，默认为 1"
                        )
    # 添加可选参数3：接收某个范围或集合中的值
    parser.add_argument("--mode", 
                        choices=["train", "test", "eval"], 
                        help="模式选择"
                        )
    # 添加可选参数4：指定参数的别名
    parser.add_argument("-m", "--mode", 
                        choices=["train", "test", "eval"]
                        )




    '''第三步：解析命令行参数'''
    # args 就是一个包含解析后参数的命名空间对象, 属性名即为参数名。
    args = parser.parse_args()
    # 通过 args.filename 访问参数 filename
    print("文件名：", args.filename)
    print("是否详细输出：", args.verbose)
    print("操作次数：", args.number)

if __name__ == "__main__":
    main()
```

- 必选参数：
    - `help="输入文件的路径"`: 在 `--help` 命令中显示的参数说明
    - 当执行脚本时，需要紧随其后提供必选参数 filename，否则会报错。例如（下面指令中的 `input.txt` 就是参数 "filename"）
    ```bash
    python script.py input.txt
    ```
    
- 可选参数1：
    - `-v` 和 `--verbose`: 代表同一个可选参数，用户可以使用任一形式。
    - `action="store_true"`: 当这个选项被使用时，将在解析结果中把 `verbose` 设置为 `True`（不使用则为 `False`）。
    - `help="是否输出详细信息（布尔开关）"`: help 中的内容会在 `--help` 命令中显示。
- 可选参数2：
    - `type=int`：将输入值转换为整数类型（如果传入值无法转换会报错）。
    - `default=1`：当用户没有提供该参数时，使用默认值 1。


定义完上面的代码文件后，在命令行的执行如下

```bash
# 带所有参数
python script.py myfile.txt -v -n 3
# 或者：python script.py myfile.txt --verbose --number 3

# 不带可选参数
python script.py myfile.txt
```