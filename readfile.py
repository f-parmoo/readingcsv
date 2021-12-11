import pandas as pd
import numpy as np
import os

path_to_read = 'csv'
filelist = os.listdir(path_to_read)

for item in filelist:
    filedata = pd.read_csv(path_to_read + '\\' + item)
    print(filedata.size, filedata.ndim, filedata.columns , filedata.dtypes , filedata.count())
