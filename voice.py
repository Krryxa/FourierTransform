import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt

# 一段简单的正弦波音频信号
fs = 1000  # 采样率（Hz）
t = np.linspace(0, 1, fs, endpoint=False)  # 时间轴
freq = 5  # 频率（Hz）
audio_signal = np.sin(2 * np.pi * freq * t)  # 生成音频信号

# 应用傅里叶变换
audio_freq = fft(audio_signal)

# 获取频率分量的幅度
magnitude = np.abs(audio_freq)

# 创建频率轴
frequencies = np.linspace(0, fs, len(magnitude))

# 只显示前一半的频率（正频率）
half = len(magnitude) // 2
frequencies = frequencies[:half]
magnitude = magnitude[:half]

# 绘制频谱
plt.plot(frequencies, magnitude)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum')
plt.show()
