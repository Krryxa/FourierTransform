import numpy as np
from scipy.fft import fft, ifft
import matplotlib.pyplot as plt

# 创建一个简单的正弦波音频信号并添加噪音
fs = 1000  # 采样率（Hz）
t = np.linspace(0, 1, fs, endpoint=False)  # 时间轴
freq = 5  # 频率（Hz）
audio_signal = np.sin(2 * np.pi * freq * t)  # 生成音频信号

# 添加一些噪音
noise_freq = 50  # 噪音频率（Hz）
noise = 0.5 * np.sin(2 * np.pi * noise_freq * t)  # 噪音信号
audio_signal_noisy = audio_signal + noise  # 含噪音的音频信号

# 应用傅里叶变换
audio_freq = fft(audio_signal_noisy)

# 获取频率分量的幅度
magnitude = np.abs(audio_freq)

# 创建频率轴
frequencies = np.linspace(0, fs, len(magnitude))

# 找到噪音频率成分的位置（考虑两侧）
noise_indices = np.where((frequencies > noise_freq - 1) & (frequencies < noise_freq + 1))[0]
# 由于对称性，需要找到对应的负频率部分
# 注意：由于频率轴是从0到fs，所以负频率部分实际上是在数组的后半部分
noise_indices = np.concatenate((noise_indices, len(audio_freq) - noise_indices))

# 滤除噪音：将噪音频率成分的幅度设置为0
audio_freq_filtered = audio_freq.copy()
audio_freq_filtered[noise_indices] = 0

# 应用逆傅里叶变换，转换回时域信号
audio_signal_filtered = ifft(audio_freq_filtered)

# 取实部，因为处理的是实际的物理信号
audio_signal_filtered = np.real(audio_signal_filtered)

# 绘制原始、含噪音和滤波后的信号
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, audio_signal)
plt.title('Original Audio Signal')

plt.subplot(3, 1, 2)
plt.plot(t, audio_signal_noisy)
plt.title('Noisy Audio Signal')

plt.subplot(3, 1, 3)
plt.plot(t, audio_signal_filtered)
plt.title('Filtered Audio Signal (Noise Removed)')

plt.tight_layout()
plt.show()
