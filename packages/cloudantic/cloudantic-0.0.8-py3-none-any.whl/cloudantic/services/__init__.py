from .apiclient import APIClient
from .functions import *
from .kinesis import KinesisStream
from .openai import *
from .storage import StorageBucket


class Agent(BaseModel):
	chat_completion: ChatCompletion = Field(default_factory=ChatCompletion)
	completion: Completion = Field(default_factory=Completion)
	embeddings: Embeddings = Field(default_factory=Embeddings)
	audio: Audio = Field(default_factory=Audio)
	image: Image = Field(default_factory=Image)
	vector:VectorClient = Field(default_factory=VectorClient)

