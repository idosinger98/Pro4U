from django.db import models
from django.utils import timezone
from account.models.professional import Professional
from account.models.client import Client
# from django.db.models import Max


class SearchHistory(models.Model):
    search_id = models.BigAutoField(primary_key=True)
    professional_id = models.ForeignKey(Professional, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'SearchHistory'
        permissions = [
            ('create_search_history', 'Can create search history'),
        ]

    def __str__(self):
        return f"{self.client_id} search {self.professional_id} [{self.date}]"

    @staticmethod
    def create_new_search_history(client_id, professional_id):
        search_history = SearchHistory(client_id=client_id, professional_id=professional_id)
        search_history.save()

        return search_history

    @staticmethod
    def get_last_professionals_search_by_client(client_id, expected_result=5):
        return SearchHistory.objects.filter(client_id=client_id).order_by('-date')[:expected_result]

        # lst = lst.annotate(max_date=Max('date')).order_by('-max_date')[:expected_result]
        # lst = [row['professional_id'] for row in lst]
        # return  lst
