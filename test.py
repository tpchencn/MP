# coding: utf-8
import matplotlib.pyplot as plt
from random import choice


# 折线图
# input_value = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_value, squares, linewidth=5)
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# plt.tick_params(axis='both', labelsize=14)
# plt.show()

# 散点图
# x_value = list(range(1, 1001))
# y_value = [i ** 2 for i in x_value]
#
# plt.scatter(x_value, y_value, edgecolors='none', c=y_value, cmap=plt.cm.Blues, s=10)
#
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("value", fontsize=24)
# plt.ylabel("Square of Value", fontsize=14)
# plt.axis([0, 1100, 0, 1100000])
#
# plt.tick_params(axis='both', which='major', labelsize=14)
#
# plt.savefig('squares_plot.png', bbox_inches='tight')
# plt.show()


class RandomWalk():
    def __init__(self, num_points=500):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
