import random
import datetime
import logging
from typing import Any, Dict
from freqtrade.exceptions import OperationalException
from freqtrade.state import RunMode
from freqtrade.configuration import setup_utils_configuration
from freqtrade.commands import start_download_data

from sklearn.neural_network import MLPClassifier

logger = logging.getLogger(__name__)


def random_dataset(args: Dict[str, Any]):
    """
    Create a random arg dictionary given the ranges for timeframe, pairs and days
    """

    # Pick a random period of 1 day
    start_date = datetime.datetime.today() - datetime.timedelta(days=args['period_length'] + 3)
    end_date = datetime.datetime.today() - datetime.timedelta(days=3)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    start_timerange = str(random_date)
    end_timerange = str(random_date + datetime.timedelta(days=args['opt_days_amount']))
    timerange = f"{start_timerange[0:4]}{start_timerange[5:7]}{start_timerange[8:10]}-{end_timerange[0:4]}{end_timerange[5:7]}{end_timerange[8:10]}"

    possible_pairs = args['possible_pairs']
    possible_timeframes = args['possible_timeframes']

    # Pick a random pair
    pair = possible_pairs[random.randint(0, len(possible_pairs)-1)]

    # Pick a random timeframe
    timeframe = possible_timeframes[random.randint(0, len(possible_timeframes)-1)]

    # Build the dictionary
    args.update({
        "timerange": timerange,
        "pairs": pair,
        "timeframes": timeframe
    })


def proces_data(args: Dict[str, Any]):
    """
    Proces the data in a way that it can be used by the AI
    """
    #start_download_data(args)
    return data

def random_strategy(args: Dict[str, Any]):
    """
    Create a random strategy to have 
    """

def start_generate_strategy(args: Dict[str, Any]):
    """
    Start generating a strategy for a range of timeframes, pairs and days
    """
    config = setup_utils_configuration(args, RunMode.UTIL_NO_EXCHANGE)

    if not 'possible_timeframes' in args or not args['possible_timeframes']:
        raise OperationalException("`generate-strategy` requires --possible-timeframes to be set.")
    if not 'possible_pairs' in args or not args['possible_pairs']:
        raise OperationalException("`generate-strategy` requires --possible-pairs to be set.")
    if not 'opt_days_amount' in args or not args['opt_days_amount']:
        args['opt_days_amount'] = 1
    if not 'period_length' in args or not args['period_length']:
        args['period_length'] = 1
    if not 'exchange' in args or not args['exchange']:
        args['exchange'] = "binance"

    random_dataset(args)
    data = proces_data(args)
