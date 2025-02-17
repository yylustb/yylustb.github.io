---
title: "一键安装ROS1"
# 文章摘要，通常用于 列表页面 或 SEO 描述
summary: Read aboout Install and Update instructions and sampled configuration templates
# 文章的发布日期，未来时间不会发布
date: 2025-02-11
# 文章所属的 系列，可以用 series 在 Hugo 的主题（如 PaperMod）中生成一个系列的导航
series: ["PaperMod"]
weight: 1
# 旧的 URL 映射到这个页面，防止 404 错误（适用于 URL 变更）。
aliases: ["/ros-installation"]
# 文章的标签（关键词），用于 Hugo 的 标签分类（类似于博客的 tag）
tags: ["Ubuntu", "ROS1"]
author: ["Yongliang Yang", "杨永亮"]
cover:
  # 图片路径
  image: images/papermod-cover.png
  # 在文章列表中隐藏封面图，但在文章页面内可能会显示。
  hiddenInList: true
  
---


## 1.安装必要软件

一行代码搭建机器人开发环境(ROS/ROS2/ROSDEP)

  ```Powershell
  wget http://fishros.com/install -O fishros && . fishros
  ```

选项：
- [1] 安装 noetic(ros1)
- [3] 安装 rosdep









