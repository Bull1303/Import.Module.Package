import application.salary as salary
import application.db.people as people
import datetime

if __name__ == '__main__':
    print(datetime.date.today())
    salary.calculate_salary()
    people.get_employees()
