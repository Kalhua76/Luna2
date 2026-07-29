from luna.ai.prompt_manager import PromptManager, PromptContext

def test_build_prompt():
    pm=PromptManager()
    ctx=PromptContext(system_prompt="SYS",history=["A","B"],user_input="Hello")
    prompt=pm.build(ctx)
    assert "SYS" in prompt and "Hello" in prompt
