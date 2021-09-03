#!/usr/bin/env python
# coding: utf-8
'''
Combine the MP and RTB account data (assumes both are in json)
'''

import sys
import json


def main(mp_data_fn, rtb_data_fn):
    with open(mp_data_fn) as mp_data_file:
        mp_data = json.load(mp_data_file)
        print(F"{len(mp_data)} mp accounts")
    with open(rtb_data_fn) as rtb_data_file:
        rtb_data = json.load(rtb_data_file)
        print(F"{len(rtb_data)} rtb accounts")

    code2rtb = {rtb['code']: rtb for rtb in rtb_data}
    print(F"rtb codes: {json.dumps(list(code2rtb.keys()))}")

    for mp_acc in mp_data:
        if mp_acc['code'] not in code2rtb:
            print(F"no rtb account for code={mp_acc['code']}")
            continue
        rtb_acc = code2rtb[mp_acc['code']]
        rtb_acc.update(mp_acc)

    fn = "prod.account.combined.json"
    with open(fn, "w") as output:
        print(json.dumps(rtb_data, indent=4), file=output)
        print(F"{fn} written")
        
if __name__ == '__main__':
    try:
        mp_data_fn = sys.argv[1]
        rtb_data_fn = sys.argv[2]
    except IndexError:
        print("usage: combine_account_data.py <mp_data_fn> <rtb_data_fn>")
        sys.exit(1)
        
    main(mp_data_fn, rtb_data_fn)


