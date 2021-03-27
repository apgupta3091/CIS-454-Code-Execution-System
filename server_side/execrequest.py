import os
import tempfile
import subprocess
import json

#  DOCKER_RUNTIMES = {
#
#          }

DOCKER_RUN_CMDS = {
        "py": "python python",
        "rkt": "racket/racket racket"
        }

# Adjust accordingly to local machine
LOCAL_DIR = os.getcwd()
MOUNTED_DIR = "/mnt/src"

class ExecRequest:
    ''' State and logic for a code execution request '''

    def __init__(self, json_input):
        self.ext = json_input["lang"]
        self.src_code = json_input["src"]

    def get_docker_runtime(self):
        ''' determine appropriate Docker runtime for filetype '''
        pass

    def get_docker_cmd(self):
        ''' determine commands to pass to the Docker engine '''
        return DOCKER_RUN_CMDS[self.ext]

    def check_runtime_install(self):
        ''' check that the Docker runtime is installed '''
        pass

    def run_tmp_file(self):
        fd, path = tempfile.mkstemp(suffix=f".{self.ext}", dir=".")
        with open(path, 'w') as f:
            f.write(self.src_code)

        file_name = os.path.split(path)[1]
        # TODO: generalize this
        proc = subprocess.run(f"docker run -v {LOCAL_DIR}:{MOUNTED_DIR} --rm python python /mnt/src/{file_name}", shell=True, stdout=subprocess.PIPE)
        #  proc = subprocess.run(f"docker run -v {LOCAL_DIR}:{MOUNTED_DIR} --rm racket/racket racket /mnt/src/{file_name}", shell=True, stdout=subprocess.PIPE)
        output = proc.stdout.decode().strip()
        os.remove(file_name)
        return output


#  if __name__ == "__main__":
#      pyRequest = ExecRequest("pythoncode.json")
#      print(pyRequest.run_tmp_file())
