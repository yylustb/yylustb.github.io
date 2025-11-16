import torch, time

N = 4000

# case1：GPU 乘法计算
a1 = torch.randn(N, N, device="cuda")
b1 = torch.randn(N, N, device="cuda")
t0 = time.perf_counter()
c1 = a1 @ b1              # GPU：第 1 次执行乘法
t1 = time.perf_counter()
print(f"[GPU] 耗时: {t1 - t0:.6f}s")

# case2：GPU 乘法计算
a2 = torch.randn(N, N, device="cuda")
b2 = torch.randn(N, N, device="cuda")
t0 = time.perf_counter()
c2 = a2 @ b2              # GPU：第 2 次执行乘法
t1 = time.perf_counter()
print(f"[GPU] 耗时: {t1 - t0:.6f}s")