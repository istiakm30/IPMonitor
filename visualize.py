import matplotlib.pyplot as plt
import datetime
import re

# Parse log file
ip_durations = {}
with open('connection_log.txt', 'r') as f:
    for line in f:
        if "Current IP" in line:
            # Extract IP and duration from line
            ip = re.search(r'Current IP (\d+\.\d+\.\d+\.\d+)', line).group(1)
            duration = float(re.search(r'used for (\d+\.\d+)', line).group(1))
            ip_durations[ip] = max(ip_durations.get(ip, 0), duration)

# Plot durations
bars = plt.bar(range(len(ip_durations)), list(ip_durations.values()), align='center')
plt.xticks(range(len(ip_durations)), list(ip_durations.keys()))
plt.ylabel('Duration (minutes)')
plt.xlabel('IP Address')
plt.title('Duration each IP was used')

# Add exact duration on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, round(yval, 2), ha='center', va='bottom')

# Add padding to y-axis limits
plt.ylim(0, max(ip_durations.values()) * 1.1)

plt.show()

