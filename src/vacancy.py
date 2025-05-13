from dataclasses import asdict, dataclass


@dataclass
class Vacancy:
    """Класс для предоставления вакансии"""
    __slots__ = ["title", "url", "salary", "description"]


    def __init__(self, title, url, salary, description):
        """Инициализация вакансии"""
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description


    def to_dict(self):
        """Преобразует объект Vacancy в словарь"""
        return asdict(self)


    def check_salary(self):
        """Проверка указания зарплаты"""
        if not self.salary:
            self.salary = 0


    def comparison(self, other):
        """Сранвнение зарплат у вакансий"""
        return self.salary < other.salary



