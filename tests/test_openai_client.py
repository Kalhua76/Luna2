from luna.ai.openai_client import OpenAIClient, OpenAIConfig

def test_client_config():
    c=OpenAIClient(OpenAIConfig(api_key="test"))
    assert c.config.model=="gpt-5"
