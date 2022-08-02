import subprocess

from monitorings.monitoring_abc import MonitoringABC


class InternetPing(MonitoringABC):
    __HOSTS = {
        'Google': 'google.com',
        'Instagram': 'instagram.com',
        'Overwatch': 'dynamodb.sa-east-1.amazonaws.com',
    }

    @classmethod
    def get_ping(cls, url: str) -> float:
        response = subprocess.Popen(
            f'ping -c 3 {url}', shell=True, stdout=subprocess.PIPE
        ).stdout.read().decode('utf-8')

        try:
            return float(response.split('\n')[-2].split('/')[4])
        except Exception:
            return 0.0

    def run(self):
        for host_name, url in self.__HOSTS.items():
            ping = self.get_ping(url=url)

            points = self.generate_points(
                tags={
                    "host_name": host_name,
                    "url": url
                },
                fields={
                    'ping': ping
                }
            )

            self.influxdb.write_points(points)
