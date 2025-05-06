from django.test import TestCase
from banks.models import Bank, Branch

class BankModelTest(TestCase):
    def setUp(self):
        self.bank = Bank.objects.create(id=1, name='Test Bank')
        Branch.objects.create(
            ifsc='TEST0001',
            bank=self.bank,
            branch='Main',
            address='123 Street',
            city='TestCity',
            district='TestDistrict',
            state='TestState'
        )

    def test_branch_creation(self):
        branch = Branch.objects.get(ifsc='TEST0001')
        self.assertEqual(branch.bank.name, 'Test Bank')
