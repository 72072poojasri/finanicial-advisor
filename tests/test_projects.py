def test_projects_requires_auth(test_client):
    response = test_client.get("/api/projects")
    assert response.status_code == 401