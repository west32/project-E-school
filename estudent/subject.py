from dataclasses import dataclass, field
from typing import List

@dataclass
class Subject:
    identifier: int
    name: str
    is_obligatory: bool = True
    teachers_names: List[str]= field(default_factory=list)

    def assign_teacher(self,name):
        return self.teachers_names.append(name)
def run_example():
    math = Subject(identifier=1, name="Matematyka",is_obligatory=True)

    print(math)

if __name__=="__main__":
    run_example()