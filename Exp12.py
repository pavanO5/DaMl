import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\pavan\Downloads\IRIS (1).csv")
df.head(10)
df.info()

from ydata_profiling import ProfileReport
prof = ProfileReport(df)
prof.to_file(output_file='EDA.html')
from IPython.core.display import display, HTML
display(HTML(prof.to_html()))



