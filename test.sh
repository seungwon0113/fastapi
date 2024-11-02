#!/usr/bin/env bash
set -eo pipefail # pipefail : 실행시 하나가 False면 더이상 실행 X

COLOR_GREEN=`tput setaf 2;`
COLOR_NC=`tput sgr0;` # No Color

echo "Starting black"
poetry run black .
echo "OK"

echo "Starting isort"
poetry run isort .
echo "OK"

echo "Starting mypy"
poetry run mypy .
echo "OK"

echo "Starting pytest with coverage"
poetry run coverage run -m pytest # coverage 를 측정하면서 "pytest" 를 실행할 것이다.
poetry run coverage report -m # 테스트가 끝나고 coverage 가 어떻게 되는지 조회
poetry run coverage html

echo "${COLOR_GREEN}All tests passed successfully!${COLOR_NC}"

# test.sh 권한 설정 : chmod +x ./test.sh