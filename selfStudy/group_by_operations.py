import pandas as pd

df = pd.read_csv("diamonds.csv")
print("********df************")
print(df)

# group_by_cut = df.groupby('cut').cut.count()
# print("********group_by_cut************")
# print(group_by_cut)
#
# group_by_cut_mib_price = df.groupby('cut').price.min()
# print("********group_by_cut_mib_price************")
# print(group_by_cut_mib_price)

# group_by_price = df.groupby('price').price.count()
# print("********group_by_price************")
# print(group_by_price)

# group_by_cut_carat = df.groupby(['cut', 'carat']).carat.count()
# print("********group_by_cut_carat************")
# print(group_by_cut_carat.head(100))

# group_by_cut_carat = df.groupby(['cut', 'carat']).apply(lambda data : data.loc[data.carat.idxmax()])
# print("********group_by_cut_carat************")
# print(group_by_cut_carat)

# group_by_cut_agg = df.groupby('cut').price.agg([len, min, max])
# print("********group_by_cut_agg************")
# print(group_by_cut_agg)

group_by_cut_carat = df.groupby(['cut', 'carat']).carat.agg([len])
print("********group_by_cut_carat************")
print(group_by_cut_carat)
print(type(group_by_cut_carat.index))
print("********group_by_cut_carat - reset_index ************")
print(group_by_cut_carat.reset_index())