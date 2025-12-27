#!/bin/bash
set -e

./solution.sh
pytest tests -q

echo "ALL TESTS PASSED"
