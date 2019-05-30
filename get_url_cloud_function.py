import logging
import json
import os
import settings
import boto3
from boto3.dynamodb.conditions import Key, Attr

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_item(cnpj : str = None, nome_fantasia : str = None):

    table: str = os.getenv('DYNAMODB_TABLE')
    print(table)
    dynamodb = boto3.resource(
        'dynamodb',
        aws_access_key_id=os.getenv('ACCESS_TOKEN'),
        aws_secret_access_key=os.getenv('SECRET_ACCESS_TOKEN'),
        region_name=os.getenv('REGION')
    )

    db = dynamodb.Table(table)

    if nome_fantasia is not None and cnpj is not None:
        rs = db.scan(
                Select='ALL_ATTRIBUTES',
                FilterExpression=Attr('cnpj').begins_with(cnpj) | Attr('nome_fantasia').begins_with(nome_fantasia)
            )
    elif nome_fantasia is not None and cnpj is None:
        rs = db.scan(
                Select='ALL_ATTRIBUTES',
                FilterExpression=Attr('nome_fantasia').begins_with(nome_fantasia)
            )
    elif nome_fantasia is None and cnpj is not None:
        rs = db.scan(
                Select='ALL_ATTRIBUTES',
                FilterExpression=Attr('cnpj').begins_with(cnpj)
            )

    else:
        raise Exception('Informe um cnpj ou nome_fantasia')

    if 'Items' in rs:
        return json.dumps(rs['Items'])
    else:
        return json.dumps([])

from swfastwork import cloud_function

def get_url_cloud_function(request, context):

   request, context = cloud_function.start(request, context)

   print(request)

   url = 'http://google.com/'

   return cloud_function.end({
       'url' : url
   })

