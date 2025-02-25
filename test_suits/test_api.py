import pytest
import requests
import sys
import os

BASE_URL = "https://jsonplaceholder.typicode.com"

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from test_suits.base_test import BaseTest  
class TestAPI(BaseTest):
    
    def test_get_users(self):
        """Test to verify the GET /users API"""
        self.logger.info("Starting test: test_get_users")
        try:
            response = requests.get(f"{BASE_URL}/users")
            self.logger.info(f"GET /users - Status Code: {response.status_code}")
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            assert len(response.json()) > 0, "Expected non-empty response, but got empty"
            self.logger.info("Successfully validated GET /users response.")
        except Exception as e:
            self.logger.error(f"Test test_get_users failed: {str(e)}")
            raise

    def test_create_user(self):
        """Test to verify the POST /users API"""
        self.logger.info("Starting test: test_create_user")
        try:
            payload = {
                "name": "John Doe",
                "username": "johndoe",
                "email": "johndoe@example.com"
            }
            response = requests.post(f"{BASE_URL}/users", json=payload)
            self.logger.info(f"POST /users - Status Code: {response.status_code}")
            assert response.status_code == 201, f"Expected 201, got {response.status_code}"
            response_data = response.json()
            assert response_data["name"] == "John Doe", "User creation response does not match"
            self.logger.info("Successfully created new user.")
        except Exception as e:
            self.logger.error(f"Test test_create_user failed: {str(e)}")
            raise

    def test_update_user(self):
        """Test to verify the PUT /users API"""
        self.logger.info("Starting test: test_update_user")
        try:
            user_id = 1
            payload = {
                "name": "Jane Doe",
                "username": "janedoe",
                "email": "janedoe@example.com"
            }
            response = requests.put(f"{BASE_URL}/users/{user_id}", json=payload)
            self.logger.info(f"PUT /users/{user_id} - Status Code: {response.status_code}")
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            response_data = response.json()
            assert response_data["name"] == "Jane Doe", "User update response does not match"
            self.logger.info("Successfully updated user.")
        except Exception as e:
            self.logger.error(f"Test test_update_user failed: {str(e)}")
            raise

    def test_delete_user(self):
        """Test to verify the DELETE /users API"""
        self.logger.info("Starting test: test_delete_user")
        try:
            user_id = 1
            response = requests.delete(f"{BASE_URL}/users/{user_id}")
            self.logger.info(f"DELETE /users/{user_id} - Status Code: {response.status_code}")
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            assert response.json() == {}, "Expected empty JSON response after deletion"
            self.logger.info("Successfully deleted user.")
        except Exception as e:
            self.logger.error(f"Test test_delete_user failed: {str(e)}")
            raise
