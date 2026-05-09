def test_unregister_existing_student_returns_200(client):
    """Arrange: Pre-signed student | Act: DELETE unregister | Assert: Status 200, student removed"""
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already signed up in sample data

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister?email={email}"
    )

    # Assert
    assert response.status_code == 200
    assert "Unregistered" in response.json()["message"]


def test_unregister_nonexistent_student_returns_400(client):
    """Arrange: Non-signed-up student | Act: DELETE unregister | Assert: Status 400"""
    # Arrange
    activity_name = "Chess Club"
    email = "notregistered@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister?email={email}"
    )

    # Assert
    assert response.status_code == 400
    assert "not registered" in response.json()["detail"]


def test_unregister_from_nonexistent_activity_returns_404(client):
    """Arrange: Non-existent activity | Act: DELETE unregister | Assert: Status 404"""
    # Arrange
    activity_name = "Nonexistent Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister?email={email}"
    )

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]
