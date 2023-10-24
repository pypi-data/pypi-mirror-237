from healthcheck import HealthCheck


def add_healthcheck_url(app, check_func, url: str):
    health_check = HealthCheck()
    health_check.add_check(check_func)
    app.add_url_rule(url, "healthcheck", view_func=lambda: health_check.run())
    return app