import pandas as pd
import numpy as ny

data = ny.random.randn(1000)
df = pd.DataFrame(data, columns=["matrix"])

print(df)
print(df.head())
