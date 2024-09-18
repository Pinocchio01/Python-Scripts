import numpy as np
from scipy.fft import fft

# 创建一个示例输入信号
fs = 512  # 采样频率为1000 Hz
t = np.linspace(0, 1, fs, endpoint=False)  # 1秒内的时间序列
frequencies = [5, 20, 100]  # 三个不同频率的成分
signal = np.sin(2 * np.pi * frequencies[0] * t) + np.sin(2 * np.pi * frequencies[1] * t) + np.sin(2 * np.pi * frequencies[2] * t)

# 计算信号的DFT

def test_fft():
    fft(signal)

# def test():
#     """Stupid test function"""
#     L = [i for i in range(100)]

if __name__ == '__main__':
    
    # # 1. timeit
    # import timeit
    # execution_time = timeit.timeit("test_fft()", globals=globals(), number=1000)
    # print(f"Average execution time for fft: {execution_time / 1000:.6f} seconds")

    # 2. test_module and cProfile
    # import cProfile
    # cProfile.run('test_fft()')

    import cProfile
    import pstats

    # 创建cProfile对象
    profiler = cProfile.Profile()

    # 开始性能分析
    profiler.enable()

    # 执行你的代码
    test_fft()

    # 结束性能分析
    profiler.disable()

    # 创建一个Stats对象，用于分析性能数据
    stats = pstats.Stats(profiler)
    stats.print_stats()

    for func, (cc, nc, tt, ct, callers) in stats.stats.items():
        print(f"Function: {func}")
        print(f"  Calls: {nc}")
        print(f"  Total Time: {tt:.10f} seconds")  # 设置为较高的精度
        print(f"  Cumulative Time: {ct:.10f} seconds")  # 设置为较高的精度
        print(f"  Callers: {callers}")
        print()