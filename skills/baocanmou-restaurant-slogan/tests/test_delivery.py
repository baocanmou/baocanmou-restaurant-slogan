import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('checker', ROOT/'scripts/check_delivery.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class DeliveryTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT/'examples/delivery.json').read_text(encoding='utf-8'))

    def errors(self):
        return checker.check(self.data)['errors']

    def test_complete_example(self):
        self.assertTrue(checker.check(self.data)['passed'])

    def test_multiple_declared_media_are_valid(self):
        self.data['brief']['primary_medium'] = ['菜单首页', '店内海报']
        self.assertTrue(checker.check(self.data)['passed'])

    def test_invalid_media_list_is_visible(self):
        self.data['brief']['primary_medium'] = ['菜单首页', None]
        self.assertTrue(any('primary_medium' in e for e in self.errors()))

    def test_duplicate_master_cannot_substitute_for_tenth(self):
        self.data['candidates'][-1]['master_id'] = 'ogilvy'
        self.assertTrue(any('exactly once' in e for e in self.errors()))

    def test_duplicate_wording_is_not_two_solutions(self):
        self.data['candidates'][2]['line'] = self.data['candidates'][0]['line'].replace('，',' ')
        self.assertTrue(any('duplicate slogan' in e for e in self.errors()))

    def test_new_recommendation_not_in_ten_is_rejected(self):
        self.data['recommendations'][0]['candidate_id'] = 'C11'
        self.assertTrue(any('unique listed candidate' in e for e in self.errors()))

    def test_conditional_usp_cannot_be_recommended(self):
        self.data['recommendations'][0]['candidate_id'] = 'C02'
        self.assertTrue(any('only eligible' in e for e in self.errors()))

    def test_unknown_fact_cannot_be_declared_ready(self):
        self.data['candidates'][1]['eligibility'] = 'eligible'
        self.assertTrue(any('unknown facts' in e for e in self.errors()))

    def test_lost_fact_reference_is_visible(self):
        self.data['brief']['facts'] = self.data['brief']['facts'][1:]
        self.assertTrue(any('valid fact_ids' in e for e in self.errors()))

    def test_fictional_evidence_cannot_lose_label(self):
        self.data['brief'].pop('fictional')
        self.assertTrue(any('fictional brief label' in e for e in self.errors()))

    def test_fewer_than_three_is_not_complete(self):
        self.data['recommendations'].pop()
        self.assertTrue(any('exactly 3' in e for e in self.errors()))

    def test_honest_partial_delivery_is_allowed(self):
        self.data['recommendations'].pop()
        self.data['status'] = 'partial'
        self.data['shortage_reason'] = '第三条所需经营事实尚未确认。'
        self.assertTrue(checker.check(self.data)['passed'])

    def test_malformed_data_has_readable_failure(self):
        self.assertFalse(checker.check([])['passed'])


if __name__ == '__main__':
    unittest.main()
