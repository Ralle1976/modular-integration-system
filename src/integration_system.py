from modules.google_drive_module import GoogleDriveModule
from modules.mysql_module import MySQLModule
from modules.github_module import GitHubModule
from modules.openapi_chatgpt_module import OpenAIChatGPTModule

class IntegrationSystem:
    def __init__(self, config):
        self.google_drive = GoogleDriveModule(config['google_drive_credentials'])
        self.mysql = MySQLModule()
        self.github = GitHubModule(config['github_token'])
        self.chatgpt = OpenAIChatGPTModule(config['openai_api_key'])
    
    def example_workflow(self):
        try:
            # 1. Verbinde mit MySQL und erstelle Backup
            self.mysql.connect_to_db(
                host="localhost",
                user="user",
                password="password",
                database="mydatabase"
            )
            backup_file = self.mysql.backup_database("./backups")
            
            # 2. Lade Backup in Google Drive hoch
            folder_id = self.google_drive.create_folder("Database Backups")
            file_id = self.google_drive.upload_file(
                "latest_backup.sql",
                folder_id,
                backup_file
            )
            
            # 3. Erstelle GitHub Branch und pushe Backup
            self.github.set_repo("myproject")
            self.github.create_branch("backup/latest")
            self.github.push_file(
                "myproject",
                "backups/latest_backup.sql",
                open(backup_file).read(),
                "Automated database backup"
            )
            
            # 4. Sende Bestätigungsnachricht an ChatGPT
            status = self.chatgpt.send_message(
                "Bitte erstelle eine Zusammenfassung des Backup-Prozesses"
            )
            
            return {
                "backup_file": backup_file,
                "drive_file_id": file_id,
                "status_summary": status
            }
        
        except Exception as e:
            raise Exception(f"Workflow-Fehler: {str(e)}")