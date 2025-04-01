# Car Insurance Premium Simulator


___
Python version used
---
Python 3.11+

## installation 



```bash
pip install -r requirements.txt
```

## Docker
```bash

1. docker build -t car-insurance-premium-simulator .

2. docker run -p 8000:8000 car-insurance-premium-simulator
```




## Available endpoints:

___
• quote/generate : Route to generate a Quote according to the data entered. 
---
```bash
curl --location 'http://127.0.0.1:8000/quote/generate' \
--header 'Content-Type: application/json' \
--data '{
  "car": {
    "make": "Toyota",
    "model": "Corolla",
    "year": 2012,
    "value": 100000.0
  },
  "broker_fee": 50.0,
  "coverage_percentage": 1.0,
  "deductible_percentage": 0.10
}'

#This request returns something like this:
{
    "car_details": {
        "make": "Toyota",
        "model": "Corolla",
        "year": 2012,
        "value": 100000.0
    },
    "applied_rate": 0.115,
    "calculated_premium": 10400.0,
    "deductible_value": 1150.0,
    "policy_limit": 90000.0
}



## Project Structure

```bash
.
.
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   ├── application
│   │   ├── __init__.py
│   │   ├── dto
│   │   │   ├── __init__.py
│   │   │   ├── insurence.py
│   │   │   ├── policy_response.py
│   │   │   └── quote_response.py
│   │   └── use_cases
│   │       ├── __init__.py
│   │       ├── policy.py
│   │       ├── premium.py
│   │       ├── quote.py
│   │       └── rate.py
│   ├── domain
│   │   ├── __init_.py
│   │   ├── entities
│   │   │   ├── __init__.py
│   │   │   ├── car.py
│   │   │   └── quotation.py
│   │   ├── events
│   │   │   └── __init__.py
│   │   ├── services
│   │   │   ├── __init__.py
│   │   │   ├── policy.py
│   │   │   ├── premium.py
│   │   │   ├── quote.py
│   │   │   └── rate.py
│   │   └── value_objects
│   │       ├── __init__.py
│   │       └── factor_risk.py
│   ├── infra
│   │   ├── __init__.py
│   │   ├── config
│   │   │   ├── __init__.py
│   │   │   └── settings.py
│   │   ├── database
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── config.py
│   │   │   └── session.py
│   │   └── repositories
│   │       ├── __init__.py
│   │       └── quotation.py
│   ├── main.py
│   ├── presentation
│   │   ├── __init__.py
│   │   ├── controllers
│   │   │   └── quote.py
│   │   └── routes
│   │       ├── __init__.py
│   │       └── quote.py
│   └── shared
│       ├── __init__.py
│       └── utils.py
├── requirements.txt
└── tests
    └── __init__.py