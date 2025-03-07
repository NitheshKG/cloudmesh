from pycloudmesh.providers.aws import AWSReservationCost
from pycloudmesh.providers.azure import AzureReservationCost
from pycloudmesh.providers.gcp import GCPReservationCost

class CloudMesh:
    def __init__(self, provider, **kwargs):
        if provider == "aws":
            self.client = AWSReservationCost(
                kwargs["access_key"], kwargs["secret_key"], kwargs["region"]
            )
        elif provider == "azure":
            self.client = AzureReservationCost(kwargs["subscription_id"], kwargs["token"])
        elif provider == "gcp":
            self.client = GCPReservationCost(kwargs["project_id"], kwargs["credentials_path"])
        else:
            raise ValueError(f"Unsupported cloud provider: {provider}")

    def get_reservation_cost(self):
        """Fetch reservation cost for the selected cloud provider."""
        return self.client.get_reservation_cost()

    def get_azure_reservation_order_details(self):
        """Fetch reservation order details (Only available for Azure)."""
        if isinstance(self.client, AzureReservationCost):
            return self.client.get_azure_reservation_order_details()
        raise AttributeError("get_reservation_order_details() is only available for Azure.")
