import functools
import glob
from typing import Callable, Optional

import pydantic.alias_generators


@functools.cache
def get_icons() -> list[str]:
    return glob.glob('asset/aws/*.svg')


def aws_icon(name: str) -> Optional[str]:
    icons = get_icons()
    mappings = {
        'dynamodb': 'DynamoDB',
        'states': 'Step-Functions',
    }

    name = mappings.get(name, name)

    fns: list[Callable[[str], str]] = [
        lambda name: name,
        lambda name: pydantic.alias_generators.to_pascal(name),
    ]

    for fn in fns:
        elm = fn(name)
        if (res := f'asset/aws/Arch_{elm}_16.svg') in icons:
            return res

        if (res := f'asset/aws/Arch_Amazon-{elm}_16.svg') in icons:
            return res

        if (res := f'asset/aws/Arch_AWS-{elm}_16.svg') in icons:
            return res
