from typing import Optional, TypedDict

class GraphState(TypedDict):
    input: str
    resume_file: Optional[bytes]  # binary resume file
    output: str
