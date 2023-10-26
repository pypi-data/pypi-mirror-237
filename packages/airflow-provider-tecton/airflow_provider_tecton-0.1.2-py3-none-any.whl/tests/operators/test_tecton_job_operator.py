# Copyright 2022 Tecton, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from datetime import datetime
import unittest
from unittest.mock import patch, MagicMock, Mock

from tecton_provider.operators.tecton_job_operator import (
    TectonJobOperator,
)


class TestTectonJobOperator(unittest.TestCase):
    JOB = {"job": {"id": "abc"}}
    OTHER_JOB = {"job": {"id": "cba"}}
    OTHER_JOB_TO_CANCEL = {"id": "cba", "state": "running"}
    OTHER_JOB_TO_CANCEL_CANCELLED = {"id": "cba", "state": "manually_cancelled"}
    GET_JOB_RUNNING_NO_ATTEMPT = {"job": {"id": "abc", "state": "RUNNING"}}
    GET_JOB_RUNNING = {
        "job": {
            "id": "abc",
            "state": "RUNNING",
            "attempts": [{"state": "RUNNING", "run_url": "example.com"}],
        }
    }
    FIND_JOB_SUCCESS = {
        "id": "abc",
        "state": "SUCCESS",
        "attempts": [{"state": "SUCCESS", "run_url": "example.com"}],
    }
    GET_JOB_SUCCESS = {"job": FIND_JOB_SUCCESS}
    GET_OTHER_JOB_SUCCESS = {
        "job": {
            "id": "cba",
            "state": "SUCCESS",
            "attempts": [{"state": "SUCCESS", "run_url": "example.com"}],
        }
    }
    GET_JOB_FAILURE_NO_ATTEMPTS = {"job": {"id": "abc", "state": "ERROR"}}
    GET_JOB_FAILURE = {
        "job": {
            "id": "abc",
            "state": "ERROR",
            "attempts": [{"state": "ERROR", "run_url": "example.com"}],
        }
    }

    @patch("time.sleep", return_value=None)
    @patch("tecton_provider.operators.tecton_job_operator.TectonHook.create")
    def test_execute(self, mock_create, mock_sleep):
        mock_hook = MagicMock()
        mock_create.return_value = mock_hook
        mock_hook.get_materialization_job.side_effect = [
            self.GET_JOB_RUNNING_NO_ATTEMPT,
            self.GET_JOB_RUNNING,
            self.GET_JOB_SUCCESS,
        ]
        mock_hook.find_materialization_job.return_value = None
        mock_hook.submit_materialization_job.return_value = self.JOB

        operator = TectonJobOperator(
            task_id="abc",
            workspace="prod",
            feature_view="fv",
            online=True,
            offline=True,
            start_time=datetime(2022, 7, 1),
            end_time=datetime(2022, 7, 2),
        )
        operator.execute(None)

    @patch("time.sleep", return_value=None)
    @patch("tecton_provider.operators.tecton_job_operator.TectonHook.create")
    def test_execute_cancel_existing(self, mock_create, mock_sleep):
        mock_hook = MagicMock()
        mock_create.return_value = mock_hook
        mock_hook.get_materialization_job.side_effect = [
            {"job": self.OTHER_JOB_TO_CANCEL},
            {"job": self.OTHER_JOB_TO_CANCEL_CANCELLED},
            self.GET_JOB_RUNNING_NO_ATTEMPT,
            self.GET_JOB_RUNNING,
            self.GET_JOB_SUCCESS,
        ]
        mock_hook.find_materialization_job.return_value = self.OTHER_JOB_TO_CANCEL
        mock_hook.cancel_materialization_job.return_value = None
        mock_hook.submit_materialization_job.return_value = self.JOB

        operator = TectonJobOperator(
            task_id="abc",
            workspace="prod",
            feature_view="fv",
            online=True,
            offline=True,
            start_time=datetime(2022, 7, 1),
            end_time=datetime(2022, 7, 2),
        )
        operator.execute(None)
        assert mock_hook.cancel_materialization_job.call_count == 1

    @patch("tecton_provider.operators.tecton_job_operator.TectonHook.create")
    def test_execute_existing_success(self, mock_create):
        mock_hook = MagicMock()
        mock_create.return_value = mock_hook
        mock_hook.find_materialization_job.return_value = self.FIND_JOB_SUCCESS

        operator = TectonJobOperator(
            task_id="cba",
            workspace="prod",
            feature_view="fv",
            online=True,
            offline=True,
            start_time=datetime(2022, 7, 1),
            end_time=datetime(2022, 7, 2),
        )
        operator.execute(None)
        assert mock_hook.submit_materialization_job.call_count == 0

    @patch("tecton_provider.operators.tecton_job_operator.TectonHook.create")
    def test_execute_existing_success_allow_overwrite(self, mock_create):
        mock_hook = MagicMock()
        mock_create.return_value = mock_hook
        mock_hook.find_materialization_job.return_value = self.FIND_JOB_SUCCESS
        mock_hook.submit_materialization_job.return_value = self.OTHER_JOB
        mock_hook.get_materialization_job.side_effect = [
            self.GET_OTHER_JOB_SUCCESS,
        ]

        operator = TectonJobOperator(
            task_id="cba",
            workspace="prod",
            feature_view="fv",
            online=True,
            offline=True,
            start_time=datetime(2022, 7, 1),
            end_time=datetime(2022, 7, 2),
            allow_overwrite=True,
        )
        operator.execute(None)
        assert mock_hook.submit_materialization_job.call_count == 1

    @patch("time.sleep", return_value=None)
    @patch("tecton_provider.operators.tecton_job_operator.TectonHook.create")
    def test_execute_failed(self, mock_create, mock_time):
        mock_hook = MagicMock()
        mock_create.return_value = mock_hook
        mock_hook.get_materialization_job.side_effect = [
            self.GET_JOB_RUNNING_NO_ATTEMPT,
            self.GET_JOB_RUNNING,
            self.GET_JOB_FAILURE,
        ]
        mock_hook.find_materialization_job.return_value = None
        mock_hook.submit_materialization_job.return_value = self.JOB

        operator = TectonJobOperator(
            task_id="abc",
            workspace="prod",
            feature_view="fv",
            online=True,
            offline=True,
            start_time=datetime(2022, 7, 1),
            end_time=datetime(2022, 7, 2),
        )
        with self.assertRaises(Exception) as e:
            operator.execute(None)
        self.assertIn("Final job state", str(e.exception))

    @patch("time.sleep", return_value=None)
    @patch("tecton_provider.operators.tecton_job_operator.TectonHook.create")
    def test_execute_failed_no_attempts(self, mock_create, mock_time):
        mock_hook = MagicMock()
        mock_create.return_value = mock_hook
        mock_hook.get_materialization_job.side_effect = [
            self.GET_JOB_RUNNING_NO_ATTEMPT,
            self.GET_JOB_RUNNING,
            self.GET_JOB_FAILURE_NO_ATTEMPTS,
        ]
        mock_hook.find_materialization_job.return_value = None
        mock_hook.submit_materialization_job.return_value = self.JOB

        operator = TectonJobOperator(
            task_id="abc",
            workspace="prod",
            feature_view="fv",
            online=True,
            offline=True,
            start_time=datetime(2022, 7, 1),
            end_time=datetime(2022, 7, 2),
        )
        with self.assertRaises(Exception) as e:
            operator.execute(None)
        self.assertIn("Final job state", str(e.exception))

    @patch("tecton_provider.operators.tecton_job_operator.TectonHook.create")
    def test_on_kill(self, mock_create):
        mock_hook = MagicMock()
        mock_create.return_value = mock_hook
        mock_hook.cancel_materialization_job.return_value = True
        mock_hook.find_materialization_job.return_value = None
        operator = TectonJobOperator(
            task_id="abc",
            workspace="prod",
            feature_view="fv",
            online=True,
            offline=True,
            start_time=datetime(2022, 7, 1),
            end_time=datetime(2022, 7, 2),
        )
        operator.on_kill()
        self.assertEqual(0, mock_hook.cancel_job.call_count)
        operator.job_id = "abc"
        operator.on_kill()
