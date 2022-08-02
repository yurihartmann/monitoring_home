from monitorings.internet_ping import InternetPing
from services.influxdb_service import InfluxDBService

influxdb = InfluxDBService()

monitorings = [
    InternetPing(influxdb=influxdb, measurement="internet_ping")
]

for monitoring in monitorings:
    monitoring.run()
