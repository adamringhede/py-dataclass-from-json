import unittest

import fromjson


class TestFromJson(unittest.TestCase):

    def test_create_dataclasses(self):
        code = fromjson.generate("""
            {
                "minions": [
                    {
                        "name": "evil minion"
                    },
                    {
                        "name": "very evil minion"
                    }
                ]
            }
            """.strip(), name="Boss")
        self.assertEqual(code.strip(), """
@dataclass
class Minion():
    name: str


@dataclass
class Boss():
    minions: List[Minion]
""".strip())
