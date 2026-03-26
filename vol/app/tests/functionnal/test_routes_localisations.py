def test_get_localiser(client, localiser_test):
    """Test de la route GET /api/localisations pour récupérer les localisations."""
    response = client.get(f'/api/localisations')
    assert response.status_code == 200

def test_post_localiser(client, aeroport_test, compagnie_test):
    """Test de la route POST /api/localisations pour créer une nouvelle localisation."""
    response = client.post(f'/api/localisations', json={"id_aeroport": aeroport_test.id_aeroport, "id_compagnie": compagnie_test.id_compagnie})
    assert response.status_code == 201
