# Open Notify ISS Now To Prometheus-metrics

Run:
```console
docker compose -p otus-sre-hw15-p2 up
```

## About

Transfrom http://api.open-notify.org/iss-now.json response:

```json
{
  "message": "success", 
  "timestamp": UNIX_TIME_STAMP, 
  "iss_position": {
    "latitude": CURRENT_LATITUDE, 
    "longitude": CURRENT_LONGITUDE
  }
}
```

to Prometheus-metrics:

```plain
# HELP iss_position_latitude International Space Station Current Location Latitude
# TYPE iss_position_latitude gauge
iss_position_latitude{source="open-notify.org"} 39.1092
# HELP iss_position_longitude International Space Station Current Location Longitude
# TYPE iss_position_longitude gauge
iss_position_longitude{source="open-notify.org"} -102.1833
```

Open Notify REST API International Space Station Current Location [description](http://open-notify.org/Open-Notify-API/ISS-Location-Now/).

## Pipenv

```console
python -m pipenv install --python 3.11
python -m pipenv install fastapi==0.103.1 gunicorn==21.2.0 prometheus-client==0.17.1 requests==2.31.0 uvicorn==0.23.2
```

## Dockerize

Build container:

```console
docker build -t open-notify-iss-now-to-prometheus .
```

Run container:

```console
docker run -d -p 9998:8080 --name open-notify-iss-now-to-prometheus open-notify-iss-now-to-prometheus
```