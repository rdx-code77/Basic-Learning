import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r'degrees-that-pay-back.csv')

df = pd.DataFrame(data)

plt.bar(df["Undergraduate Major"], df["Starting Median Salary"], label="Starting Median Salary")
plt.bar(df["Undergraduate Major"], df["Mid-Career Median Salary"], label="Mid-Career Median Salary")
plt.xlabel("Undergraduate Major")
plt.ylabel("Salary ($)")
plt.title("Starting vs Mid-Career Median Salary by Major")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.show()

plt.plot(df["Undergraduate Major"], df["Starting Median Salary"], marker='o', label='Starting Median Salary')
plt.plot(df["Undergraduate Major"], df["Mid-Career Median Salary"], marker='o', label='Mid-Career Median Salary')
plt.xlabel("Undergraduate Major")
plt.ylabel("Salary ($)")
plt.title("Starting vs Mid-Career Median Salary Trend by Major")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()

plt.stackplot(df["Undergraduate Major"], df["Starting Median Salary"], df["Mid-Career Median Salary"],
              labels=['Starting Median Salary', 'Mid-Career Median Salary'])
plt.xlabel("Undergraduate Major")
plt.ylabel("Salary ($)")
plt.title("Starting and Mid-Career Median Salary Distribution by Major")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15))

# Bar chart
ax1.bar(df["Undergraduate Major"], df["Starting Median Salary"], label="Starting Median Salary")
ax1.bar(df["Undergraduate Major"], df["Mid-Career Median Salary"], label="Mid-Career Median Salary")
ax1.set_ylabel("Salary ($)")
ax1.set_title("Starting vs Mid-Career Median Salary by Major")
ax1.legend()
ax1.grid(True)
ax1.set_xticks([])  # Remove x-axis ticks

# Line chart
ax2.plot(df["Undergraduate Major"], df["Starting Median Salary"], marker='o', label='Starting Median Salary')
ax2.plot(df["Undergraduate Major"], df["Mid-Career Median Salary"], marker='o', label='Mid-Career Median Salary')
ax2.set_xlabel("Undergraduate Major")
ax2.set_ylabel("Salary ($)")
ax2.set_title("Starting vs Mid-Career Median Salary Trend by Major")
ax2.legend()
ax2.grid(True)
ax2.set_xticks([])  # Remove x-axis ticks


# Area chart
ax3.stackplot(df["Undergraduate Major"], df["Starting Median Salary"], df["Mid-Career Median Salary"],
              labels=['Starting Median Salary', 'Mid-Career Median Salary'])
ax3.set_xlabel("Undergraduate Major")
ax3.set_ylabel("Salary ($)")
ax3.set_title("Starting and Mid-Career Median Salary Distribution by Major")
ax3.legend()
ax3.grid(True)
ax3.set_xticks([])  # Remove x-axis ticks


plt.tight_layout()
plt.show()



