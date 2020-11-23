from django.test import TestCase, Client
from user.models import User
from problem.models import Problem, Solution
from analysis.models import SolutionReport
import json


class AnalysisTestCase(TestCase):
    def test_user_report_view(self):
        client = Client()

        User.objects.create_user(
            username="test", password="123", email="test@test.com", salt="123", role=1
        )
        client.login(username="test", password="123")

        problem1 = Problem(desc="For test", input_desc="For test",
                           output_desc="Fore test", pid="ITP1_6_B", objective=1)
        problem1.save()

        problem2 = Problem(desc="For test", input_desc="For test",
                           output_desc="Fore test", pid="ITP2_3_B", objective=1)
        problem2.save()

        solution1_body = {
            "erase_cnt": 12,
            "elapsed_time": 30,
            "evaluation": 66.0,
            "code": "n=int(input())\na=[[0 for i in range(13)]for j in range(4)]\nfor k in range(n):\ncard=input().split()\np=5\nif (card[0]=='S'):\np=0\nelif (card[0]=='H':\np=1\nelif (card[0]=='C'):\np=2\nelse:\np=3\nq=int(card[1])-1\na[p][q]=1\nfor i in range(4):\nfor j in range(13):\nif a[i][j]==0:\ntype=''\nif i==0 :\ntype='S'\nelif i==1:\ntype='H'\nelif i==2:\ntype='C'\nelse:\ntype='D'\nprint('{0} {1}'.format(type,j+1))",
        }

        response = client.post(
            "/api/problem/1/solution/",
            json.dumps(solution1_body),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 204)

        solution2_body = {
            "erase_cnt": 12,
            "elapsed_time": 30,
            "evaluation": 66.0,
            "code": "n=int(input())\na=[[0 for i in range(13)]for j in range(4)]\nfor k in range(n):\ncard=input().split()\np=5\nif (card[0]=='S'):\np=0\nelif (card[0]=='H':\np=1\nelif (card[0]=='C'):\np=2\nelse:\np=3\nq=int(card[1])-1\na[p][q]=1\nfor i in range(4):\nfor j in range(13):\nif a[i][j]==0:\ntype=''\nif i==0 :\ntype='S'\nelif i==1:\ntype='H'\nelif i==2:\ntype='C'\nelse:\ntype='D'\nprint('{0} {1}'.format(type,j+1))",
        }

        response = client.post(
            "/api/problem/2/solution/",
            json.dumps(solution2_body),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 204)

        client.post("/api/analysis/")
        self.assertEqual(response.status_code, 204)

    def test_user_report_analysis_exception(self):
        client = Client()

        User.objects.create_user(
            username="test", password="123", email="test@test.com", salt="123", role=1
        )
        client.login(username="test", password="123")

        res = client.put("/api/analysis/", {})

        self.assertEqual(res.status_code, 405)
