# Import modules
import os
import psutil
import subprocess
import pandas as pd

# Define a function to get disk usage %
def get_disk_usage():
    # Get the disk partitions
    partitions = psutil.disk_partitions()
    # Create an empty list to store the results
    results = []
    # Loop through each partition
    for partition in partitions:
        # Get the device name, mount point, and usage %
        device = partition.device
        mountpoint = partition.mountpoint
        usage = psutil.disk_usage(mountpoint).percent
        # Append the result as a tuple to the list
        results.append((device, mountpoint, usage))
    # Return the list of results
    return results

# Define a function to get CPU usage %
def get_cpu_usage():
    # Get the CPU usage % as a float
    usage = psutil.cpu_percent()
    # Return the result
    return usage

# Define a function to get memory utilization %
def get_memory_utilization():
    # Get the memory utilization % as a float
    utilization = psutil.virtual_memory().percent
    # Return the result
    return utilization

# Define a function to get CPU temperature
def get_cpu_temperature():
    # Run the command 'sensors' and capture the output as a string
    output = subprocess.check_output('sensors').decode('utf-8')
    # Split the output by lines
    lines = output.split('\n')
    # Loop through each line
    for line in lines:
        # If the line contains 'Core 0'
        if 'Core 0' in line:
            # Split the line by spaces and get the third element as the temperature
            temperature = line.split()[2]
            # Remove the '+' sign and the '°C' unit from the temperature
            temperature = temperature.replace('+', '').replace('°C', '')
            # Convert the temperature to a float
            temperature = float(temperature)
            # Return the result
            return temperature

# Call the functions and store the results in variables
disk_usage = get_disk_usage()
cpu_usage = get_cpu_usage()
memory_utilization = get_memory_utilization()
cpu_temperature = get_cpu_temperature()

# Create a pandas DataFrame from the results
df = pd.DataFrame(disk_usage, columns=['Device', 'Mountpoint', 'Disk Usage %'])
df['CPU Usage %'] = cpu_usage
df['Memory Utilization %'] = memory_utilization
df['CPU Temperature'] = cpu_temperature

# Convert the DataFrame to an HTML file with a table
df.to_html('system_values.html', index=False)
