from depencency_injection.dependency import make_fake_dependency
from depencency_injection.display import display


make_fake_dependency()

if __name__ == "__main__":
    display(file="data/sample.txt")
