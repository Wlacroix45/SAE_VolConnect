def test_get_aeroport(client, aeroport_test):
    """Test de la route GET /api/aeroports/<id> pour récupérer un aéroport spécifique."""
    response = client.get(f'/api/aeroports/{aeroport_test.id_aeroport}')
    assert response.status_code == 200

def test_get_aeroports(client):
    """Test de la route GET /api/aeroports pour récupérer tous les aéroports."""
    response = client.get(f'/api/aeroports')
    assert response.status_code == 200

def test_delete_aeroport(client, aeroport_test):
    """Test de la route DELETE /api/aeroports/<id> pour supprimer un aéroport spécifique."""
    response = client.delete(f'/api/aeroports/{aeroport_test.id_aeroport}')
    assert response.status_code == 204

def test_update_aeroport(client, aeroport_test):
    """Test de la route PUT /api/aeroports/<id> pour mettre à jour un aéroport spécifique."""
    new_data = {"nom_aeroport": "Pierre de Gaulle", "ville": aeroport_test.ville, "pays": aeroport_test.pays}
    response = client.put(f'/api/aeroports/{aeroport_test.id_aeroport}', json=new_data)
    assert response.status_code == 200
    assert response.json['nom_aeroport'] == "Pierre de Gaulle"
    assert response.json['pays'] == "France"

def test_get_terminaux_by_aeroport(client, aeroport_test):
    """Test de la route GET /api/aeroports/<id>/terminaux pour récupérer les terminaux d'un aéroport spécifique."""
    response = client.get(f'/api/aeroports/{aeroport_test.id_aeroport}/terminaux')
    assert response.status_code == 200

def test_post_aeroport(client):
    """Test de la route POST /api/aeroports pour créer un nouvel aéroport."""
    new_data = {"nom_aeroport": "Orly", "ville": "Paris", "pays": "France"}
    response = client.post(f'/api/aeroports', json=new_data)
    assert response.status_code == 201

def test_aeroport_not_found(client):
    """Test de la route GET /api/aeroports/<id> pour un aéroport qui n'existe pas."""
    response = client.get('/api/aeroports/9999')
    assert response.status_code == 404

def test_put_aeroport_not_found(client):
    """Test de la route PUT /api/aeroports/<id> pour un aéroport qui n'existe pas."""
    new_data = {"nom_aeroport": "Orly", "ville": "Paris", "pays": "France"}
    response = client.put('/api/aeroports/9999', json=new_data)
    assert response.status_code == 404