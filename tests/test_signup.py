def test_signup_new_student_returns_200(client):
    """Arrange: New email | Act: POST signup | Assert: Status 200, student added"""
    # Arrange
    activity_name = "Programming Class"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )

    # Assert
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]


def test_signup_duplicate_email_returns_400(client):
    """Arrange: Email already signed up | Act: POST signup same email twice | Assert: Status 400"""
    # Arrange
    activity_name = "Programming Class"
    email = "duplicate@mergington.edu"
    
    # First signup
    client.post(f"/activities/{activity_name}/signup?email={email}")

    # Act - Try signup again with same email
    response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_nonexistent_activity_returns_404(client):
    """Arrange: Non-existent activity | Act: POST signup | Assert: Status 404"""
    # Arrange
    activity_name = "Nonexistent Club"
    email = "student@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]
