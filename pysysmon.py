# Import modules
import os
import psutil
import datetime
import pandas as pd

# Define system parameters to monitor
parameters = ["system errors (24 hours)", "disk(s) usage", "CPUs usage", "memory utilization %", "CPU and GPU temperature"]

# Define function to get system errors from journalctl
def get_system_errors():
    # Run journalctl command with -p err and -S options to filter errors in the last 24 hours
    command = "journalctl -p err -S '24 hours ago'"
    # Get the output of the command as a string
    output = os.popen(command).read()
    # Return the output or "No errors" if empty
    return output or "No errors"

# Define function to get disk(s) usage from psutil
def get_disk_usage():
    # Get a list of disk partitions from psutil
    partitions = psutil.disk_partitions()
    # Initialize an empty list to store disk usage information
    disk_usage = []
    # Loop through each partition
    for partition in partitions:
        # Get the device name, mount point and usage percentage from psutil
        device = partition.device
        mountpoint = partition.mountpoint
        usage = psutil.disk_usage(mountpoint).percent
        # Append a tuple of device, mountpoint and usage to the disk_usage list
        disk_usage.append((device, mountpoint, usage))
    # Return the disk_usage list
    return disk_usage

# Define function to get CPUs usage from psutil
def get_cpus_usage():
    # Get the number of logical CPUs from psutil
    cpus = psutil.cpu_count()
    # Get the usage percentage of each CPU from psutil
    usage = psutil.cpu_percent(percpu=True)
    # Zip the cpus and usage lists into a list of tuples
    cpus_usage = list(zip(range(1, cpus + 1), usage))
    # Return the cpus_usage list
    return cpus_usage

# Define function to get memory utilization % from psutil
def get_memory_utilization():
    # Get the memory usage percentage from psutil
    memory = psutil.virtual_memory().percent
    # Return the memory value
    return memory

# Define function to get CPU and GPU temperature from psutil (Linux only)
def get_temperature():
    # Get the sensors temperature information from psutil
    sensors = psutil.sensors_temperatures()
    # Initialize an empty list to store temperature information
    temperature = []
    # Loop through each sensor in sensors
    for sensor in sensors:
        # Get the label and current value of the sensor
        label = sensor
        value = sensors[sensor][0].current
        # Append a tuple of label and value to the temperature list
        temperature.append((label, value))
    # Return the temperature list
    return temperature

# Define function to generate an HTML file with a table of system parameters and values
def generate_html(parameters):
    # Initialize an empty dictionary to store parameter names and values
    data = {}
    # Loop through each parameter in parameters
    for parameter in parameters:
        # Evaluate the parameter as a function call and assign the result to data[parameter]
        data[parameter] = eval(parameter + "()")
    # Convert the data dictionary into a pandas DataFrame with parameter names as columns and values as rows
    df = pd.DataFrame(data, index=[0])
    # Convert the DataFrame into an HTML table with bootstrap styling and save it as "system_monitor.html"
    df.to_html("system_monitor.html", classes="table table-striped")
    
# Call the generate_html function with parameters as argument    
generate_html(parameters)

# Print a message indicating the script is done and where to find the HTML file 
print("The script is done. You can find the HTML file with the system parameters in system_monitor.html")
