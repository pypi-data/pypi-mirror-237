# LLM API for python

This python library connects to [llm-api](https://github.com/1b5d/llm-api) using python, it was build to mimic [OpenAI's python library](https://github.com/openai/openai-python)

# Usage

You can install this library using pip

```
pip install llm-api-python
```

After running [llm-api](https://github.com/1b5d/llm-api), simply configure your client as if it's OpenAI's python binding

```python
import llm_api

llm_api.api_key = "<your llm-api api key here>"

completion = llm_api.ChatCompletion.create(messages=[
    {
        "role": "system", 
        "content": "You are a helpful assistant, please answer the users' questions with honesty and accuracy."
    }, {
        "role": "user", "content": "What is the capital of France?"
    }
])  # returns a chat completion object

completion = llm_api.ChatCompletion.create(messages=[
    ...
], stream=True) # returns a generator

completion = await llm_api.ChatCompletion.acreate(messages=[
    ...
]) # returns a chat completion object

completion = await llm_api.ChatCompletion.acreate(messages=[
    ...
], stream=True) # returns a async generator

```

# Limitations

- `request_id` and `request_ms` are currently returned empty
- `created` timestamp is not set by the server
- `finish_reason` is hardcoded to `stop`
- `usage` values are set to `None`
- the `model` attribute is not being used

# Credit

OpenAI's python implementation since this implementation is technically a fork of it.
