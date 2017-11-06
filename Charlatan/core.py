from charlatan.data.address import Address
from charlatan.data.business import Business
from charlatan.data.clothing import Clothing


if __name__ == '__main__':
    print(Address('en_GB').address)
    print(Business('en_CA').copyright)
    print(Clothing().international)
