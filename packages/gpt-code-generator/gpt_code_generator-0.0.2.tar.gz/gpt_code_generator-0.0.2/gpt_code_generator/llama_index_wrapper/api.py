import sys
from typing import List

from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from llama_index import (
    Document,
    LangchainEmbedding,
    LLMPredictor,
    ServiceContext,
    StorageContext,
    load_index_from_storage,
)
from llama_index.indices.vector_store import GPTVectorStoreIndex
from llama_index.storage.docstore import SimpleDocumentStore
from llama_index.storage.index_store import SimpleIndexStore
from llama_index.vector_stores import SimpleVectorStore

from ..args.env import Env


class Api:
    def __init__(self, env: Env):
        self.env = env

    def get_service_context(self) -> ServiceContext:
        llm = AzureChatOpenAI(
            temperature=0,
            deployment_name=self.env.azure_open_ai_model_deploy_name,
            model=self.env.azure_open_ai_model_name,
            openai_api_base=self.env.azure_open_ai_endpoint,
            openai_api_key=self.env.azure_open_ai_key,
            openai_api_type="azure",
            openai_api_version=self.env.azure_open_ai_version,
        )
        llm_predictor = LLMPredictor(llm=llm)

        embedding_llm = LangchainEmbedding(
            OpenAIEmbeddings(
                model=self.env.azure_open_ai_embedding_model_name,
                deployment=self.env.azure_open_ai_embedding_model_deploy_name,
                openai_api_base=self.env.azure_open_ai_endpoint,
                openai_api_key=self.env.azure_open_ai_key,
                openai_api_type="azure",
                openai_api_version=self.env.azure_open_ai_version,
            ),
            embed_batch_size=1,
        )
        return ServiceContext.from_defaults(
            llm_predictor=llm_predictor,
            embed_model=embedding_llm,
        )

    def save_documents(self, documents: List[Document]) -> None:
        service_context = self.get_service_context()
        storage_context = StorageContext.from_defaults(
            docstore=SimpleDocumentStore(),
            vector_store=SimpleVectorStore(),
            index_store=SimpleIndexStore(),
        )

        index = GPTVectorStoreIndex.from_documents(
            documents=documents,
            service_context=service_context,
            storage_context=storage_context,
        )
        index.storage_context.persist(persist_dir=self.env.storage_context_tmp_dir)

    def ask(self, query: str) -> None:
        print("query: \n" + query, file=sys.stderr)
        service_context = self.get_service_context()
        storage_context = StorageContext.from_defaults(
            docstore=SimpleDocumentStore.from_persist_dir(
                persist_dir=self.env.storage_context_tmp_dir
            ),
            vector_store=SimpleVectorStore.from_persist_dir(
                persist_dir=self.env.storage_context_tmp_dir
            ),
            index_store=SimpleIndexStore.from_persist_dir(
                persist_dir=self.env.storage_context_tmp_dir
            ),
        )
        index = load_index_from_storage(
            service_context=service_context,
            storage_context=storage_context,
        )

        qe = index.as_query_engine()
        response = qe.query(query)

        print(response)
