from application.db.people import *
from application.salary import *
from datetime import *


def curr_dt():
    print(f"dirty {datetime.now()}: ", end='')


if __name__ == '__main__':
    curr_dt()
    get_employees()
    curr_dt()
    calculate_salary()
