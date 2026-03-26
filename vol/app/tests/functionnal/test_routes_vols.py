from datetime import datetime

def test_get_vol(client, vol_test):
    """Test de la route GET /api/vols/<id> pour récupérer un vol spécifique."""
    response = client.get(f'/api/vols/{vol_test.id_vol}')
    assert response.status_code == 200

def test_get_vols(client):
    """Test de la route GET /api/vols pour récupérer tous les vols."""
    response = client.get(f'/api/vols')
    assert response.status_code == 200

def test_delete_vol(client, vol_test):
    """Test de la route DELETE /api/vols/<id> pour supprimer un vol spécifique."""
    response = client.delete(f'/api/vols/{vol_test.id_vol}')
    assert response.status_code == 204

def test_update_vol(client, vol_test):
    """Test de la route PUT /api/vols/<id> pour mettre à jour un vol spécifique."""
    new_data = {
        "nom_vol": "AF202",
        "id_compagnie": vol_test.id_compagnie,
        "id_terminal_depart": vol_test.id_terminal_depart,
        "id_terminal_arrivee": vol_test.id_terminal_arrivee,
        "date_heure_depart": vol_test.date_heure_depart.isoformat(),
        "date_heure_arrivee": vol_test.date_heure_arrivee.isoformat(),
    }
    response = client.put(f'/api/vols/{vol_test.id_vol}', json=new_data)
    assert response.status_code == 200
    assert response.json['nom_vol'] == "AF202"

def test_post_vol(client, compagnie_test, terminal_test):
    """Test de la route POST /api/vols pour créer un nouveau vol."""
    new_data = {
        "nom_vol": "AF203",
        "id_compagnie": compagnie_test.id_compagnie,
        "id_terminal_depart": terminal_test.id_terminal,
        "id_terminal_arrivee": terminal_test.id_terminal,
        "date_heure_depart": datetime(2026, 4, 1, 10, 0, 0).isoformat(),
        "date_heure_arrivee": datetime(2026, 4, 1, 12, 0, 0).isoformat(),
    }
    response = client.post(f'/api/vols', json=new_data)
    assert response.status_code == 201

def test_vol_not_found(client):
    """Test de la route GET /api/vols/<id> pour un vol qui n'existe pas."""
    response = client.get('/api/vols/9999')
    assert response.status_code == 404

def test_put_vol_not_found(client):
    """Test de la route PUT /api/vols/<id> pour un vol qui n'existe pas."""
    new_data = {
        "nom_vol": "AF204",
        "id_compagnie": 1,
        "id_terminal_depart": 1,
        "id_terminal_arrivee": 1,
        "date_heure_depart": datetime(2026, 4, 1, 10, 0, 0).isoformat(),
        "date_heure_arrivee": datetime(2026, 4, 1, 12, 0, 0).isoformat(),
    }
    response = client.put('/api/vols/9999', json=new_data)
    assert response.status_code == 404