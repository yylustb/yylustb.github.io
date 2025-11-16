import torch, time

N = 4000

# GPU 预热
a0 = torch.randn(N, N, device="cuda")
b0 = torch.randn(N, N, device="cuda")
t0 = time.perf_counter()
c0 = a0 @ b0              # 提交 “a @ b” 
torch.cuda.synchronize()  # 【强制同步】等待GPU完成!
t1 = time.perf_counter()
print(f"[GPU] 预热耗时: {t1 - t0:.6f}s")

# case 1: GPU 同步方式 1
a1 = torch.randn(N, N, device="cuda")
b1 = torch.randn(N, N, device="cuda")
t0 = time.perf_counter()
c1 = a1 @ b1              # 提交 “a @ b” 
torch.cuda.synchronize()  # 【强制同步】等待GPU完成!
t1 = time.perf_counter()
print(f"[GPU] 同步1耗时: {t1 - t0:.6f}s")


# case 2: GPU 同步方式 2
# 在 GPU 内创建两个大矩阵
a = torch.randn(N, N, device="cuda")
b = torch.randn(N, N, device="cuda")
# 创建两个 CUDA 事件（Event）:在 GPU 时间线上插两个“标记点”
start = torch.cuda.Event(enable_timing=True) 
end = torch.cuda.Event(enable_timing=True) 

start.record()    # 开始标记
c = a @ b         # 提交 “a @ b” （不会立即执行完）
end.record()      # 结束标记
end.synchronize() # 到这里为止，计时结束
T = start.elapsed_time(end) # 统计从 start.record() 到 end.synchronize() 之间的耗时

print(f"[GPU] 同步2耗时: {T/1000:.6f}s") # T/1000：把毫秒变成秒