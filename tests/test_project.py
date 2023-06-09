from project.models.person.user import UserModel

"""
def test_home(client):
    response = client.get("/role")
    assert b"Ceyhun" in response.data
"""


def test_registration(client, app):
    response = client.post("/register", data={
        "username": "sun",
        "password": "1234",
        "name": "jose",
        "surname": "coach",
        "role_id": 1,
        "command_collar_mark_id": 1,
        "command_collar_mark_rank_id": 1,
        "command_id": 1,
        "hierarchy_id": 1,
        "status": 1
    })
    with app.app_context():
        assert UserModel.query.count == 1
        assert UserModel.query.first().username == "sun"
