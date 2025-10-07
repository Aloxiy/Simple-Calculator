import pytest
from unittest.mock import MagicMock, patch
from main import is_number, casting, add, sub, mul, div


# ==========================
# ЛОГИЧЕСКИЕ ТЕСТЫ
# ==========================

@pytest.mark.parametrize("s,expected", [
    ('123', True),
    ('12.34', True),
    ('12,34', True),
    ('-12', True),
    ('', False),
    ('asda', False),
])
def test_is_number(s, expected):
    """Тест проверки является ли ввод числом"""
    assert is_number(s) == expected


@pytest.mark.parametrize("num,expected", [
    ('123', 123),
    ('12.34', 12.34),
    ('12,34', 12.34),
    ('-123', -123),
    ('0', 0)
])
def test_casting(num, expected):
    """Тест перевода строки в число"""
    assert casting(num) == expected


@pytest.mark.parametrize("a, b, expected", [
    ('1', '2', 3),
    ('12.34', '56.78', 69.12),
    ('12,34', '56,78', 69.12),
    ('12,34', '56.78', 69.12),
    ('-123', '100', -23),
    ('-123', '-100', -223),
    ('-123', '0', -123),
    ('123', '0', 123)
])
def test_add(a, b, expected):
    """Тест сложения"""
    assert round(add(a, b), 8) == expected


@pytest.mark.parametrize("a, b, expected", [
    ('1', '2', -1),
    ('56.78', '12.34', 44.44),
    ('12,34', '56,78', -44.44),
    ('12,34', '56.78', -44.44),
    ('-123', '100', -223),
    ('-123', '-100', -23),
    ('-123', '0', -123),
    ('123', '0', 123)
])
def test_sub(a, b, expected):
    """Тест вычитания"""
    assert round(sub(a, b), 8) == expected


@pytest.mark.parametrize("a, b, expected", [
    ('1', '2', 2),
    ('56.78', '12.34', 700.6652),
    ('12,34', '56,78', 700.6652),
    ('12,34', '56.78', 700.6652),
    ('-123', '100', -12300),
    ('-123', '-100', 12300),
    ('-123', '0', 0),
    ('12,01', '0', 0),
    ('12,01', '1', 12.01),
    ('123', '-1', -123)
])
def test_mul(a, b, expected):
    """Тест умножения"""
    assert round(mul(a, b), 8) == expected


@pytest.mark.parametrize("a, b, expected", [
    ('1', '2', 0.5),
    ('56.78', '12.34', 4.6012966),
    ('12,34', '56,78', 0.21733005),
    ('12,34', '56.78', 0.21733005),
    ('-123', '100', -1.23),
    ('-123', '-100', 1.23),
    ('-123', '0', "ZeroDivisionError"),
    ('12,01', '1', 12.01),
    ('123', '-1', -123)
])
def test_div(a, b, expected):
    """Тест деления"""
    if expected == "ZeroDivisionError":
        with pytest.raises(ZeroDivisionError):
            div(a, b)
    else:
        assert round(div(a, b), 8) == expected


# ==========================
# GUI-ТЕСТЫ (без Tkinter)
# ==========================

@pytest.fixture(autouse=True)
def setup_gui_mocks():
    """Создаёт поддельные Entry и Label для GUI-функций"""
    import main
    from unittest.mock import MagicMock

    main.Numberentry1 = MagicMock()
    main.Numberentry2 = MagicMock()
    main.Showlabel = MagicMock()



def test_actionPlus(monkeypatch):
    """Тест кнопки '+'"""
    from main import Numberentry1, Numberentry2, Showlabel, actionPlus

    Numberentry1.get.return_value = "5"
    Numberentry2.get.return_value = "3"

    actionPlus()
    Showlabel.delete.assert_called_once_with(0, "end")
    Showlabel.insert.assert_called_once_with(0, "8")


def test_actionMinus(monkeypatch):
    """Тест кнопки '-'"""
    from main import Numberentry1, Numberentry2, Showlabel, actionMinus

    Numberentry1.get.return_value = "10"
    Numberentry2.get.return_value = "4"

    actionMinus()
    Showlabel.insert.assert_called_once_with(0, "6")


def test_actionMul(monkeypatch):
    """Тест кнопки '*'"""
    from main import Numberentry1, Numberentry2, Showlabel, actionMul

    Numberentry1.get.return_value = "3"
    Numberentry2.get.return_value = "5"

    actionMul()
    Showlabel.insert.assert_called_once_with(0, "15")


def test_actionDiv(monkeypatch):
    """Тест кнопки '/'"""
    from main import Numberentry1, Numberentry2, Showlabel, actionDiv

    Numberentry1.get.return_value = "8"
    Numberentry2.get.return_value = "2"

    actionDiv()
    Showlabel.insert.assert_called_once_with(0, "4.0")


def test_actionDiv_zero(monkeypatch):
    """Тест кнопки '/' при делении на ноль"""
    from main import Numberentry1, Numberentry2, actionDiv

    Numberentry1.get.return_value = "5"
    Numberentry2.get.return_value = "0"

    with patch("main.messagebox.showerror") as mock_error:
        actionDiv()
        mock_error.assert_called_once()


if __name__ == "__main__":
    pytest.main([__file__, "-q", "-s"])
