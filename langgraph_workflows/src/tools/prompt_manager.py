import os
import yaml
from typing import Any, Dict, List, Optional
from jinja2 import Template
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

class PromptManager:
    def __init__(self, agent_name: str, config_dir: str = "src/prompts"):
        self.agent_name = agent_name
        self.config_path = os.path.join(config_dir, f"{agent_name}.yaml")
        self.config = self._load_config()
        
    def _load_config(self) -> Dict[str, Any]:
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        with open(self.config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def get_llm(self, model_override: Optional[str] = None):
        selected_model = model_override or self.config.get("selected_model")
        model_config = self.config.get("models", {}).get(selected_model)
        
        if not model_config:
            raise ValueError(f"Model configuration for '{selected_model}' not found in {self.agent_name}.yaml")
            
        provider = model_config.get("provider", "ollama").lower()
        temperature = model_config.get("temperature", 0.7)
        base_url = model_config.get("base_url")
        timeout = model_config.get("timeout", 120)  # Default to 120s
        num_ctx = model_config.get("num_ctx")

        if provider == "ollama":
            kwargs = {
                "model": selected_model, 
                "temperature": temperature,
                "timeout": timeout,
            }
            if base_url:
                kwargs["base_url"] = base_url
            if num_ctx:
                kwargs["num_ctx"] = num_ctx
                
            return ChatOllama(**kwargs)
        elif provider == "google":
            kwargs = {"model": selected_model, "temperature": temperature}
            return ChatGoogleGenerativeAI(**kwargs)
        else:
            raise ValueError(f"Unsupported provider: {provider}")

    def render_prompts(self, state: Dict[str, Any], model_override: Optional[str] = None) -> List[Any]:
        selected_model = model_override or self.config.get("selected_model")
        model_config = self.config.get("models", {}).get(selected_model)
        
        if not model_config:
            raise ValueError(f"Model configuration for '{selected_model}' not found in {self.agent_name}.yaml")

        system_template = model_config.get("system_prompt", "")
        user_template = model_config.get("user_prompt_template", "")

        system_content = Template(system_template).render(**state)
        user_content = Template(user_template).render(**state)

        return [
            SystemMessage(content=system_content),
            HumanMessage(content=user_content)
        ]

    def get_model_name(self) -> str:
        return self.config.get("selected_model", "unknown")
