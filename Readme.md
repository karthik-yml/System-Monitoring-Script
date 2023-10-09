# System Monitoring and Reporting Script

This Python script collects system performance data, including CPU and RAM usage, and generates a PDF report containing this data along with information about open ports and associated processes. The report includes graphs to visualize CPU and RAM usage trends.

## Prerequisites

Before running the script, ensure you have the following prerequisites installed:

- Python 3.x
- `psutil` library (for system data collection)
- `matplotlib` library (for graph generation)
- `reportlab` library (for PDF generation)

## Usage

Step 1 - Clone this repository to your local machine:

git clone https://github.com/karthik-yml/System-Monitoring-Script.git

Step 2 - Navigate to the project directory:

cd system-monitoring-script

Step 3 - Install required libraries

pip install -r requirements.txt

Step 4 - Run the script:

sudo python3 system_monitoring.py

After execution, a PDF report named system_report.pdf will be generated in the project directory.

## Report Contents

The generated PDF report includes the following sections:

CPU and RAM Usage Graphs: Line graphs displaying CPU and RAM usage over time.

System Information: Timestamps, CPU usages, and RAM usages during data collection.

Open Ports Information: Information about open ports and associated process names and PIDs.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

The script utilizes the psutil library to gather system data.

Graphs are generated using matplotlib.

The PDF report is created with reportlab.

Feel free to customize and enhance this script to suit your needs.

