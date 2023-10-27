import unittest
from unittest.mock import patch
from io import StringIO
import sys
import json

from src.cli.commands.cmd_print_config import print_json_tree
from src.cli.utils import  print_info,  print_rule

import re
    
def test_print_json_tree():

    file = open("tests/unit/data/newmsgram.json")
    data = json.load(file)

    captured_output = StringIO()
    sys.stdout = captured_output

    characteristics = data.get("characteristics", [])

    result = print_json_tree(characteristics[0])

    fileExpected = open("tests/unit/data/expected_list.txt")

    compare = fileExpected.read()

    # O padrão de regex para cores no formato [#FFFFFF] e [#458B00]
    color_pattern = r'\[#\w+\]'

    # Substituir todas as ocorrências do padrão pelo texto vazio
    result = re.sub(color_pattern, '', result)
    result = re.sub('\n', '', result)
    compare = re.sub('\n', '', compare)

    assert result == compare