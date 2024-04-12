# ValueError: Grouper for 'X' not 1-dimensional

import pandas as pd

df = pd.DataFrame({
    'first': [10, 15, 20],
    'second': [10, 15, 20],
})

df.columns = ['first', 'second']

#    first  second
# 0     10      10
# 1     15      15
# 2     20      20
print(df)

# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f8a62579270>
print(df.groupby('second'))