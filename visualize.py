import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from utils import *

def plot_mfcc(mfcc):
    plt.figure(figsize=(25, 5))
    librosa.display.specshow(mfcc, x_axis='time')
    plt.colorbar()

def plot_dataset(dataset):
    plt.figure(figsize=(25, 5))
    plt.plot(dataset)

def plot_testfile(file_dir, n_samples=1):
    test_files = resolve_csv_files(file_dir)
    for i in range(n_samples):
        data  = pd.read_csv(test_files[i], dtype={'acoustic_data': np.float32})
        fig = plt.figure(figsize=(25, 5))
        ax = fig.add_subplot(111)
        data.plot(ax=ax, legend=True)

