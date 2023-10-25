import sys
import os
script_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_directory, '..'))

import re
from typing import List
from dotenv import load_dotenv
from circles_local_database_python.generic_crud import GenericCRUD
from language_local.lang_code import LangCode
load_dotenv()
from logger_local.Logger import Logger  # noqa: E402
from .constants_location_profile import LocationProfileLocalConstants  # noqa: E402

logger = Logger.create_logger(
    object=LocationProfileLocalConstants.OBJECT_FOR_LOGGER_CODE)


class Location:
    def __init__(self, location_id, profile_id):
        self.profile_id = profile_id
        self.location_id = location_id

    def __dict__(self):
        return {
            'profile_id': self.profile_id,
            'location_id': self.location_id
        }


class LocationProfiles(GenericCRUD):
    def __init__(self):
        INIT_METHOD_NAME = '__init__'
        logger.start(INIT_METHOD_NAME)
        super().__init__(schema_name="location_profile")
        logger.end(INIT_METHOD_NAME)


    @staticmethod
    def is_valid_time_range(time_range: tuple) -> bool:
        """
        Validate that the time range is in the format 'YYYY-MM-DD'.
        """
        if len(time_range) != 2:
            return False

        for time_str in time_range:
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', time_str):
                return False

        return True

    @staticmethod
    def get_last_location_id_by_profile_id(profile_id: int) -> int:
        GET_LAST_LOCATION_ID_BY_PROFILE_ID_METHOD_NAME = "get_last_location_id_by_profile_id"
        logger.start(GET_LAST_LOCATION_ID_BY_PROFILE_ID_METHOD_NAME,
                     object={'profile_id': profile_id})
        location_id = LocationProfiles.select_multi_by_where(LocationProfiles(), view_table_name="location_profile_view", select_clause_value="location_id",
                                                             where=f"profile_id = {profile_id}", limit=1, order_by="start_timestamp desc")
        logger.end(GET_LAST_LOCATION_ID_BY_PROFILE_ID_METHOD_NAME,
                   object={'location_id': location_id})
        return location_id[0]

    @staticmethod
    def get_location_ids_by_profile_id(profile_id: int, limit: int = 1, time_range: tuple = None) -> List[Location]:
        GET_LOCATION_IDS_BY_PROFILE_ID_METHOD_NAME = "get_location_ids_by_profile_id"
        logger.start(GET_LOCATION_IDS_BY_PROFILE_ID_METHOD_NAME,
                     object={'profile_id': profile_id})
        
        if time_range and not LocationProfiles.is_valid_time_range(time_range):
            raise ValueError("Invalid time_range format. It should be 'YYYY-MM-DD'.")

        where_clause = f"profile_id = {profile_id}"
        if time_range:
            where_clause += f" AND updated_timestamp BETWEEN '{time_range[0]} 00:00:00' AND '{time_range[1]} 23:59:59'"

        location_ids = LocationProfiles.select_multi_by_where(LocationProfiles(), view_table_name="location_profile_view", select_clause_value="location_id",
                                                              where=where_clause, limit=limit, order_by="updated_timestamp desc")      

        location_ids = [Location(
            location_id=location_id, profile_id=profile_id) for location_id in location_ids]
        location_dicts = [loc.__dict__() for loc in location_ids]
        logger.end(GET_LOCATION_IDS_BY_PROFILE_ID_METHOD_NAME,
                   object={'location_ids': location_dicts})
        return location_ids

    @staticmethod
    def insert_location_profile(profile_id: int, location_id: int, title: str, lang_code: LangCode = LangCode.ENGLISH):
        INSERT_LOCATION_PROFILE_METHOD_NAME = 'insert_location_profile'
        logger.start(INSERT_LOCATION_PROFILE_METHOD_NAME,
                     object={"location_id": location_id})
        data = {
            "profile_id": profile_id,
            "location_id": location_id
        }
        location_profile_id = LocationProfiles.insert(
            LocationProfiles(), table_name="location_profile_table", json_data=data)
        data = {
            "location_profile_id": location_profile_id,
            "lang_code": lang_code.value,
            "title": title,
            "title_approved": False
        }
        LocationProfiles.insert(
            LocationProfiles(), table_name="location_profile_ml_table", json_data=data)
        logger.end(INSERT_LOCATION_PROFILE_METHOD_NAME)
