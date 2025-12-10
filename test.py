import sys
import platform
import os
import psutil


def display_system_info():
    """Zeigt grundlegende Systeminformationen an."""
    
    print("=" * 60)
    print("SYSTEMINFORMATIONEN")
    print("=" * 60)
    
    # Betriebssystem
    print(f"\nBetriebssystem: {platform.system()}")
    print(f"OS Version: {platform.release()}")
    print(f"Architektur: {platform.machine()}")
    print(f"Hostname: {platform.node()}")
    
    # Python Information
    print(f"\nPython Version: {platform.python_version()}")
    print(f"Python Implementation: {platform.python_implementation()}")
    print(f"Executable: {sys.executable}")
    
    # CPU Information
    print(f"\nCPU Kerne (physisch): {psutil.cpu_count(logical=False)}")
    print(f"CPU Kerne (logisch): {psutil.cpu_count(logical=True)}")
    print(f"CPU Auslastung: {psutil.cpu_percent(interval=1)}%")
    
    # RAM Information
    ram = psutil.virtual_memory()
    print(f"\nRAM Gesamt: {ram.total / (1024**3):.2f} GB")
    print(f"RAM Verfügbar: {ram.available / (1024**3):.2f} GB")
    print(f"RAM Auslastung: {ram.percent}%")
    
    # Disk Information
    disk = psutil.disk_usage('/')
    print(f"\nSpeicher Gesamt: {disk.total / (1024**3):.2f} GB")
    print(f"Speicher Verfügbar: {disk.free / (1024**3):.2f} GB")
    print(f"Speicher Auslastung: {disk.percent}%")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    display_system_info()
