from enum import Enum
from typing import Dict, List, Optional

class Provider(Enum):
    AWS = "Amazon Web Services"
    ANTHROPIC = "Anthropic"
    # OPENAI = "OpenAI"

class ModelName(Enum):
    CLAUDE_3_OPUS = "Claude 3 Opus"
    CLAUDE_3_7_SONNET = "Claude 3.7 Sonnet"
    CLAUDE_3_5_SONNET_V2 = "Claude 3.5 Sonnet V2"
    CLAUDE_3_5_SONNET = "Claude 3.5 Sonnet"
    CLAUDE_3_SONNET = "Claude 3 Sonnet"
    CLAUDE_3_5_HAIKU = "Claude 3.5 Haiku"
    CLAUDE_3_HAIKU = "Claude 3 Haiku"
    # GPT_4O = "GPT 4o"
    # GPT_4O_MINI = "GPT 4o mini"

# Define the model mappings as a constant
MODEL_MAPPINGS: Dict[str, Dict[str, str]] = {
    Provider.AWS.value: {
        ModelName.CLAUDE_3_OPUS.value: "us.anthropic.claude-3-opus-20240229-v1:0",
        ModelName.CLAUDE_3_7_SONNET.value: "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        ModelName.CLAUDE_3_5_SONNET_V2.value: "us.anthropic.claude-3-5-sonnet-20241022-v2:0",
        ModelName.CLAUDE_3_5_SONNET.value: "us.anthropic.claude-3-5-sonnet-20240620-v1:0",
        ModelName.CLAUDE_3_SONNET.value: "us.anthropic.claude-3-sonnet-20240229-v1:0",
        ModelName.CLAUDE_3_5_HAIKU.value: "us.anthropic.claude-3-5-haiku-20241022-v1:0",
        ModelName.CLAUDE_3_HAIKU.value: "us.anthropic.claude-3-haiku-20240307-v1:0"
    },
    Provider.ANTHROPIC.value: {
        ModelName.CLAUDE_3_OPUS.value: "claude-3-opus-20240229",
        ModelName.CLAUDE_3_7_SONNET.value: "claude-3-7-sonnet-20250219",
        ModelName.CLAUDE_3_5_SONNET_V2.value: "claude-3-5-sonnet-20241022",
        ModelName.CLAUDE_3_5_SONNET.value: "claude-3-5-sonnet-20240620",
        ModelName.CLAUDE_3_SONNET.value: "claude-3-sonnet-20240229",
        ModelName.CLAUDE_3_5_HAIKU.value: "claude-3-5-haiku-20241022",
        ModelName.CLAUDE_3_HAIKU.value: "claude-3-haiku-20240307"
    }
}

# String-based validation and lookup
def validate_provider(provider_name: str) -> bool:
    """Validate if the provider name is valid."""
    return provider_name in MODEL_MAPPINGS

def validate_model_for_provider(provider_name: str, model_name: str) -> bool:
    """Validate if the model name is valid for the given provider."""
    return provider_name in MODEL_MAPPINGS and model_name in MODEL_MAPPINGS[provider_name]

def get_all_provider_names() -> List[str]:
    """Get all provider display names."""
    return [provider.value for provider in Provider]

def get_models_for_provider_name(provider_name: str) -> List[str]:
    """Get all model display names for a given provider name."""
    if provider_name in MODEL_MAPPINGS:
        return list(MODEL_MAPPINGS[provider_name].keys())
    return []

def get_api_name_from_strings(provider_name: str, model_name: str) -> Optional[str]:
    """Get API name using string values."""
    if validate_model_for_provider(provider_name, model_name):
        return MODEL_MAPPINGS[provider_name][model_name]
    return None