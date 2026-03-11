# Environment_Intelligence

### https://environment-intelligence.onrender.com

This repository contains a small FastAPI service that acts as an orchestration API. It aggregates environmental information by calling multiple external APIs and returning a combined response. The service retrieves weather data, air quality information, and country metadata for a specified location.

Features
The API collects and merges data from three sources:

* Open-Meteo API for current weather conditions
* WAQI API for air quality and pollution levels
* RestCountries API for country information

The service exposes a single endpoint that returns all this data in one response.

Endpoint

POST `/environment-intelligence`

Example request body

```
{
  "city": "tokyo",
  "country": "japan",
  "latitude": 35.6762,
  "longitude": 139.6503
}
```

Example response (simplified)

```
{
  "weather": {...},
  "air_quality": {...},
  "country": {...}
}
```

Environment Variables

The WAQI API token must be provided as an environment variable.

```
WAQI_TOKEN=your_api_token
```

Installation

```
pip install -r requirements.txt
```

Run locally

```
uvicorn main:app --reload
```

Deployment

This service can be deployed on platforms such as Render. Use the following start command:

```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Once deployed, the endpoint can be used as an orchestration layer for AI tool systems or agent platforms that need to combine environmental data from multiple APIs.
