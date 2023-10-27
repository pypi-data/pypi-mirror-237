import os
import subprocess
import sys


def init():
    if os.path.exists('venv'):
        print("Virtual environment already exists.")
        return

    subprocess.run([sys.executable, '-m', 'venv', 'venv'])

    if not os.path.exists('requirements.txt'):
        with open('requirements.txt', 'w') as f:
            f.write("# Add your project dependencies here\n")


def add_dependency(package_name):
    venv_python = os.path.join('venv', 'bin', 'python') if sys.platform != 'win32' else os.path.join('venv', 'Scripts',
                                                                                                     'python.exe')

    subprocess.run([venv_python, '-m', 'pip', 'install', package_name])

    installed_version = subprocess.check_output([venv_python, '-m', 'pip', 'show', package_name])
    installed_version = installed_version.decode("utf-8").split('\n')[1].split(': ')[1]

    with open('requirements.txt', 'a') as f:
        f.write(f"{package_name}=={installed_version}\n")


def remove_dependency(package_name):
    venv_python = os.path.join('venv', 'bin', 'python') if sys.platform != 'win32' else os.path.join('venv', 'Scripts',
                                                                                                     'python.exe')

    subprocess.run([venv_python, '-m', 'pip', 'uninstall', '-y', package_name])

    with open('requirements.txt', 'r') as f:
        lines = f.readlines()

    with open('requirements.txt', 'w') as f:
        for line in lines:
            if not line.startswith(f"{package_name}=="):
                f.write(line)


def run_python_file(file_name):
    venv_python = os.path.join('venv', 'bin', 'python') if sys.platform != 'win32' else os.path.join('venv', 'Scripts',
                                                                                                     'python.exe')
    subprocess.run([venv_python, file_name])


def main():
    if len(sys.argv) < 2:
        print("Usage: yav <command> [args]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "init":
        init()
    elif command == "add" and len(sys.argv) == 3:
        package_name = sys.argv[2]
        add_dependency(package_name)
    elif command == "remove" and len(sys.argv) == 3:
        package_name = sys.argv[2]
        remove_dependency(package_name)
    elif command == "run" and len(sys.argv) == 3:
        file_name = sys.argv[2]
        run_python_file(file_name)
    else:
        print("Usage: yav <command> [args]")
        sys.exit(1)


if __name__ == "__main__":
    main()
