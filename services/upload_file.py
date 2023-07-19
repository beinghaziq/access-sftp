import paramiko
from decouple import config


class UploadFile:
    def __init__(self):
        self.hostname = config("HOST_NAME")
        self.port = 22
        self.username = config("USER_NAME")
        self.private_key_path = 'id'
        self.local_file_path = 'api-gateway.zip'
        self.remote_directory = '/sftp-data-a/abc'

    def call(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.hostname, self.port, self.username, key_filename=self.private_key_path)
        self._upload_file_on_server(ssh)
          

    def _upload_file_on_server(ssh, self):
        # Open SFTP session
        sftp = ssh.open_sftp()

        # Upload file to remote directory
        remote_file_path = self.remote_directory + '/api-gateway.zip'
        sftp.put(self.local_file_path, remote_file_path)

        # Close SFTP session and SSH connection
        sftp.close()
        ssh.close()




