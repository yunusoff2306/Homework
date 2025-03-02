import numpy as np

arr = np.arange(1, 11)
squared_arr = np.square(arr)
sum_squared = np.sum(squared_arr)
mean_squared = np.mean(squared_arr)
std_squared = np.std(squared_arr)
print("Asl massiv:", arr)
print("Kvadratlar massivi:", squared_arr)
print("Yig‘indisi:", sum_squared)
print("O‘rtacha qiymati:", mean_squared)
print("Standart og‘ish:", std_squared)
