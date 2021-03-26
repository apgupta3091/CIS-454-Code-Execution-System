import os
import tempfile
import subprocess
import json

#  DOCKER_RUNTIMES = {
#
#          }

#  DOCKER_RUN_CMDS = {
#
#          }

# Adjust accordingly to local machine
LOCAL_DIR = "/home/christian/Documents/dock"
MOUNTED_DIR = "/mnt/src"

class ExecRequest:
    ''' State and logic for a code execution request '''

    def __init__(self, json_input):
        with open(json_input) as json_conn:
            self.data = json.load(json_conn)
            self.ext = self.data["lang"]
            self.src_code = self.data["src"]

    def get_docker_runtime(self):
        ''' determine appropriate Docker runtime for filetype '''
        pass

    def get_docker_cmd(self):
        ''' determine commands to pass to the Docker engine '''
        pass

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
        output = proc.stdout.decode().strip()
        os.remove(file_name)
        return output


if __name__ == "__main__":
    pyRequest = ExecRequest("pythoncode.json")
    print(pyRequest.run_tmp_file())
