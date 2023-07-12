import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('/').percent

def get_cpu_temperature():
    return psutil.sensors_temperatures()['coretemp'][0].current

def generate_html_file():
    html = "<table><tr><th>Parameter</th><th>Value</th></tr>"
    html += f"<tr><td>Disk(s) usage %</td><td>{get_disk_usage()}</td></tr>"
    html += f"<tr><td>CPU usage %</td><td>{get_cpu_usage()}</td></tr>"
    html += f"<tr><td>Memory utilization %</td><td>{get_memory_usage()}</td></tr>"
    html += f"<tr><td>CPU temperature</td><td>{get_cpu_temperature()}</td></tr>"
    html += "</table>"
    
    with open("pysysmon.html", "w") as file:
        file.write(html)
        
