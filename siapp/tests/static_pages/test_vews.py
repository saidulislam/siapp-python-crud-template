from flask import url_for


# to run test
# docker-compose exec website py.test siapp/tests

# to check code coverage
# docker-compose exec website py.test --conv-report term-missing --cov siapp

# running static code analysis
# docker-compose exec website flake8 . --exclude __init__.py
# or docker-compose exec website flake8 siapp --exclude __init__.py
class TestPage(object):
    def test_home_page(self, client):
        """ Home page should respond with a success 200. """
        response = client.get(url_for('static_pages.home'))
        assert response.status_code == 200

    def test_terms_page(self, client):
        """ Terms page should respond with a success 200. """
        response = client.get(url_for('static_pages.terms'))
        assert response.status_code == 200

    def test_privacy_page(self, client):
        """ Privacy page should respond with a success 200. """
        response = client.get(url_for('static_pages.privacy'))
        assert response.status_code == 200

    def test_faq_page(self, client):
        """ faq page should respond with a success 200. """
        response = client.get(url_for('static_pages.faq'))
        assert response.status_code == 200
