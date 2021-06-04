from numpy.lib import math
import statistics 
import pandas as pd
import csv


df = pd.read_csv("StudentsPerformance.csv")

# For math scores
math_score_list = df["math score"].to_list()

#Finding the central tendencies

# Property : Central tendies have a similar value
math_score_mean = statistics.mean(math_score_list)
math_score_mode = statistics.mode(math_score_list)
math_score_median = statistics.median(math_score_list)

# printing central tendencies
print("The mean,median and mode are {},{} and {} respectively".format(math_score_mean,math_score_median,math_score_mode))

# getting standard deviation
math_score_stDev = statistics.stdev(math_score_list)

#Getting 1st , 2nd and 3rd deviations
first_math_score_deviation_start,first_math_score_deviation_end = math_score_mean-math_score_stDev,math_score_mean+math_score_stDev 
second_math_score_deviation_start,second_math_score_deviation_end = math_score_mean-(2*math_score_stDev),math_score_mean+(2*math_score_stDev)
third_math_score_deviation_start,third_math_score_deviation_end = math_score_mean-(3*math_score_stDev),math_score_mean+(3*math_score_stDev) 

#Getting data within the deviations

# Property: first deviation has almost 68% of the data
math_score_within_first_deviation = [result for result in math_score_list if result>first_math_score_deviation_start and result<first_math_score_deviation_end]
# Property: second deviation has almost 95% of the data
math_score_within_second_deviation = [result for result in math_score_list if result>second_math_score_deviation_start and result<second_math_score_deviation_end]
# Property: third deviation has almost 99% of the data
math_score_within_third_deviation = [result for result in math_score_list if result>third_math_score_deviation_start and result<third_math_score_deviation_end]

print("{}% of data lies in first standard deviation ".format(len(math_score_within_first_deviation)*100.0/len(math_score_list)))
print("{}% of data lies in second standard deviation ".format(len(math_score_within_second_deviation)*100.0/len(math_score_list)))
print("{}% of data lies in third standard deviation ".format(len(math_score_within_third_deviation)*100.0/len(math_score_list)))

