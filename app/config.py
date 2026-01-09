
import os


class Settings:
    """
    Centralized application configuration.

    All environment variables are read here to avoid
    scattered configuration access across the codebase.
    """

    # Environment
    ENV: str = os.getenv("ENV", "development")

    # LLM Providers
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

    # Observability
    LANGFUSE_PUBLIC_KEY: str = os.getenv("LANGFUSE_PUBLIC_KEY", "")
    LANGFUSE_SECRET_KEY: str = os.getenv("LANGFUSE_SECRET_KEY", "")

    # Notifications
    SLACK_WEBHOOK_URL: str = os.getenv("SLACK_WEBHOOK_URL", "")

    @classmethod
    def validate(cls) -> None:
        """
        Fail fast if required configuration is missing.
        """
        required = [
            cls.OPENAI_API_KEY,
            cls.DATABASE_URL
        ]

        if not all(required):
            raise EnvironmentError(
                "Missing required environment variables. "
                "Check configuration before starting the service."
            )
