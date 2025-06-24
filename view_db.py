# view_db.py
import sqlite3
import csv

DB_FILE = "network_traffic.db"

def export_to_csv():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM packets")
    packets = cursor.fetchall()
    with open("packets_export.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "src_ip", "dst_ip", "protocol", "length"])
        writer.writerows(packets)
    print("✅ Packets exported to packets_export.csv")

    cursor.execute("SELECT * FROM anomalies")
    anomalies = cursor.fetchall()
    with open("anomalies_export.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "type", "description"])
        writer.writerows(anomalies)
    print("✅ Anomalies exported to anomalies_export.csv")

    conn.close()

def filter_by_ip(ip):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    print(f"\n📦 Packets involving IP {ip}:")
    cursor.execute("""
        SELECT * FROM packets 
        WHERE src_ip = ? OR dst_ip = ?
    """, (ip, ip))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No packets found for this IP.")

    conn.close()

def view_all():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    print("\n📦 Packets Table:")
    cursor.execute("SELECT * FROM packets")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No packet data found.")

    print("\n🚨 Anomalies Table:")
    cursor.execute("SELECT * FROM anomalies")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No anomaly data found.")

    conn.close()

if __name__ == "__main__":
    print("\n👑 Network Sniffer DB Viewer")
    print("1️⃣ View all records")
    print("2️⃣ Filter packets by IP")
    print("3️⃣ Export packets + anomalies to CSV")
    choice = input("Select an option (1/2/3): ").strip()

    if choice == "1":
        view_all()
    elif choice == "2":
        ip = input("Enter IP to filter: ").strip()
        filter_by_ip(ip)
    elif choice == "3":
        export_to_csv()
    else:
        print("❌ Invalid choice.")
