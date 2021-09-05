#!/bin/bash

. scripts/env_prepare.sh
python scripts/insert_account_data.py $SQLALCHEMY_DB_URI tests/data/raw/prod.account.combined.json
