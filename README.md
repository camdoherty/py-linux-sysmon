# pysysmon

A python script that collects and displays system information in an HTML file. It uses the psutil to get metrics of system performance, health and security.

## Features

The following system information is displayed in a table format in an html file.

- Disk usage percentage
- CPU usage percentage
- Memory usage percentage
- Network in and out rate (bytes/second)
- Thermal sensors output
- User accounts and privileges
- Processes and attributes
- Network connections and details

## Requirements

- psutil

Installation:

```bash
sudo apt install python3-psutil
```

## Usage

```bash
python pysysmon.py
```

This will create an HTML file called pysysmon.html in the same directory as the script. You can open this file in your browser to view the system information.
