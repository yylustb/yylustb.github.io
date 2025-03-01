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

下面是关于 Git 分支（branch）的常见基本操作及其示例，供你参考和使用：

1. **查看分支列表**  
   - 查看本地分支：  
     ```
     git branch
     ```
   - 查看远程分支：  
     ```
     git branch -r
     ```
   - 查看所有分支（本地 + 远程）：  
     ```
     git branch -a
     ```

2. **创建新分支**  
   - 只创建分支，不切换到该分支：  
     ```
     git branch <新分支名>
     ```
   - 创建并切换到新分支（常用）：  
     ```
     # 旧写法
     git checkout -b <新分支名>
     
     # 或者 Git 2.23+ 推荐用法
     git switch -c <新分支名>
     ```

3. **切换分支**  
   - 切换到已有分支：  
     ```
     # 旧写法
     git checkout <分支名>

     # Git 2.23+ 推荐用法
     git switch <分支名>
     ```

4. **重命名分支**  
   - 重命名当前所在分支：  
     ```
     git branch -m <新分支名>
     ```
   - 重命名指定分支（需先切换到其他分支）：  
     ```
     git branch -m <旧分支名> <新分支名>
     ```
    注意: `git branch -m` 和 `git branch -M`的区别：

    | 命令 | 是否允许覆盖已有分支 | 作用 |
    |------|----------------|------|
    | `git branch -m` | ❌ 不允许 | 安全重命名，不覆盖已有分支 (如果 `新分支名` 已经存在，则报错) |
    | `git branch -M` | ✅ 允许 | 强制重命名，覆盖已有分支 (如果 `新分支名` 已经存在，会强制覆盖，即删除 `新分支名` 并重命名) |

5. **合并分支**  
   下面示例演示使用 `git merge` 将其它分支上的工作合并到当前分支：
   1. 先切换到目标分支（例如 `main` 分支）：  
      ```
      git switch main
      ```
   2. 将另外一个分支（例如 `feature`）的改动合并到当前分支：  
      ```
      git merge feature
      ```
   3. 如果合并过程中有冲突，需要手动解决冲突后再提交。

   另外，`git rebase` 也可以用于合并分支
   让 `feature` 变基到 `main`**
   ```sh
   git switch feature
   git rebase main
   ```
   上面指令作用：
   - `feature` 分支的 `新提交` (不同于 `main`  的提交) 会被取出，然后依次 “重放” 到 `main` 最新提交之后。
   - `feature` 分支现在看起来像是从 `main` 最新提交直接创建的，历史是线性的。

   如果 feature 和 main 都修改了相同的代码，可能会发生冲突，解决办法：
   1. 手动编辑冲突的文件，解决冲突。
   2. 添加解决后的文件：
   ```sh
   git add file.txt
   git rebase --continue
   ```
   3. 如果多个提交发生冲突，重复上述步骤，直到 `rebase` 完成。

   如果 `rebase` 过程中出现问题，你可以**放弃 `rebase`，恢复原状态**：
   ```sh
   git rebase --abort
   ```
   这会让 `feature` 分支回到 `rebase` 之前的状态，避免修改提交历史。

   **`git rebase` 和 `git merge` 二者区别：**

   1. `git rebase` 和 `git merge` 对两个分支的影响：

    | 操作 | 对 `main` 的影响 | 对 `feature` 的影响 |
    |------|---------------|----------------|
    | `git rebase main` | **不变** | 变基到 `main` 最新提交，提交 ID 可能会改变 |
    | `git merge main` | 产生一个合并提交 `M` | **不变** |
   
   2. `git rebase` 和 `git merge` 对提交历史的影响：

    |  | `merge` | `rebase` |
    |---|--------|---------|
    | 提交历史 | 保留分支合并历史（会产生合并提交） | 提交历史保持线性 |
    | 是否创建新提交 | 产生一个新的合并提交 | 重新应用原始提交，可能修改提交哈希 |
    | 适用场景 | 团队协作，保留完整历史 | 个人开发，保持整洁的历史 |
    | 是否会修改提交历史 | ❌ 不会 | ✅ 会修改提交历史 |


6. **删除本地分支**  
   - 安全删除，若本地分支改动未合并到其他分支，Git 会警告：  
     ```
     git branch -d <分支名>
     ```
   - 强制删除，不管是否合并：  
     ```
     git branch -D <分支名>
     ```

7. **推送本地分支到远程**  
   - 如果远程不存在同名分支，需要指定要推送到的远程仓库并创建对应分支：  
     ```
     git push origin <分支名>
     ```
   - 若希望本地分支和远程分支保持相同名称，可加上 `-u`（设置跟踪关系），下次只需 `git push`：  
     ```
     git push -u origin <分支名>
     ```

8. **从远程拉取分支**  
   - 获取最新的远程信息：  
     ```
     git fetch
     ```
   - 检出（创建并切换到）远程分支到本地：  
     ```
     git checkout -b <本地分支名> origin/<远程分支名>
     ```
     或使用 Git 2.23+ 的写法：
     ```
     git switch -c <本地分支名> origin/<远程分支名>
     ```

9. **查看分支合并图/历史记录**  
   - 可以使用 `git log --graph --oneline --decorate` 来查看分支的历史演进关系，直观地了解分支如何合并和分叉。

---

以上是 Git 分支的基本操作流程及常见用法。根据团队协作和项目规范的不同，你可能需要结合 Pull Request 流程、代码审阅等来进行分支管理。合理地使用分支能让开发流程更有条理、降低冲突并提升协作效率。
