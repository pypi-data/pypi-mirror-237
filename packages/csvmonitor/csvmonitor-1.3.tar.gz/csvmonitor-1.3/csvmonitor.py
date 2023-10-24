"""Lightweight HTTP integration for the csvmonitor.com heartbeat service."""
import requests

__version__ = '1.3'

def fire_beacon(org_id, beacon_id, event):
    "Safely fire a success, error, or reset event for the beacon beacon_id of organization org_id."
    try:
        resp = requests.get(f'https://csvmonitor.com/api/beacons/{org_id}/{beacon_id}/{event}', timeout=.3)
        return 200 <= resp.status_code <= 300
    except:
        return False