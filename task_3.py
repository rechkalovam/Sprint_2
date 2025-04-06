class PointsForPlace:
    @staticmethod
    def get_points_for_place(place):
        points = 0
        if place == str(place):
            print('Ошибка: введите число количества очков, равное месту')
            return 0
        elif place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return 0
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return 0
        points += (101 - place)
        return points

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        points = 0
        if meters == str(meters):
            print('Ошибка: введите число количества очков с учётом расстояния')
            return 0
        elif meters < 0:
            print('Количество метров не может быть отрицательным')
            return 0
        points += meters * 0.5
        return points

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, meters, place):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))
