#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Insert list of accounts (JSON format) into the db

usage: python insert_account_data.py <db_uri> <accounts_fn>
'''

import sys
import json
import sqlalchemy as sa


def main(db_uri, accounts_fn):
    engine = sa.create_engine(db_uri)

    with open(accounts_fn) as accounts_json:
        accounts = json.load(accounts_json)

    fields = list(accounts[0].keys())
    fields.remove('id')
    columns = ','.join(fields)
    values = ','.join(F":{col}" for col in fields)
    sql = f"INSERT INTO account ({columns}) VALUES ({values})"
    query = sa.sql.text(sql)

    with engine.connect() as conn:
        conn.execute("DELETE FROM account")

        for account in accounts:
            # inserting accounts one-by-one ok because not very many of them
            if 'config' not in account:
                print(F"no config for account {account['code']}")
                continue
            account['config'] = json.dumps(account['config'])

            del account['id']
            conn.execute(query, account)


if __name__ == '__main__':
    try:
        db_uri = sys.argv[1]
        if db_uri == '-h':
            raise IndexError
        accounts_fn = sys.argv[2]
    except IndexError:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    main(db_uri, accounts_fn)
