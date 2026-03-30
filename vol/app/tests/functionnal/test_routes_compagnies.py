def test_get_compagnie(client, compagnie_test):
    """Test de la route GET /api/compagnies/<id> pour récupérer une compagnie spécifique."""
    response = client.get(f'/api/compagnies/{compagnie_test.id_compagnie}')
    assert response.status_code == 200

def test_get_compagnies(client):
    """Test de la route GET /api/compagnies pour récupérer toutes les compagnies."""
    response = client.get(f'/api/compagnies')
    assert response.status_code == 200

def test_delete_compagnie(client, compagnie_test):
    """Test de la route DELETE /api/compagnies/<id> pour supprimer une compagnie spécifique."""
    response = client.delete(f'/api/compagnies/{compagnie_test.id_compagnie}')
    assert response.status_code == 204

def test_update_compagnie(client, compagnie_test):
    """Test de la route PUT /api/compagnies/<id> pour mettre à jour une compagnie spécifique."""
    new_data = {"nom_comp": "Air France nouveau"}
    response = client.put(f'/api/compagnies/{compagnie_test.id_compagnie}', json=new_data)
    assert response.status_code == 200
    assert response.json['nom_comp'] == "Air France nouveau"

def test_get_vols_by_compagnie(client, compagnie_test):
    """Test de la route GET /api/compagnies/<id>/vols pour récupérer les vols d'une compagnie spécifique."""
    response = client.get(f'/api/compagnies/{compagnie_test.id_compagnie}/vols')
    assert response.status_code == 200

def test_post_compagnie(client):
    """Test de la route POST /api/compagnies pour créer une nouvelle compagnie."""
    new_data = {"nom_comp": "Air France"}
    response = client.post(f'/api/compagnies', json=new_data)
    assert response.status_code == 201

def test_compagnie_not_found(client):
    """Test de la route GET /api/compagnies/<id> pour une compagnie qui n'existe pas."""
    response = client.get('/api/compagnies/9999')
    assert response.status_code == 404

def test_put_compagnie_not_found(client):
    """Test de la route PUT /api/compagnies/<id> pour une compagnie qui n'existe pas."""
    new_data = {"nom_comp": "Air France"}
    response = client.put('/api/compagnies/9999', json=new_data)
    assert response.status_code == 404