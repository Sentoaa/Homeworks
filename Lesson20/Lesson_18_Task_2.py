# Реалізуйте 2 класи, перший з яких - Бос, а другий - Робітник.
# Працівник має властивість "бос", і його значенням має бути екземпляр класу Бос.
# Ви можете перепризначити це значення, але ви повинні перевірити, чи є нове значення босом.
# Кожен бос має список своїх робітників. Ви повинні реалізувати метод, який дозволяє додавати робітників до боса.
# Вам не дозволяється додавати екземпляри класу Boss до списку робітників безпосередньо через доступ до атрибуту,
# використовуйте геттери та сеттери замість цього!

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id_ = id_
        self.name = name
        self.company = company
        self.workers = []

    def __str__(self):
        return f'id_: {self.id_}, name: {self.name}, company: {self.company}'

    def add_workers(self, worker):
        self.workers.append({worker.name: {'id_':worker.id_, 'company':worker.company}})

    def get_workers(self):
        return self.workers

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        if not isinstance(boss, Boss):
            raise ValueError('boss should be an instance of class Boss')
        self.id_ = id_
        self.name = name
        self.company = company
        self.boss = boss

    @property
    def get_boss(self):
        return self.boss

    @get_boss.setter
    def get_boss(self, other):
        if not isinstance(other, Boss):
            raise ValueError('boss should be an instance of class Boss')
        self.boss = other

    def __str__(self):
        return f'id_: {self.id_}, name: {self.name}, company: {self.company}, boss: {self.boss}'


# boss_1 = Boss(1, 'Karl', 'Emiflex')
# boss_2 = Boss(2, 'Brehman', 'ARI-Armaturen')
#
# worker_1 = Worker(1, 'Many', 'Emiflex', boss_1)
# worker_2 = Worker(1, 'Johny', 'Emiflex', boss_1)
#
# print(worker_1.get_boss)
#
# worker_1.get_boss = boss_2
# print(worker_1.get_boss)
#
# boss_1.add_workers(worker_1)
# print(boss_1.workers)
# boss_1.add_workers(boss_2)
# print(boss_1.get_workers())







