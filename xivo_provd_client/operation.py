# -*- coding: utf-8 -*-

# Copyright (C) 2011-2015 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import re

OIP_WAITING = 'waiting'
OIP_PROGRESS = 'progress'
OIP_SUCCESS = 'success'
OIP_FAIL = 'fail'


class OperationInProgress(object):

    def __init__(self, label=None, state=OIP_WAITING, current=None, end=None, sub_oips=[]):
        self.label = label
        self.state = state
        self.current = current
        self.end = end
        self.sub_oips = list(sub_oips)


def _split_top_parentheses(str_):
    idx = 0
    length = len(str_)
    result = []
    while idx < length:
        if str_[idx] != '(':
            raise ValueError('invalid character: %s' % str_[idx])
        start_idx = idx
        idx += 1
        count = 1
        while count:
            if idx >= length:
                raise ValueError('unbalanced number of parentheses: %s' % str_)
            c = str_[idx]
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            idx += 1
        end_idx = idx
        result.append(str_[start_idx + 1:end_idx - 1])
    return result


_PARSE_OIP_REGEX = re.compile(r'^(?:(\w+)\|)?(\w+)(?:;(\d+)(?:/(\d+))?)?')

def parse_oip(oip_string):
    m = _PARSE_OIP_REGEX.search(oip_string)
    if not m:
        raise ValueError('invalid oip string: %s' % oip_string)
    else:
        label, state, raw_current, raw_end = m.groups()
        raw_sub_oips = oip_string[m.end():]
        current = raw_current if raw_current is None else int(raw_current)
        end = raw_end if raw_end is None else int(raw_end)
        sub_oips = [parse_oip(sub_oip_string) for sub_oip_string in
                    _split_top_parentheses(raw_sub_oips)]
        return OperationInProgress(label, state, current, end, sub_oips)
