from johnsnowlabs import try_import_lib

if try_import_lib("haystack"):
    from johnsnowlabs.frameworks.embedding_retrival.haystack_node import (
        JohnSnowLabsHaystackEmbedder,
    )

if try_import_lib("langchain"):
    from johnsnowlabs.frameworks.embedding_retrival.langchain_node import (
        JohnSnowLabsLangChainEmbedder,
    )
