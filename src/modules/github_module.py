from github import Github

class GitHubModule:
    def __init__(self, access_token):
        self.github = Github(access_token)
        self.repo = None
    
    def set_repo(self, repo_name):
        self.repo = self.github.get_user().get_repo(repo_name)
    
    def push_file(self, repo_key, file_path, content, message):
        try:
            if not self.repo:
                self.set_repo(repo_key)
            
            try:
                file = self.repo.get_contents(file_path)
                self.repo.update_file(
                    file_path,
                    message,
                    content,
                    file.sha
                )
            except:
                self.repo.create_file(
                    file_path,
                    message,
                    content
                )
            return True
        except Exception as e:
            raise Exception(f"GitHub Push-Fehler: {str(e)}")