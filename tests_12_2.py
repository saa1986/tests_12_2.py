import unittest  # Импортируем модуль unittest для написания тестов
from runner import Runner, Tournament  # Импортируем классы Runner и Tournament

class TournamentTest(unittest.TestCase):
    all_results = {}  # Атрибут класса для хранения результатов всех тестов

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # Инициализируем словарь для результатов

    def setUp(self):
        # Создаём 3 объекта Runner
        self.runner1 = Runner("Усэйн", 10)  # Бегун Усэйн со скоростью 10
        self.runner2 = Runner("Андрей", 9)  # Бегун Андрей со скоростью 9
        self.runner3 = Runner("Ник", 3)  # Бегун Ник со скоростью 3

    @classmethod
    def tearDownClass(cls):
        # Выводим результаты всех тестов
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_race_1(self):
        tournament = Tournament(90)  # Создаём турнир на дистанцию 90
        tournament.add_runner(self.runner1)
        tournament.add_runner(self.runner3)
        results = tournament.start()  # Запускаем турнир
        self.all_results[1] = results  # Сохраняем результаты
        self.assertTrue(max(results, key=lambda k: results[k]) == self.runner1.name)  # Проверяем, что Усэйн выиграл

    def test_race_2(self):
        tournament = Tournament(90)  # Создаём турнир на дистанцию 90
        tournament.add_runner(self.runner2)
        tournament.add_runner(self.runner3)
        results = tournament.start()  # Запускаем турнир
        self.all_results[2] = results  # Сохраняем результаты
        self.assertTrue(max(results, key=lambda k: results[k]) == self.runner2.name)  # Проверяем, что Андрей выиграл

    def test_race_3(self):
        tournament = Tournament(90)  # Создаём турнир на дистанцию 90
        tournament.add_runner(self.runner1)
        tournament.add_runner(self.runner2)
        tournament.add_runner(self.runner3)
        results = tournament.start()  # Запускаем турнир
        self.all_results[3] = results  # Сохраняем результаты
        self.assertTrue(max(results, key=lambda k: results[k]) == self.runner2.name)  # Проверяем, что Ник остался последним

if __name__ == "__main__":
    unittest.main()  # Запускаем все тесты