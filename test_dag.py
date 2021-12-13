from dag import bash_start, api_call
from unittest.mock import patch
from airflow.models import Connection
import airflow


def test_bash_start():
    result = bash_start.execute(context={})
    assert result == "starting dag"


@patch('airflow.hooks.base.BaseHook.get_connection')
def test_api_call(mm_connection):
    mm_connection.return_value = Connection(conn_id="sun_conn",
                                            schema="https",
                                            host="api.sunrise-sunset.org")
    exp_keys = ["sunrise", "sunset"]
    result = api_call.execute(context={})
    assert all([ek in result.keys() for ek in exp_keys])
