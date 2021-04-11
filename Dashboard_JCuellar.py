# Julia Cuellar
# DSC 640
# Dashboard

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_file():
    accident = pd.read_csv('Accidents and fatalities per year - Accidents and fatalities per year.csv')
    print("Display data with null:\n", accident.isnull())
    print("Display counts of null from data:\n", accident.isnull().sum())
    accident = accident.fillna(" ")
    print("Display data with replaced nulls:\n", accident)
    print("Display recounts of null from data:\n", accident.isnull().sum())
    print('Data:\n', accident)
    accident.to_csv('Accident.csv')


# Will use in Dashboard
def read_file2():
    air = pd.read_csv('air-safety.csv')
    print("Display data with null:\n", air.isnull())
    print("Display counts of null from data:\n", air.isnull().sum())
    print('Data:\n', air)
    plt.hist(air)
    plt.title('Histogram of Air')
    # plt.show()


def read_file3():
    seat = pd.read_excel('Departed Seats.xls', index_col=0)
    print("Display data with null:\n", seat.isnull())
    print("Display counts of null from data:\n", seat.isnull().sum())
    seat = seat.fillna(" ")
    print("Display data with replaced nulls:\n", seat)
    print("Display recounts of null from data:\n", seat.isnull().sum())
    print('Data:\n', seat)
    seat.to_csv('Seat.csv')


# Will use in Dashboard
def read_file4():
    financial = pd.read_csv('Financials_Full_Data_data.csv')
    print("Display data with null:\n", financial.isnull())
    print("Display counts of null from data:\n", financial.isnull().sum())
    print('Data:\n', financial)
    plt.hist(financial)
    plt.title('Histogram of Financials')
    # plt.show()


# Will use in Dashboard
def read_file5():
    safety = pd.read_csv('Safety Record of U.S. Air Carriers.csv')
    print("Display data with null:\n", safety.isnull())
    print("Display counts of null from data:\n", safety.isnull().sum())
    print('Data:\n', safety)
    plt.hist(safety)
    plt.title('Histogram of Safety')
    # plt.show()


def read_file6():
    traffic = pd.read_csv('Traffic_&_Capacity_Full_Data_data.csv')
    print("Display data with null:\n", traffic.isnull())
    print("Display counts of null from data:\n", traffic.isnull().sum())
    traffic = traffic.fillna(" ")
    print("Display data with replaced nulls:\n", traffic)
    print("Display recounts of null from data:\n", traffic.isnull().sum())
    print('Data:\n', traffic)
    traffic.to_csv('Traffic.csv')


if __name__ == "__main__":
    read_file()
    read_file2()
    read_file3()
    read_file4()
    read_file5()
    read_file6()