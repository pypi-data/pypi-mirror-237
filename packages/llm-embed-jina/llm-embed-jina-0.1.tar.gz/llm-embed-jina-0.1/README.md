# llm-embed-jina

[![PyPI](https://img.shields.io/pypi/v/llm-embed-jina.svg)](https://pypi.org/project/llm-embed-jina/)
[![Changelog](https://img.shields.io/github/v/release/simonw/llm-embed-jina?include_prereleases&label=changelog)](https://github.com/simonw/llm-embed-jina/releases)
[![Tests](https://github.com/simonw/llm-embed-jina/workflows/Test/badge.svg)](https://github.com/simonw/llm-embed-jina/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/llm-embed-jina/blob/main/LICENSE)

Embedding models from Jina AI

## Background

[Jina AI Launches World's First Open-Source 8K Text Embedding, Rivaling OpenAI](https://jina.ai/news/jina-ai-launches-worlds-first-open-source-8k-text-embedding-rivaling-openai/) introduces these models.

See also [Embeddings: What they are and why they matter](https://simonwillison.net/2023/Oct/23/embeddings/) for background on embeddings and an explanation of the LLM embeddings tool.

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).

    llm install llm-embed-jina

## Usage

This plugin adds support for three new embedding models:

- [`jina-embeddings-v2-small-en`](https://huggingface.co/jinaai/jina-embeddings-v2-small-en): 33 million parameters.
- [`jina-embeddings-v2-base-en`](https://huggingface.co/jinaai/jina-embeddings-v2-base-en): 137 million parameters.
- [`jina-embeddings-v2-large-en`](https://huggingface.co/jinaai/jina-embeddings-v2-large-en): 435 million parameters - not yet released, but it will work once it has been released.

The models will be downloaded the first time you try to use them.

See [the LLM documentation](https://llm.datasette.io/en/stable/embeddings/index.html) for everything you can do.

To get started embedding a single string, run the following:

```bash
llm embed -m jina-embeddings-v2-small-en -c 'Hello world'
```
This will output a JSON array of 512 floating point numbers to your terminal.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-embed-jina
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
pytest
```
