from rest_framework.test import APITestCase
from rest_framework import status
from produto.models import Produto

class ProdutoAPI(APITestCase):


    def test_create_ok(self):
        data_input = \
        {
            "nome": "Perfume",
            "descricao": "Cheiroso",
        }

        response = self.client.post('/produto/', data=data_input)

        data_response = \
        {
            "id": Produto.objects.get(nome="Perfume").id,
            "nome": "Perfume",
            "descricao": "Cheiroso",
            "foto_b64": "",
            "validade": 2,
            "unidade_validade": "Anos",
            "peso": 0,
            "unidade_peso": "gramas",
            "codigo_barras": "",
            "codigo_revista": "",
            "obs": ""
        }

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 11)
        self.assertEqual(response.data, data_response)


    def test_create_not_unique(self):
        data_input = \
        {
            "nome": "Perfume",
            "descricao": "Cheiroso",
        }

        response1 = self.client.post('/produto/', data=data_input)

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)

        response2 = self.client.post('/produto/', data=data_input)

        data_response = \
        {
            'nome': ['produto with this nome already exists.']
        }

        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(response2.data), 1)
        self.assertEqual(response2.data, data_response)