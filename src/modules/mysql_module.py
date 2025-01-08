import mysql.connector
import subprocess
from datetime import datetime

class MySQLModule:
    def __init__(self):
        self.connection = None
    
    def connect_to_db(self, host, user, password, database):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            return True
        except Exception as e:
            raise Exception(f"Datenbankverbindungsfehler: {str(e)}")
    
    def backup_database(self, backup_path):
        if not self.connection:
            raise Exception("Keine aktive Datenbankverbindung")
        
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_file = f"{backup_path}/backup_{timestamp}.sql"
            
            with open(backup_file, 'w') as output:
                subprocess.run(
                    ['mysqldump', '-h', self.connection.server_host,
                     '-u', self.connection.user, f'-p{self.connection.password}',
                     self.connection.database],
                    stdout=output
                )
            return backup_file
        except Exception as e:
            raise Exception(f"Backup-Fehler: {str(e)}")