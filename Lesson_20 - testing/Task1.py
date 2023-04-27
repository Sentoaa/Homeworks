import Lesson_18_Task_2
import unittest


class BossTestCase(unittest.TestCase):

    def setUp(self):
        self.the_boss_1 = Lesson_18_Task_2.Boss(1, 'Karl', 'Emiflex')
        self.the_worker = Lesson_18_Task_2.Worker(1, 'Many', 'Emiflex', self.the_boss_1)

    def test_boss_add_workers(self):
        self.assertEqual(self.the_boss_1.workers, [])
        self.the_boss_1.add_workers(self.the_worker)
        self.assertEqual(self.the_boss_1.workers, [{self.the_worker.name: {'id_':self.the_worker.id_, 'company':self.the_worker.company}}])

    def test_boss_get_workers(self):
        self.assertEqual(self.the_boss_1.workers, [])
        self.the_boss_1.add_workers(self.the_worker)
        self.assertEqual(self.the_boss_1.workers, [{'Many': {'id_':1, 'company':'Emiflex'}}])


class WorkersTestCase(unittest.TestCase):

    def setUp(self):
        self.the_boss_1 = Lesson_18_Task_2.Boss(1, 'Karl', 'Emiflex')
        self.the_boss_2 = Lesson_18_Task_2.Boss(2, 'Brehman', 'ARI-Armaturen')
        self.the_worker = Lesson_18_Task_2.Worker(1, 'Many', 'Emiflex', self.the_boss_1)

    def test_worker_get_boss(self):
        self.assertEqual(self.the_worker.get_boss, self.the_boss_1)

    def test_worker_sett_boss(self):
        self.the_worker.get_boss = self.the_boss_2
        self.assertEqual(self.the_worker.get_boss, self.the_boss_2)



# unittest.main()