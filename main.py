from application.db.people import get_employees as g_e
from application.salary import calculate_salary as c_s
from datetime import datetime as dt


def curr_dt():
    print(f"{dt.now()}: ", end='')


if __name__ == '__main__':
    curr_dt()
    g_e()
    curr_dt()
    c_s()
