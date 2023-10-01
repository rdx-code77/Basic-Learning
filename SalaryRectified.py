import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Undergraduate Major": ["Accounting", "Aerospace Engineering", "Chemical Engineering", "Computer Engineering", "Economics", "Math", "Physics", "Political Science"],
    "Starting Median Salary": [46000, 57700, 63200, 61400, 50100, 45400, 50300, 40800],
    "Mid-Career Median Salary": [77100, 101000, 107000, 105000, 98600, 92400, 97300, 78200],
    "Percent change from Starting to Mid-Career Salary": [67.6, 75, 69.3, 71, 96.8, 103.5, 93.4, 91.7],
    "Mid-Career 10th Percentile Salary": [42200, 64300, 71900, 66100, 50600, 64200, 56000, 43500],
    "Mid-Career 25th Percentile Salary": [56100, 82100, 87300, 84100, 70600, 65200, 74200, 55300],
    "Mid-Career 75th Percentile Salary": [108000, 127000, 143000, 135000, 145000, 128000, 132000, 114000],
    "Mid-Career 90th Percentile Salary": [152000, 161000, 194000, 162000, 210000, 183000, 178000, 124000]
}

df = pd.DataFrame(data)

# Create a figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(16, 12))
fig.subplots_adjust(hspace=0.3)

# Bar chart for starting and mid-career salaries
axs[0, 0].bar(df["Undergraduate Major"], df["Starting Median Salary"], label="Starting Salary")
axs[0, 0].bar(df["Undergraduate Major"], df["Mid-Career Median Salary"], label="Mid-Career Salary")
axs[0, 0].set_ylabel("Salary ($)")
axs[0, 0].set_title("Starting vs Mid-Career Median Salary by Major")
axs[0, 0].legend()

# Line chart for percent change
axs[0, 1].plot(df["Undergraduate Major"], df["Percent change from Starting to Mid-Career Salary"], marker='o')
axs[0, 1].set_ylabel("Percent Change")
axs[0, 1].set_title("Percent Change from Starting to Mid-Career Salary")
axs[0, 1].set_ylim(0, max(df["Percent change from Starting to Mid-Career Salary"]) + 10)

# Bar chart for salary distribution percentiles
percentiles = ["Mid-Career 10th Percentile Salary", "Mid-Career 25th Percentile Salary", "Mid-Career 75th Percentile Salary", "Mid-Career 90th Percentile Salary"]
for percentile in percentiles:
    axs[1, 0].bar(df["Undergraduate Major"], df[percentile], label=percentile)

axs[1, 0].set_ylabel("Salary ($)")
axs[1, 0].set_title("Mid-Career Salary Distribution by Major")
axs[1, 0].legend()

# Bar chart for starting and mid-career salaries with percent change
axs[1, 1].bar(df["Undergraduate Major"], df["Starting Median Salary"], label="Starting Salary")
axs[1, 1].bar(df["Undergraduate Major"], df["Mid-Career Median Salary"], label="Mid-Career Salary")
axs[1, 1].set_ylabel("Salary ($)")
axs[1, 1].set_title("Starting vs Mid-Career Median Salary by Major with Percent Change")
axs[1, 1].legend()

# Adding percent change as secondary y-axis
ax2 = axs[1, 1].twinx()
ax2.plot(df["Undergraduate Major"], df["Percent change from Starting to Mid-Career Salary"], color='tab:red', linestyle='--', marker='o', label='Percent Change')
ax2.set_ylabel("Percent Change", color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Rotate x-axis labels for better readability
for ax in axs.flat:
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

plt.tight_layout()
plt.show()
