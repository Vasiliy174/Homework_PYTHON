import requests
import pytest

#Тест для метода [POST]/api-v2/projects:


def test_create_project():
    url = 'https://ru.yougile.com/api-v2/projects'
    data = {
        "title": "Тестирование ресурса YuoGile"
        }
    response = requests.post(url, json=data)
    assert response.status_code == 201
    assert id in response.json()

#Тест для метода [GET]/api-v2/projects:


def test_get_projects():
    url = 'https://ru.yougile.com/api-v2/projects'
    response = requests.get(url)
    assert response.status_code == 200
    assert 'projects' in response.json()

#Тест для метода [PUT]/api-v2/projects/{id}:


def test_update_project():
    project_id = 'f5c59ecd-71f9-4b93-a5c8-597bd9460de0'
    # Заменить на существующий ID проекта
    url = f'https://ru.yougile.com/api-v2/projects/{project_id}'
    data = {
        "title": "Тестирование_YuoGile_1"
    }
    response = requests.put(url, json=data)
    assert response.status_code == 200


#Тест для метода [GET]/api-v2/projects/{id}:

def test_get_project_by_id():
    project_id = 'f5c59ecd-71f9-4b93-a5c8-597bd9460de0'
    # Заменить на существующий ID проекта
    url = f'https://ru.yougile.com/api-v2/projects/{project_id}'
    response = requests.get(url)
    assert response.status_code == 200
    assert 'name' in response.json()
