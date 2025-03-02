---
title: "Git 系列 - 5. Git 分支协作案例"
summary: Learn About Git & Matlab
date: 2025-03-02
weight: 1
aliases: ["/git-branch-demo"]
tags: ["Git", "branch"]
categories: ["Git"]
author: ["Yongliang Yang"]
cover:
  image: images/git.png
---


## 1. Github 建立仓库 `git_test`（会产生默认分支 `main`），同时确保A和B都有 Github 仓库的权限



## 2. A 和 B 两个人分别在本地建立文件夹 `git_test`

## 3. A 进入本地文件夹 `git_test`

- 初始化A的本地仓库（会产生默认分支 `master`），
- 修改 `master` 分支为 `main`

```bash
git init
git branch -m master main
```

## 4. A 在本地仓库创建文件并同步至 Github

- 新建文件 test.txt，并添加内容 `main 的第一次修改`

- 并提交至本地仓库的 main 分支
```bash
git add .
git commit -m "main 的第一次修改"
```

- 然后同步至 Github 仓库的 main 分支
```bash
git remote add origin git@github.com:yylustb/git_test.git
git push -u origin main
```
接下来检查github，可以看到 Github 仓库的 main 分支已经同步成功

## 5. B 初次链接 Github 仓库，并初次同步

- 初始化 git 仓库（会产生默认分支 `master`），
- 修改 `master` 分支为 `main`
- 链接Github 仓库
- 从 Github 仓库同步至本地仓库的 main 分支
```bash
git init
git branch -m master main
git remote add origin git@github.com:yylustb/git_test.git
git pull origin main
```
接下来检查B的本地仓库，可以看到 Github 仓库的 main 分支已经同步成功

## 6. 在三个仓库（Github，A本地，和B本地）添加fth分支，并将 A 和 B 的 fth 分支与 Github 的 fth 分支同步

- 在 `Github` 添加 fth 分支 (网页操作)
- 在 `A本地` 添加 fth 分支 (命令行操作)
```bash
git branch fth
git checkout fth
git pull origin fth
```
- 在 `B本地` 添加 fth 分支 (命令行操作)
```bash
git branch fth
git checkout fth
git pull origin fth
```

## 7. 接下来，A在本地仓库的main分支进行工作，B在本地的fth分支进行工作（A每次工作完要同步到Github的main，B每次工作完要同步到Github的fth）

### 7.1 A在本地仓库的main分支进行工作

A 切换回 main 分支，修改test.txt文件，添加内容 `main 的第二次修改`，提交至本地仓库的 main 分支，并同步至 Github 仓库的 main 分支
```bash
git add .
git commit -m "main 的第二次修改"
git push -u origin main
```

A 继续修改test.txt文件，添加内容 `main 的第三次修改`，提交至本地仓库的 main 分支，并同步至 Github 仓库的 main 分支
```bash
git add .
git commit -m "main 的第三次修改"
git push 
```

可以看到，本地仓库和Github仓库的main分支都已经同步成功（都包含main的三次修改记录）

### 7.2 B在本地的fth分支进行工作

B 切换回 fth 分支，修改test.txt文件，添加内容 `fth 的第一次修改`，提交至本地仓库的 fth 分支，并同步至 Github 仓库的 main 分支
```bash
git add .
git commit -m "fth 的第一次修改"
git push -u origin fth
```

B 继续修改 test.txt 文件，添加内容 `fth 的第二次修改`，提交至本地仓库的 fth 分支，并同步至 Github 仓库的 fth 分支
```bash
git commit -am "main 的第二次修改"
git push 
```

B 新建 paper/paper.txt 文件，添加内容 `111 \n 222 \n 333 \n`，提交至本地仓库的 fth 分支，并同步至 Github 仓库的 fth 分支
```bash
git add .
git commit -m "main 的第三次修改"
git push 
```

## 8. 接下来，A 在本地仓库的 main 分支进行工作，B 在本地的 fth 分支进行工作（A 每次工作前要和工作后同步到 Github 的所有分支, A 每次工作前要和工作后同步到 Github 的所有分支）


### 8.1 对于 A 每次工作的要求（先处理冲突）

A 工作前，在 main 分支和 fth 分支分别同步 Github 仓库的 main 分支和 fth 分支

```bash
git switch main
git pull 
git switch fth
git pull origin fth
```

然后再本地，进行 main 和 fth 的 merge
```bash
git switch main
git merge fth
```

如没有冲突，继续工作。如有冲突，解决冲突。例如如下冲突（就在 test.txt 文档中）：

```bash
main 的第一次修改

<<<<<<< HEAD
main 的第二次修改



main 的第三次修改：asdasdasdasdas
=======

fth 的第一次修改


fth 的第二次修改：acsc
>>>>>>> fth

```

在 test.txt 这个文档中，手动选择保留哪一部分，处理完冲突后删除 `<<<<<<< HEAD`, `=======`, `>>>>>>> fth` 这三行，最后保存 test.txt 文档。

处理完冲突后，提交到本地仓库的 main 分支，同时将 main 分支 merge 到 fth 分支。 
```bash
git add.
git commit -am "main 和 fth 的 merge"
git switch fth
git merge main
```

至此，main 和 fth 的冲突在本地解决完毕，接下来，需要A将本地的没有冲突的 main 分支和 fth 分支推送到 github

```bash
git switch main
git push
git switch fth
git push origin fth
```

### 8.2 A 处理完冲突后的工作

接下来，A 在本地的 main 分支进行工作

修改 paper/paper.txt

修改后提交到本地，同步至github

```bash
git add.
git commit -am "main 对 paper.txt 的修改"
git push
```


### 8.3 对于 B 每次工作的要求（先处理冲突）


B 工作前，在 main 分支和 fth 分支分别同步 Github 仓库的 main 分支和 fth 分支

```bash
git switch main
git pull 
git switch fth
git pull origin fth
```

然后再本地，进行 main 和 fth 互相之间的 merge
```bash
git switch main
git merge fth
git switch fth
git merge main
```

如没有冲突，继续工作。如有冲突，解决冲突 (仿照 8.1 中A的做法)。

### 8.4 

接下来，B 在本地的 fth 分支进行工作，

工作结束后，提交本地的 fth 分支到本地仓库、且同步至 Github 仓库的 fth 分支

如果B没改动main分支，不需要对main分支进行任何操作，如果B改动了main分支，需要将改动同步到Github的main分支