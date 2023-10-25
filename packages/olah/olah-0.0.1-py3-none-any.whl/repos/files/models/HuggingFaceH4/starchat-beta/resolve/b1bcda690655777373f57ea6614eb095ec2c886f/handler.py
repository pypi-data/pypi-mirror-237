from typing import Any, Dict

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from peft import PeftConfig, PeftModel


class EndpointHandler:
    def __init__(self, path=""):
        # load model and processor from path
        self.tokenizer = AutoTokenizer.from_pretrained(path)
        try:
            config = PeftConfig.from_pretrained(path)
            model = AutoModelForCausalLM.from_pretrained(
                config.base_model_name_or_path,
                return_dict=True,
                load_in_8bit=True,
                device_map="auto",
                torch_dtype=torch.float16,
                trust_remote_code=True,
            )
            model.resize_token_embeddings(len(self.tokenizer))
            model = PeftModel.from_pretrained(model, path)
        except Exception:
            model = AutoModelForCausalLM.from_pretrained(
                path, device_map="auto", load_in_8bit=True, torch_dtype=torch.float16, trust_remote_code=True
            )
        self.model = model
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def __call__(self, data: Dict[str, Any]) -> Dict[str, str]:
        # process input
        inputs = data.pop("inputs", data)
        parameters = data.pop("parameters", None)

        # preprocess
        inputs = self.tokenizer(inputs, return_tensors="pt").to(self.device)

        # pass inputs with all kwargs in data
        if parameters is not None:
            outputs = self.model.generate(**inputs, **parameters)
        else:
            outputs = self.model.generate(**inputs)

        # postprocess the prediction
        prediction = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return [{"generated_text": prediction}]
