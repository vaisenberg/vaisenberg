from maping_filter import data
import pandas as pd
from functools import reduce



people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

df = pd.DataFrame(data)
print("Original DataFrame:")
#discover if the len(name) <= 4
#say hello just for those that len(name) <= 4
# use map() and filter()
df = pd.DataFrame(data)
filtered_names = list(filter(lambda name: len(name) <= 4, people))
print(filtered_names)

say_hello = list(map(lambda name: f'Hello {name}', filtered_names))
print(say_hello)

#map
salary_increment = list(map(lambda row: {**row, 'Salary': row['Salary'] * 1.10}, df.to_dict('records')))

print(pd.DataFrame(salary_increment))

#reduce
total_salary = reduce(lambda acc, row: acc + row['Salary'], df.to_dict('records'), 0)
print(total_salary)