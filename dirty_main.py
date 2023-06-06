from application.salary import *
from application.db.people import *
import datetime

if __name__ == '__main__':
    print(datetime.date.today())
    calculate_salary()
    get_employees()