import vbml
import re
from typing import (
    Iterable,
    Optional,
    Union,
)

from vkbottle.dispatch.rules import ABCRule
from vkbottle.bot import Message

class AsyaCommandRule(ABCRule[Message]):
    def __init__(
        self,
        prefixes: list,
        pattern: Union[str, Iterable[str]],
        patcher: Optional["vbml.Patcher"] = None,
        flags: Optional[re.RegexFlag] = None,
    ):
        flags = flags or self.config.get("vbml_flags") or re.DOTALL

        if isinstance(pattern, str):
            pattern = [vbml.Pattern(pattern, flags=flags or self.config.get("vbml_flags"))]
        elif isinstance(pattern, Iterable):
            pattern = [
                p if isinstance(p, vbml.Pattern) else vbml.Pattern(p, flags=flags) for p in pattern
            ]

        self.prefixes = prefixes
        self.patterns = pattern
        self.patcher = patcher or self.config.get("vbml_patcher") or vbml.Patcher()
    
    async def check(self, event: Message) -> Union[Optional[dict], bool]:
        for prefix in self.prefixes:
            if event.text.startswith(prefix):
                break
        else:
            return False
        for pattern in self.patterns:
            result = self.patcher.check(pattern, event.text.lstrip(prefix))
            if result not in (None, False):
                return result
        return False