import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
employee_data = json.loads(sampleJson)
print(employee_data)

salary = employee_data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)


employee_data["company"]["employee"]["birth_date"] = "2001-01-01"
# birth_date = employee_data["company"]["employee"]["birth_date"]
# print("birth_date",birth_date)

with open("updated_employee_data.json", "w") as json_file:
    json.dump(employee_data, json_file)


