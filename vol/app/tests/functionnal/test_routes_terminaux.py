def test_get_terminal(client, terminal_test):
    response = client.get(f'/api/terminaux/{terminal_test.id_terminal}')
    assert response.status_code == 200

def test_get_terminaux(client):
    response = client.get(f'/api/terminaux')
    assert response.status_code == 200

def test_delete_terminal(client, terminal_test):
    response = client.delete(f'/api/terminaux/{terminal_test.id_terminal}')
    assert response.status_code == 204

def test_update_terminal(client, terminal_test):
    new_data = {"nom_terminal": "Terminal 2", "id_aeroport": terminal_test.id_aeroport}
    response = client.put(f'/api/terminaux/{terminal_test.id_terminal}', json=new_data)
    assert response.status_code == 200
    assert response.json['nom_terminal'] == "Terminal 2"