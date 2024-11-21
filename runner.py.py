

class Runner:
    def __init__(self, name, speed):
        self.name = name  # Инициализируем имя бегуна
        self.speed = speed  # Инициализируем скорость бегуна
        self.distance = 0  # Устанавливаем начальное значение дистанции в 0

    def walk(self):
        self.distance += self.speed * 0.5  # При каждом вызове метода walk увеличиваем дистанцию на speed * 0.5

    def run(self):
        self.distance += self.speed  # При каждом вызове метода run увеличиваем дистанцию на speed

    def __eq__(self, other):
        return self.name == other.name  # Сравниваем имена бегунов

class Tournament:
    def __init__(self, distance):
        self.distance = distance  # Устанавливаем дистанцию для турнира
        self.runners = []  # Список участников

    def add_runner(self, runner):
        self.runners.append(runner)  # Добавляем бегуна в список участников

    def start(self):
        results = {}
        for runner in self.runners:
            # Логика бега
            while runner.distance < self.distance:
                runner.run()  # Бегун бежит
            results[runner.name] = runner.distance  # Сохраняем результат
        return results