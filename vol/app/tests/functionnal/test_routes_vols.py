def test_get_vol(client, vol_test):
    response = client.get(f'/api/vols/{vol_test.id_vol}')
    assert response.status_code == 200

def test_get_vols(client):
    response = client.get(f'/api/vols')
    assert response.status_code == 200

def test_delete_vol(client, vol_test):
    response = client.delete(f'/api/vols/{vol_test.id_vol}')
    assert response.status_code == 204

def test_update_vol(client, vol_test):
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