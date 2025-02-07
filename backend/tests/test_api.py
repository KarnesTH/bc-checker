
def test_index(client):
    """Test the index endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == 'ok'
    assert response.json['message'] == 'Service is running'

def test_get_materials_empty(client):
    """Test getting materials when DB is empty"""
    response = client.get('/api/materials')
    assert response.status_code == 404
    assert isinstance(response.json, dict)
    assert response.json['message'] == 'No materials found'

def test_get_materials(client, sample_material):
    """Test getting materials with data"""
    response = client.get('/api/materials')
    assert response.status_code == 200
    materials = response.json
    assert len(materials) == 1
    assert materials[0]['name'] == 'Test Material'

def test_get_material_by_id(client, sample_material):
    """Test getting a specific material"""
    response = client.get(f'/api/materials/{sample_material.id}')
    assert response.status_code == 200
    assert response.json['name'] == 'Test Material'

def test_get_material_not_found(client):
    """Test getting a non-existent material"""
    response = client.get('/api/materials/999')
    assert response.status_code == 404

def test_search_materials(client, sample_material):
    """Test searching for materials"""
    response = client.get('/api/materials/search/Test')
    assert response.status_code == 200
    materials = response.json
    assert len(materials) == 1
    assert materials[0]['name'] == 'Test Material'
