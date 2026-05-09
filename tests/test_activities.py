def test_get_all_activities_returns_200(client):
    """Arrange: Client ready | Act: GET /activities | Assert: Status 200 with activities"""
    # Arrange - nothing needed, client is ready

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert isinstance(activities, dict)
    assert len(activities) > 0


def test_get_activities_returns_correct_structure(client):
    """Arrange: Client ready | Act: GET /activities | Assert: Response has expected fields"""
    # Arrange - nothing needed

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    for activity_name, details in activities.items():
        assert "description" in details
        assert "schedule" in details
        assert "max_participants" in details
        assert "participants" in details
        assert isinstance(details["participants"], list)
        assert isinstance(details["max_participants"], int)
