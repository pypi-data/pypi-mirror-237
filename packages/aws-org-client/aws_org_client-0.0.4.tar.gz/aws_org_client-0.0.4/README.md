# aws_org_client

![version number](https://img.shields.io/pypi/v/aws_org_client?color=blue&label=version)

This project is a python package, aimed at providing a simple interface with AWS
organisation & identity services.

Using boto3 clients:
  * identitystore
  * organizations
  * sso-admin


# Project processes
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