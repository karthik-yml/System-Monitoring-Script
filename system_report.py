import psutil
from datetime import datetime
import time
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import matplotlib.pyplot as plt

# Lists to store data
timestamps = []
cpu_usages = []
ram_usages = []

# Number of data points to collect
num_data_points = 5  # Collect data for 10 seconds

for _ in range(num_data_points):
    # Get current timestamp
    current_time = datetime.now().strftime("%H:%M:%S")

    # Collect CPU usage
    cpu_usage = psutil.cpu_percent(1)

    # Collect RAM usage
    ram_usage = psutil.virtual_memory()[2]

    # Append data to lists
    timestamps.append(current_time)
    cpu_usages.append(cpu_usage)
    ram_usages.append(ram_usage)

    # Wait for 1 second before collecting the next data point
    time.sleep(1)

# Create PDF report
pdf_file = "system_report.pdf"
pdf_buffer = io.BytesIO()

# Create a canvas for PDF
c = canvas.Canvas(pdf_buffer, pagesize=letter)
c.setFont("Helvetica", 12)

# Add CPU and RAM graphs to the PDF
plt.figure(figsize=(6, 3))
plt.plot(timestamps, cpu_usages, label='CPU Usage', marker='o', linestyle='-')
plt.title('CPU Usage Over Time')
plt.xlabel('Time')
plt.ylabel('CPU Usage (%)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.savefig("cpu_graph.png")

plt.figure(figsize=(6, 3))
plt.plot(timestamps, ram_usages, label='RAM Usage', marker='o', linestyle='-')
plt.title('RAM Usage Over Time')
plt.xlabel('Time')
plt.ylabel('RAM Usage (%)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.savefig("ram_graph.png")

# Draw CPU and RAM graphs in the PDF
c.drawImage("cpu_graph.png", 50, 500, width=400, height=200)
c.drawImage("ram_graph.png", 50, 300, width=400, height=200)

# Add other data to the PDF
c.drawString(50, 750, "CPU and RAM Usage Report")
c.drawString(50, 730, "Timestamps: " + ', '.join(timestamps))
c.drawString(50, 710, "CPU Usages: " + ', '.join(map(str, cpu_usages)))
c.drawString(50, 690, "RAM Usages: " + ', '.join(map(str, ram_usages)))

# Get a list of all open network connections
net_connections = psutil.net_connections(kind='inet')
open_ports_info = []

# Add open ports information to the PDF
c.drawString(50, 250, "Open Ports Information:")
for i, conn in enumerate(net_connections, start=1):
    try:
        port = conn.laddr.port
        pid = conn.pid
        process_name = psutil.Process(pid).name() if pid else "N/A"
        port_info = f"Port: {port}, Process Name: {process_name}, PID: {pid}"
        open_ports_info.append(port_info)
        c.drawString(50, 230 - (i * 20), port_info)
    except psutil.AccessDenied:
        port_info = f"Port: {port}, Process Name: N/A (Access Denied), PID: N/A"
        open_ports_info.append(port_info)
        c.drawString(50, 230 - (i * 20), port_info)

# Save the PDF report
c.save()
pdf_buffer.seek(0)

# Write the PDF report to a file
with open(pdf_file, 'wb') as f:
    f.write(pdf_buffer.read())

print(f"PDF report saved to {pdf_file}")
