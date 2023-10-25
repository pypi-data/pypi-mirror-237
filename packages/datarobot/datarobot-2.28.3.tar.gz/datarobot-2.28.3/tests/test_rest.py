#
# Copyright 2021-2022 DataRobot, Inc. and its affiliates.
#
# All rights reserved.
#
# DataRobot, Inc.
#
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
#
# Released under the terms of DataRobot Tool and Utility Agreement.
import json

from mock import patch
import pytest
import responses

from datarobot import AppPlatformError, errors, Project
from datarobot.enums import DEFAULT_TIMEOUT
from tests.utils import assert_raised_regex, SDKTestcase


class Test400LevelErrors(SDKTestcase):
    @responses.activate
    def test_401_error_message(self):
        """For whatever reason, the `requests` library completely ignores the
        body in a 401 error, so, here is our own message
        """
        responses.add(
            responses.GET,
            "https://host_name.com/projects/",
            status=401,
        )

        with pytest.raises(AppPlatformError) as exc_info:
            Project.list()
        assert_raised_regex(exc_info, "not properly authenticated")

    @responses.activate
    def test_404_error_message(self):
        """Check that we handle correctly 4xx error with empty string in response body"""
        responses.add(responses.GET, "https://host_name.com/projects/", status=404, body="")

        with pytest.raises(AppPlatformError) as exc_info:
            Project.list()
        expected_error = "{} client error: {}".format(404, "")
        assert str(exc_info.value) == expected_error

    @responses.activate
    def test_403_error_message(self):
        """Check that we output same error message that server returns on 403"""
        error_text = "Some permission error"
        error_response = {"message": error_text}

        responses.add(
            responses.GET,
            "https://host_name.com/projects/",
            status=403,
            body=json.dumps(error_response),
        )

        with pytest.raises(AppPlatformError) as exc_info:
            Project.list()
        expected_error = "{} client error: {}".format(403, json.dumps(error_response))
        assert str(exc_info.value) == expected_error

    @responses.activate
    def test_model_already_added_exception(self):
        responses.add(
            responses.POST,
            "https://host_name.com/projects/p-id/models/",
            status=422,
            body=json.dumps({"message": "Model already added", "errorName": "JobAlreadyAdded"}),
        )

        with pytest.raises(errors.JobAlreadyRequested):
            Project("p-id").train("some-blueprint-id")

    @responses.activate
    def test_extracts_error_message(self):
        data = {"message": "project p-id has been deleted"}
        responses.add(
            responses.GET,
            "https://host_name.com/projects/p-id/models/",
            status=422,
            body=json.dumps(data),
            content_type="application/json",
        )

        with pytest.raises(AppPlatformError) as exc_info:
            Project("p-id").get_models()
        assert_raised_regex(exc_info, "project p-id has been deleted")


class DeprecationHeader(SDKTestcase):
    # These tests are based on the syntax in expired IETF draft doc
    # https://tools.ietf.org/id/draft-dalal-deprecation-header-03.html#syntax

    error_text = "Some error about deprecation"
    error_response = {"message": error_text}

    default_warning_message = (
        "The resource you are trying to access will be or is deprecated. "
        "For additional guidance, login to the DataRobot app for this project."
    )

    @responses.activate
    def test_client_handles_deprecation_header(self):
        responses.add(
            responses.GET,
            "https://host_name.com/projects/p-id/",
            status=200,
            json={},
            headers={"deprecation": "true"},
        )

        with pytest.warns(errors.PlatformDeprecationWarning, match=self.default_warning_message):
            Project("p-id").get("p-id")

    @responses.activate
    def test_client_handles_deprecation_header_empty_string_value(self):
        responses.add(
            responses.GET,
            "https://host_name.com/projects/p-id/",
            status=200,
            json={},
            headers={"deprecation": ""},
        )

        with pytest.warns(errors.PlatformDeprecationWarning, match=self.default_warning_message):
            Project("p-id").get("p-id")

    @responses.activate
    def test_client_handles_deprecation_header_with_date(self):
        dep_header_value = "Sun, 11 Nov 2018 23:59:59 GMT"
        responses.add(
            responses.GET,
            "https://host_name.com/projects/p-id/",
            status=200,
            json={},
            headers={"deprecation": dep_header_value},
        )

        with pytest.warns(errors.PlatformDeprecationWarning, match=dep_header_value):
            Project("p-id").get("p-id")

    @responses.activate
    def test_client_handles_deprecation_header_on_update(self):
        responses.add(
            responses.POST,
            "https://host_name.com/projects/p-id/models/",
            status=405,
            body=json.dumps(self.error_response),
            content_type="application/json",
        )

        with pytest.raises(errors.ClientError):
            with pytest.warns(errors.PlatformDeprecationWarning, match=self.error_text):
                Project("p-id").train("some-blueprint-id")


def test_client_uses_both_timeouts(client):
    connect_timeout = 33
    client.connect_timeout = connect_timeout

    with patch("datarobot.rest.requests.Session.request") as request_mock:
        client.get("ping")
        args, kwargs = request_mock.call_args
        called_timeout = kwargs["timeout"]
        assert called_timeout == (connect_timeout, DEFAULT_TIMEOUT.READ)


@responses.activate
def test_client_passes_read_timeout_from_build_request(client, temporary_file):
    connect_timeout = 33
    read_timeout = 180
    client.connect_timeout = connect_timeout

    with patch("datarobot.rest.requests.Session.request") as request_mock:
        client.build_request_with_file(
            "POST",
            "file_upload",
            "my_file.csv",
            file_path=temporary_file,
            read_timeout=read_timeout,
        )
        args, kwargs = request_mock.call_args
        called_timeout = kwargs["timeout"]
        assert called_timeout == (connect_timeout, read_timeout)
