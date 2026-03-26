def test_get_aeroport(client, aeroport_test):
    response = client.get(f'/api/aeroports/{aeroport_test.id_aeroport}')
    assert response.status_code == 200

def test_get_aeroports(client):
    response = client.get(f'/api/aeroports')
    assert response.status_code == 200

def test_delete_aeroport(client, aeroport_test):
    response = client.delete(f'/api/aeroports/{aeroport_test.id_aeroport}')
    assert response.status_code == 204

def test_update_aeroport(client, aeroport_test):
    new_data = {"nom_aeroport": "Pierre de Gaulle", "ville": aeroport_test.ville, "pays": aeroport_test.pays}
    response = client.put(f'/api/aeroports/{aeroport_test.id_aeroport}', json=new_data)
    assert response.status_code == 200
    assert response.json['nom_aeroport'] == "Pierre de Gaulle"
    assert response.json['pays'] == "France"

def test_get_terminaux_by_aeroport(client, aeroport_test):
    response = client.get(f'/api/aeroports/{aeroport_test.id_aeroport}/terminaux')
    assert response.status_code == 200

def test_post_aeroport(client):
    new_data = {"nom_aeroport": "Orly", "ville": "Paris", "pays": "France"}
    response = client.post(f'/api/aeroports', json=new_data)
    assert response.status_code == 201

def test_aeroport_not_found(client):
    response = client.get('/api/aeroports/9999')
    assert response.status_code == 404

def test_put_aeroport_not_found(client):
    new_data = {"nom_aeroport": "Orly", "ville": "Paris", "pays": "France"}
    response = client.put('/api/aeroports/9999', json=new_data)
    assert response.status_code == 404