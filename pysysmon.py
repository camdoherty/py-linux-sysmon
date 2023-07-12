import psutil

# gives a single float value
cpu_usage = psutil.cpu_percent(interval=1) / psutil.cpu_count()

# gives an object with many fields
mem = psutil.virtual_memory()
mem_usage = mem.percent

# disk usage
disk_usage = psutil.disk_usage('/').percent

# CPU temperature
temp = psutil.sensors_temperatures()['coretemp'][0].current

with open('pysysmon.html', 'w') as f:
    f.write('<table>\n')
    f.write('<tr><th>Parameter</th><th>Value</th></tr>\n')
    f.write(f'<tr><td>Disk Usage %</td><td>{disk_usage}</td></tr>\n')
    f.write(f'<tr><td>CPU Usage %</td><td>{cpu_usage}</td></tr>\n')
    f.write(f'<tr><td>Memory Utilization %</td><td>{mem_usage}</td></tr>\n')
    f.write(f'<tr><td>CPU Temperature</td><td>{temp}</td></tr>\n')
    f.write('</table>')

