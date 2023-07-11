# pysysmon

pysysmon is a Python script that monitors the following system parameters on Linux:

- system errors (24 hours)
- disk(s) usage
- CPUs usage
- memory utilization %
- CPU and GPU temperature

The script generates an HTML file with a table that includes all the system parameters and their respective values.

## Requirements

pysysmon requires Python 3 and the psutil module. You can install psutil using pip or apt:

```pip install psutil```

or

```apt install python3-psutil```
