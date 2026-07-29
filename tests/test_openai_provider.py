from luna.ai.openai_provider import OpenAIProvider

def test_provider_metadata():
    provider=OpenAIProvider()
    assert provider.name=="openai"
    assert provider.model=="gpt-5"
