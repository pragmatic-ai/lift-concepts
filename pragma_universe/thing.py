from typing import Optional
from dataclasses import dataclass


@dataclass
class Thing:
    """
     Thing (Entity) is the most generic type of item.
     Anything with tangible or intangible. 
    """
    identifier: str = None # a unique identifier
    description: Optional[str] = None # A description of the thing.
    is_tangible: Optional[bool] = None # if is tangible
    class_wikidata_id: str = 'Q35120'  # wikidata id of the class thing
    class_schema_org_url: str = 'http://schema.org/Thing'
    pragma_id: str = "thing"
