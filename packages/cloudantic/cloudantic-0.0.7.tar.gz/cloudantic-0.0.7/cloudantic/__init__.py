from aiohttp.web import HTTPFound, Request, Response

from .router import (APIRouter, APIServer, EventSourceResponse, StreamResponse,
                     WebSocketResponse)
from .schema import DynamoDBStreams, DynaModel, Field
from .services import APIClient, KinesisStream, StorageBucket

__title__ = "Cloudantic"
__version__ = "0.0.7s"
__author__ = "Oscar Bahamonde <o.bahamonde@globant.com>"
__description__ = "Aiohttps + AWS (DynamoDB, Kinesis, S3, Dynamo Streams)"
