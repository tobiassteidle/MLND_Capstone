import librosa, librosa.display
import matplotlib.pyplot as plt

def plot_mfcc(mfcc):
    plt.figure(figsize=(25, 5))
    librosa.display.specshow(mfcc, x_axis='time')
    plt.colorbar()
