import sys
import os
import datetime
import re
from dotenv import load_dotenv
sys.path.append(os.getcwd())
from .constants import *  # noqa: E402¸
load_dotenv()
from logger_local.Logger import Logger  # noqa: E402

logger = Logger.create_logger(object=OBJECT_TO_INSERT_CODE)


def timedelta_to_time_format(timedelta: datetime.timedelta):
    TIMEDELTA_TO_TIME_FORMAT_METHOD_NAME = "timedelta_to_time_format()"
    logger.start(TIMEDELTA_TO_TIME_FORMAT_METHOD_NAME)
    # The following line will cause TypeError: Object of type timedelta is not JSON serializable
    # logger.start(TIMEDELTA_TO_TIME_FORMAT_METHOD_NAME, object={'timedelta':  timedelta})

    # Calculate the total seconds and convert to HH:MM:SS format
    total_seconds = int(timedelta.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    # Format as "HH:MM:SS"
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    logger.end(TIMEDELTA_TO_TIME_FORMAT_METHOD_NAME,
               object={'formatted_time':  formatted_time})
    return formatted_time


def is_valid_time_range(time_range: tuple) -> bool:
    """
    Validate that the time range is in the format 'HH:MM:SS'.
    """
    IS_VALID_TIME_RANGE_METHOD_NAME = "is_valid_time_range"
    logger.start(IS_VALID_TIME_RANGE_METHOD_NAME,
                 object={"time_range": time_range})
    if len(time_range) != 2:
        logger.end(IS_VALID_TIME_RANGE_METHOD_NAME, object={
                   "is_valid_time_range_result": False, "reason": "len(time_range) != 2"})
        return False

    for time_str in time_range:
        if not re.match(r'^\d{2}:\d{2}:\d{2}$', time_str):
            logger.end(IS_VALID_TIME_RANGE_METHOD_NAME, object={
                       "is_valid_time_range_result": False, "reason": "not re.match(r'^\d{2}:\d{2}:\d{2}$', time_str)"})
            return False
    return True


def is_valid_date_range(date_range: tuple) -> bool:
    """
    Validate that the date range is in the format 'YYYY-MM-DD'.
    """
    IS_VALID_DATE_RANGE_METHOD_NAME = "is_valid_date_range"
    logger.start(IS_VALID_DATE_RANGE_METHOD_NAME,
                 object={"date_range": date_range})
    if len(date_range) != 2:
        logger.end(IS_VALID_DATE_RANGE_METHOD_NAME, object={
                   "is_valid_date_range_result": False, "reason": "len(date_range) != 2"})
        return False

    for date_str in date_range:
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
            logger.end(IS_VALID_DATE_RANGE_METHOD_NAME, object={
                       "is_valid_date_range_result": False, "reason": "not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str)"})
            return False
    logger.end(IS_VALID_DATE_RANGE_METHOD_NAME, object={
               "is_valid_date_range_result": True})
    return True


def is_valid_datetime_range(datetime_range: tuple) -> bool:
    """
    Validate that the datetime range is in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    IS_VALID_DATETIME_RANGE_METHOD_NAME = "is_valid_datetime_range"
    logger.start(IS_VALID_DATETIME_RANGE_METHOD_NAME,
                 object={"datetime_range": datetime_range})
    if len(datetime_range) != 2:
        logger.end(IS_VALID_DATETIME_RANGE_METHOD_NAME, object={
                   "is_valid_datetime_range_result": False, "reason": "len(datetime_range) != 2"})
        return False

    for datetime_str in datetime_range:
        if not re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', datetime_str):
            logger.end(IS_VALID_DATETIME_RANGE_METHOD_NAME, object={
                       "is_valid_datetime_range_result": False, "reason": "not re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', datetime_str)"})
            return False
    logger.end(IS_VALID_DATETIME_RANGE_METHOD_NAME, object={
               "is_valid_datetime_range_result": True})
    return True


def is_list_of_dicts(obj):
    IS_LIST_OF_DICTS_FUNCTION_NAME = "is_list_of_dicts()"
    logger.start(IS_LIST_OF_DICTS_FUNCTION_NAME, object={"obj": obj})
    if not isinstance(obj, list):
        is_list_of_dicts_result = False
        logger.end(IS_LIST_OF_DICTS_FUNCTION_NAME, object={
                   "is_list_of_dicts_result": is_list_of_dicts_result})
        return is_list_of_dicts_result
    for item in obj:
        if not isinstance(item, dict):
            is_list_of_dicts_result = False
            logger.end(IS_LIST_OF_DICTS_FUNCTION_NAME, object={
                       'is_list_of_dicts_result': is_list_of_dicts_result})
            return is_list_of_dicts_result
    is_list_of_dicts_result = True
    logger.end(IS_LIST_OF_DICTS_FUNCTION_NAME, object={
               'is_list_of_dicts_result': is_list_of_dicts_result})
    return is_list_of_dicts_result
