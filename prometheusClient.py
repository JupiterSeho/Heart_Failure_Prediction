from prometheus_client import Counter, make_asgi_app

survived_counter = Counter("survived", "Counter for survived")
not_survived_counter = Counter(
    "not_survived", "Counter for not survived")
age_risk_counter = Counter(
    "age_risk", "Counter for age risk", labelnames=['age_group'])
smoking_risk_counter = Counter(
    "smoking_risk", "Counter for smoking risk", labelnames=['smoking_status'])
sex_risk_counter = Counter(
    "sex_risk", "Counter for sex risk", labelnames=['sex'])

metrics_app = make_asgi_app()
