import subprocess
import random
import pdb
import os
import common_handler
from common_handler import *
from create_pr import CreatePR


class CommitAndPR:
    def __init__(self):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.file_path = f"{ROOT_DIR}/src/main.js"
        self.messages = ["Updated main.js", "Added console", "console.log hello added"]
        self.branch_name = "test_programetically"

    def call(self):
        subprocess.call(["git", "checkout", "main"])
        subprocess.call(["git", "checkout", "-b", f"{self.branch_name}"])
        edit_file(self.file_path)
        subprocess.call(["git", "add", self.file_path])
        subprocess.call(
            [
                "git",
                "commit",
                "--date",
                "-m",
                random.sample(self.messages, 1)[0],
            ],
            env=os.environ,
        )
        subprocess.call(["git", "push", "origin", f"{self.branch_name}"])
        CreatePR().call()
