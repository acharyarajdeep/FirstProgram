person=dict(Name="Raj", Age=22, Salary=37000)
print(person["Salary"])
person["Name"]="CR7"
print(person["Name"])
person["Married"]="No"
print(person)
del person["Age"]
print(person["Salary"])