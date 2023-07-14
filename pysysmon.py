import psutil
import subprocess

# network usage in bytes
net_io = psutil.net_io_counters()
net_in_bytes = net_io.bytes_recv
net_out_bytes = net_io.bytes_sent

# disk usage
disk_usage = psutil.disk_usage('/').percent

# CPU usage
cpu_usage = psutil.cpu_percent(interval=1)

# memory utilization
mem = psutil.virtual_memory()
mem_usage = mem.percent

# CPU temperature
temp = psutil.sensors_temperatures()['coretemp'][0].current

# themal sensors
tsense = subprocess.run(['sensors'], stdout=subprocess.PIPE).stdout.decode('utf-8')

# create html file with a table displaying system info

with open('pysysmon.html', 'w') as f:
    f.write('<table>\n')
    f.write('<tr><th>Parameter</th><th>Value</th></tr>\n')
    f.write(f'<tr><td>Disk Usage %</td><td>{disk_usage}</td></tr>\n')
    f.write(f'<tr><td>CPU Usage %</td><td>{cpu_usage}</td></tr>\n')
    f.write(f'<tr><td>Memory Usage %</td><td>{mem_usage}</td></tr>\n')
    f.write(f'<tr><td>CPU Temperature</td><td>{temp}</td></tr>\n')
    f.write(f'<tr><td>Network In Bytes</td><td>{net_in_bytes:.2f}</td></tr>\n')
    f.write(f'<tr><td>Network Out Bytes</td><td>{net_out_bytes:.2f}</td></tr>\n')
    f.write(f'<tr><td>Thermal sensors</td><td><pre>{tsense}</pre></td></tr>\n')
    f.write('</table>')
