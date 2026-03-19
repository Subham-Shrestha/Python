#!/usr/bin/env python3
import platform
import subprocess
import shutil
import sys

def run(cmd):
    return subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode(errors='ignore')

def windows():
    out = run(['netsh', 'wlan', 'show', 'profiles'])
    profiles = []
    for line in out.splitlines():
        if "All User Profile" in line or "Profile" in line and "All User Profile" in line:
            try:
                profiles.append(line.split(":",1)[1].strip().strip('"'))
            except Exception:
                pass
    results = []
    for p in profiles:
        try:
            out = run(['netsh', 'wlan', 'show', 'profile', p, 'key=clear'])
            pwd = ""
            for l in out.splitlines():
                if "Key Content" in l:
                    pwd = l.split(":",1)[1].strip()
                    break
            results.append((p, pwd))
        except subprocess.CalledProcessError:
            results.append((p, ""))
    return results

def macos():
    if not shutil.which('networksetup'):
        raise RuntimeError('networksetup not found')
    # find wifi device (e.g., en0)
    hw = run(['networksetup', '-listallhardwareports'])
    device = None
    for block in hw.split('\n\n'):
        if 'Wi-Fi' in block or 'AirPort' in block:
            for line in block.splitlines():
                if line.strip().startswith('Device:'):
                    device = line.split(':',1)[1].strip()
                    break
            if device:
                break
    if not device:
        raise RuntimeError('Wi‑Fi device not found')
    pref = run(['networksetup', '-listpreferredwirelessnetworks', device])
    ssids = [line.strip() for line in pref.splitlines()[1:] if line.strip()]
    results = []
    for s in ssids:
        try:
            pwd = run(['security', 'find-generic-password', '-D', 'AirPort network password', '-a', s, '-gw']).strip()
        except subprocess.CalledProcessError:
            pwd = ""
        results.append((s, pwd))
    return results

def linux():
    if shutil.which('nmcli'):
        conns = run(['nmcli', '-t', '-f', 'NAME,TYPE', 'connection', 'show'])
        ssids = [line.split(':',1)[0] for line in conns.splitlines() if '802-11-wireless' in line]
        results = []
        for s in ssids:
            try:
                psk = run(['nmcli', '-s', '-g', '802-11-wireless-security.psk', 'connection', 'show', s]).strip()
            except subprocess.CalledProcessError:
                psk = ""
            results.append((s, psk))
        return results
    else:
        raise RuntimeError('nmcli not found; try checking /etc/NetworkManager/system-connections')

def main():
    osname = platform.system()
    try:
        if osname == 'Windows':
            rows = windows()
        elif osname == 'Darwin':
            rows = macos()
        elif osname == 'Linux':
            rows = linux()
        else:
            print("Unsupported OS:", osname)
            sys.exit(1)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

    print(f"{'SSID':<40} | {'PASSWORD'}")
    print("-"*60)
    for s, p in rows:
        print(f"{s:<40} | {p}")

if __name__ == '__main__':
    main()