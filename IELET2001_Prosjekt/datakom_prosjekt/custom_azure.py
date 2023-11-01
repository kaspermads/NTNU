from storages.backends.azure_storage import AzureStorage
AZURE_ACCOUNT_KEY = 'mC5obmcDPKhswBnqwN5bc6D33CXQTDiTgHpYNOmeqTewa7aWTn78D+N1TmJ6pgV1069iWLWzrh4u+AStEwA7yQ=='


class AzureMediaStorage(AzureStorage):
    account_name = 'kaspergmstorage'  # Must be replaced by your <storage_account_name>
    account_key = AZURE_ACCOUNT_KEY  # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = 'kaspergmstorage'  # Must be replaced by your storage_account_name
    account_key = AZURE_ACCOUNT_KEY  # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
