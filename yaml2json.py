#!/usr/bin/env python3

import yaml
import json
import sys

fn_input = sys.argv[1]
fn_output = sys.argv[2]

# print(fn_input, fn_output)
with open(fn_input, "r") as fin, open(fn_output, "w") as fout:
    d = yaml.load(fin, Loader=yaml.SafeLoader)
    js_str = json.dumps(d)
    fout.write(js_str)

print("saving output to", fn_output)
