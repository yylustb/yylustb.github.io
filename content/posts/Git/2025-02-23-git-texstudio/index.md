---
title: "Git 系列 - 3. Texstudio 同步 Git"
summary: Learn About All Features in PaperMod
date: 2025-02-23
weight: 1
aliases: ["/git-texstudio"]
tags: ["Git", "Texstudio"]
categories: ["Git"]
author: ["Yongliang Yang"]
cover:
  image: images/git.png
---

### 原理
Texstudio 编译 A/main.tex，本质上是 cmd 进入路径 A，然后执行
```bash
pdflatex main.tex
```
因为推送本地仓库到 github 需要在 cmd 执行 git 指令
```bash
git add .                     
git commit -m "First Submit"  
git branch -M main            
git push -u origin main       
```
所以如果可以利用texstudio在tex文件路径执行上述指令，即可实现仅通过texstudio推送tex文件至github


### TexStudio 配置
texstudio 中如下配置

![regular](images/git_texstudio.png)

Tools -> User -> Git command 
等价于在命令行<mark>当前目录</mark>下执行 Git command

### 如何实现
第一次推送需要命令行，后续推送仅需texstudio

第一次推送：
```bash
git init
git remote add origin github_SSH_address
git add .                     # 每次推送执行
git commit -m "First Submit"  # 每次推送执行
git branch -M main            # 首次推送执行 
git push -u origin main       # 首次推送执行
```
后续推送/拉取：
```bash
git add .                     # 每次推送执行
git commit -m "First Submit"  # 每次推送执行
git push                      # 每次推送执行
git pull                      # 每次拉取执行
```

注意：上面两行命令等价于下面一行命令
```bash
git commit -am "First Submit"  # 每次推送执行
```
