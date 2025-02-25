---
title: "Ubuntu系列1. 安装AppImage应用"
# 文章摘要，通常用于 列表页面 或 SEO 描述
summary: Read aboout Install and Update instructions and sampled configuration templates
# 文章的发布日期，未来时间不会发布
date: 2025-02-17
# 文章所属的 系列，可以用 series 在 Hugo 的主题（如 PaperMod）中生成一个系列的导航
series: ["Linux"]
weight: 1
# 旧的 URL 映射到这个页面，防止 404 错误（适用于 URL 变更）。
aliases: ["/ubuntu-appimage"]
# 文章的标签（关键词），用于 Hugo 的 标签分类（类似于博客的 tag）
tags: ["AppImage", "Ubuntu"]
author: ["Yongliang Yang"]
cover:
  # 图片路径
  image: images/papermod-cover.png
  # 在文章列表中隐藏封面图，但在文章页面内可能会显示。
  hiddenInList: true
  
---

AppImage 是一种便携式软件包格式，允许你在 Linux 上运行应用程序 无需安装。以下是下载、运行和管理 AppImage 文件的方法

## 1. 下载 AppImage 文件


## 2. 赋予 AppImage 文件可执行权限

AppImage 文件运行需要赋予权限，以下是赋予权限的两种方式。

### 方法1：使用终端

```Powershell
chmod +x ~/Downloads/your_app.AppImage
./your_app.AppImage
```

### 方法2：使用图形界面
- 右键点击 AppImage 文件，选择 "属性"（Properties）。
- 切换到 "权限"（Permissions） 选项卡。
- 勾选 "允许作为可执行文件"（Allow executing file as a program）。
- 双击 AppImage 运行程序。


## 3. 使用 AppImageLauncher 管理 AppImage

AppImage 默认不会自动出现在应用菜单中。

AppImageLauncher 可以自动管理 AppImage 并集成到系统菜单中

```bash
sudo add-apt-repository ppa:appimagelauncher-team/stable
sudo apt update
sudo apt install appimagelauncher
```


## 4. 将 AppImage 移动到 /opt 并创建全局快捷方式

如果你希望让 AppImage 可在整个系统中使用

```Powershell
sudo mv ~/Downloads/your_app.AppImage /opt/your_app.AppImage
sudo chmod +x /opt/your_app.AppImage
sudo ln -s /opt/your_app.AppImage /usr/local/bin/your_app
```



## 5. 更新 AppImage

部分 AppImage 支持自动更新，例如：
```bash
./your_app.AppImage --update
```
如果 AppImage 不支持更新，你需要手动下载新版并替换旧版。

## 6. 删除 AppImage

由于 AppImage 是一个独立的可执行文件，删除它就等于卸载：

```Powershell
rm ~/Downloads/your_app.AppImage
```

如果你用 AppImageLauncher 集成了 AppImage，可以在 /Applications 目录中找到它，并右键选择 "删除"。




## 6.Hugo 部署到 Github Pages 🚀








