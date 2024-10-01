import numpy as np
import pandas as pd

series = pd.Series([1,2,3,4,5,6,7,8])
print(series)

dataframe = pd.DataFrame(
    {
        "Name": pd.array(["Sam Ainsley", "Alfie Campbell"],dtype=str),
        "Date of Birth": pd.array([pd.Timestamp("20070730"), pd.Timestamp("20070322")]),
        "Address": pd.array(["", "27 Grange Road"],dtype=str)
    }
)
print(dataframe)