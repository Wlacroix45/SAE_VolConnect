def test_get_localiser(client, localiser_test):
    response = client.get(f'/api/localisations')
    assert response.status_code == 200