import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_register_user():
    client = APIClient()
    data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "strongpassword123"
    }

    response = client.post('/api/register/', data)
    assert response.status_code == 201

    assert response.data['message'] == 'User create successfully'

@pytest.mark.django_db
def test_crud_tasks():
    client = APIClient()

    user = User.objects.create_user(username='testuser', password='qwerty12345')

    response = client.post('/api/token/', data={
            'username': 'testuser',
            'password': 'qwerty12345'})
    assert response.status_code == 200

    token = response.data['access']

    client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    #1 Create task
    created_data = {
        'title': 'TestTask',
        'description': 'TestDescription'}

    create_response = client.post('/api/tasks/', created_data)

    assert create_response.status_code == 201
    assert create_response.data['title'] == 'TestTask'
    assert create_response.data['description'] == 'TestDescription'

    task_id = create_response.data['id']

    #2 Get list of tasks
    list_response = client.get('/api/tasks/')
    assert list_response.status_code == 200

    #3 Update task

    update_data = {
        'title': 'UpdateTask',
        'description': 'UpdateDescription'
    }

    update_response = client.put(f'/api/tasks/{task_id}/', data=update_data)
    assert update_response.status_code == 200
    assert update_response.data['title'] == 'UpdateTask'
    assert update_response.data['description'] == 'UpdateDescription'

    #4 Delete task
    delete_response = client.delete(f'/api/tasks/{task_id}/')
    assert delete_response.status_code == 204

@pytest.mark.django_db
def test_user_cannot_access_another_user_task():

    client = APIClient()

    user1 = User.objects.create_user(username='user1', password='password1234')
    user2 = User.objects.create_user(username='user2', password='password6789')

    response = client.post('/api/token/', data={'username': 'user1', 'password':'password1234'})
    token1 = response.data['access']
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + token1)

    create_task_user1 = client.post('/api/tasks/', {'title': 'TaskUser1',
                                                         'description': 'Task for user1'})

    task_id = create_task_user1.data['id']

    response2 = client.post('/api/token/', data={'username': 'user2', 'password':'password6789'})
    token2 = response2.data['access']
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + token2)

    get_response = client.get(f'/api/tasks/{task_id}/')
    assert get_response.status_code == 404

    delete_response = client.delete(f'/api/tasks/{task_id}/')
    assert delete_response.status_code == 404
