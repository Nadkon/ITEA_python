from abc import ABC, abstractmethod

#Ось так погано
class Worker_bad:
    def work_bad(self):
        pass

    def eat_bad(self):
        pass


class SuperWorker_bad(Worker_bad):

    def work_bad(self):
        pass

    def eat_bad(self): #Але він не вміє їсти бо він СУПЕР і тільки працює. Але ми поминні реалізуувати цей метод бо він наслідється від Воркера
        pass


class Manager_bad:

    def manager_bad(self, worker):
        worker.work_bad()
        worker.eat_bad()



#Краще ось так: створюемо два інтерфайса для методів їсти і працювати і при створенні классу в параметри вписуємо потрібні методи

class Workable(ABC):

    @abstractmethod
    def wirk(self):
        pass

class Eatable(ABC):

    @abs
    def eat(self):
        pass

class Worker(Workable, Eatable):

    def work(self):
        pass

    def eat(self):
        pass

class SuperWorker(Workable):

    def work(self):
        pass

class Manager:

    def menager(seelf, worker):
        worker.work()