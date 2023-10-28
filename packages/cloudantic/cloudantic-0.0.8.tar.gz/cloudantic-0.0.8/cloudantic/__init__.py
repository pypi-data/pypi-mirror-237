from aiohttp.web import HTTPFound, Request, Response

from .router import (APIRouter, APIServer, EventSourceResponse, StreamResponse,
                     WebSocketResponse, component, stream_html)
from .schema import DynamoDBStreams, DynaModel, Field
from .services import (Agent, APIClient, Audio, ChatCompletion, Completion,
                       Embeddings, Image, KinesisStream, StorageBucket,
                       VectorClient)

__title__ = "Cloudantic"
__version__ = "0.0.8"
__author__ = "Oscar Bahamonde <o.bahamonde@globant.com>"
__description__ = "Aiohttps + AWS (DynamoDB, Kinesis, S3, Dynamo Streams)"
