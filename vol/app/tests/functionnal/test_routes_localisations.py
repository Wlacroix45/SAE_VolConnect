def test_get_localiser(client, localiser_test):
    response = client.get(f'/api/localisations')
    assert response.status_code == 200

def test_post_localiser(client, aeroport_test, compagnie_test):
    response = client.post(f'/api/localisations', json={"id_aeroport": aeroport_test.id_aeroport, "id_compagnie": compagnie_test.id_compagnie})
    assert response.status_code == 201
