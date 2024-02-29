from setuptools import setup, find_packages

setup(
    name="lyzr-rag",
    version="0.1.1",
    author="Lyzr",
    author_email="contact@lyzr.ai",
    description="Lyzr Core",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://lyzr.ai",
    project_urls={
        "Documentation": "https://docs.lyzr.ai/",
        "Source": "https://github.com/LyzrCore/lyzr_rag",
    },
    packages=find_packages(include=["lyzr_rag"]),
    python_requires=">=3.8.1,<4.0",
    install_requires=[
        "SQLAlchemy[asyncio]>=1.4.49",
        "dataclasses-json",
        "deprecated>=1.2.9.3",
        "fsspec>=2023.5.0",
        "httpx",
        "langchain>=0.0.303; extra == 'langchain'",
        "nest-asyncio==1.5.8",
        "nltk==3.8.1",
        "numpy",
        "openai>=1.1.0",
        "pandas",
        "tenacity>=8.2.0,<9.0.0",
        "tiktoken>=0.3.3",
        "typing-extensions>=4.5.0",
        "typing-inspect>=0.8.0",
        "requests>=2.31.0",  # Pin to avoid CVE-2023-32681 in requests 2.3 to 2.30
        "gradientai>=1.4.0; extra == 'gradientai'",
        "asyncpg==0.28.0; extra == 'postgres'",
        "pgvector==0.1.0; extra == 'postgres'",
        "optimum[onnxruntime]==1.13.2; extra == 'local_models'",
        "sentencepiece==0.1.99; extra == 'local_models'",
        "transformers[torch]==4.33.1; extra == 'local_models'",
        "guidance==0.0.64; extra == 'query_tools'",
        "lm-format-enforcer==0.4.3; extra == 'query_tools'",
        "jsonpath-ng==1.6.0; extra == 'query_tools'",
        "rank-bm25==0.2.2; extra == 'query_tools'",
        "scikit-learn; extra == 'query_tools'",
        "spacy==3.7.1; extra == 'query_tools'",
        "aiohttp==3.8.6",
        "networkx>=3.0",
        "psycopg2-binary==2.9.9; extra == 'postgres'",
        "dirtyjson==1.0.8",
    ],
    license="MIT",
    include_package_data=True,
)
