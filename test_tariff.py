import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
import tariff


def main():
    """main"""
    # create logger
    logger = logging.getLogger('myems-aggregation')
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    fh = RotatingFileHandler('myems-aggregation.log', maxBytes=1024 * 1024, backupCount=0)
    fh.setLevel(logging.ERROR)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    cost_center_id = 1
    energy_category_id = 1
    start_date_time_utc = datetime.strptime('2020-06-29 16:00:00', '%Y-%m-%d %H:%M:%S')
    end_date_time_utc = datetime.strptime('2020-07-01 15:59:59', '%Y-%m-%d %H:%M:%S')
    tariffs = tariff.get_tariffs(cost_center_id,
                                 energy_category_id,
                                 start_date_time_utc,
                                 end_date_time_utc)
    for k, v in sorted(tariffs.items()):
        print(k, v)


if __name__ == "__main__":
    main()
