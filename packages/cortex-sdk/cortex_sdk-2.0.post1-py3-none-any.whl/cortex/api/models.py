from typing import List, Optional
from .api_resource import APIResource
from ..types.cortex_model import CortexModel

class Models(APIResource):
    @classmethod
    def get(
        cls,
        resource_id: Optional[str] = None
    ) -> CortexModel | List[CortexModel]:
        """
        Gets one or many inferences.

        Args:
            resource_id (str, optional):
            The ID of the model to retrieve. If None, retrieves all models.

        Returns:
            CortexInference or list[CortexInference]: 
            If resource_id is provided, returns a single CortexInference object.
            If resource_id is None, returns a list of CortexInference objects.
        """
        return cls._generic_get(
            path        = f'/models/{resource_id or ""}',
            return_type = CortexModel
        )
