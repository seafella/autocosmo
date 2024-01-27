import os, sys, re, time
from datetime import datetime, timedelta

project_root = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(project_root, 'Lib')
sys.path.append(lib_path)

import curses
import requests
import pytz # replace this .. not needed https://stackoverflow.com/questions/64463898/regarding-the-pytz-module-and-the-time-module-in-python


def draw_big_digit(stdscr, digit, y, x):
    digit_map = {
        '0': ['###', '# #', '# #', '# #', '###'],
        '1': ['  #', '  #', '  #', '  #', '  #'],
        '2': ['###', '  #', '###', '#  ', '###'],
        '3': ['###', '  #', '###', '  #', '###'],
        '4': ['# #', '# #', '###', '  #', '  #'],
        '5': ['###', '#  ', '###', '  #', '###'],
        '6': ['###', '#  ', '###', '# #', '###'],
        '7': ['###', '  #', '  #', '  #', '  #'],
        '8': ['###', '# #', '###', '# #', '###'],
        '9': ['###', '# #', '###', '  #', '###'],
        ':': [' ', ' ', '#', ' ', '#'],
    }

    for i, row in enumerate(digit_map[digit]):
        for j, char in enumerate(row):
            if char == '#':
                stdscr.addch(y + i, x + j, char, curses.color_pair(4))

def draw_digital_clock(stdscr):
    now = datetime.now()
    time_str = now.strftime('%H:%M:%S')

    y, x = 1, 40
    for digit in time_str:
        draw_big_digit(stdscr, digit, y, x)
        x += 4

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']

def format_org_mode(data):
    return f"* Network Details - {data['timestamp']} - {data['public_ip']}\n"

def log_data(formatter, data):
    with open("ip_changes.org", "a") as f:
        f.write(formatter(data))

def load_history(filename, pattern):
    past_ips = []
    try:
        with open(filename, "r") as f:
            content = f.read()
            matches = re.findall(pattern, content, flags=re.MULTILINE)
            for match in matches:
                past_ips.append(f"{match[0]} - {match[1]}")
    except FileNotFoundError:
        pass
    return past_ips

#### draw window without counts 

def draw_window(stdscr, current_ip, past_ips, ip_change_counter, changes_per_hour):
    stdscr.clear()
    stdscr.addstr(1, 2, "Current IP Address:", curses.color_pair(1))
    stdscr.addstr(1, 21, current_ip, curses.color_pair(2))
    stdscr.addstr(2, 2, f"Total IP Address Changes Tracked: {ip_change_counter}", curses.color_pair(1))
    # stdscr.addstr(3, 2, f"IP Address Changes in the past hour: {changes_per_hour[0]}", curses.color_pair(1))

    stdscr.addstr(4, 2, "Past IP Addresses (date-time - IP):", curses.color_pair(1))
    for i, past_ip in enumerate(past_ips[:10]):
        dt, ip = past_ip.split(" - ")
        stdscr.addstr(5 + i, 2, f"{dt} - {ip}", curses.color_pair(2))

    stdscr.addstr(16, 2, "Changes per Hour (last 48 hours):", curses.color_pair(1))
    max_changes = max(changes_per_hour)
    max_lines = 10
    for i, count in enumerate(changes_per_hour):
        bar_height = int((count / max_changes) * max_lines) if max_changes > 0 else 0
        for j in range(bar_height):
            stdscr.addstr(25 - j, 2 + i * 2, "█", curses.color_pair(3))

    draw_digital_clock(stdscr)

    stdscr.refresh()

def main(stdscr, interval):
    curses.curs_set(0)  # Hide the cursor

    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # New color pair

    current_ip = get_public_ip()
    now = datetime.now(pytz.utc)

    filename = "ip_changes.org"
    pattern = r'\* IP Address Change - (\d{8}T\d{6}Z) - (.*?)$'
    past_ips = load_history(filename, pattern)

    ip_change_counter = len(past_ips)

    changes_per_hour = [0] * 48
    timestamp_pattern = r'(\d{8}T\d{6}Z)'

    for past_ip_change in past_ips:
        timestamp_match = re.search(timestamp_pattern, past_ip_change)
        if timestamp_match:
            dt = datetime.strptime(timestamp_match.group(1), '%Y%m%dT%H%M%SZ').replace(tzinfo=pytz.utc)
            hours_passed = int((now - dt).total_seconds() // 3600)
            if hours_passed < 48:
                changes_per_hour[47 - hours_passed] += 1
    changes_per_hour.reverse()

    draw_window(stdscr, current_ip, past_ips, ip_change_counter, changes_per_hour)

    while True:
        time.sleep(interval)
        new_ip = get_public_ip()
        if new_ip != current_ip:
            now = datetime.now(pytz.utc)
            past_ips.insert(0, f"{now.strftime('%Y%m%dT%H%M%SZ')} - {current_ip}")
            ip_change_counter += 1
            log_data(format_org_mode, {'public_ip': current_ip, 'timestamp': now.strftime('%Y%m%dT%H%M%SZ')})
            current_ip = new_ip

            # Update changes_per_hour list
            changes_per_hour.pop()
            changes_per_hour.insert(0, 1)
            for i in range(1, 48):
                dt = now - timedelta(hours=i)
                if dt.strftime('%Y%m%dT%H%M%SZ') in past_ips[1]:
                    changes_per_hour[i] -= 1
                    break

        draw_window(stdscr, current_ip, past_ips, ip_change_counter, changes_per_hour)

if __name__ == "__main__":
    curses.wrapper(main, 60 * 5)  # Check every 5 minutes


