def test_get_compagnie(client, compagnie_test):
    response = client.get(f'/api/compagnies/{compagnie_test.id_compagnie}')
    assert response.status_code == 200

def test_get_compagnies(client):
    response = client.get(f'/api/compagnies')
    assert response.status_code == 200

def test_delete_compagnie(client, compagnie_test):
    response = client.delete(f'/api/compagnies/{compagnie_test.id_compagnie}')
    assert response.status_code == 204

def test_update_compagnie(client, compagnie_test):
    new_data = {"nom_comp": "Air France nouveau"}
    response = client.put(f'/api/compagnies/{compagnie_test.id_compagnie}', json=new_data)
    assert response.status_code == 200
    assert response.json['nom_comp'] == "Air France nouveau"