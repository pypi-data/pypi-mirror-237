import typing


StepTasksType = typing.Tuple[int, ...]
StepTaskNumberType = typing.Optional[typing.Tuple[int, ...]]

OptionTypeLiteral = typing.Literal['string', 'boolean', 'integer', 'float']
OptionDeprecatedTypeLiteral = typing.Literal['str', 'bool', 'int']
LocationLiteral = typing.Literal['step', 'recipe', 'config', 'product']

SubDomainDefinitionType = typing.Dict[
    LocationLiteral,
    typing.Union[str, typing.Sequence[typing.Optional[str]], None]
]
