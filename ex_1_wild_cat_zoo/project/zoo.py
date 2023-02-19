from project import animal
from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self._budget = budget
        self._animal_capacity = animal_capacity
        self._workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, anima: Animal, price):

        if self._budget >= price and self._animal_capacity >= 1:
            self._budget -= price
            self._animal_capacity -= 1
            self.animals.append(anima)
            return f"{anima.name} the {anima.__class__.__name__} added to the zoo"
        if self._budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self._workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for wrk in self.workers:
            if wrk.name == worker_name:
                self.workers.remove(wrk)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum(w.salary for w in self.workers)
        if salaries > self._budget:
            return "You have no budget to pay your workers. They are unhappy"
        self._budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self._budget}"

    def tend_animals(self):
        animals_expenses = sum(e.money_for_care for e in self.animals)
        if self._budget >= animals_expenses:
            self._budget -= animals_expenses
            return f"You tended all the animals. They are happy. Budget left: {self._budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self._budget += amount

    def animals_status(self):
        lions = [repr(l) for l in self.animals if isinstance(l, Lion)]
        tigers = [repr(t) for t in self.animals if isinstance(t, Tiger)]
        cheetahs = [repr(c) for c in self.animals if isinstance(c, Cheetah)]
        result = f"You have {len(self.animals)} animals\n"
        result += f'----- {len(lions)} Lions:\n'
        for lion in lions :
            result += lion +'\n'
        result += f'----- {len(tigers)} Tigers:\n'
        for tiger in tigers:
            result += tiger + '\n'
        result += f'----- {len(cheetahs)} Cheetahs:\n'
        for cheetah in cheetahs:
            result += cheetah + '\n'
        return result
    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'

        keepers = [repr(k) for k in self.workers if isinstance(k,Keeper)]
        caretakers = [repr(c) for c in self.workers if isinstance(c,Caretaker)]
        vets = [repr(v) for v in self.workers if isinstance(v,Vet)]

        result += f'----- {len(keepers)} Keepers:\n'
        result += '\n'.join(keepers) + '\n'
        result += f'----- {len(caretakers)} Caretakers:\n'
        result += '\n'.join(caretakers) + '\n'
        result += f'----- {len(vets)} Vets:\n'
        result += '\n'.join(vets) + '\n'
        return result












