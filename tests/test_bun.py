from bun import Bun


class TestBun:

    def test_init_sets_name_and_price(self):
        bun = Bun("black bun", 100)

        assert bun.name == "black bun"
        assert bun.price == 100

    def test_get_name_returns_bun_name(self):
        bun = Bun("black bun", 100)

        assert bun.get_name() == "black bun"

    def test_get_price_returns_bun_price(self):
        bun = Bun("black bun", 100)

        assert bun.get_price() == 100