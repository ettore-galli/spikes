class A:
    class Coso:
        X = 2

    def get_coso(self):
        return self.Coso.X


class B(A):
    class Coso:
        X = 3

    pass


if __name__ == "__main__":
    print(A().get_coso())  # 2
    print(B().get_coso())  # 3
