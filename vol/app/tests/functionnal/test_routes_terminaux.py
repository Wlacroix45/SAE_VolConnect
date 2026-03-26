def test_get_terminal(client, terminal_test):
    """Test de la route GET /api/terminaux/<id> pour récupérer un terminal spécifique."""
    response = client.get(f'/api/terminaux/{terminal_test.id_terminal}')
    assert response.status_code == 200

def test_get_terminaux(client):
    """Test de la route GET /api/terminaux pour récupérer tous les terminaux."""
    response = client.get(f'/api/terminaux')
    assert response.status_code == 200

def test_delete_terminal(client, terminal_test):
    """Test de la route DELETE /api/terminaux/<id> pour supprimer un terminal spécifique."""
    response = client.delete(f'/api/terminaux/{terminal_test.id_terminal}')
    assert response.status_code == 204

def test_update_terminal(client, terminal_test):
    """Test de la route PUT /api/terminaux/<id> pour mettre à jour un terminal spécifique."""
    new_data = {"nom_terminal": "Terminal 2", "id_aeroport": terminal_test.id_aeroport}
    response = client.put(f'/api/terminaux/{terminal_test.id_terminal}', json=new_data)
    assert response.status_code == 200
    assert response.json['nom_terminal'] == "Terminal 2"

def test_post_terminal(client, aeroport_test):
    """Test de la route POST /api/terminaux pour créer un nouveau terminal."""
    new_data = {"nom_terminal": "Terminal 3", "id_aeroport": aeroport_test.id_aeroport}
    response = client.post(f'/api/terminaux', json=new_data)
    assert response.status_code == 201

def test_terminal_not_found(client):
    """Test de la route GET /api/terminaux/<id> pour un terminal qui n'existe pas."""
    response = client.get('/api/terminaux/9999')
    assert response.status_code == 404

def test_put_terminal_not_found(client, aeroport_test):
    """Test de la route PUT /api/terminaux/<id> pour un terminal qui n'existe pas."""
    new_data = {"nom_terminal": "Terminal 4", "id_aeroport": aeroport_test.id_aeroport}
    response = client.put('/api/terminaux/9999', json=new_data)
    assert response.status_code == 404