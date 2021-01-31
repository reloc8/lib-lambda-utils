import boto3
import json

from typing import Dict, Any, AnyStr


def invoke_lambda(payload: Dict[AnyStr, Any], lambda_name: AnyStr) -> bool:
    """Invokes a Lambda asynchronously with a payload

    Data must be serializable.

    :param payload:     Data to send
    :param lambda_name: Name of the Lambda to invoke
    :return:            True if data was sent
    """

    status_code = boto3.client('lambda').invoke(
        FunctionName=lambda_name,
        InvocationType='Event',
        Payload=json.dumps(payload).encode('utf-8')
    ).get('StatusCode')

    return 200 <= status_code <= 208
