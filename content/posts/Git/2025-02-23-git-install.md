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

## 2. 利用 git 配置 github 账户

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


# 3. 将本地 Git 仓库与 GitHub 仓库**首次**关联



- 步骤 1：准备本地仓库
- 步骤 2：在本地 Git 仓库中执行 Git 操作
  ```Powershell
  # 2.1 切换到仓库根目录
  cd "本地仓库路径"
  # 2.2 初始化 Git 仓库
  git init
  # 2.3 添加所有文件到暂存区
  git add .
  # 2.4 提交文件
  git commit -m "Initial commit" 
  # 2.5 告诉 Git，本地仓库的 origin 远程地址是 GitHub 仓库的 SSH 地址
  git remote add origin git@github.com:你的GitHub用户名/你的仓库名.git
  # 2.6 强制重命名当前分支为 main
  git branch -M main
  # 2.7 第一次推送：将本地的 main 分支推送到 GitHub
  git push -u origin main
  ```
  - 注意事项1：Git 仓库默认的主分支是 `master`，但 GitHub 仓库采用 `main` 作为默认分支，所以用此命令改为 `main`。
  - 注意事项2：第一次推送时，需要使用 `git push -u origin main` 。以后推送/拉去只需使用：
    ```Powershell
    git push 
    git pull
    ```

- 步骤 3：检查 GitHub 仓库
  打开 GitHub 主页 (https://github.com/GitHub用户名), 会看到一个新创建的仓库，且代码已经上传.




