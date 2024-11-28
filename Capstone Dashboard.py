import pandas as pd
import matplotlib.pyplot as plt

xls = pd.ExcelFile(r"C:\Users\akhas\OneDrive\Desktop\Capstone digital\Data Request Information.xlsx")
df_daily = pd.read_excel(xls, "Daily Data")
df_hourly = pd.read_excel(xls,"Hourly Chiller Power Use")

df_daily = pd.DataFrame(df_daily)
df_hourly = pd.DataFrame(df_hourly)

print(df_daily.iloc[:,2])

plt.figure(figsize=(8, 6))
plt.plot(df_daily.iloc[:,0], df_daily.iloc[:,1])
plt.title("Daily Chiller output")
plt.ylabel("Chiller output (kwh)")
plt.xlabel("Date")
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(df_daily.iloc[:,0], df_daily.iloc[:,2])
plt.title("Daily Building Cooling Demand")
plt.ylabel("Building Cooling Demand (kWh)")
plt.xlabel("Date")
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(df_daily.iloc[:,0], df_daily.iloc[:,3])
plt.title("Daily Cogen Gas Usage")
plt.ylabel("Cogen Gas Usage (GJ)")
plt.xlabel("Date")
plt.show()








