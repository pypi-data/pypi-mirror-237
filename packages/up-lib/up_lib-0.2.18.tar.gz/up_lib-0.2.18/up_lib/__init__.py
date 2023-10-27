import pluggy
from typing import TypeAlias
from .containers import RunConfig, RunConfigs
from .plugins import match_prompt

Context:TypeAlias = dict[str, str]
Prompt:TypeAlias = list[str]

hookimpl = pluggy.HookimplMarker("up")
pm = pluggy.PluginManager("up")

