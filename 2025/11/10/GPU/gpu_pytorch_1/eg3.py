import torch, time

N = 4

# Case1: CPU 第一次计算
a1 = torch.randn(N, N)
b1 = torch.randn(N, N)
t0 = time.perf_counter()
c1 = a1 @ b1         # CPU：调用会一直等到乘法真正算完才返回
t1 = time.perf_counter()
print(f"[CPU] 耗时: {t1 - t0:.6f}s")

# Case2: CPU 第二次计算
a2 = torch.randn(N, N)
b2 = torch.randn(N, N)
t0 = time.perf_counter()
c2 = a2 @ b2         # CPU：调用会一直等到乘法真正算完才返回
t1 = time.perf_counter()
print(f"[CPU] 耗时: {t1 - t0:.6f}s")

# Case3: GPU（预热计时）
a3 = torch.randn(N, N, device="cuda")
b3 = torch.randn(N, N, device="cuda")
t0 = time.perf_counter()
c3 = a3 @ b3                  # GPU：只是把任务放进队列,立即返回
t1 = time.perf_counter()
print(f"[GPU] 耗时: {t1 - t0:.6f}s")

# case4：GPU（错误计时示范）
a4 = torch.randn(N, N, device="cuda")
b4 = torch.randn(N, N, device="cuda")
t0 = time.perf_counter()
c4 = a4 @ b4                  # GPU：只是把任务放进队列,立即返回
t1 = time.perf_counter()
print(f"[GPU] 耗时: {t1 - t0:.6f}s")

# case5：GPU（正确计时示范）
a5 = torch.randn(N, N, device="cuda")
b5 = torch.randn(N, N, device="cuda")
t0 = time.perf_counter()
c5 = a5 @ b5              # GPU：只是把任务放进队列,立即返回
torch.cuda.synchronize()  # 【显示同步】等待GPU完成!
t1 = time.perf_counter()
print(f"[GPU] 耗时: {t1 - t0:.6f}s")