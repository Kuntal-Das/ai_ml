import random
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


class LinReg:
    def __init__(self):
        self.epoch = 10**5
        self.lr = 0.1
        self.slope = random.random()
        self.y_intercept = random.random()

    def train(self, experiences, salaries):
        for i in range(self.epoch):
            # randIndx = random.randint(0, len(experiences)-1)
            for j in range(len(experiences)):
                if random.randint(0, len(experiences)-1) == j:
                    continue
                salPred = self.slope * \
                    experiences[j] + self.y_intercept
                if salPred < salaries[j]:  # above
                    self.slope += self.lr * experiences[j]
                    self.y_intercept += self.lr
                else:  # below
                    self.slope -= self.lr * experiences[j]
                    self.y_intercept -= self.lr

            if i % 10000 == 0:
                print(
                    f"MAE loss: {self.calc_MAE_error(experiences,salaries)}")
                self.lr -= 0.01

    def calc_MAE_error(self, experiences, salaries):
        error = 0.0
        for (x, y) in zip(experiences, salaries):
            error += abs(y - ((self.slope*x) + self.y_intercept))

        return error / len(experiences)

    def predict_y(self, experience):
        return (self.slope * experience) + self.y_intercept

    def plot(self, experiences, salary):
        plt.plot(experiences, salary, linestyle="dashed")
        plt.plot(experiences, [self.predict_y(exp)
                 for exp in experiences], linestyle="dashed")


if __name__ == '__main__':
    df = pd.read_csv('datasets/Salary_Data.csv')
    linreg = LinReg()
    linreg.train(df['YearsExperience'], df['Salary'])
    pred_sal = linreg.predict_y(2.5)
    print(f"Predicted salary for 2.5 year experienced: {pred_sal}")
    # linreg.plot(df['YearsExperience'], df['Salary'])
