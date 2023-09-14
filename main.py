import requests

from fastapi import FastAPI
from prometheus_client import Gauge, make_asgi_app
from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY

app = FastAPI(debug=False)

class ISSCurentLocationCollector(object):
    def collect(self):
        try:
            r = requests.get('http://api.open-notify.org/iss-now.json')
            j = r.json()['iss_position']
            print(f"{j}")

            lat = GaugeMetricFamily('iss_position_latitude',
                                         'International Space Station Current Location Latitude',
                                         labels=['source'])
            lat.add_metric(['open-notify.org'], value=j['latitude'])
            yield lat

            lon = GaugeMetricFamily('iss_position_longitude',
                                          'International Space Station Current Location Longitude',
                                          labels=['source'])
            lon.add_metric(['open-notify.org'], value=j['longitude'])
            yield lon

        except Exception as e:
            print(e)

REGISTRY.register(ISSCurentLocationCollector())

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)