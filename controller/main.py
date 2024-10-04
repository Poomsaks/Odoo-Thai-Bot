import requests
import logging
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class MyWebsite(http.Controller):
    @http.route('/my_website', type='http', auth="public", website=True)
    def my_website(self, start_date=None, end_date=None, **kwargs):
        data = {}

        if start_date and end_date:
            url = f'https://apigw1.bot.or.th/bot/public/Stat-ReferenceRate/v2/DAILY_REF_RATE/?start_period={start_date}&end_period={end_date}'
            headers = {
                'X-IBM-Client-Id': '29eba4b0-1f2d-4aa3-b8d1-fd8f6731e87a',
                'accept': 'application/json'
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                _logger.info("API Response: %s", data)
            else:
                _logger.error("Failed to fetch data: %s", response.status_code)
        return request.render('Odoo-Thai-Bot.my_template', {'data': data})
