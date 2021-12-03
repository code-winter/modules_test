from datetime import datetime as dt


def get_employees(employee_list):
    print(f'\nCurrent time {dt.now()}, running on {__name__}')
    print('Employees: ', employee_list)
