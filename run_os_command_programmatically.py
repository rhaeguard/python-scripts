import subprocess
import logging

def run_command_get_output(args, capture_output = False, out = subprocess.DEVNULL):
    """
    args: ["python", "path_to_a_python_file", "arg_1", "arg_2", ...]
    capture_output: a flag (especially useful when we're saving output to files)
    out: file or DEVNULL
    """
    returncode = subprocess.run(args, capture_output, stdout=out).returncode
    if returncode == 0:
        return True
    logging.error(f"Operation {args} failed and returned {returncode}")
    return False

def pipe_out_as_in_to_other_process():
    p1 = subprocess.Popen(f"ls -la", stdout=subprocess.PIPE)
    p2 = subprocess.Popen(f"wc", stdin=p1.stdout, stdout=subprocess.PIPE)
    stdout, stderr = p2.communicate()
    if p2.returncode == 0:
        print(stdout.decode('UTF-8'))
    else:
        print(stderr.decode('UTF-8'))


with open("example_log", "w") as file:
    success = run_command_get_output([
        "ls", "-la"
    ], False, file)

pipe_out_as_in_to_other_process()