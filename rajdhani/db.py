"""
Module to interact with the database.
"""

from . import placeholders
from . import db_ops

db_ops.ensure_db()


def search_stations(q):
    """Returns the top ten stations matching the given query string.

    This is used to get show the auto complete on the home page.

    The q is the few characters of the station name or
    code entered by the user.
    """
    # TODO: make a db query to get the matching stations
    # and replace the following dummy implementation
    return placeholders.AUTOCOMPLETE_STATIONS

def search_trains(
        from_station_code,
        to_station_code,
        ticket_class=None,
        departure_date=None,
        departure_time=[],
        arrival_time=[]):
    """Returns all the trains that source to destination stations on
    the given date. When ticket_class is provided, this should return
    only the trains that have that ticket class.

    This is used to get show the trains on the search results page.
    """
    # TODO: make a db query to get the matching trains
    # and replace the following dummy implementation

    return placeholders.SEARCH_TRAINS

def get_schedule(train_number):
    """Returns the schedule of a train.
    """
    return placeholders.SCHEDULE

def book_ticket(train_number, ticket_class, date):
    """Books a ticket and returns the booking ID.
    """
    # TODO: make a db query and insert a new booking
    # into the booking table

    return 1
