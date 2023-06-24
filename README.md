# GitHub Repository: CPU Temperature Noise Reduction

This GitHub repository contains a Python program, `smooth_temperature.py`, that aims to reduce noise and extract the true CPU temperature from the provided data. The data consists of CPU temperature, CPU usage, system load, and fan speed measurements collected over time.

**Instructions:**
Follow the steps below to run the program and perform noise reduction on the CPU temperature data:

1. Clone the repository: Start by cloning the repository to your local machine using the following command:
```
git clone https://github.com/jaisreet/cpu-temperature-noise-reduction.git
```

2. Navigate to the project directory: Move into the project directory using the command:
```
cd cpu-temperature-noise-reduction
```

3. Run the program: Execute the Python program `smooth_temperature.py` with the input CSV file as a command-line argument. Replace `sysinfo.csv` with the actual filename if different.
```
python smooth_temperature.py sysinfo.csv
```

4. View the results: The program will generate a plot with the original CPU temperature data points, LOESS-smoothed line, and Kalman-smoothed line. The legend will distinguish between the lines. The plot will be saved as `cpu.svg` in the repository directory.

For detailed code implementation and analysis, please refer to the [GitHub repository](https://github.com/jaisreet/cpu-temperature-noise-reduction).
