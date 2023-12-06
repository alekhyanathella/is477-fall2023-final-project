import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("./data/iris/iris.data")

profile = ProfileReport(df, title="Profiling Report")
profile.to_file("profiling/report.html")
