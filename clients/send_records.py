import aiohttp
import asyncio
import csv
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Employee:
    employee_id: int
    name: str
    email: str
    department: str
    designation: str
    salary: int
    date_of_joining: str

async def send_employee(session, employee: Employee):
    async with session.post("http://localhost:8000/api/employee/", json=employee.__dict__) as resp:
        print(f"Sent {employee.employee_id} - Status: {resp.status}")

async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        with open('employee_data.csv', newline='') as file:
            reader = csv.DictReader(file)
            print("csv headers:",reader.fieldnames)
            for row in reader:
                emp = Employee(
                    employee_id=int(row['Employee ID'.strip()]),
                    name=row['Name'],
                    email=row['Email'],
                    department=row['Department'],
                    designation=row['Designation'],
                    salary=int(row['Salary']),
                    date_of_joining=datetime.strptime(row['Date of Joining'], "%Y-%m-%d").date().isoformat()
                )
                tasks.append(send_employee(session, emp))
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
