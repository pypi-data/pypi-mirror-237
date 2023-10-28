import boto3


class Organizations:
    def __init__(self):
        self.org_client = boto3.client("organizations")

    def list_accounts(self):
        accounts = []
        next_token = None

        while True:
            if next_token:
                response = self.org_client.list_accounts(NextToken=next_token)
            else:
                response = self.org_client.list_accounts()

            accounts.extend(response.get("Accounts", []))
            next_token = response.get("NextToken")

            if not next_token:
                break

        return accounts
