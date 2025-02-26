---
title: "Git 系列 - 2. Git 分支管理"
summary: Learn About Git & branch
date: 2025-02-23
weight: 1
aliases: ["/git-branch"]
tags: ["Git", "branch"]
categories: ["Git"]
author: ["Yongliang Yang"]
cover:
  image: images/git.png
---

## 分支的本地操作

### 新建分支

新建分支 branch_A
```bash
git branch branch_A
```

切换到分支 branch_A
```bash
git checkout branch_A
```

新建分支 branch_B 并切换到分支 branch_B (下面一行效果等同于上面两行)
```bash
git checkout -b branch_B
```

### 查看分支

查看本地分支
```bash
git branch
```

### 合并分支

合并分支 branch_B 到分支 branch_A: 先切换到分支 branch_A，再执行 git merge
```bash
git checkout branch_A  # 切换当前分支为 branch_A
git merge branch_B     # 合并分支 branch_B 到当前分支 (branch_A)
```

### 删除分支

删除分支 branch_B
```bash
git branch -d branch_B # 安全删除 
git branch -D branch_B # 强制删除
```



## 分支的远程操作

### 查看本地仓库关联的远程分支

查看远程分支
```bash
git branch -r
```

查看所有分支
```bash
git branch -a
```

## 推送本地分支到远程仓库

本地分支 branch_A 推送到远程仓库
```bash
git push origin branch_A
```

关联本地分支与远程分支








### 删除远程分支
删除远程仓库 origin 的分支 branch_C
```bash
git push origin --delete branch_C
```
注意，远程不一定叫origin，可以是其他名字。