---
title: "强化学习系列：DQN"
# 文章摘要，通常用于 列表页面 或 SEO 描述
summary: Python argparse
# 文章的发布日期，未来时间不会发布
date: 2025-02-13
# 文章所属的 系列，可以用 series 在 Hugo 的主题（如 PaperMod）中生成一个系列的导航
series: ["RL"]
weight: 1
# 旧的 URL 映射到这个页面，防止 404 错误（适用于 URL 变更）。
aliases: ["/RL-dqn"]
# 文章的标签（关键词），用于 Hugo 的 标签分类（类似于博客的 tag）
tags: ["RL", "DQN"]
author: ["Yongliang Yang"]
cover:
  # 图片路径
  image: images/papermod-cover.png
  # 在文章列表中隐藏封面图，但在文章页面内可能会显示。
  hiddenInList: true  
---




## 1.DQN 算法流程

```python             
# 0. 初始化
# 初始化环境 env
# 初始化神经网络
# M 个episode
for episode = 1 to M:

    # 1. 重置env，得到当前状态 s_t 
    s_t = env.reset()

    # 每个 episode 最多执行 T 步
    for t = 1 to T:

        # 2. 以 ε-贪婪策略生成动作 a_t
        a_t = argmax_a Q(s_t, a; θ) or random
        
        # 3. 执行动作 a_t，得到奖励 r_t、新状态 s_{t+1}、以及游戏结束标志 done
        s_{t+1}, r_t, done, _ = env.step(a_t)
        
        # 4. 存储一次交互数据 (s_t, a_t, r_t, φ_{t+1}, done) 至经验回放库 D
        D.append( (s_t, a_t, r_t, φ_{t+1}, done) )
        
        # 4. 从 D 中随机抽取一批数据 batch（ batch 数据量为 minimal_size ）
        batch =  {φ_j, a_j, r_j, φ_{j+1}, done_j}, j = 1, ..., minimal_size
        
        # 5. 对目标值 y_j 进行计算
        对于每条采样到的转移：
            if done_j:
                y_j = r_j
            else:
                y_j = r_j + γ * max_{a'} Q^{-}(φ_{j+1}, a'; θ^-)
        
        # 6. 最小化损失函数并更新评估网络参数 θ
        #     损失函数通常为：(y_j - Q(φ_j, a_j; θ))^2 的平均
        计算梯度并执行一次反向传播，更新 θ
        
        # 7. 定期（例如每 C 步）同步目标网络
        if t % C == 0:
            θ^- = θ  # 将评估网络参数复制到目标网络
        
        # 8. 若 done=True，则当前回合结束，跳出循环
        if done:
            break

```
