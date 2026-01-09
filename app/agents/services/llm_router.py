class LLMRouter:
    """
    Routes requests across LLM providers
    based on cost, latency, and confidence policies.
    """

    def select_model(self, context):
        raise NotImplementedError
