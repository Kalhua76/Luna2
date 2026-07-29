from luna.ai.ollama_provider import OllamaProvider

def test_provider_defaults():
    p=OllamaProvider()
    assert p.name=="ollama"
    assert p.model=="llama3"
