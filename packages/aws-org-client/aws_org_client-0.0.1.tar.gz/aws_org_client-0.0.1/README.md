## Coverage report

run coverage report:
```bash
poetry run coverage run -m --source=aws_org_client pytest tests
poetry run coverage report
```

## Linting

run pylint with:
```bash
poetry run pylint aws_org_client
poetry run pylint tests
```

run black formatter with:
```bash
poetry run black .
```