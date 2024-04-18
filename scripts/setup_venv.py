import os
import subprocess
import sys

venv_path = os.path.join(os.path.dirname(__file__), '..', 'venv')

def check_python_version():
    if sys.version_info < (3, 11):
        raise Exception("Python 3.11 or newer is required.")

def create_venv():
    if not os.path.exists(venv_path):
        subprocess.check_call([sys.executable, '-m', 'venv', venv_path])
    else:
        print("Virtual environment already exists.")

if __name__ == "__main__":
    try:
        check_python_version()
        create_venv()
    except Exception as e:
        print(str(e))
        sys.exit(1)
