from typing import Dict
try:
    # Works when running the tests from this package
    from constants_profiles_local import *
except Exception as e:
    # Works when importing this module from another package
    from profile_local.constants_profiles_local import *
from dotenv import load_dotenv
load_dotenv()
from circles_local_database_python.generic_crud import GenericCRUD  # noqa: E402
from logger_local.Logger import Logger  # noqa: E402
from circles_number_generator.number_generator import NumberGenerator  # noqa: E402

logger = Logger.create_logger(object=OBJECT_TO_INSERT_CODE)

# Named ProfileLocalClass because Profile is already taken by the class in profile.py in python 3.11 library


class ProfilesLocal(GenericCRUD):

    def __init__(self):
        super().__init__("profile")
        logger.start()
        logger.end()

    '''
    person_id: int,
    data: Dict[str, any] = {
        'profile_name': profile_name,
        'name_approved': name_approved,
        'lang_code': lang_code,
        'user_id': user_id,                             #Optional
        'is_main': is_main,                             #Optional
        'visibility_id': visibility_id,
        'is_approved': is_approved,
        'profile_type_id': profile_type_id, #Optional
        'preferred_lang_code': preferred_lang_code,     #Optional
        'experience_years_min': experience_years_min,   #Optional
        'main_phone_id': main_phone_id,                 #Optional
        'rip': rip,                                     #Optional
        'gender_id': gender_id,                         #Optional
        'stars': stars,
        'last_dialog_workflow_state_id': last_dialog_workflow_state_id
    },
    profile_id: int
    '''

    def insert(self, person_id: int, data: Dict[str, any]) -> int:
        logger.start(object={'data': str(data)})

        json_data = {
            "`number`": NumberGenerator.get_random_number("profile", "profile_table", "`number`"),
            "user_id": data['user_id'],
            "person_id": person_id,
            "is_main": data['is_main'],
            "visibility_id": data['visibility_id'],
            "is_approved": data['is_approved'],
            "profile_type_id": data['profile_type_id'],
            "preferred_lang_code": data['preferred_lang_code'],
            "experience_years_min": data['experience_years_min'],
            "main_phone_id": data['main_phone_id'],
            "rip": data['rip'],
            "gender_id": data['gender_id'],
            "stars": data['stars'],
            "last_dialog_workflow_state_id": data['last_dialog_workflow_state_id']
        }

        super().insert("profile_table", json_data)
        profile_ml_table_json = {
            "profile_id": self.cursor.lastrowid(),
            "lang_code": data['lang_code'],
            "`name`": data['profile_name'],
            "name_approved": data['name_approved']
        }
        super().insert("profile_ml_table", profile_ml_table_json)

        logger.end(object={'profile_id': profile_ml_table_json['profile_id']})
        return profile_ml_table_json['profile_id']

    '''
    profile_id: int,
    data: Dict[str, any] = {
        'profile_name': profile_name,
        'name_approved': name_approved,
        'lang_code': lang_code,
        'user_id': user_id,                             #Optional
        'is_main': is_main,                             #Optional
        'visibility_id': visibility_id,
        'is_approved': is_approved,
        'profile_type_id': profile_type_id, #Optional
        'preferred_lang_code': preferred_lang_code,     #Optional
        'experience_years_min': experience_years_min,   #Optional
        'main_phone_id': main_phone_id,                 #Optional
        'rip': rip,                                     #Optional
        'gender_id': gender_id,                         #Optional
        'stars': stars,
        'last_dialog_workflow_state_id': last_dialog_workflow_state_id
    }
    person_id: int                                      #Optional
    '''

    def update(self, profile_id: int, data: Dict[str, any]) -> None:
        logger.start(object={'profile_id': profile_id, 'data': str(data)})
        json_data = {
            "person_id": data['person_id'],
            "user_id": data['user_id'],
            "is_main": data['is_main'],
            "visibility_id": data['visibility_id'],
            "is_approved": data['is_approved'],
            "profile_type_id": data['profile_type_id'],
            "preferred_lang_code": data['preferred_lang_code'],
            "experience_years_min": data['experience_years_min'],
            "main_phone_id": data['main_phone_id'],
            "rip": data['rip'],
            "gender_id": data['gender_id'],
            "stars": data['stars'],
            "last_dialog_workflow_state_id": data['last_dialog_workflow_state_id']
        }
        super().update_by_id(table_name="profile_table", id_column_name="profile_id", id_column_value=profile_id, json_data=json_data)

        profile_ml_table_json = {
            "profile_id": profile_id,
            "lang_code": data['lang_code'],
            "`name`": data['profile_name'],
            "name_approved": data['name_approved']
        }
        super().update_by_id(table_name="profile_ml_table", id_column_name="profile_id", id_column_value=profile_id, json_data=profile_ml_table_json)
        logger.end()

    # TODO develop get_profile_object_by_profile_id( self, profile_id: int ) -> Profile[]:
    def get_profile_dict_by_profile_id(self, profile_id: int) -> Dict[str, any]:
        logger.start(object={'profile_id': profile_id})

        profile_view = self.select_one_dict_by_id(view_table_name="profile_view", id_column_name="profile_id", id_column_value=profile_id)

        profile_ml_view = self.select_one_dict_by_id(view_table_name="profile_ml_view", id_column_name="profile_id", id_column_value=profile_id)
        if not profile_view or not profile_ml_view:
            return {}

        # merge dicts
        get_result = {**profile_view, **profile_ml_view}

        logger.end(object={'get_result': str(get_result)})
        return get_result

    def delete_by_profile_id(self, profile_id: int):
        logger.start(object={'profile_id': profile_id})
        self.delete_by_id("profile_table", "profile_id", profile_id)
        logger.end()
