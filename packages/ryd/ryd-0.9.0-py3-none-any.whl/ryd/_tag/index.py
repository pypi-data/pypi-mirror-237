# coding: 'utf-8'

from __future__ import annotations

import os
from ryd._tag._handler import BaseHandler
import ruamel.yaml
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ryd._convertor._base import ConvertorBase
else:
    ConvertorBase = Any


class Index(BaseHandler):
    def __init__(self, convertor: ConvertorBase) -> None:
        super().__init__(convertor)

    def __call__(self, d: Any) -> None:
        """
        insert an index
        mkdocs local expands this and buttons (default hidden) for 2nd level:
           <a class="reference internal" href="overview/">Overview</a>
        for readthedocs you need (within <ul>:
           <li><a href="http://yaml.readthedocs.io/en/latest/basicuse/">Basic Usage</a></li>
        """
        # print(f'{d}')
        # print(f'{self.c._ryd.data}')
        max_lvl = d.get('level', 3)
        data = self.c._ryd.data.get('index', {})
        if not data:
            return
        s = '\n<pre>'
        for path, lvl_val in data.items():
            # print(path)
            stem = path.stem
            # s += f'  {stem}\n'
            s += '\n'
            for lvl, val in lvl_val:
                if lvl > max_lvl:
                    continue
                # print(lvl, val)
                indent = ' ' * 2 * (lvl+1)
                xval = self.reference(val)
                # print(f'{xval=}')
                prefix = d['prefix']
                prefix = ''
                s += f'{indent}<a href="{prefix}{stem}/#{xval}">{val}</a>\n'
        s += '</pre>\n\n'
        self.c.add_text(s, gather=False)

    @staticmethod
    def reference(s):
        s = s.lower()
        for ch in '":\'.,`=(){}[]#/':
            s = s.replace(ch, '')
        while '  ' in s:
            s = s.replace('  ', ' ')
        s = s.strip()
        s = s.replace(' ', '-')
        return s
