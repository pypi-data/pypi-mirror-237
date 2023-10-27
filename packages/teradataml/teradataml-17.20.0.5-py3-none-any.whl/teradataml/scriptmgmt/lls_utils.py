"""
Copyright (c) 2020 by Teradata Corporation. All rights reserved.
TERADATA CORPORATION CONFIDENTIAL AND TRADE SECRET

Primary Owner: Trupti.purohit@teradata.com
Secondary Owner: Gouri.patwardhan@Teradata.com

teradataml load library service wrappers.
----------
All teradataml wrappers to provide interface to load library service stored procedures
from Open Analytics Framework.
"""
import concurrent.futures
import functools
import operator
import pandas as pd
import requests
from teradataml import configure
from teradataml.context.context import _get_user
from teradataml.common.constants import HTTPRequest, AsyncStatusColumns
from teradataml.common.exceptions import TeradataMlException
from teradataml.common.messages import Messages
from teradataml.common.messagecodes import MessageCodes
from teradataml.common.utils import UtilFuncs
from teradataml.clients.pkce_client import _DAWorkflow
from teradataml.utils.internal_buffer import _InternalBuffer
from teradataml.scriptmgmt.UserEnv import UserEnv, _get_auth_token, \
    _process_ues_response, _get_ues_url, _AuthToken
from teradataml.utils.validators import _Validators
from time import time, sleep
import warnings
import webbrowser
from urllib.parse import parse_qs, urlparse
from teradataml.utils.utils import _async_run_id_info


def list_base_envs():
    """
    DESCRIPTION:
        Lists the available Python OR R base environments versions configured in the
        Open Analytics Framework.

    PARAMETERS:
            None.

    RETURNS:
        Pandas DataFrame.
        If the operation is successful, function returns
        environment name, language and version of the language interpreter in a Pandas dataframe.

    RAISES:
        TeradataMlException.

    EXAMPLES:
            >>> from teradataml import list_base_envs
            >>> list_base_envs()
                   base_name language version
            0  python_3.7.13   Python  3.7.13
            1  python_3.8.13   Python  3.8.13
            2  python_3.9.13   Python  3.9.13
            3        r_4.1.3        R   4.1.3
            4        r_3.6.3        R   3.6.3
            5        r_4.0.2        R   4.0.2
            >>>
    """
    try:
        response = UtilFuncs._http_request(_get_ues_url("base_environments"), headers=_get_auth_token())

        response = _process_ues_response(api_name="list_base_envs", response=response)
        data = response.json()

        # If no data, raise warning.
        if len(data) == 0:
            warnings.warn(Messages.get_message(MessageCodes.NO_ENVIRONMENT_FOUND, "Python/R base"))
            return

        # Create a pandas DataFrame from data.
        return pd.DataFrame.from_records(data)

    except (TeradataMlException, RuntimeError):
        raise
    except Exception as emsg:
        msg_code = MessageCodes.FUNC_EXECUTION_FAILED
        error_msg = Messages.get_message(msg_code, "list_base_envs", str(emsg))
        raise TeradataMlException(error_msg, msg_code)


def list_user_envs(env_name=None, **kwargs):
    """
    DESCRIPTION:
        Lists the Python OR R environments created by the session user in
        Open Analytics Framework.

    PARAMETERS:
        env_name:
            Optional Argument.
            Specifies the string or regular expression to filter name of the environment.
            Types: str

        base_env:
            Optional Argument.
            Specifies the string or regular expression to filter the base Python environment.
            Types: str

        desc:
            Optional Argument.
            Specifies the string or regular expression to filter the description
            about the environment.
            Types: str
        
        case:
            Optional Argument.
            Specifies whether filtering operation should be case sensitive or not.
            Default Value: False
            Types: boolean
        
        regex:
            Optional Argument.
            Specifies whether string passed to "env_name", "base_env", and "desc"
            should be treated as regular expression or a literal.
            When set to True, string is considered as a regular expression pattern,
            otherwise treats it as literal string.
            Default Value: True
            Types: boolean
        
        flags:
            Optional Argument.
            Specifies flags to pass for regular expressions in filtering.
            For example
                re.IGNORECASE.
            Default Value: 0
            Types: int

    RETURNS:
        Pandas DataFrame.
        Function returns remote user environments and their details in a Pandas dataframe.
        Function will help user find environments created, version of Python language used
        in the environment and description of each environment if provided at the time of
        environment creation.

    RAISES:
        TeradataMlException.

    EXAMPLES:
        # Create example environments.
        >>> create_env('Fraud_Detection',
        ...            'python_3.7.13',
        ...            'Fraud detection through time matching')
            User environment 'Fraud_detection' created.
        >>> create_env('Lie_Detection',
        ...            'python_3.7.13',
        ...            'Lie detection through time matching')
            User environment 'Lie_Detection' created.
        >>> create_env('Lie_Detection_ML',
        ...            'python_3.8.13',
        ...            'Detect lie through machine learning.')
            User environment 'Lie_Detection_ML' created.
        >>> create_env('Sales_env',
        ...            'python_3.9.13',
        ...            'Sales team environment.')
            User environment 'Sales_env' created.
        >>> create_env('Customer_Trends',
        ...            'r_4.1.3',
        ...            'Analyse customer trends.')
        User environment 'Customer_Trends' created.
        >>> create_env('Carbon_Credits',
        ...            'r_3.6.3',
        ...            'Prediction of carbon credits consumption.')
        User environment 'Carbon_Credits' created.
        
        # Example 1: List all available user environments.
        >>> list_user_envs()
                   env_name                           env_description  base_env_name language
        0    Carbon_Credits  Prediction of carbon credits consumption        r_3.6.3        R
        1   Customer_Trends                   Analyse customer trends        r_4.1.3        R
        2   Fraud_Detection     Fraud detection through time matching  python_3.7.13   Python
        3     Lie_Detection       Lie detection through time matching  python_3.7.13   Python
        4  Lie_Detection_ML      Detect lie through machine learning.  python_3.8.13   Python
        5         Sales_env                   Sales team environment.  python_3.9.13   Python
        >>>

        # Example 2: List all user environments with environment name containing string
        #            "Detection" and description that contains string "."(period).
        >>> list_user_envs(env_name="Detection", desc=".", regex=False)
                   env_name                       env_description  base_env_name language
        4  Lie_Detection_ML  Detect lie through machine learning.  python_3.8.13   Python
        >>>

        # Example 3: List all user environments with description that contains string "lie"
        #            and is case sensitive. 
        >>> list_user_envs(desc="lie", case=True)
                   env_name                       env_description  base_env_name language
        4  Lie_Detection_ML  Detect lie through machine learning.  python_3.8.13   Python
        >>>

        # Example 4: List all user environments with base environment version containing string
        #            "3.".
        >>> list_user_envs(base_env="3.")
                   env_name                           env_description  base_env_name language
        0    Carbon_Credits  Prediction of carbon credits consumption        r_3.6.3        R
        2   Fraud_Detection     Fraud detection through time matching  python_3.7.13   Python
        3     Lie_Detection       Lie detection through time matching  python_3.7.13   Python
        4  Lie_Detection_ML      Detect lie through machine learning.  python_3.8.13   Python
        5         Sales_env                   Sales team environment.  python_3.9.13   Python
        >>>

        # Example 5: List all user environments with environment name contains string "detection",
        #            description containing string "fraud" and base environment containing string "3.7".
        >>> list_user_envs("detection", desc="fraud", base_env="3.7")
                  env_name                        env_description  base_env_name language
        2  Fraud_Detection  Fraud detection through time matching  python_3.7.13   Python
        >>>

        # Example 6: List all user environments with environment name that ends with "detection".
        >>> list_user_envs("detection$")
                  env_name                        env_description  base_env_name language
        2  Fraud_Detection  Fraud detection through time matching  python_3.7.13   Python
        3    Lie_Detection    Lie detection through time matching  python_3.7.13   Python
        >>>

        # Example 7: List all user environments with description that has either "lie" or "sale".
        #            Use re.VERBOSE flag to add inline comment.
        >>> list_user_envs(desc="lie|sale # Search for lie or sale.", flags=re.VERBOSE)
                   env_name                       env_description  base_env_name language
        3     Lie_Detection   Lie detection through time matching  python_3.7.13   Python
        4  Lie_Detection_ML  Detect lie through machine learning.  python_3.8.13   Python
        5         Sales_env               Sales team environment.  python_3.9.13   Python
        >>>

        # Example 8: List all user environments where python 3 environment release version has 
        #            odd number. For e.g. python_3.7.x. 
        >>> list_user_envs(base_env="\.\d*[13579]\.")
                  env_name                        env_description  base_env_name language
        1  Customer_Trends                Analyse customer trends        r_4.1.3        R
        2  Fraud_Detection  Fraud detection through time matching  python_3.7.13   Python
        3    Lie_Detection    Lie detection through time matching  python_3.7.13   Python
        5        Sales_env                Sales team environment.  python_3.9.13   Python
        >>>

        # Remove example environments.
        remove_env("Fraud_Detection")
        remove_env("Lie_Detection")
        remove_env("Lie_Detection_ML")
        remove_env("Sales_env")
        remove_env("Carbon_Credits")
        remove_env("Customer_Trends")
    """
    base_env = kwargs.pop("base_env", None)
    desc = kwargs.pop("desc", None)
    case = kwargs.pop("case", False)
    __arg_info_matrix = []
    __arg_info_matrix.append(["env_name", env_name, True, (str), True])
    __arg_info_matrix.append(["base_env", base_env, True, (str), True])
    __arg_info_matrix.append(["desc", desc, True, (str), True])

    # Validate arguments
    _Validators._validate_function_arguments(__arg_info_matrix)

    try:
        response = UtilFuncs._http_request(_get_ues_url(), headers=_get_auth_token())
        # Below condition is special case handeling when remove_all_envs() used by user, remove_all_envs()
        # removes all the envs which result in a status_code 404 and due to which warnings provided in
        # list_user_envs() not appears.
        if response.status_code == 404 and "No user environments found." in response.text:
            data = []
        else:
            response = _process_ues_response(api_name="list_user_envs", response=response)
            data = response.json()

        if len(data) > 0:
            unknown_label = "Unknown"
            # Check if environment is corrupted or not. If it is corrupted, alter the details.
            for base_env_details in data:
                if base_env_details["base_env_name"] == "*":
                    base_env_details["base_env_name"] = unknown_label
                    base_env_details["language"] = unknown_label
                    base_env_details["env_description"] = "Environment is corrupted. Use remove_env() to remove environment."

            # Return result as Pandas dataframe.
            pandas_df = pd.DataFrame.from_records(data)

            # Filter based on arguments passed by user.
            exprs = []
            if env_name is not None:
                exprs.append(pandas_df.env_name.str.contains(pat=env_name, case=case, **kwargs))
            if base_env is not None:
                exprs.append(pandas_df.base_env_name.str.contains(pat=base_env, case=case, **kwargs))
            if desc is not None:
                exprs.append(pandas_df.env_description.str.contains(pat=desc, case=case, **kwargs))

            pandas_df = pandas_df[functools.reduce(operator.and_, exprs)] if exprs else pandas_df

            # Return the DataFrame if not empty.
            if len(pandas_df) > 0:
                return pandas_df
        
        print("No user environment(s) found.")
    except (TeradataMlException, RuntimeError):
        raise
    except Exception as emsg:
        msg_code = MessageCodes.FUNC_EXECUTION_FAILED
        error_msg = Messages.get_message(msg_code, "list_user_envs", emsg)
        raise TeradataMlException(error_msg, msg_code)


def create_env(env_name, base_env, desc=None):
    """
    DESCRIPTION:
        Creates an isolated remote user environment in the Open Analytics Framework that
        includes a specific Python or R language interpreter version.
        Available base Python or R environments can be found using list_base_envs() function.

    PARAMETERS:
        env_name:
            Required Argument.
            Specifies the name of the environment to be created.
            Types: str

        base_env:
            Required Argument.
            Specifies the name of the base Python or R environment to be used to create remote
            user environment.
            Types: str

        desc:
            Optional Argument.
            Specifies description about the environment's usage or purpose.
            Types: str

    RETURNS:
        An object of class UserEnv representing the remote user environment.

    RAISES:
        TeradataMlException.

    EXAMPLES:
        # List all available user environments.
        >>> list_base_envs()
                   base_name language version
                0  python_3.7.13   Python  3.7.13
                1  python_3.8.13   Python  3.8.13
                2  python_3.9.13   Python  3.9.13
                3  python_3.10.5   Python  3.10.5
                4          r_4.1        R   4.1.3
                5          r_4.0        R   4.0.5
                6          r_4.2        R   4.2.2

        # create a Python 3.7.13 environment with given name and description in the Vantage.
        >>> fraud_detection_env = create_env('Fraud_detection',
        ...                                  'python_3.7.13',
        ...                                  'Fraud detection through time matching')
            User environment 'Fraud_detection' created.

        # create a R 4.1.3 environment with given name and description in the Vantage.
        >>> fraud_detection_env = create_env('Carbon_Credits',
        ...                                  'r_4.1',
        ...                                  'Prediction of carbon credits consumption')
            User environment 'Carbon_Credits' created.
    """
    __arg_info_matrix = []
    __arg_info_matrix.append(["env_name", env_name, False, (str), True])
    __arg_info_matrix.append(["base_env", base_env, False, (str), True])
    __arg_info_matrix.append(["desc", desc, True, (str)])

    # Validate arguments
    _Validators._validate_function_arguments(__arg_info_matrix)

    try:
        data = {"env_name": env_name,
                "env_description": desc,
                "base_env_name": base_env
                }

        response = UtilFuncs._http_request(
            _get_ues_url(), HTTPRequest.POST, headers=_get_auth_token(), json=data)

        # Validate the ues response.
        _process_ues_response(api_name="create_env", response=response)

        print("User environment '{0}' created.".format(env_name))

        # Return an instance of class UserEnv.
        return UserEnv(env_name, base_env, desc)

    except (TeradataMlException, RuntimeError):
        raise

    except Exception as emsg:
        msg_code = MessageCodes.FUNC_EXECUTION_FAILED
        error_msg = Messages.get_message(msg_code, "create_env", str(emsg))
        raise TeradataMlException(error_msg, msg_code)


def _async_run_status_open_af(claim_id):
    """
    DESCRIPTION:
        Internal function to get the status of a claim_id.


    PARAMETERS:
        claim_id:
            Required Argument.
            Specifies the unique identifier of the asynchronous process.
            Types: str

    RETURNS:
        list

    RAISES:
        None

    EXAMPLES:
        __get_claim_id_status('278381bf-e3b3-47ff-9ba5-c3b5d9007363')
    """
    # Get the claim id status.
    resp_data = __get_status(claim_id)

    desc = _async_run_id_info.get(claim_id, {}).get("description", "Unknown")
    get_details = lambda data: {AsyncStatusColumns.ADDITIONAL_DETAILS.value:
                                    data.pop("details", None),
                                AsyncStatusColumns.STATUS.value:
                                    data.pop("stage", None),
                                AsyncStatusColumns.TIMESTAMP.value:
                                    data.pop("timestamp", None),
                                AsyncStatusColumns.RUN_ID.value:
                                    claim_id,
                                AsyncStatusColumns.RUN_DESCRIPTION.value: desc}

    return [get_details(sub_step) for sub_step in resp_data]


def __get_status(claim_id):
    """
    DESCRIPTION:
        Internal function to get the status of a claim_id using
        status API's REST call.


    PARAMETERS:
        claim_id:
            Required Argument.
            Specifies the unique identifier of the asynchronous process.
            Types: str

    RETURNS:
        list

    RAISES:
        None

    EXAMPLES:
        __get_status('278381bf-e3b3-47ff-9ba5-c3b5d9007363')
    """
    # Get the claim id status
    response = UtilFuncs._http_request(_get_ues_url(env_type="fm",
                                                    claim_id=claim_id,
                                                    api_name="status"),
                                       headers=_get_auth_token())
    return _process_ues_response(api_name="status",
                                 response=response).json()


def remove_env(env_name, **kwargs):
    """
    DESCRIPTION:
        Removes the user's Python or R environment from the Open Analytics Framework.
        The remote user environments are created using create_env() function.
        Note:
            remove_env() should not be triggered on any of the environment if
            install_lib/uninstall_lib/update_lib is running on the corresponding
            environment.

    PARAMETERS:
        env_name:
            Required Argument.
            Specifies the name of the environment to be removed.
            Types: str

        **kwargs:
            asynchronous:
                Optional Argument.
                Specifies whether to remove environment synchronously or
                asynchronously. When set to True, environment will be removed
                asynchronously. Otherwise, the environment will be removed synchronously.
                Default Value: False
                Types: bool


    RETURNS:
        True, if the operation is synchronous, str otherwise.

    RAISES:
        TeradataMlException, RuntimeError.

    EXAMPLES:
        # Create a Python 3.7.13 environment with given name and description in the Vantage.
        >>> fraud_detection_env = create_env('Fraud_detection',
        ...                                  'python_3.7.13',
        ...                                  'Fraud detection through time matching')
        User environment 'Fraud_detection' created.
        >>>
        # Create a R 4.1.3 environment with given name and description in the Vantage.
        >>> fraud_detection_env = create_env('Carbon_Credits',
        ...                                  'r_4.1',
        ...                                  'Prediction of carbon credits consumption')
        User environment 'Carbon_Credits' created.
        >>>
        # Example 1: Remove Python environment asynchronously.
        >>> remove_env('Fraud_detection', asynchronous=True)
        Request to remove environment initiated successfully. Check the status using list_user_envs(). If environment is not removed, check the status of asynchronous call using async_run_status('ab34cac6-667a-49d7-bac8-d0456f372f6f') or get_env('Fraud_detection').status('ab34cac6-667a-49d7-bac8-d0456f372f6f')
        'ab34cac6-667a-49d7-bac8-d0456f372f6f'

        >>>
        # Example 2: Remove R environment synchronously.
        >>> remove_env('Carbon_Credits')
        User environment 'Carbon_Credits' removed.
        True
    """
    __arg_info_matrix = []
    __arg_info_matrix.append(["env_name", env_name, False, (str), True])

    # Validate arguments
    _Validators._validate_function_arguments(__arg_info_matrix)

    status = __manage_envs(env_name=env_name, api_name="remove_env",
                           **kwargs)

    return status


def __manage_envs(env_name=None, api_name="remove_env", **kwargs):
    """
    Internal function to manage environment deletion synchronously or
    asynchronously.

    PARAMETERS:
        env_name:
            Optional Argument.
            Specifies the name of the environment to be removed.
            Types: str

        api_name:
            Optional Argument.
            Specifies the name of the API.
            Permitted Values: remove_env, remove_all_envs
            Default Value: remove_env
            Types: str

        kwargs:
            asynchronous:
                Optional Argument.
                Specifies whether to remove environment synchronously or
                asynchronously.
                Default Value: False
                Types: bool

            is_print:
                Optional Argument.
                Specifies whether to print the message or not.
                Default Value: True
                Types: bool


    RETURNS:
        True, if the operation is synchronous, str otherwise.

    RAISES:
        TeradatamlException.

    EXAMPLES:
        __manage_envs(env_name="test_env", api_name="remove_env", asynchronous=True)
    """
    asynchronous = kwargs.get("asynchronous", False)
    # In case of remove_all_envs(env_type="R") it was printing async msges
    # multiple times. To restrict that internally introduced is_print.
    is_print = kwargs.get("is_print", True)

    __arg_info_matrix = []
    __arg_info_matrix.append(["api_name", api_name, False, (str), True,
                              ["remove_env", "remove_all_envs"]])
    __arg_info_matrix.append(["asynchronous", asynchronous, True, bool])
    __arg_info_matrix.append(["is_print", is_print, True, bool])

    # Argument validation.
    _Validators._validate_missing_required_arguments(__arg_info_matrix)
    _Validators._validate_function_arguments(__arg_info_matrix)

    try:
        # Get the ues url for corresponding API.
        ues_url = _get_ues_url(env_name=env_name) if api_name == "remove_env" \
            else _get_ues_url(remove_all_envs=True)

        response = UtilFuncs._http_request(ues_url, HTTPRequest.DELETE,
                                           headers=_get_auth_token())

        resp = _process_ues_response(api_name=api_name, response=response)
        claim_id = resp.json().get("claim_id", "")

        # If env removal is asynchronous, then print the msg for user with
        # the claim_id. Else, poll the status using __poll_claim_id_status().
        if asynchronous:
            if is_print:
                msg = "Request to remove environment initiated successfully. " \
                      "Check the status using "
                if api_name == "remove_env":
                    msg = "{2}list_user_envs(). If environment is not removed, " \
                          "check the status of asynchronous call using" \
                          " async_run_status('{1}') or get_env('{0}').status('{1}')".\
                        format(env_name, claim_id, msg)
                else:
                    msg = "{0}async_run_status('{1}')".format(msg, claim_id)
                print(msg)
            # End of 'is_print' condition.

            # Get the description as per the API.
            desc = "Remove '{}' user environment.".format(env_name) \
                if api_name == "remove_env" else "Removing all user environments."

            _async_run_id_info[claim_id] = {"mapped_func": _async_run_status_open_af,
                                            "description": desc}
            return claim_id
        else:
            # Poll the claim_id status.
            __poll_claim_id_status(claim_id, api_name)
            msg = "User environment '{}' removed.".format(env_name) \
                if api_name == "remove_env" else \
                "All user environment(s) removed."
            print(msg)
            return True

    except Exception as exc:
        raise exc


def __poll_claim_id_status(claim_id, api_name="remove_env"):
    """
    Internal function to periodically poll and check the
    status of a claim_id.

    PARAMETERS:
        claim_id:
            Required Argument.
            Specifies the unique identifier of the asynchronous process.
            Types: str

        api_name:
            Optional Argument.
            Specifies the name of the API.
            Permitted Values: remove_env, remove_all_envs
            Default Value: remove_env
            Types: str



    RETURNS:
        None.

    RAISES:
        None.

    EXAMPLES:
        __poll_claim_id_status('cf7245f0-e962-4451-addf-efa7e123998d')
    """
    while True:
        sleep(2)

        # Poll the claim id to get the status.
        resp_data = __get_status(claim_id)

        # Breaking condition -
        # For remove_env: Check for the 'Finished' stage in the list of resp.
        # For remove_all_envs: above cond. and No user envs condition should break it .
        for data in resp_data:
            if ("Finished" in data["stage"]) or \
                    (api_name == "remove_all_envs" and "Errored" in data["stage"]):
                return


def get_env(env_name):
    """
    DESCRIPTION:
        Returns an object of class UserEnv which represents an existing remote user environment
        created in the Open Analytics Framework. The user environment can be created using
        create_env() function. This function is useful to get an object of existing user
        environment. The object returned can be used to perform further operations such as
        installing, removing files and libraries.

    PARAMETERS:
        env_name:
            Required Argument.
            Specifies the name of the existing remote user environment.
            Types: str

    RETURNS:
        An object of class UserEnv representing the remote user environment.

    RAISES:
        TeradataMlException.

    EXAMPLES:
        # List available Python environments in the Vantage.
        >>> list_base_envs()
           base_name      language  version
        0  python_3.6.11  Python   3.6.11
        1  python_3.7.9   Python   3.7.9
        2  python_3.8.5   Python   3.8.5

        # Create a Python 3.8.5 environment with given name and description in the Vantage and
        # get an object of class UserEnv.
        #
        >>> test_env = create_env('test_env', 'python_3.8.5', 'Fraud detection through time matching')
        User environment 'test_env' created.

        # In a new terdataml session, user can use get_env() function to get an object pointing to
        # existing user environment created in previous step so that further operations can be
        # performed such as install files/libraries.
        >>> test_env = get_env('test_env')
    """
    __arg_info_matrix = []
    __arg_info_matrix.append(["env_name", env_name, False, (str), True])

    # Validate arguments
    _Validators._validate_function_arguments(__arg_info_matrix)

    try:
        # Get environments created by the current logged in user.
        user_envs_df = list_user_envs()

        if env_name not in user_envs_df.env_name.values:
            msg_code = MessageCodes.FUNC_EXECUTION_FAILED
            error_msg = Messages.get_message(msg_code, "get_env()", "User environment '{}' not found."
                                                                    " Use 'create_env()' function to create"
                                                                    " user environment.".format(env_name))
            raise TeradataMlException(error_msg, msg_code)

        # Get row matching the environment name.
        userenv_row = user_envs_df[user_envs_df['env_name'] == env_name]

        if userenv_row.base_env_name.values[0] == "Unknown":
            msg_code = MessageCodes.FUNC_EXECUTION_FAILED
            error_msg = Messages.get_message(msg_code, "get_env()", "User environment '{}' is corrupted."
                                                                    " Use 'remove_env()' function to remove"
                                                                    " user environment.".format(env_name))
            raise TeradataMlException(error_msg, msg_code)

        # Return an instance of class UserEnv.
        return UserEnv(userenv_row.env_name.values[0],
                       userenv_row.base_env_name.values[0],
                       userenv_row.env_description.values[0])
    except (TeradataMlException, RuntimeError) as tdemsg:
        # TeradataMlException and RuntimeError are raised by list_user_envs.
        # list_user_envs should be replaced with get_env in the error 
        # message for final users.
        tdemsg.args = (tdemsg.args[0].replace("list_user_envs", "get_env"),)
        raise tdemsg
    except Exception as emsg:
        msg_code = MessageCodes.FUNC_EXECUTION_FAILED
        error_msg = Messages.get_message(msg_code, "get_env", emsg)
        raise TeradataMlException(error_msg, msg_code)


def remove_all_envs(env_type=None, **kwargs):
    """
        DESCRIPTION:
            Removes user environments from the Open Analytics Framework. Function allows user
            to remove only Python user environments or only R user environments or all user
            environments based on the value passed to argument "env_type".
            Note:
                * Do not execute remove_all_envs() if any of the library management functions(install_lib()
                  /uninstall_lib()/update_lib()) are being executed on any environment.

        PARAMETERS:
            env_type:
                Optional Argument.
                Specifies the type of the user environment to be removed.
                Permitted Values:
                    * 'PY' - Remove only Python user environments.
                    * 'R'  - Remove only R user environments.
                    * None - Remove all (Python and R) user environments.
                Default Value: None
                Types: str

            kwargs:
                asynchronous:
                    Optional Argument.
                    Specifies whether to remove environment synchronously or
                    asynchronously.
                    Default Value: False
                    Types: bool


        RETURNS:
            True when
                * Operation is synchronous.
                * Operation is asynchronous with "env_type".
            str otherwise.

        RAISES:
            TeradataMlException, RuntimeError.

        EXAMPLES:
            # Example 1: Remove all the Python and R user environments.
            >>> create_env('Lie_Detection_ML', 'python_3.8.13', 'Detect lie through machine learning.')
            >>> create_env('Customer_Trends', 'r_4.1.3', 'Analyse customer trends.')
            >>> list_user_envs()
                           env_name                           env_description  base_env_name language
            0   Customer_Trends                   Analyse customer trends        r_4.1.3        R
            1  Lie_Detection_ML      Detect lie through machine learning.  python_3.8.13   Python

            >>> remove_all_envs()
            All user environment(s) removed.
            True

            >>> list_user_envs()
            No user environment(s) found.


            # Example 2: Remove all the Python user environments.
            >>> create_env('Lie_Detection_ML', 'python_3.8.13', 'Detect lie through machine learning.')
            >>> create_env('Customer_Trends', 'r_4.1.3', 'Analyse customer trends.')
            >>> list_user_envs()
                          env_name                           env_description  base_env_name language
            0   Customer_Trends                   Analyse customer trends        r_4.1.3        R
            1  Lie_Detection_ML      Detect lie through machine learning.  python_3.8.13   Python

            >>> remove_all_envs(env_type="PY")
            User environment 'Lie_Detection_ML' removed.
            All Python environment(s) removed.
            True
            >>> list_user_envs()
                         env_name                           env_description  base_env_name language
            0   Customer_Trends                   Analyse customer trends        r_4.1.3        R


            # Example 3: Remove all the R user environments.
            >>> create_env('Lie_Detection_ML', 'python_3.8.13', 'Detect lie through machine learning.')
            >>> create_env('Customer_Trends', 'r_4.1.3', 'Analyse customer trends.')
            >>> list_user_envs()
                          env_name                           env_description  base_env_name language
            0   Customer_Trends                   Analyse customer trends        r_4.1.3        R
            1  Lie_Detection_ML      Detect lie through machine learning.  python_3.8.13   Python

            >>> remove_all_envs(env_type="R")
            User environment 'Customer_Trends' removed.
            All R environment(s) removed.
            True
            >>> list_user_envs()
                         env_name                           env_description  base_env_name language
            0  Lie_Detection_ML      Detect lie through machine learning.  python_3.8.13   Python


            # Example 4: Remove all Python and R environments synchronously.
            #            Note: The example first removes all R environments synchronously,
            #                  followed by Python environments.
            >>> env1 = create_env("env1", "python_3.7.13", "Environment 1")
            >>> env2 = create_env("env2", "python_3.7.13", "Environment 2")
            >>> env3 = create_env("env3", "r_4.1", "Environment 3")
            >>> env4 = create_env("env4", "r_4.1", "Environment 4")

            >>> list_user_envs()
              env_name env_description  base_env_name language
            0     env1   Environment 1  python_3.7.13   Python
            1     env2   Environment 2  python_3.7.13   Python
            2     env3   Environment 3          r_4.1        R
            3     env4   Environment 4          r_4.1        R

            # Remove all R environments.
            >>> remove_all_envs(env_type="R")
            User environment 'env3' removed.
            User environment 'env4' removed.
            All R environment(s) removed.
            True
            >>> list_user_envs()
              env_name env_description  base_env_name language
            0     env1   Environment 1  python_3.7.13   Python
            1     env2   Environment 2  python_3.7.13   Python

            # Try to remove R environments again.
            >>> remove_all_envs(env_type="R")
            No R user environment(s) found.
            True

            # Remove all remaining Python environments.
            >>> remove_all_envs()
            All user environment(s) removed.
            True


            # Example 5: Remove all Python and R environments asynchronously.
            #            Note: The example first removes all R environments asynchronously,
            #                  followed by Python environments.
            >>> env1 = create_env("env1", "python_3.7.13", "Environment 1")
            >>> env2 = create_env("env2", "python_3.7.13", "Environment 2")
            >>> env3 = create_env("env3", "r_4.1", "Environment 3")
            >>> env4 = create_env("env4", "r_4.1", "Environment 4")

            >>> list_user_envs()
              env_name env_description  base_env_name language
            0     env1   Environment 1  python_3.7.13   Python
            1     env2   Environment 2  python_3.7.13   Python
            2     env3   Environment 3          r_4.1        R
            3     env4   Environment 4          r_4.1        R

            # Remove all R environments asynchronously.
            >>> remove_all_envs(env_type="R", asynchronous=True)
            Request to remove environment initiated successfully. Check the status using async_run_status(['5c23f956-c89a-4d69-9f1e-6491bac9973f', '6ec9ecc9-9223-4d3f-92a0-9d1abc652aca'])
            True
             >>> list_user_envs()
              env_name env_description  base_env_name language
            0     env1   Environment 1  python_3.7.13   Python
            1     env2   Environment 2  python_3.7.13   Python

            # Remove all remaining Python environments asynchronously.
            >>> remove_all_envs(asynchronous=True)
            Request to remove environment initiated successfully. Check the status using async_run_status('7d86eb99-9ab3-4e0d-b4dd-8b5f1757b9c7')
            '7d86eb99-9ab3-4e0d-b4dd-8b5f1757b9c7'


            # Example 6: Remove all environments asynchronously.
            >>> env1 = create_env("env1", "python_3.7.13", "Environment 1")
            >>> env2 = create_env("env2", "python_3.7.13", "Environment 2")
            >>> env3 = create_env("env3", "r_4.1", "Environment 3")
            >>> env4 = create_env("env4", "r_4.1", "Environment 4")

            >>> list_user_envs()
              env_name env_description  base_env_name language
            0     env1   Environment 1  python_3.7.13   Python
            1     env2   Environment 2  python_3.7.13   Python
            2     env3   Environment 3          r_4.1        R
            3     env4   Environment 4          r_4.1        R

            # Remove all environments asynchronously.
            >>> remove_all_envs(asynchronous=True)
            Request to remove environment initiated successfully. Check the status using async_run_status('22f5d693-38d2-469e-b434-9f7246c7bbbb')
            '22f5d693-38d2-469e-b434-9f7246c7bbbb'
        """
    __arg_info_matrix = []
    __arg_info_matrix.append(["env_type", env_type, True, (str), True, ["PY", "R"]])

    # Validate arguments
    _Validators._validate_function_arguments(__arg_info_matrix)
    if env_type is None:
        status = __manage_envs(api_name="remove_all_envs",
                               **kwargs)
        return status
    else:
        return _remove_all_envs(env_type, **kwargs)


def _remove_all_envs(env_type, **kwargs):
    """
    DESCRIPTION:
        Internal Function removes Python or R user environments.

    PARAMETERS:
            env_type:
                Required Argument.
                Specifies the type of the user environment to be removed.
                Permitted Values:
                    * 'PY' - Remove only Python user environments.
                    * 'R' - Remove only R user environments.
                Types: str

            kwargs:
                asynchronous:
                    Optional Argument.
                    Specifies whether to remove environment synchronously or
                    asynchronously.
                    Default Value: False
                    Types: bool

                is_print:
                    Optional Argument.
                    Specifies whether to print the message or not.
                    Default Value: True
                    Types: bool


    RETURNS:
        True, if the operation is successful.

    RAISES:
        TeradataMlException, RuntimeError.

    EXAMPLES:
          >>> _remove_all_envs(env_type="PY")
              User environment 'Fraud_detection' removed.
              User environment 'Sales' removed.
              User environment 'Purchase' removed.
              All Python environment(s) removed.
          >>> _remove_all_envs(env_type="R")
              User environment 'Fraud_detection' removed.
              User environment 'Carbon_Credits' removed.
              All R environment(s) removed.
          >>> remove_all_envs(env_type="R", asynchronous=True)
              Request to remove environment initiated successfully. Check status using async_run_status(['82cd24d6-1264-49f5-81e1-76e83e09c303'])
    """
    env_type = "Python" if env_type.capitalize() == "Py" else "R"
    asynchronous = kwargs.get("asynchronous", False)

    try:
        # Retrieve all user env data.
        user_envs_df = list_user_envs()
        user_envs_lang_df = user_envs_df[user_envs_df.language == env_type] if \
            user_envs_df is not None else pd.DataFrame(index=[])

        claim_id_list = []
        if not user_envs_lang_df.empty:
            env_name = user_envs_lang_df["env_name"]
            # Executing remove_env in multiple threads (max_workers set to 10).
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                # Execute remove_env for each env_name.
                future_remove_env = {
                    executor.submit(remove_env, env,
                                    asynchronous=asynchronous, is_print=False):
                        env for env in env_name}
                # Get the result of all executions.
                failed_envs = {}
                for future in concurrent.futures.as_completed(future_remove_env):
                    env = future_remove_env[future]
                    try:
                        future_result = future.result()
                        # Populate the claim ids of all the envs that
                        # have been removed asynchronously.
                        if asynchronous:
                            claim_id_list.append(future_result)

                    except (TeradataMlException, RuntimeError, Exception) as emsg:
                        # Catching exceptions by remove_env if occured in any thread.
                        failed_envs[env] = emsg

            # Negative case - Failed to remove env.
            if len(failed_envs) > 0:
                emsg = ""
                for env, tdemsg in failed_envs.items():
                    emsg += "\nUser environment '{0}' failed to remove. Reason: {1}"\
                        .format(env, tdemsg.args[0])
                msg_code = MessageCodes.FUNC_EXECUTION_FAILED
                error_msg = Messages.get_message(msg_code, "remove_all_envs()", emsg)
                raise TeradataMlException(error_msg, msg_code)

            # Positive case - Envs removed without any failure print msg
            # as per sync or async removal.
            if not asynchronous:
                msg = "All {} environment(s) removed.".format(env_type)
            else:
                msg = "Request to remove environment initiated successfully. Check " \
                      "the status using " \
                      "async_run_status(['" + "', '".join(claim_id_list) + "'])"
            print(msg)
        elif user_envs_lang_df.empty and user_envs_df is not None:
            print("No {} user environment(s) found.".format(env_type))
        return True
    except (TeradataMlException, RuntimeError) as tdemsg:
        # TeradataMlException and RuntimeError are raised by list_user_envs.
        # list_user_envs should be replaced with remove_all_envs in the error 
        # message for final users.
        tdemsg.args = (tdemsg.args[0].replace("list_user_envs", "remove_all_envs"),)
        raise tdemsg
    except Exception as emsg:
        msg_code = MessageCodes.FUNC_EXECUTION_FAILED
        error_msg = Messages.get_message(msg_code, "remove_all_envs", emsg)
        raise TeradataMlException(error_msg, msg_code)


def set_user_env(env):
    """
    DESCRIPTION:
        Function allows to set the default user environment to be used for the Apply()
        and DataFrame.apply() function execution.

    PARAMETERS:
        env:
            Required Argument.
            Specifies the remote user environment name to set as default for the session.
            Types: str OR Object of UserEnv

    RETURNS:
        True, if the operation is successful.

    RAISES:
        TeradataMlException, RuntimeError.

    EXAMPLES:
        # Create remote user environment.
        >>> env = create_env('testenv', 'python_3.7.9', 'Test environment')
        User environment 'testenv' created.

        # Example 1: Set the environment 'testenv' as default environment.
        >>> set_user_env('testenv')
        Default environment is set to 'testenv'.
        >>>

        # Example 2: Create an environment with name 'demo_env' and set it as default environment.
        >>> set_user_env(get_env('test_env'))
        User environment 'testenv' created.
        Default environment is set to 'testenv'.
        >>>
    """
    __arg_info_matrix = []
    __arg_info_matrix.append(["env", env, False, (str, UserEnv), True])

    # Validate arguments
    _Validators._validate_function_arguments(__arg_info_matrix)

    # Get the environment name.
    env = get_env(env_name=env) if isinstance(env, str) else env

    configure._default_user_env = env
    print("Default environment is set to '{}'.".format(env.env_name))

    return True


def get_user_env():
    """
    DESCRIPTION:
        Function to get the default user environment set for the session.

    PARAMETERS:
        None.

    RETURNS:
        An object of UserEnv, if the operation is successful.

    RAISES:
        TeradataMlException, RuntimeError.

    EXAMPLES:
        # Create remote user environment.
        >>> env = create_env('testenv', 'python_3.7.9', 'Test environment')
        User environment 'testenv' created.
        >>> set_user_env('testenv')
        Default environment is set to 'testenv'.
        >>>

        # Example 1: Get the default environment.
        >>> env = get_user_env()
    """
    if configure._default_user_env is None:
        print("Default environment is not set. Set default environment using set_user_env().")
        return

    return configure._default_user_env


def set_auth_token(ues_url, client_id=None):
    """
    DESCRIPTION:
        Function to set the Authentication token to connect to User Environment Service
        in VantageCloud Lake.
        Note:
            User must have a privilage to login with a NULL password to use set_auth_token().
            Please refer to GRANT LOGON section in Teradata Documentation for more details.


    PARAMETERS:
        ues_url:
            Required Argument.
            Specifies the URL for User Environment Service in VantageCloud Lake.
            Types: str

        client_id:
            Optional Argument.
            Specifies the id of the application that requests the access token from
            VantageCloud Lake.
            Types: str


    RETURNS:
        True, if the operation is successful.

    RAISES:
        TeradataMlException, RuntimeError.

    EXAMPLES:

        # Example 1: Set the Authentication token using default client_id.
        >>> import getpass
        >>> set_auth_token(ues_url=getpass.getpass("ues_url : "))

        # Example 2: Set the Authentication token by specifying the client_id.
        >>> set_auth_token(ues_url=getpass.getpass("ues_url : "),
        ...                client_id=getpass.getpass("client_id : "))
    """
    __arg_info_matrix = []
    __arg_info_matrix.append(["ues_url", ues_url, False, (str), True])
    __arg_info_matrix.append(["client_id", client_id, True, (str), True])

    # Validate arguments.
    _Validators._validate_function_arguments(__arg_info_matrix)

    # Extract the base URL from "ues_url".
    url_parser = urlparse(ues_url)
    base_url = "{}://{}".format(url_parser.scheme, url_parser.netloc)

    if client_id is None:
        netloc = url_parser.netloc
        client_id = "tdpub-" + netloc.split('.')[0]

    da_wf = _DAWorkflow(base_url, client_id)
    token_data = da_wf._get_token_data()

    # Set Open AF parameters.
    configure._oauth_client_id = client_id
    configure.ues_url = ues_url
    configure._oauth_end_point = da_wf.device_auth_end_point
    configure._auth_token_expiry_time = time() + token_data["expires_in"] - 15
    # Store the jwt token in internal class attribute.
    _InternalBuffer.add(auth_token=_AuthToken(token=token_data["access_token"]))

    return True
