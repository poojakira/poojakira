import unittest

from scripts.verify_profile import PORTFOLIO, RESUME, validate_portfolio_links


class ProfileLinksTest(unittest.TestCase):
    def test_generated_resume_link(self):
        text = f'<a href="{PORTFOLIO}">Site</a><a href="{RESUME}">Résumé</a>'
        self.assertEqual(validate_portfolio_links(text), [])

    def test_legacy_resume_link_is_rejected(self):
        legacy = PORTFOLIO + "Pooja_Kiran_Security_Engineer_Resume.pdf"
        text = f'<a href="{PORTFOLIO}">Site</a><a href="{legacy}">Résumé</a>'
        self.assertTrue(validate_portfolio_links(text))
