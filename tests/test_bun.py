from bun import Bun


class TestBun:

    def test_init(self):
        bun = Bun("black bun", 100)

        assert bun.name == "black bun"
        assert bun.price == 100

    def test_get_name(self):
        bun = Bun("black bun", 100)

        assert bun.get_name() == "black bun"

    def test_get_price(self):
        bun = Bun("black bun", 100)

        assert bun.get_price() == 100