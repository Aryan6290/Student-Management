import json
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.



class StudentTest(APITestCase):
    def testgetAll(self):
        response = self.client.get('/api/all')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def testAddStudent(self):
        data={
    "id": 6,
    "name": "anhi",
    "grade": 9,
    "section": "C",
    "roll": 30
}
        print(data)
        response = self.client.post('/api/add',data=json.dumps(data),
                                content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


          
