import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'Data sold to the grid.xlsx'
df = pd.read_excel(file_path)

print(df.head())

sns.set(style="whitegrid")

df['year'] = df['year'].ffill()

df['year_month'] = df['year'].astype(int).astype(str) + '-' + df['month_name']

df['year_month'] = pd.to_datetime(df['year_month'], format='%Y-%B')

plt.figure(figsize=(12, 6))
sns.lineplot(x='year_month', y='Generator Export to Grid (MWh)', data=df, marker='o')
plt.title("Monthly Generator Export to Grid (MWh)", fontsize=16)
plt.ylabel("Generator Export to Grid (MWh)", fontsize=14)
plt.xlabel("Month", fontsize=14)
plt.xticks(df['year_month'][::4].dt.strftime('%Y-%m'), rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(x='year_month', y='Payment from AESO (Thousands $)', data=df, marker='o')
plt.title("Monthly Payment from AESO (Thousands $)", fontsize=16)
plt.ylabel("Payment from AESO (Thousands $)", fontsize=14)
plt.xlabel("Month", fontsize=14)
plt.xticks(df['year_month'][::4].dt.strftime('%Y-%m'), rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
