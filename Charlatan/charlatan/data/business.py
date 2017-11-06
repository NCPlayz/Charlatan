from charlatan.helper import fetch
from random import choice, uniform
from charlatan.misc.business import CURRENCIES, CURRENCY_SYMBOLS


class Business:
    def __init__(self, locale):
        self.locale = locale
        self.data = 'business'
        self.fetch = fetch(self.data, self.locale)

    @property
    def company_type(self):
        company_type = self.fetch['company']['type']['title']
        return choice(company_type)

    @property
    def company_type_abbr(self):
        company_type_abbr = self.fetch['company']['type']['title']
        return choice(company_type_abbr)

    @property
    def company(self):
        companies = self.fetch['company']['name']
        return choice(companies)

    @property
    def copyright(self):
        return f'© {self.company}, {self.company_type_abbr}'

    @property
    def currency_iso(self):
        return choice(CURRENCIES)

    def price(self, minimum=10.00, maximum=1000.00):
        currencies = CURRENCY_SYMBOLS

        price = uniform(
            float(minimum),
            float(maximum),
        )

        fmt = '{0:.2f} {1}'

        if self.locale in currencies:
            return fmt.format(price, currencies[self.locale])

        return fmt.format(price, currencies['default'])