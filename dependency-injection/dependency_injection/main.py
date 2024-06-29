from dependency_injection.dependency import make_normal_dependency
from dependency_injection.display import display


make_normal_dependency()

if __name__ == "__main__":
    display(file="./dependency_injection/data/sample.txt")
