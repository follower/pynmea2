import pytest
import pynmea2

import datetime

from decimal import Decimal

def test_GGA():
    data = "$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D"
    msg = pynmea2.parse(data)
    assert msg.talker == 'GP'
    assert msg.type == 'GGA'

    # Timestamp
    assert msg.timestamp        == datetime.time(18, 43, 53)
    # Latitude
    assert msg.lat              == '1929.045'
    # Latitude Direction
    assert msg.lat_dir          == 'S'
    # Longitude
    assert msg.lon              == '02410.506'
    # Longitude Direction
    assert msg.lon_dir          == 'E'
    # GPS Quality Indicator
    assert msg.gps_qual         == '1'
    # Number of Satellites in use
    assert msg.num_sats         == '04'
    # Horizontal Dilution of Precision
    assert msg.horizontal_dil   == '2.6'
    # Antenna Alt above sea level (mean)
    assert msg.altitude         == 100.0
    # Units of altitude (meters)
    assert msg.altitude_units   == 'M'
    # Geoidal Separation
    assert msg.geo_sep          == '-33.9'
    # Units of Geoidal Separation (meters)
    assert msg.geo_sep_units    == 'M'
    # Age of Differential GPS Data (secs)
    assert msg.age_gps_data     == ''
    # Differential Reference Station ID
    assert msg.ref_station_id   == '0000'


def test_MWV():
    data = "$IIMWV,271.0,R,000.2,N,A*3B"
    msg = pynmea2.parse(data)

    assert msg.talker == 'II'
    assert msg.type == 'MWV'

    # Wind angle in degrees
    assert msg.wind_angle == Decimal('271.0')

    # Reference type
    assert msg.reference == 'R'

    # Wind speed
    assert msg.wind_speed == Decimal('0.2')

    # Wind speed units
    assert msg.wind_speed_units == 'N'

    # Device status
    assert msg.status == 'A'

