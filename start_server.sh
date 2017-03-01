#!/bin/bash

echo "Migrate Database..."
./update_db.sh

echo "Run Server..."
python3 movie_explorer/movie_rating/browser_tests.py

echo "DONE"