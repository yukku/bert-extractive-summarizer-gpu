from setuptools import setup
from setuptools import find_packages

setup(
    name="bert-extractive-summarizer",
    version="0.4.0",
    description="Extractive Text Summarization with BERT",
    keywords=[
        "bert",
        "pytorch",
        "machine learning",
        "deep learning",
        "extractive summarization",
        "summary",
    ],
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yukku/bert-extractive-summarizer-gpu",
    download_url="https://codeload.github.com/yukku/bert-extractive-summarizer-gpu/zip/master",
    author="Derek Miller",
    author_email="yukikumagai@gmail.com",
    install_requires=["transformers", "scikit-learn", "spacy"],
    license="MIT",
    packages=find_packages(),
    zip_safe=False,
)
