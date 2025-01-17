import os
import ctypes
import platform
import subprocess

def is_windows():
    return platform.system() == "Windows"

def check_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_defrag(drive_letter="C:"):
    if not is_windows():
        raise EnvironmentError("This program is only supported on Windows.")

    if not check_admin():
        raise PermissionError("This program must be run with administrator privileges.")

    print(f"Starting defragmentation on {drive_letter} drive...")

    try:
        subprocess.check_call(['defrag', drive_letter, '/O'], shell=True)
        print("Defragmentation completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during defragmentation: {e}")

def main():
    try:
        drive_letter = input("Enter the drive letter to defragment (default is C): ") or "C:"
        run_defrag(drive_letter)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()