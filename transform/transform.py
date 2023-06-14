import json
from enum import Enum

with open("input.json", "r") as file:
    data_in = json.load(file)


class Department(Enum):
    IT = "it-services.com"
    SALES = "sales-dep.com"
    PRESALES = "pre-sales.com"
    FULFILLMENT = "fulfillment.com"
    SUPPORT = "customer-support.com"


def transform(data_in):
    emp_id = data_in["id"]
    first_name = data_in["first_name"]
    last_name = data_in["last_name"]
    full_name = first_name + " " + last_name
    age = int(data_in["age"])
    adult = age > 18
    department = Department[data_in["department"]].value
    salary = data_in['salary']
    if salary < 10000:
        tax_percent = 0
    elif salary < 20000:
        tax_percent = 10
    elif salary < 30000:
        tax_percent = 20
    elif salary < 40000:
        tax_percent = 30
    else:
        tax_percent = 0
    after_tax = salary - (salary * tax_percent)

    return {
        "emp_id": emp_id,
        "full_name": full_name,
        "adult": adult,
        "domain": department,
        "tax_percent": tax_percent,
        "after_tax": after_tax
    }


transformData = transform(data_in)


with open("output.json", "w") as file:
    json.dump(transformData, file, indent=2)
