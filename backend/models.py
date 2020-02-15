from django.db import models
from grappelli_extras.models import base
from django.contrib.auth.models import User


class Account(base):
    """
        account for journals
    """
    code = models.CharField(max_length=65, null=True, blank=True)
    name = models.CharField(max_length=165, null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return "-".join([self.code or "", self.name or ""])


class Document(base):
    """
        accounting general document
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    date = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    number = models.CharField(max_length=25, null=True, blank=True)
    concept = models.TextField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.number


class Journal(base):
    """
        journals for accounting.
        debit --
        credit ++
    """
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="account_journals")
    debit = models.FloatField(default=0.0)
    credit = models.FloatField(default=0.0)

    def __str__(self):
        return ""

