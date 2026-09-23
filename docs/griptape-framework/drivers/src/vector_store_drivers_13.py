import os

from griptape.artifacts import TextArtifact
from griptape.drivers.embedding.openai import OpenAiEmbeddingDriver
from griptape.drivers.vector.local import LocalVectorStoreDriver

# Initialize an Embedding Driver
embedding_driver = OpenAiEmbeddingDriver(api_key=os.environ["OPENAI_API_KEY"])

vector_store_driver = LocalVectorStoreDriver(embedding_driver=embedding_driver)

# Insert a value with an automatically generated ID
vector_store_driver.insert("Griptape is an enterprise AI framework.")

# Insert a collection of Artifacts with automatically generated IDs
vector_ids = vector_store_driver.insert_collection(
    [
        TextArtifact("Griptape provides abstractions for working with LLMs."),
        TextArtifact("Griptape supports retrieval-augmented generation."),
    ]
)

print(f"Inserted {len(vector_ids) + 1} entries.")
