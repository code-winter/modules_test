from application.salary import calculate_salary
from db.people import get_employees


def create_waves():
    print('_.~"(_.~"(_.~"(_.~"(_.~"(_.~"(_.~"(_.~"(')


def draw_fish():
    print('.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>¸_.~"(_.~"(')


def main():
    salary = 865
    employees = ['Albert Einstein', 'Isaac Newton', 'Leonard Hoffsteader']
    calculate_salary(salary)
    get_employees(employees)
    for it in range(6):
        create_waves()
        if it == 2:
            draw_fish()



    main()

