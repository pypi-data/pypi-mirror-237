import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import json

from dotenv import load_dotenv
from logger_local import Logger
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from profile_local.comprehensive_profile import ComprehensiveProfile
from zoomus import ZoomClient

load_dotenv()

PROFILE_ZOOM_GRAPHQL_IMPORTER_LOCAL_PYTHON_PACKAGE_COMPONENT_ID = 178
PROFILE_ZOOM_GRAPHQL_IMPORTER_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME = 'profile-zoominfo-graphql-imp-local-python-package/src/ZoomInfo.py'
PROFILE_ZOOM_GRAPHQL_IMPORTER_LOCAL_PYTHON_PACKAGE_COMPONENT_TYPE = LoggerComponentEnum.ComponentCategory.Code.value
PROFILE_ZOOM_GRAPHQL_IMPORTER_LOCAL_PYTHON_PACKAGE__COMPONENT_CATEGORY = LoggerComponentEnum.ComponentCategory.Code.value
DEVELOPER_EMAIL = 'sahar.g@circ.zone'

obj = {
    'component_id': PROFILE_ZOOM_GRAPHQL_IMPORTER_LOCAL_PYTHON_PACKAGE_COMPONENT_ID,
    'component_name': PROFILE_ZOOM_GRAPHQL_IMPORTER_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME,
    'component_category': PROFILE_ZOOM_GRAPHQL_IMPORTER_LOCAL_PYTHON_PACKAGE_COMPONENT_TYPE,
    'developer_email': DEVELOPER_EMAIL,
}

logger_local = Logger.Logger.create_logger(object=obj)


class ZoomInfo:

    def __init__(self, client_id, client_secret, account_id) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.account_id = account_id
        self.client = ZoomClient(
            client_id=self.client_id, client_secret=self.client_secret, api_account_id=self.account_id)
        self.pl = ComprehensiveProfile()

    def get_user_by_email(self, email: str):
        logger_local.start(object={'email': email})
        users = self.get_all_users()
        for user in users['users']:
            if user['email'] == email:
                user = self.get_user_by_id(user['id'])
                compatible_json = self.generate_compatible_json(user)
                self.pl.insert(compatible_json)
                logger_local.end(object=user)
                return user
        return None

    def _get_next_page(self, next_page_token: str):
        logger_local.start(object={'next_page_token': next_page_token})
        response = self.client.user.list(page_token=next_page_token)
        users_list = response.json()
        logger_local.end(object=users_list)
        return users_list

    def get_all_users(self):
        logger_local.start()
        response = self.client.user.list()
        users_list = response.json()
        while users_list['page_number'] <= users_list['page_count']:
            for user in users_list['users']:
                user = self.get_user_by_id(user['id'])
                compatible_json = self.generate_compatible_json(user)
                self.pl.insert(compatible_json)
            if users_list['next_page_token'] == "":
                break
            users_list = self._get_next_page(users_list['next_page_token'])
        logger_local.end(object=users_list)
        return users_list

    def get_all_users_emails(self):
        logger_local.start()
        users = self.get_all_users()
        emails = []
        for user in users['users']:
            emails.append(user['email'])
        logger_local.end(object={'emails': emails})
        return emails

    def get_user_by_phone_number(self, phone_number: str):
        logger_local.start(object={'phone_number': phone_number})
        users = self.get_all_users()

        while users['page_number'] <= users['page_count']:
            for user in users['users']:
                if phone_number in user['phone_number']:
                    user = self.get_user_by_id(user['id'])
                    compatible_json = self.generate_compatible_json(user)
                    self.pl.insert(compatible_json)
                    logger_local.end(object=user)
                    return user
            if users['next_page_token'] == "":
                break
            users = self._get_next_page(users['next_page_token'])
        logger_local.end(object={'user': None})
        return None

    def get_user_by_name(self, first_name: str, last_name: str):
        logger_local.start(
            object={'first_name': first_name, 'last_name': last_name})
        users = self.get_all_users()
        while users['page_number'] <= users['page_count']:
            for user in users['users']:
                if user['first_name'] == first_name and user['last_name'] == last_name:
                    user = self.get_user_by_id(user['id'])
                    compatible_json = self.generate_compatible_json(user)
                    self.pl.insert(compatible_json)
                    logger_local.end(object=user)
                    return user
            if users['next_page_token'] == "":
                break
            users = self._get_next_page(users['next_page_token'])
        logger_local.end(object={'user': None})
        return None

    def get_user_by_id(self, user_id: str):
        logger_local.start(object={'user_id': user_id})
        user = self.client.user.get(id=user_id)
        user_json = json.loads(user.content)
        compatible_json = self.generate_compatible_json(user_json)
        self.pl.insert(compatible_json)
        logger_local.end(object={'user': user_json})
        return user_json

    def get_all_users_by_location(self, location: str):
        logger_local.start(object={'location': location})
        users = self.get_all_users()
        users_by_location = []

        while users['page_number'] <= users['page_count']:
            for user in users['users']:
                if user['location'] == location:
                    user = self.get_user_by_id(user['id'])
                    compatible_json = self.generate_compatible_json(user)
                    self.pl.insert(compatible_json)
                    users_by_location.append(user)
            if users['next_page_token'] == "":
                break
            users = self._get_next_page(users['next_page_token'])
        logger_local.end(object={'response': users_by_location})
        return users_by_location

    def get_all_users_by_job_title(self, job_title: str):
        logger_local.start(object={'job_title': job_title})
        users = self.get_all_users()
        users_by_job_title = []

        while users['page_number'] <= users['page_count']:
            for user in users['users']:
                if user['job_title'] == job_title:
                    user = self.get_user_by_id(user['id'])
                    compatible_json = self.generate_compatible_json(user)
                    self.pl.insert(compatible_json)
                    users_by_job_title.append(user)
            if users['next_page_token'] == "":
                break
            users = self._get_next_page(users['next_page_token'])
        logger_local.end(object={'response': users_by_job_title})
        return users_by_job_title

    def generate_compatible_json(self, user_info: dict):

        plan_type_dict = {
            1: "Basic",
            2: "Licensed",
            99: "None (can only be set with ssoCreate)"
        }

        person = {

        }

        profile = {
            'profile_name': user_info['display_name'],
            'name_approved': True,
            'lang_code': user_info['language'],
            'user_id': user_info['id'],
            'is_approved': True,
            'profile_type_id': plan_type_dict[user_info['type']],
            'preferred_lang_code': user_info['language'],
            'main_phone_id': user_info['phone_number'],
        }

        location = {
            'address_local_language': user_info['language'],
            'coordinate': {},
            'plus_code': user_info['phone_numbers'][0]['code'],
            'country': user_info['location']
        }

        storage = {
            'path': user_info['pic_url'],
            'url': user_info['pic_url'],
            'file_extension': 'jpg',
            'file_type': 'Profile Image'
        }

        entry = {
            "person": person,
            "location": location,
            "profile": profile,
            "storage": storage,
        }

        return json.dumps({'results': entry})
