import pytest

@pytest.fixture(scope="session")
def testdata():
    return """CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER);
              INSERT INTO fish VALUES ('Sammy', 'shark', 1);
              INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7);"""
