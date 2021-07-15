import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_open_page(app):
    app.open_home_page()
    app.login(email="auto_moderator_user@severex.io", password="Password!1")
