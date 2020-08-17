from fastapi import FastAPI

from api import urls, views


def create_routes(app: FastAPI):
    app.add_api_route(
        urls.LOAD_TARIFF_URL, views.load_tariff_view,
        methods=['POST'])
    app.add_api_route(
        urls.GET_INSURANCE_PRICE_URL, views.get_insurance_price_view,
        methods=['POST'])
