# 🛡️ Network Packet Sniffer with Anomaly Detection

A Python-based tool that monitors, logs, and visualizes network traffic in real-time, while detecting anomalies like DoS attempts. Designed for cybersecurity interns, students, and professionals.

---

## 🚀 Features

✅ Real-time packet sniffing (IP, ports, protocol, size)  
✅ SQLite DB logging (packets + anomalies)  
✅ Basic DoS detection (packets/sec threshold)  
✅ Auto-generated matplotlib traffic & anomaly graphs  
✅ CSV export + DB viewer CLI  
✅ Modular, extendable architecture  

---

## 🛠️ Technologies

- Python 3.12  
- scapy  
- sqlite3  
- matplotlib  
- threading  

---

## 📂 Project Structure

```bash
.
├── sniffer.py
├── db_handler.py
├── visualizer.py
├── view_db.py
├── config.py
├── requirements.txt
├── PROJECT_IMAGES/
├── traffic_plot.png
├── anomalies_plot.png
├── report.pdf
└── README.md
⚡ Usage

1️⃣ Install requirements
pip install -r requirements.txt

2️⃣ Run the sniffer
python sniffer.py

3️⃣ View DB / export CSV
python view_db.py

📊 Example Output
Architecture Diagram
Traffic Graph
Anomalies Graph

📜 License
MIT License — see LICENSE for details.







