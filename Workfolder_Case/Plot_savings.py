import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import matplotlib.ticker as ticker

dpi_number = 300
figsize = (8, 4)
base_case = 15644.05

df_savings = pd.DataFrame(
    data=[[8473.03, 10370.85, 25553.99], 
          [978.27, 3148.74, 19552.68], 
          [5875.66, 5875.66, 5875.66]],
    columns=["No FFR", "Profil", "Flex"],
    index=["PV on, B on", "PV off, B on", "PV on, B off"]
)

# plot the savings as a bar chart
df_savings_vs_basecase = df_savings / base_case * 100

colors = ['#97E7F5', '#009DD1', '#01377D']

fig, ax = plt.subplots()
df_savings_vs_basecase.plot(kind='bar', ax=ax, color=colors)
ax.set_ylabel('Savings compared to the Base Case [%]')
plt.xticks(rotation='horizontal')

ax.axhline(100, color='#26B170', linestyle='--') 
ax.text(2.28, 100, 'Profitability line', color='#000000', va='center', ha='right',
        bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.5'))

plt.show()




# Plot the ratios of PV off, B on against PV on, B on
# Barchart
plt.figure(figsize=figsize)
plt.bar(df_savings.columns, df_savings.iloc[0], label="PV on, B on", color="#01377D", width = 0.5)
plt.bar(df_savings.columns, df_savings.iloc[1], label="PV off, B on", color="#009DD1", width = 0.5)
formatter = ticker.FuncFormatter(lambda x, p: format(int(x), ' '))
plt.gca().yaxis.set_major_formatter(formatter)
plt.ylabel("Cost savings [NOK]")
plt.legend(loc="upper left")

# Lineplot
ax2 = plt.gca().twinx()
ax2.plot(df_savings.columns, (df_savings.iloc[1]/df_savings.iloc[0])*100, label="Ratio", color="#7ED348")
ax2.set_ylabel("(PV off, B on) / (PV on, B on)")
ax2.legend(loc="upper right")
ax2.set_ylim(0, 100)

# Write each percent on the line
for i, v in enumerate((df_savings.iloc[1]/df_savings.iloc[0])*100):
    ax2.text(i, v, str(round(v, 1))+"%", color="#000000", ha="center", va="bottom", 
             bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.5'))
plt.show()
