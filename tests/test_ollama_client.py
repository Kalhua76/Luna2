from luna.ai.ollama_client import OllamaClient,OllamaConfig

def test_client():
    c=OllamaClient(OllamaConfig())
    assert c.config.model=="llama3"
