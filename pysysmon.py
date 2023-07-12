# Import the modules
import os
import psutil
import subprocess
import html

# Define the function to get disk usage percentage
def get_disk_usage():
    # Get the disk partitions
    partitions = psutil.disk_partitions()
    # Initialize an empty list to store the results
    disk_usage_list = []
    # Loop through each partition
    for partition in partitions:
        # Get the mount point of the partition
        mount_point = partition.mountpoint
        # Get the disk usage of the partition
        disk_usage = psutil.disk_usage(mount_point)
        # Get the percentage of used space
        percent = disk_usage.percent
        # Append the result to the list as a tuple of mount point and percentage
        disk_usage_list.append((mount_point, percent))
    # Return the list of results
    return disk_usage_list

# Define the function to get CPU usage percentage
def get_cpu_usage():
    # Get the CPU usage percentage as a float
    cpu_usage = psutil.cpu_percent()
    # Return the result
    return cpu_usage

# Define the function to get memory utilization percentage
def get_memory_utilization():
    # Get the memory usage information
    memory_usage = psutil.virtual_memory()
    # Get the percentage of used memory
    percent = memory_usage.percent
    # Return the result
    return percent

# Define the function to get CPU temperature in Celsius
def get_cpu_temperature():
    # Use a subprocess to run the sensors command and capture the output
    output = subprocess.check_output(["sensors"])
    # Decode the output from bytes to string
    output = output.decode("utf-8")
    # Split the output by lines
    lines = output.split("\n")
    # Initialize an empty list to store the results
    cpu_temperature_list = []
    # Loop through each line
    for line in lines:
        # Check if the line contains the word "Core"
        if "Core" in line:
            # Split the line by spaces and get the third element, which is the temperature value
            temperature = line.split()[2]
            # Remove the plus sign and the degree symbol from the temperature value
            temperature = temperature.replace("+", "").replace("°C", "")
            # Convert the temperature value from string to float
            temperature = float(temperature)
            # Append the result to the list as a tuple of core number and temperature value
            cpu_temperature_list.append((line.split()[0], temperature))
    # Return the list of results
    return cpu_temperature_list

# Define the function to generate an HTML file with a table of system parameters and values
def generate_html_file(disk_usage_list, cpu_usage, memory_utilization, cpu_temperature_list):
    # Create an HTML document object
    doc = html.HTMLDocument()
    # Add a title to the document
    doc.add_title("PySysMon - Python System Monitor")
    # Add a heading to the document body with the title text
    doc.add_heading("PySysMon - Python System Monitor", level=1)
    # Add a paragraph to the document body with some introduction text
    doc.add_paragraph("This is a simple Python script that checks some system parameters and generates an HTML file with a table of results.")
    # Add a table to the document body with two columns and a header row
    table = doc.add_table(columns=2, header_row=["Parameter", "Value"])
    # Loop through each disk usage result and add a row to the table with the mount point and percentage value
    for disk_usage in disk_usage_list:
        table.add_row([f"Disk usage ({disk_usage[0]})", f"{disk_usage[1]}%"])
    # Add a row to the table with the CPU usage percentage value
    table.add_row(["CPU usage", f"{cpu_usage}%"])
    # Add a row to the table with the memory utilization percentage value
    table.add_row(["Memory utilization", f"{memory_utilization}%"])
    # Loop through each CPU temperature result and add a row to the table with the core number and temperature value in Celsius
    for cpu_temperature in cpu_temperature_list:
        table.add_row([f"CPU temperature ({cpu_temperature[0]})", f"{cpu_temperature[1]} °C"])
    # Write the HTML document to a file named pysysmon.html
    doc.write_to_file("pysysmon.html")

# Call the functions to get the system parameters values
disk_usage_list = get_disk_usage()
cpu_usage = get_cpu_usage()
memory_utilization = get_memory_utilization()
cpu_temperature_list = get_cpu_temperature()

# Call the function to generate the HTML file with the table of results
generate_html_file(disk_usage_list, cpu_usage, memory_utilization, cpu_temperature_list)
    
