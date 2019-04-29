import os
from pathlib import Path
from tqdm import tqdm_notebook as tqdm

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def resolve_csv_files(directory):
    files = []
    for file_name in tqdm(os.listdir(directory)):
        if file_name.endswith(".csv"):
            files.append(os.path.join(directory, file_name))
    return files

def stem_filename(path):
    return Path(path).stem
