"""A module for interfacing with the OpenAI API"""
import logging

from sciphi.interface.base import LLMInterface, LLMProviderName, ModelName
from sciphi.interface.llm_interface_manager import llm_interface
from sciphi.llm import OpenAIConfig, OpenAILLM

logger = logging.getLogger(__name__)


@llm_interface
class OpenAILLMInterface(LLMInterface):
    """A class to interface with the OpenAI API."""

    instruct_models = [
        ModelName.GPT_3p5_TURBO_INSTRUCT,
    ]
    llm_provider_name = LLMProviderName.OPENAI
    supported_models = [
        ModelName.GPT_3p5_TURBO_0301,
        ModelName.GPT_3p5_TURBO_0613,
        ModelName.GPT_3p5_TURBO,
        ModelName.GPT_3p5_TURBO_INSTRUCT,
        ModelName.GPT_3p5_TURBO_16k_0613,
        ModelName.GPT_4_0314,
        ModelName.GPT_4_0613,
        ModelName.GPT_4,
        ModelName.GPT_4_32k,
    ]
    system_message = "You are a helpful assistant."

    def __init__(
        self,
        config: OpenAIConfig,
    ) -> None:
        self.config = config
        self._model = OpenAILLM(config)

    def get_completion(self, prompt: str) -> str:
        """Get a completion from the OpenAI API based on the provided prompt."""

        logger.debug(
            f"Getting completion from OpenAI API for model={self.config.model_name}"
        )
        if ModelName(self.config.model_name) in self.instruct_models:
            return self.model.get_instruct_completion(prompt)
        else:
            return self._model.get_chat_completion(
                [
                    {
                        "role": "system",
                        "content": OpenAILLMInterface.system_message,
                    },
                    {"role": "user", "content": prompt},
                ]
            )

    @property
    def model(self) -> OpenAILLM:
        return self._model
