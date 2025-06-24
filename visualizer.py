# visualizer.py
import sqlite3
import matplotlib.pyplot as plt

def generate_graphs():
    conn = sqlite3.connect('network_traffic.db')
    cursor = conn.cursor()

    cursor.execute("SELECT timestamp, length FROM packets")
    data = cursor.fetchall()

    timestamps = [row[0][-8:] for row in data]
    lengths = [row[1] for row in data]

    plt.figure(figsize=(10, 4))
    plt.plot(lengths, label="Packet Lengths", color='blue')
    plt.title("Traffic Packet Sizes Over Time")
    plt.xlabel("Packet #")
    plt.ylabel("Length (bytes)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("traffic_plot.png")
    plt.close()

    cursor.execute("SELECT timestamp, type FROM anomalies")
    anomaly_data = cursor.fetchall()
    if anomaly_data:
        times = [row[0][-8:] for row in anomaly_data]
        labels = [row[1] for row in anomaly_data]
        plt.figure(figsize=(8, 4))
        plt.bar(times, [1]*len(times), color='red')
        plt.title("Detected Anomalies (Timestamps)")
        plt.ylabel("Alert Triggered")
        plt.tight_layout()
        plt.savefig("anomalies_plot.png")
        plt.close()

    conn.close()
    print("📊 Graphs generated.")
