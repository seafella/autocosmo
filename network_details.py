import sys, os
project_root = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(project_root, 'Lib')
sys.path.append(lib_path)

import subprocess
import time
from datetime import datetime
from typing import Callable, Dict, List, Tuple

import requests
from bs4 import BeautifulSoup
import pytz


def get_public_ip() -> str:
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']

def run_ping(host: str = '8.8.8.8', count: int = 40) -> Dict[str, str]:
    output = subprocess.check_output(["ping", "-c", str(count), host]).decode()
    ping_lines = output.splitlines()
    ping_times = [float(line.split(' ')[6].split('=')[1]) for line in ping_lines if 'time=' in line]
    timeouts = sum(1 for line in ping_lines if 'Request timeout' in line)
    avg_ping_time = sum(ping_times) / len(ping_times)
    # return {'host': host, 'output': output, 'avg_time': avg_ping_time}
    # return {'host': host, 'output': output, 'avg_time': round(avg_ping_time, 3)}
    return {'host': host, 'output': output, 'avg_time': round(avg_ping_time, 3) if avg_ping_time else None, 'timeouts': timeouts}



def get_network_details() -> Dict[str, str]:
    return {
        'public_ip': get_public_ip(),
        'ping': run_ping()
    }

def format_org_mode(data: Dict[str, str]) -> str:
    now = datetime.now(pytz.utc).strftime('%Y%m%dT%H%M%SZ')
    avg_time = f'{data["ping"]["avg_time"]} ms' if data["ping"]["avg_time"] is not None else 'N/A'
    timeouts = data["ping"]["timeouts"]
    formatted = f'* Network Details - {now} - {avg_time} - {timeouts} timeouts - {data["public_ip"]}\n'
    print(formatted)
    for key, value in data.items():
        formatted += f'** {key.capitalize()}\n'
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                formatted += f'*** {sub_key.capitalize()} : {sub_value}\n'
        else:
            formatted += f'*** {value}\n'
    return formatted

def log_data(formatter: Callable[[Dict[str, str]], str], data: Dict[str, str]) -> None:
    formatted_data = formatter(data)
    with open('network_details.org', 'a') as f:
        f.write(formatted_data)

def main(interval: int, checks: List[Callable[[], Dict[str, str]]]) -> None:
    while True:
        data = {}
        for check in checks:
            data.update(check())
        log_data(format_org_mode, data)
        time.sleep(interval)

if __name__ == '__main__':
    print('leggo!')
    # checks_to_run = [get_network_details, get_big_mac_prices]
    checks_to_run = [get_network_details]
    main(60 * 1, checks_to_run)  # Run every 5 minutes
