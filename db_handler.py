# db_handler.py
import sqlite3
import threading
import queue

class DBHandler:
    def __init__(self, db_file='network_traffic.db'):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.queue = queue.Queue()
        self._create_tables()
        self.lock = threading.Lock()

        # Start a thread to handle all DB writes
        threading.Thread(target=self._writer, daemon=True).start()

    def _create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS packets (
                timestamp TEXT, src_ip TEXT, dst_ip TEXT, protocol TEXT, length INTEGER
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS anomalies (
                timestamp TEXT, type TEXT, description TEXT
            )
        ''')
        self.conn.commit()

    def log_packet(self, packet):
        self.queue.put(('packet', packet))

    def log_anomaly(self, anomaly):
        self.queue.put(('anomaly', anomaly))

    def _writer(self):
        while True:
            task_type, data = self.queue.get()
            with self.lock:
                if task_type == 'packet':
                    self.cursor.execute("INSERT INTO packets VALUES (?, ?, ?, ?, ?)", data)
                elif task_type == 'anomaly':
                    self.cursor.execute("INSERT INTO anomalies VALUES (?, ?, ?)", data)
                self.conn.commit()
