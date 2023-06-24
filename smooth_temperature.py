import matplotlib.pyplot as plt
import sys
import numpy as np
import pandas as pd
from statsmodels.nonparametric.smoothers_lowess import lowess
from pykalman import KalmanFilter


filename = sys.argv[1]
cpu_data = pd.read_csv(filename)

loess_smoothed = lowess(cpu_data['temperature'], cpu_data.index, frac=0.1)
kalman_data = cpu_data[['temperature', 'cpu_percent', 'sys_load_1', 'fan_rpm']]


initial_state = kalman_data.iloc[0]
observation_covariance = np.diag([1, 1, 1, 1])
transition_covariance = np.diag([1, 1, 1, 1])
transition = [[0.94, 0.5, 0.2, -0.01], [0.1, 0.4, 2.1, 0], [0, 0, 0.94, 0], [0, 0, 0, 1]]

kf = KalmanFilter( initial_state_mean=initial_state.to_numpy(),
    initial_state_covariance=np.eye(4),
    observation_covariance=observation_covariance,
    transition_covariance=transition_covariance,
    transition_matrices=transition)
kalman_smoothed, _ = kf.smooth(kalman_data)


plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(cpu_data['timestamp'], cpu_data['temperature'], 'b.', alpha=0.5, label='Temperature')
plt.plot(cpu_data['timestamp'], loess_smoothed[:, 1], 'r-', label='LOESS Smoothed')
plt.xlabel('Timestamp')
plt.ylabel('Temperature')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(cpu_data['timestamp'], cpu_data['temperature'], 'b.', alpha=0.5, label='Temperature')
plt.plot(cpu_data['timestamp'], kalman_smoothed[:, 0], 'g-', label='Kalman Smoothed')
plt.xlabel('Timestamp')
plt.ylabel('Temperature')
plt.legend()
plt.show()