import pytest
from tools import Calculator


# FIXTURE - прописываются в отдельном файле, НЕ в одном с тестами
# если нам нужно поменять значения - @pytest.fixture(scope="module)
# после return - код не выполняется
# yield - н-р до - авторизуемся, затем возвращаем страницу для какого-то теста, но
# после каждого теста нам нужно закрыть браузер, если мы это не сделаем, то он будет
# постоянно открыт и для этого можно написать кусок кода, чтобы браузер закрылся -
# это и будет выполнение после
@pytest.fixture(scope='module')
def calc():
    # что-то выполняем до
    yield Calculator()
    # что-то делаем после


@pytest.mark.slow
# запускаем pytest -s -v -m 'slow'
def test_add(calc):
    result = calc.add(4, 5)

    assert result == 9


 # pytest -s -v -m 'slow or smoke'
 # pytest -s -v -m 'slow and smoke'
 # @pytest.mark.window - на маке не сработат
 # Все нужно прописать в pytest_ini
@pytest.mark.windows
@pytest.mark.slow
@pytest.mark.smoke
def test_sub(calc):
    result = calc.sub(10, 2)

    assert result == 8


def test_div(calc):
    result = calc.div(10, 2)

    assert result == 5.0


# kip - скипает и даже не запускает
@pytest.mark.kip(reason='will be fixed later')

# @pytest.mark.xfail - предупреждаем заранее, что тест упадет

def test_div_by_zero(calc):
    result = calc.div(5, 0)

    assert result == None