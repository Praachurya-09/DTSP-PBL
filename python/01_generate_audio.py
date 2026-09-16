import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------
# 1. Signal Parameters
# -----------------------------------------

fs = 8000          # Sampling frequency = 8 kHz
duration = 2       # Duration = 2 seconds

t = np.arange(0, duration, 1/fs)

# -----------------------------------------
# 2. Generate Original Audio-like Signal
# -----------------------------------------

# Two frequency components representing
# a simple audio signal

audio = (
    0.6 * np.sin(2 * np.pi * 500 * t) +
    0.3 * np.sin(2 * np.pi * 1000 * t)
)

# -----------------------------------------
# 3. Generate High-Frequency Noise
# -----------------------------------------

noise = 0.3 * np.sin(2 * np.pi * 3000 * t)

# -----------------------------------------
# 4. Add Noise to Audio
# -----------------------------------------

noisy_audio = audio + noise

# -----------------------------------------
# 5. Plot Original and Noisy Signals
# -----------------------------------------

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t[:500], audio[:500])
plt.title("Original Audio Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.subplot(2, 1, 2)
plt.plot(t[:500], noisy_audio[:500])
plt.title("Noisy Audio Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

# -----------------------------------------
# 6. Save Samples
# -----------------------------------------

np.savetxt(
    "original_audio_samples.txt",
    audio
)

np.savetxt(
    "noisy_audio_samples.txt",
    noisy_audio
)

print("Audio generation completed!")
print("Sampling frequency:", fs, "Hz")
print("Number of samples:", len(audio))
