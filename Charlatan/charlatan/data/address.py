from charlatan.helper import fetch
from random import choice, randint, uniform
import rstr


class Address:
    def __init__(self, locale):
        self.locale = locale
        self.data = 'address'
        self.fetch = fetch(self.data, self.locale)

    @property
    def building(self):
        building_type = ''.join(choice(self.fetch['building']['type']))
        building_name = ''.join(choice(self.fetch['building']['names']))
        return f"{randint(1, 100)} {building_name} {building_type}"

    @property
    def road(self):
        road = ' '.join([
            choice(self.fetch['street']['name']),
            choice(self.fetch['street']['suffix'])
        ])
        return road

    @property
    def city(self):
        city = ''.join(choice(self.fetch['city']))
        return city

    @property
    def county(self):
        county = ''.join(choice(self.fetch['county']))
        return county

    @property
    def country(self):
        country = ''.join(choice(self.fetch['country']))
        return country

    @property
    def postcode(self):
        postcode = rstr.xeger(''.join(self.fetch['postcode-fmt']).replace('\\', '\d'))
        return postcode

    @property
    def latitude(self):
        return 180 * randint(1, 49) / 90

    @property
    def longitude(self):
        return 90 * randint(1, 49) / 180

    @property
    def state(self):
        if self.locale in ['en_US', 'en_CA']:
            return ''.join(choice(self.fetch['state']['name']))
        else:
            return None

    @property
    def state_abbr(self):
        if self.locale in ['en_US', 'en_CA']:
            return ''.join(choice(self.fetch['state']['abbr']))
        else:
            return None

    @property
    def address(self):
        return {
            # "Building": self.building,
            "Road": self.road,
            "City": self.city,
            # "County": self.county,
            "State": {
                "Name": self.state,
                "Abbr": self.state_abbr
            },
            "Country": self.country,
            "Postcode": self.postcode
        }
