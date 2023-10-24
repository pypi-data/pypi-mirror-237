"""
SkylabStudio - Python Client
For more information, visit https://studio.skylabtech.ai
"""

import json
import logging
import requests
import os
import time
import hmac
import base64
import hashlib

from .version import VERSION

API_HEADER_KEY = 'X-SLT-API-KEY'
API_HEADER_CLIENT = 'X-SLT-API-CLIENT'

LOGGER = logging.getLogger('skylab_studio')
LOGGER.propagate = False

class api: #pylint: disable=invalid-name
    """
    The client for accessing the Skylab Studio platform.

    Args:
        api_key (str): Your account's API KEY.

    Attributes:
        api_proto (str): The API endpoint protocol.
        api_port (str): The API endpoint port.
        api_host (str): The API endpoint host name.
        api_version (str): The API endpoint version number.
        api_key (str): The API key to use.
        debug (boolean): Whether or not to allow debugging information to be printed.
    """

    # initialization
    api_proto=os.environ['API_PROTO'] or 'https'
    api_port=os.environ['API_PORT'] or '443'
    api_host=os.environ['API_HOST'] or 'studio.skylabtech.ai'

    # this is not package version -> used to construct the request base url
    api_version = '1'
    api_key = 'THIS_IS_A_TEST_API_KEY'

    debug = False

    def __init__(self, api_key=None, **kwargs):
        if not api_key:
            raise Exception("You must specify an api key")

        self.api_key = api_key

        if 'api_host' in kwargs:
            self.api_host = kwargs['api_host']
        if 'api_proto' in kwargs:
            self.api_proto = kwargs['api_proto']
        if 'api_port' in kwargs:
            self.api_port = kwargs['api_port']
        if 'api_version' in kwargs:
            self.api_version = kwargs['api_version']
        if 'debug' in kwargs:
            self.debug = kwargs['debug']

        if self.debug:
            logging.basicConfig(format='%(asctime)-15s %(message)s', level=logging.DEBUG)

            LOGGER.debug('Debug enabled')
            LOGGER.propagate = True

    def _build_http_auth(self):
        return (self.api_key, '')

    def _build_request_headers(self):
        client_header = '%s-%s' % (
            'python',
            VERSION
        )

        headers = {
            API_HEADER_CLIENT: client_header,
            'X-SLT-API-KEY': self.api_key,
            'Content-type': 'application/json',
            'Accept': 'text/plain'
        }

        return headers

    def _build_request_path(self, endpoint):
        path = '/api/public/v%s/%s' % (self.api_version, endpoint)

        path = "%s://%s:%s%s" % (
            self.api_proto,
            self.api_host,
            self.api_port,
            path
        )

        return path

    @staticmethod
    def _build_payload(data):
        if not data:
            return None

        return json.dumps(data)

    def _api_request(self, endpoint, http_method, **kwargs):
        """Private method for api requests"""
        LOGGER.debug(' > Sending API request to endpoint: %s', endpoint)

        headers = self._build_request_headers()
        LOGGER.debug('\theaders: %s', headers)

        path = self._build_request_path(endpoint)
        LOGGER.debug('\tpath: %s', path)

        data = self._build_payload(kwargs.get('payload'))
        if not data:
            data = kwargs.get('data')
        LOGGER.debug('\tdata: %s', data)

        req_kw = dict(
            headers=headers,
        )

        if http_method == 'POST':
            if data:
                response = requests.post(path, data=data, **req_kw)
            else:
                response = requests.post(path, **req_kw)
        elif http_method == 'PUT':
            response = requests.put(path, data=data, **req_kw)
        elif http_method == 'DELETE':
            response = requests.delete(path, **req_kw)
        else:
            response = requests.get(path, data=data, **req_kw)

        LOGGER.debug('\tresponse code:%s', response.status_code)

        try:
            LOGGER.debug('\tresponse: %s', response.json())
        except ValueError:
            LOGGER.debug('\tresponse: %s', response.content)

        return response

    def list_jobs(self):
        """ API call to get all jobs """
        return self._api_request(
            'jobs',
            'GET'
        )

    def create_job(self, payload=None):
        """ API call to create a job """
        return self._api_request(
            'jobs',
            'POST',
            payload=payload
        )

    def get_job(self, job_id):
        """ API call to get a specific job """
        return self._api_request(
            'jobs/%s' % job_id,
            'GET'
        )

    def get_job_by_name(self, payload=None):
        return self._api_request(
            'jobs/find_by_name',
            'GET',
            payload=payload
        )

    def update_job(self, job_id, payload=None):
        """ API call to update a specific job """
        return self._api_request(
            'jobs/%s' % job_id,
            'PATCH',
            payload=payload
        )

    def queue_job(self, job_id, payload=None):
        return self._api_request(
            'jobs/%s/queue' % job_id,
            'POST',
            payload=payload
        )

    def fetch_jobs_in_front(self, job_id):
        return self._api_request(
            'jobs/%s/jobs_in_front' % job_id,
            'GET',
        )

    def delete_job(self, job_id):
        """ API call to delete a specific job """
        return self._api_request(
            'jobs/%s' % job_id,
            'DELETE'
        )

    def cancel_job(self, job_id):
        """ API call to cancel a specific job """
        return self._api_request(
            'jobs/%s/cancel' % job_id,
            'POST'
        )

    def list_profiles(self):
        """ API call to get all profiles """
        return self._api_request(
            'profiles',
            'GET'
        )

    def create_profile(self, payload=None):
        """ API call to create a profile """
        return self._api_request(
            'profiles',
            'POST',
            payload=payload
        )

    def get_profile(self, profile_id):
        """ API call to get a specific profile """
        return self._api_request(
            'profiles/%s' % profile_id,
            'GET'
        )

    def update_profile(self, profile_id, payload=None):
        """ API call to update a specific profile """
        return self._api_request(
            'profiles/%s' % profile_id,
            'PATCH',
            payload=payload
        )

    def list_photos(self):
        """ API call to get all photos """
        return self._api_request(
            'photos',
            'GET'
        )

    def get_upload_url(self, payload={"use_cache_upload": True}):
      return self._api_request('photos/upload_url', 'GET', payload=payload)

    def create_photo(self, payload=None):
        """ API call to create a photo """
        return self._api_request(
            'photos',
            'POST',
            payload=payload
        )

    def upload_photo(self, photo_path, model, id, use_cache_upload=False):
        photo_name = os.path.basename(photo_path)
        tags = {}
        # Read file contents to binary
        with open(photo_path, "rb") as file:
            data = file.read()

        # model - either job or profile (job_id/profile_id)
        photo_data = { f"{model}_id": id, "name": photo_name }

        if not use_cache_upload and model == 'job':

            photo_data['use_cache_upload'] = use_cache_upload
            job_type = self.get_job(id).json()['type']

            if job_type == 'regular':
                tags = { 'X-Amz-Tagging': 'job=photo&api=true' }

            # Ask studio to create the photo record
            photo_resp = self.create_photo(photo_data)
            photo_id = photo_resp.json()['id']

            payload = {
                "use_cache_upload": use_cache_upload,
                "photo_id": photo_id,
            }

            # Ask studio for a presigned url
            upload_url_resp = self.get_upload_url(payload=payload)
            upload_url = upload_url_resp.json()['url']

        else:
            # Ask studio for a presigned url + key
            upload_url_resp = self.get_upload_url()

            key = upload_url_resp.json()['key']
            upload_url = upload_url_resp.json()['url']

            if not key:
              raise Exception('Unable to obtain upload key')

            if not upload_url:
              raise Exception('Unable to obtain upload_url')

            photo_data['key'] = key


        # PUT request to presigned url with image data
        try:
          upload_photo_resp = requests.put(upload_url, data, headers=tags)

          if upload_photo_resp.status_code != 200:
            print('First upload attempt failed, retrying...')
            retry = 0
            # retry upload
            while retry < 3:
                upload_photo_resp = requests.put(upload_url, data, headers=tags)

                if upload_photo_resp.status_code == 200:
                    break  # Upload was successful, exit the loop
                elif retry == 2:  # Check if retry count is 2 (0-based indexing)
                    raise Exception('Unable to upload to the bucket after retrying.')
                else:
                    time.sleep(1)  # Wait for a moment before retrying
                    retry += 1

        except Exception as e:
          print(f"An exception of type {type(e).__name__} occurred: {e}")

          if not use_cache_upload:
              print('Deleting created, but unuploaded photo...')
              self.delete_photo(photo_id)

        if use_cache_upload:
          # photo gets created after upload in cache case because photo promote job
          photo_creation_req = self.create_photo(photo_data)

          # photo will be in bucket but no record will have been created.
          if photo_creation_req.status_code != 201:
              raise Exception(photo_creation_req.json()['errors'])

        return upload_photo_resp

    def get_photo(self, photo_id):
        """ API call to get a specific photo """
        return self._api_request(
            'photos/%s' % photo_id,
            'GET'
        )

    def get_job_photos(self, job_identifier, value):
        """
          job identifier - either id or name
          value - the actual job_id or job_name
        """
        payload = {
            f"job_{job_identifier}": value
        }
        return self._api_request(
            'photos/list_for_job',
            'GET',
            payload=payload
        )

    def delete_photo(self, photo_id):
        """ API call to delete a specific photo """
        return self._api_request(
            'photos/%s' % photo_id,
            'DELETE'
        )

    def validate_hmac_headers(self, secret_key, job_json, request_timestamp, signature):
        message=f"{request_timestamp}:{job_json}".encode('utf-8')

        # Create the HMAC signature using SHA-256
        hmac_digest = hmac.new(secret_key.encode('utf-8'), message, hashlib.sha256).digest()
        generated_sig = base64.b64encode(hmac_digest).decode('utf-8')

        # Compare rails to python signature
        return signature == generated_sig
