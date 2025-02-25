---
title: "Ubuntu系列 - 2. bash shell, terminal 和 ~/.bashrc"
summary: Learn About Ubuntu
date: 2025-02-17
weight: 1
aliases: ["/Ubuntu-terminal"]
tags: ["terminal", "bash"]
categories: ["Ubuntu"]
author: ["Yongliang Yang"]
cover:
  image: images/papermod-cover.png
---



## 1. Ubuntu 目录结构

### 1.1 用户主目录 `~` = `/home/username/`
在 ubuntu 系统中，波浪线 `~` 在命令行环境下是 “用户主目录”（Home Directory）的缩写或别名。

例如 `~/.bashrc`: 
- `~` 代表的就是当前用户的主目录（`/home/username/`）
- `~/.bashrc` 实际上就是 `/home/username/.bashrc`

## 2. shell 和 terminal

### 2.1 Shell 是什么
Shell 是一种软件层，用来接收用户输入的命令，然后将这些命令传递给操作系统内核去执行。也可以理解为人与操作系统之间的“翻译”或“交互接口”。
### 2.2 Shell 的种类
- bash Shell: Ubuntu 默认的 Shell
- zsh Shell
- fish Shell
- csh/tcsh Shell

每种 Shell 都有自己的语法特性、配置文件和内置工具，但它们的基本功能相似：**运行命令、编写脚本、管理进程和环境变量**等。

### 2.3 常用的 Shell 配置文件
- `~/.bashrc`: bash Shell 的配置文件
- `~/.zshrc`: zsh Shell 的配置文件
- `~/.config/fish/config.fish`: fish Shell 的配置文件

### 2.4 Shell 的工作流程
- 读取用户输入的命令
- 解释和解析命令，交给操作系统
- 显示执行结果

### 2.5 常用的 Shell 命令
- `echo`: 打印文本或变量的值
- `cd`: 改变当前目录
- `ls`: 列出当前目录中的文件和文件夹

### 2.6 常用的 Shell 快捷键
- `Ctrl + L`: 清屏
- `Ctrl + C`: 中断当前命令
- `Ctrl + D`: 退出当前 Shell

### 2.7 什么是 terminal
- "终端" 指的是实际的**硬件设备**（如显示器/键盘），通过串口或其他方式连到主机。
- Ubuntu 的 terminal 是一个 "终端" 的**软件模拟器**

### 2.8 terminal 和 shell 的关系
- terminal: 是一个 “文本交互界面”, 提供了一个文本窗口，允许用户在其中输入命令、接收输出
- shell: 是一个命令行解释器，它接收用户在 terminal 内输入的命令，并将其传递给操作系统内核去执行。
- Terminal：<mark>相当于“聊天窗口”</mark>
- Shell：<mark>相当于“对话的另一端的人”（或自动回复程序）</mark>

### 2.9 例子
- 在 Ubuntu 的 terminal 里输入一条命令：
  ```bash
  ls -l
  ```
- Terminal 会把这条文本交给正在运行的 Shell（一般是 Bash）
- Bash 解析这条命令，调用相应的系统调用或程序来列出目录下的文件和文件夹
- 然后 Bash 把执行结果返回给 Terminal，Terminal 再把结果显示给用户

## 3. 配置脚本文件 `~/.bashrc`
### 3.1 terminal/shell 启动流程
在 `Ubuntu` 系统中，点开 `terminal` 图标，新开一个 `terminal` 窗口时，会发生以下事情：

- 启动一个终端模拟器 `terminal`，它会创建一个**非登录、交互式**的 `Bash Shell`。
- `Bash Shell` 尝试查找并读取 `/etc/bash.bashrc`（系统全局的 bashrc，可选）
- `Bash Shell` 尝试查找并读取当前用户的 `~/.bashrc`（用户自定义的 bashrc）
- `Bash Shell` 环境初始化完成，用户在就可以正常使用终端了。

### 3.2 `~/.bashrc` 的功能
- 初始化 Shell 
- 定义/修改 `PATH` 等**环境变量**
    ```bash
    export PATH="$HOME/bin:$PATH"
    export EDITOR=vim
    ```

- 为常用命令设置别名（alias），简化输入，例如
    ```bash
    alias ll='ls -l'
    alias gs='git status'
    ```

- 让 `~/.bashrc` 的修改立即生效（以下两个指令等价）：
    ```bash
    source ~/.bashrc
    . ~/.bashrc
    ```

- 配置命令提示符（PS1）：命令行中看到的提示符样式，就是由 PS1 的配置决定的
    ```bash
    PS1="\u@\h:\w\$ "
    ```
    - `PS1`: Bash 中用于定义主提示符（Primary Prompt）的变量
    - `\u`：当前用户名（user name）
    - `\h`：当前主机名（host name）中的前半部分（不含域名）
    - `\w`：当前工作目录（working directory），会以相对路径显示，如果是 home 目录则显示 ~
    - `\$`：如果是普通用户则显示 `$`，如果是 `root` 用户（即超级用户）则显示 `#`
    - 最后的空格: 是为了让命令提示符后留出一个空格，便于输入命令

### 2.3 不同类型的 Shell 的 Bash 启动流程
- **登录Shell**（Login Shell）
    - 通过 `SSH` 登录远程主机，或者在系统中输入 用户名/密码 直接登录时，启动的 Shell 就是 `登录Shell` 
    - 这种情况下，`Bash Shell` 会先读取并执行 `/etc/profile`，然后依次读取 `~/.bash_profile`, `~/.bash_login`, `~/.profile`（谁先被找到就执行哪个，通常系统会默认用 `~/.bash_profile` 或 `~/.profile`）
- **非登录Shell**（Non-login Shell）
    - 在图形界面下打开一个 Terminal: 通常是通过 `Ctrl + Alt + T` 快捷键打开的终端，或者通过 `gnome-terminal` 命令打开的终端
    - 这种情况下，`Bash Shell` 只会读取并执行 `~/.bashrc`
- **交互式**（Interactive）与**非交互式**（Non-interactive）
    - 交互式 Shell：用户与 Shell 之间的交互，例如通过 `Ctrl + Alt + T` 快捷键打开的终端，用户可以通过键盘输入命令
    - 非交互式 Shell：Shell 不与用户交互，例如通过脚本执行命令（脚本首行需要写 `#!/usr/bin/env bash`）

总结：`~/.bashrc` <mark>**默认只在“非登录式且交互式”的 Bash Shell 启动时被读取执行**</mark>



