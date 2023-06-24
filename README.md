# CPU Temperature Noise Reduction

## Problem Statement

The task is to reduce the noise in the CPU temperature data collected from a computer system. The data includes CPU temperature, CPU usage, system load, and fan speed sampled every minute. The goal is to separate the noise from the legitimate changes in the true temperature and obtain a smoothed temperature signal.

## Approach and Methods

1. **LOESS Smoothing**

   - Use the `lowess` function from the `statsmodels` library to perform LOESS (Locally Estimated Scatterplot Smoothing) smoothing on the temperature values.
   - Adjust the `frac` parameter to balance between preserving high-temperature spikes caused by momentary CPU usage and smoothing out relatively flat temperature periods.
   - Plot the original temperature data as blue dots using `plt.plot` and the LOESS-smoothed temperature values as a red line using `plt.plot`.

2. **Kalman Smoothing**

   - Select the relevant columns (temperature, CPU percent, system load, and fan RPM) from the original data and store them in a DataFrame called `kalman_data`.
   - Define the initial state and covariance matrices for the Kalman filter. Choose appropriate non-zero values for observation covariance and transition covariance matrices based on expected sensor errors and prediction accuracy.
   - Define the transition matrix to predict the "next" values of the observed variables using a regression model. Adjust the coefficients based on manual tweaking and regression analysis.
   - Experiment with the parameter values to achieve the best smoothed result while considering the tradeoff between noise removal and preserving true signal changes.
   - Apply the Kalman filter using the `KalmanFilter` class and obtain the smoothed temperature values.
   - Plot the original temperature data as blue dots, the LOESS-smoothed temperature values as a red line, and the Kalman-smoothed temperature values as a green line using `plt.plot`.

3. **Final Output**

   - Add a legend to the plot using `plt.legend` to distinguish the data points, LOESS-smoothed line, and Kalman-smoothed line.
   - Save the plot as an SVG file named "cpu.svg" using `plt.savefig('cpu.svg')`.
   - Make sure the program does not display a window during execution.

To run the program, execute the following command in the command line:

```
python3 smooth_temperature.py sysinfo.csv
```

Replace "sysinfo.csv" with the actual filename of the input CSV file containing the CPU temperature data.

The resulting plot will be saved as "cpu.svg" with the original temperature data, LOESS-smoothed line, and Kalman-smoothed line.
