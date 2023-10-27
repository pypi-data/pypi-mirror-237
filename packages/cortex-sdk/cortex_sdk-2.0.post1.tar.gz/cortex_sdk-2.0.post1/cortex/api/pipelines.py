from typing import List, Optional
from ..types.cortex_file import CortexFile
from ..types.cortex_pipeline import CortexPipeline
from .api_resource import APIResource


class Pipelines(APIResource):
    """
    Cortex Repos API.
    """
    @classmethod
    def get(
        cls, 
        resource_id: Optional[str] = None
    ) -> CortexPipeline| List[CortexPipeline]:
        """
        Gets one or many pipelines.

        Args:
            resource_id (str, optional):
            The ID of the repo to retrieve. If None, retrieves all repo.

        Returns:
            CortexPipeline or list[CortexPipeline]: 
            If resource_id is provided, returns a single CortexPipeline object.
            If resource_id is None, returns a list of CortexPipeline objects.
        """
        return cls._generic_get(
            path        = f'/pipelines/{resource_id or ""}',
            return_type = CortexPipeline
        )

    @classmethod
    def load(
        cls,
        config_path: str
    ):
        pass