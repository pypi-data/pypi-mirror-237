import boto3


class IdentityStore:
    def __init__(self, identity_store_id):
        # [TODO: replace region with something less hardcoded]
        self.client = boto3.client("identitystore")
        self.identity_store_id = identity_store_id
        self.users = self.list_users()

    def list_users(self):
        response = self.client.list_users(IdentityStoreId=self.identity_store_id)

        return response

    def describe_user(self, user_id):
        response = self.client.describe_user(
            IdentityStoreId=self.identity_store_id, UserId=user_id
        )

        return response

    def describe_group(self, group_id):
        response = self.client.describe_group(
            IdentityStoreId=self.identity_store_id, GroupId=group_id
        )

        return response

    def list_group_memberships(self, group_id):
        response = self.client.list_group_memberships(
            IdentityStoreId=self.identity_store_id, GroupId=group_id
        )

        return response.get("GroupMemberships", [])
