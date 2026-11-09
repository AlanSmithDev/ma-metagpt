#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/1/8 17:03
@Author  : alexanderwu
@File    : mock_llm_config.py
"""

from metagpt.configs.llm_config import LLMConfig

mock_llm_config = LLMConfig(
    llm_type="mock",
    <REDACTED_SECRET>,
    base_url="mock_base_url",
    app_id="mock_app_id",
    api_<REDACTED_SECRET>,
    domain="mock_domain",
    model="mock_model",
)


mock_llm_config_proxy = LLMConfig(
    llm_type="mock",
    <REDACTED_SECRET>,
    base_url="mock_base_url",
    proxy="http://localhost:8080",
)


mock_llm_config_azure = LLMConfig(
    llm_type="azure",
    api_version="2023-09-01-preview",
    <REDACTED_SECRET>,
    base_url="mock_base_url",
    proxy="http://localhost:8080",
)


mock_llm_config_zhipu = LLMConfig(
    llm_type="zhipu",
    <REDACTED_SECRET>,
    base_url="mock_base_url",
    model="mock_zhipu_model",
    proxy="http://localhost:8080",
)


mock_llm_config_spark = LLMConfig(
    api_type="spark",
    app_id="xxx",
    api_key="xxx",
    api_secret="xxx",
    domain="generalv2",
    base_url="wss://spark-api.xf-yun.com/v3.1/chat",
)

mock_llm_config_qianfan = LLMConfig(api_type="qianfan", access_key="xxx", secret_key="xxx", model="ERNIE-Bot-turbo")

mock_llm_config_dashscope = LLMConfig(api_type="dashscope", api_key="xxx", model="qwen-max")

mock_llm_config_anthropic = LLMConfig(
    api_type="anthropic", api_key="xxx", base_url="https://api.anthropic.com", model="claude-3-opus-20240229"
)

mock_llm_config_bedrock = LLMConfig(
    api_type="bedrock",
    model="gpt-100",
    region_name="somewhere",
    <REDACTED_SECRET>,
    secret_key="123abc",
    max_token=10000,
)

mock_llm_config_ark = LLMConfig(api_type="ark", <REDACTED_SECRET>, base_url="xxx", model="ep-xxx")
