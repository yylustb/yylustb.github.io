---
title: "Python系列2. tensorboard"
# 文章摘要，通常用于 列表页面 或 SEO 描述
summary: Python tensorboard
# 文章的发布日期，未来时间不会发布
date: 2025-02-15
# 文章所属的 系列，可以用 series 在 Hugo 的主题（如 PaperMod）中生成一个系列的导航
series: ["Python"]
weight: 1
# 旧的 URL 映射到这个页面，防止 404 错误（适用于 URL 变更）。
aliases: ["/python-tensorboard"]
# 文章的标签（关键词），用于 Hugo 的 标签分类（类似于博客的 tag）
tags: ["Pyhton", "tensorboard"]
author: ["Yongliang Yang"]
cover:
  # 图片路径
  image: images/papermod-cover.png
  # 在文章列表中隐藏封面图，但在文章页面内可能会显示。
  hiddenInList: true  
---




## 1. PyTorch 中使用 TensorBoard

通过 SummaryWriter 记录数据
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter
import numpy as np

# 初始化 TensorBoard 记录器

writer = SummaryWriter(log_dir="runs/experiment_1")

# 创建一个简单的模型
model = nn.Linear(1, 1)
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 训练循环
for epoch in range(100):
    x = torch.tensor([[epoch]], dtype=torch.float32)
    y = torch.tensor([[2 * epoch + 1]], dtype=torch.float32)
    
    output = model(x)
    loss = criterion(output, y)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # 记录损失
    writer.add_scalar("Loss/train", loss.item(), epoch)

    # 记录权重和梯度
    for name, param in model.named_parameters():
        writer.add_histogram(name, param, epoch)
        writer.add_histogram(f"{name}.grad", param.grad, epoch)

writer.close()
```
在终端启动 TensorBoard
```bash
tensorboard --logdir=runs --port=6006
```

## 2. TensorFlow 中使用 TensorBoard

记录数据（不需要 SummaryWriter）
```python
import tensorflow as tf
import datetime

# 创建日志目录
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# 创建一个简单模型，指定 NN 结构 
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

# 指定NN训练方法为 adam, 损失函数为 SparseCategoricalCrossentropy
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# 训练模型，并使用 TensorBoard 记录
model.fit(
            tf.random.normal([1000, 32]), tf.random.uniform([1000], 
            maxval=10, dtype=tf.int32), epochs=5, callbacks=[tensorboard_callback]
            )

```
在终端启动 TensorBoard
```bash
tensorboard --logdir=logs/fit --port=6006
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

## 3. 分析

为什么一个是 `--logdir=runs` 另一个是 `--logdir=logs`

- PyTorch 示例中，日志记录路径是 `"runs/experiment_1"`， `runs/` 是 `SummaryWriter(log_dir="runs/experiment_1")` 指定的路径的父目录
- TensorFlow 示例 中，日志记录路径是 `"logs/fit/..."`，`logs/fit/` 是 `log_dir` 变量中的路径前缀
- PyTorch 通常默认使用 `"runs/"` 作为日志目录，SummaryWriter 就是这么做的。
- TensorFlow 示例中，通常使用 `"logs/fit/" + datetime` 作为日志目录，所以 TensorBoard 需要从 `"logs/fit"` 读取数据。