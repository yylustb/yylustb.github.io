---
title: "Git 系列 - 4. Git 分支管理"
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

## 1. 分支的本地操作

### 📌新建分支

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

### 📌重命名分支
```
git branch -m old_name new_name  # 重命名本地分支
git push origin -u new_name      # 推送新分支到远程
git push origin --delete old_name  # 删除远程旧分支
```

### 📌删除分支

删除分支 branch_B
```bash
git branch -d branch_B # 安全删除 
git branch -D branch_B # 强制删除
```

### 📌切换分支

切换到分支 branch_A
```bash
git checkout branch_A
```
⚠️ 如果当前分支有未提交的更改，Git 可能会阻止切换，需要先提交


### 📌合并分支（ branch_B -> branch_A）

合并分支 `branch_B` 到分支 `branch_A`: 先切换到分支 `branch_A`，再执行 `git merge`
```bash
git checkout branch_A  # 切换当前分支为 branch_A
git merge branch_B     # 合并分支 branch_B 到当前分支 (branch_A)
```
⚠️ 只有在 `branch_B` 上执行 `git reset`、`git rebase`、`git commit` 或 `git merge` 等操作时，
它的内容才会改变。`git merge branch_B` 不会影响 `branch_B`。

### 📌变基（branch_A -> branch_B）

变基是一种将一个分支的更改应用到另一个分支的方法。它可以帮助您保持分支的整洁和有序。

```bash
git checkout branch_A  # 切换到 `branch_A`
git rebase branch_B    # 把当前分支 `branch_A` 的提交应用到 `branch_B` 的最新提交
```

⚠️ 变基 vs. 合并
- git merge 保持原有提交历史，会创建一个新的合并提交。
- git rebase 重新整理提交历史，让分支看起来像是从 main 最新开始的。

### 📌查看分支

查看本地分支
```bash
git branch
```

查看远程分支
```bash
git branch -r
```

查看所有分支
```bash
git branch -a
```


## 2. 分支的远程操作

### 📌推送本地分支到远程仓库

本地分支 branch_A 推送到远程仓库
```bash
git push origin branch_A
```

### 📌关联本地分支与远程分支
关联本地分支 branch_A 与远程分支 branch_A
```bash
git branch --set-upstream-to=origin/branch_A branch_A
```

### 📌拉取远程分支到本地

拉取远程仓库 origin 的分支 branch_B 到本地
```bash
git checkout -b branch_B origin/branch_B
```

### 📌删除远程分支
删除远程仓库 origin 的分支 branch_C
```bash
git push origin --delete branch_C
```
远程不一定叫 origin，可以是其他名字。

删除本地分支对远程分支的跟踪
```
git branch -dr origin/branch_A  # 删除本地分支 branch_A 对远程分支 origin/branch_A 的跟踪
```

