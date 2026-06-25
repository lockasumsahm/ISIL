from app.adapters.base import AdapterResult, BaseAdapter
from app.adapters.huggingface import HuggingFaceAdapter
from app.adapters.mock import (
    MockHuggingFaceAdapter,
    MockOpenAIAdapter,
    MockPerspectiveAdapter,
)
from app.adapters.openai_adapter import OpenAIAdapter
from app.adapters.perspective import PerspectiveAdapter
from app.config import Settings, get_settings


def build_adapters(settings: Settings | None = None) -> list[BaseAdapter]:
    settings = settings or get_settings()
    adapters: list[BaseAdapter] = []
    use_mock = settings.use_mock_adapters_when_no_keys

    if settings.has_perspective():
        adapters.append(PerspectiveAdapter())
    elif use_mock:
        adapters.append(MockPerspectiveAdapter())

    if settings.has_openai():
        adapters.append(OpenAIAdapter())
    elif use_mock:
        adapters.append(MockOpenAIAdapter())

    if settings.has_huggingface():
        adapters.append(HuggingFaceAdapter())
    elif use_mock:
        adapters.append(MockHuggingFaceAdapter())

    if not adapters:
        adapters = [
            MockPerspectiveAdapter(),
            MockOpenAIAdapter(),
            MockHuggingFaceAdapter(),
        ]

    return adapters
