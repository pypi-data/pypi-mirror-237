# Python Client for CSVMonitor.com
This is a thin wrapper around the Python `requests` module to trigger HTTP beacons on the [csvmonitor.com](https://csvmonitor.com) Software as a Service (SaaS) site. To use it in your project, install the csvmonitor module using pip:
```
python -m pip install csvmonitor
```

Then, after registering at csvmonitor.com, create a beacon and copy the organization and beacon keys for the beacons you wish to trigger. Use the `fire_beacon` function to trigger the beacons, and you're done!
```
from csvmonitor import fire_beacon

. . .

ok = somefunc()

fire_beacon(CSVM_ORG_ID, BEACON_KEY, 'success' if ok else 'error')
```