import pandas as pd

file_path = "Log intern - Analyst case study.xlsx"
xls = pd.ExcelFile(file_path)

df_brands = pd.read_excel(xls, sheet_name='Data brands')
df_orders = pd.read_excel(xls, sheet_name='Data orders')

df_brands_clean = df_brands[['uuid_brand', 'fg_ff_sync*']].dropna()
df_orders_clean = df_orders[['Order reference', 'uuid_brand']].dropna()

ff_synced_brands = df_brands_clean[df_brands_clean['fg_ff_sync*'] == True]

merged_df = df_orders_clean.merge(ff_synced_brands, on='uuid_brand', how='inner')

ff_synced_orders_dict = merged_df.groupby('uuid_brand')['Order reference'].apply(list).to_dict()

df_export = pd.DataFrame([(k, v) for k, v in ff_synced_orders_dict.items()], columns=['uuid_brand', 'Order references'])

df_export.to_csv("ff_synced_orders.csv", index=False)

print(df_export)


