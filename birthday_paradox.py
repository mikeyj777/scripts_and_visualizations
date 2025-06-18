import csv
import math
from random import choices
import numpy as np
import pandas as pd
import plotly.express as px



number_of_people = 100
trials = 10000

output = []
for i in range(2, number_of_people+1):
  wins = 0
  ans = {j: 0 for j in range(2, 11)}
  for _ in range(trials):
    nums = choices(range(1, 365), k=i)
    for j in range(2, 11):
      if i - len(set(nums)) == j-1:
        ans[j] += 1
    if ans[j] / trials != 1:
      output.append({
        'num_people': i, 
        'matching_birthdays': j, 
        'log_1_minus_prob': math.log10(1 - ans[j] / trials)
      })

  print(i)
  # print(f"Probability of at least two people sharing a birthday in a group of {i} people: {wins / trials:.4f}")
  

df = pd.DataFrame(output)
df.to_csv('birthday_paradox.csv', index=False)
# fig = px.scatter_3d(df, x='num_people', y='matching_birthdays', z='log_1_minus_prob',
#                     color='matching_birthdays')
# fig.show()
apple = 1
