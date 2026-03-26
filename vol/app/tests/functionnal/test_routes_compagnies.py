def test_get_compagnie(client, compagnie_test):
    response = client.get(f'/api/compagnies/{compagnie_test.id_compagnie}')
    assert response.status_code == 200