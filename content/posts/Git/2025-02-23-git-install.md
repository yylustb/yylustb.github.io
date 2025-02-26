---
title: "Git 系列 - 1. 安装 Git 与配置 Github"
summary: Learn About Git & GitHub
date: 2025-02-23
weight: 1
aliases: ["/git-install"]
tags: ["Git", "Github"]
categories: ["Git"]
author: ["Yongliang Yang"]
cover:
  image: images/git.png
---


## 1. 安装git

这里没什么好说的，官网下载，默认安装。

## 2. 配置 git 用户信息

### 2.1 配置 Git 用户信息

```Powershell
git config --global user.name "GitHub用户名" # 不需要引号
git config --global user.email "GitHub邮箱"  # 不需要引号
```

### 2.2 设置 SSH Key

- 生成 `SSH Key`
  ```Powershell
  ssh-keygen -t rsa -b 4096 -C "GitHub邮箱" # 不需要引号
  ```
  - `-t rsa`：使用 RSA 加密算法
  - `-b 4096`：密钥长度为 4096 位（更安全）
  - `-C "GitHub邮箱"`：标识 SSH Key，方便管理
- 接下来 terminal 提示：
  ```Powershell
  Enter file in which to save the key (/home/user/.ssh/id_rsa):
  ```
  直接按回车即可（使用默认路径 `~/.ssh/id_rsa`）
- 接下来 terminal 提示输入密码：
  ```Powershell
  Enter passphrase (empty for no passphrase):
  Enter same passphrase again:
  ```
  两次回车即可（默认不输入密码），否则每次推送 Git 都需要输入密码


- 生成的 `SSH密钥` 存放在 `~/.ssh/id_rsa.pub`

### 2.3 将 `SSH密钥` 添加到 GitHub 账户的 SSH Keys 中
- 复制 SSH Key
  ```Powershell
  cat ~/.ssh/id_rsa.pub
  ```
- 添加到 GitHub
  - 登录 GitHub 账户
  - 点击右上头像 -> Settings（设置）
  - 左侧选择 SSH and GPG keys（SSH 和 GPG 密钥）
  - 点击 New SSH key（新建 SSH 密钥）
    - Title: 可以自定义
    - Key: 粘贴复制的 SSH Key
  - 点击 Add SSH key


### 2.3 测试 SSH 连接

```Powershell
  ssh -T git@github.com
```
如果配置成功，会显示：
```Powershell
  Hi <GitHub用户名>! You've successfully authenticated, but GitHub does not provide shell access.

```

## 3. 修改文件，提交到本地仓库 

进入 `path/to/your/workspace/XXX` 文件夹，修改其中的文件 AAA.xx，然后执行以下命令：

```bash
git status
```
执行后，会显示
```bash
Changes not stated for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   AAA.xx
```
表明：
- AAA.xx 文件被修改
- 该文件的修改没有被添加到暂存区

接下来，执行以下命令：
```bash
git add AAA.xx # 将 AAA.xx 文件添加到暂存区
```

再次执行以下命令
```bash
git commit -m "第一次修改" # 将暂存区的文件提交到本地仓库，并添加提交备注信息
```



## 4. 本地仓库关联配置远程仓库（新建远程仓库后第一次推送）

首先，在 GitHub 上新建一个仓库 (<mark>Github 仓库新建后的默认分支是 main</mark>)

本地仓库中文件每次修改后，如需推送，需要按顺序执行以下 Git 操作
  ```Powershell
  # 1 切换到仓库根目录
  cd "本地仓库路径"
  # 2 初始化 Git 仓库
  git init
  # 3 添加所有文件到暂存区
  git add .
  # 4 提交文件
  git commit -m "Initial commit" 
  # 5 origin = SSH，并且添加 origin（以后命令行可以用 origin 代表远程仓库）
  git remote add origin SSH地址
  # 6 强制重命名本地仓库的当前分支为 main
  git branch -M main
  # 7 第一次推送：将本地的 main 分支推送到 GitHub
  git push -u origin main
  ```
注意：
  - Git 仓库默认的主分支是 `master`，但 GitHub 仓库采用 `main` 作为默认分支，所以用命令 `git branch -M main` 将本地分支当前分支 `master` 改为 `main`。
  - 第一次推送执行 `git push -u origin main` ，`-u` 选项将本地的 main 分支与远程的 origin/main 关联起来，使得后续推送和拉取更方便。
  - 如果不使用 `-u` 选项，后续推送时需要使用 `git push origin main`。
  - 使用了 `-u` 选项后，后续推送时可以直接使用 `git push`。
  - `-u` 的全写是 `--set-upstream`。

执行完上述指令后，打开 GitHub 仓库, 会看到本地仓库已经推送.








## 5. 推送本地仓库到远程仓库（非第一次推送）


执行以下指令，推送本地仓库到远程仓库
```bash
git push
```
执行以下指令，远程仓库拉取到本地仓库
```bash
git pull
```




## 总结

- SSH 密钥配置，不需要每次验证
- 从远程仓库 clone 到本地：
  - `git clone 远程仓库地址` 

- 本地仓库与远程仓库的关联配置（首次推送）：
  - `git add .`                     # 提交到暂存区
  - `git commit -m "提交备注信息"` # 提交到本地仓库
  - `git remote add origin 远程仓库地址`  # 将本地仓库与远程仓库关联
  - `git remote -v`                      # 查看远程仓库的信息
  - `git branch -M main`
  - `git push -u origin main`            # 将本地的当前分支与远程的 origin/main 关联并推送

- 本地仓库提交到远程仓库的流程（非首次推送）：
  - `git add .`                     # 提交到暂存区
  - `git commit -m "提交备注信息"` # 提交到本地仓库
  - `git push`        # 提交到远程仓库
- 上面两条指令可以简化为下面一条指令
  - `git commit -am "提交备注信息"` # 提交到本地仓库