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
# 0.1 初始化环境 env
env =
# 0.2 初始化 DQN
q(s, a; θ) = 
q_(s, a; θ_) = 
# 0.3 初始化经验回放库 Buffer
replay_buffer = 

# 主循环：N 个 episode
for episode = 1 to M:

    # 1. 初始化
    s_t = env.reset()  # 初始化状态 s_t
    episode_return = 0 # 初始化累计回报 episode_return

    # 每个 episode 
    done = False
    while not done:

        # 2. 以 ε-贪婪策略生成动作 a_t
        a_t = argmax_a Q(s_t, a; θ) or random
        
        # 3. 执行动作 a_t，得到奖励 r_t、新状态 s_{t+1}、以及游戏结束标志 done
        s_{t+1}, r_t, done, _ = env.step(a_t)
        
        # 4. 存储一次交互数据 (s_t, a_t, r_t, φ_{t+1}, done) 至经验回放库 replay_buffer
        replay_buffer.append( (s_t, a_t, r_t, s_{t+1}, done) )
        
        # 5. 当 replay_buffer 数据量满足最小长度 (比如500)，从 replay_buffer 中随机抽取一批数据 batch <-  {s_j, a_j, r_j, s_{j+1}, done_j}, j = 1, ..., minimal_size（ batch 数据量为 minimal_size ）
        if len(Buffer) > 500:
            batch <-  replay_buffer( 1, ..., minimal_size ) 
        
        # 6. 利用采样数据 batch 训练 DQN
        DQN.train(batch)        
        
        # 7. 更新状态 s_t <- s_{t+1}
        s_t = s_{t+1}

        # 8. 更新累计回报
        episode_return += reward # 更新累计回报
        
        
        if done:
            break

```
