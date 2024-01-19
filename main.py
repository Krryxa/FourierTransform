import numpy as np
import matplotlib.pyplot as plt

# 采样率和采样时间
sampling_rate = 1000
t = np.linspace(0, 1, sampling_rate, endpoint=False)

# 创建信号
freq1 = 5
freq2 = 10
signal = np.sin(2 * np.pi * freq1 * t) + 0.5 * np.sin(2 * np.pi * freq2 * t)

# 计算傅里叶变换
fft_result = np.fft.fft(signal)

# 计算频率
freqs = np.fft.fftfreq(len(signal), 1 / sampling_rate)

# 绘制原始信号
plt.figure()
plt.plot(t, signal)
plt.title("Original Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# 绘制傅里叶变换结果
plt.figure()
plt.plot(freqs, np.abs(fft_result))
plt.title("Fourier Transform")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

# 仅显示正频率部分
plt.xlim(0, sampling_rate / 2)

plt.show()

