# sniffer.py
from scapy.all import sniff, IP
from db_handler import DBHandler
from visualizer import generate_graphs
from config import THRESHOLD_PACKETS_PER_SEC, CAPTURE_DURATION
import time
import threading

db = DBHandler()
packet_counter = 0
start_time = time.time()

def packet_callback(packet):
    global packet_counter
    if IP in packet:
        ip_layer = packet[IP]
        length = len(packet)
        protocol = packet.proto
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        db.log_packet((timestamp, ip_layer.src, ip_layer.dst, str(protocol), length))
        packet_counter += 1

def monitor():
    global packet_counter
    while time.time() - start_time < CAPTURE_DURATION:
        time.sleep(1)
        rate = packet_counter
        packet_counter = 0
        print(f"[INFO] Packets/sec: {rate}")
        if rate > THRESHOLD_PACKETS_PER_SEC:
            ts = time.strftime("%Y-%m-%d %H:%M:%S")
            desc = f"DoS suspected: {rate} packets/sec"
            db.log_anomaly((ts, "DoS", desc))

if __name__ == "__main__":
    print("🔍 Starting capture...")
    t = threading.Thread(target=monitor, daemon=True)
    t.start()
    sniff(prn=packet_callback, store=False, timeout=CAPTURE_DURATION)
    t.join()
    generate_graphs()
    print("✅ Capture complete.")
