import unittest
from main import toTitleCase

class TitleTestCase(unittest.TestCase):
    def test_strings(self):
        tests = [
            ("see spot run. run spot run!", "See Spot Run. Run Spot Run!"),
            ("unsolved mystery of the xviii century", "Unsolved Mystery of the XVIII Century"),
            ("how to interpret \"the hitchhiker's guide to the galaxy\"", "How to Interpret \"The Hitchhiker's Guide to the Galaxy\""),
            ("snow white\nand the seven dwarfs", "Snow White and the Seven Dwarfs"),
            ("newcastle upon tyne","Newcastle upon Tyne"),
            ("brighton on sea ","Brighton on Sea"),
            ("A dog's Tale","A Dog's Tale"),
            ("the last of the mohicans","The Last of the Mohicans"),
            ("how to be smart","How to Be Smart"),
            ("about a boy", "About a Boy"),
            ("reading \'fight club\' through a postmodernist lens", "Reading \'Fight Club\' Through a Postmodernist Lens"),
            ("I'm Henry VIII i am. henry viii i am, I am.", "I'm Henry VIII I Am. Henry VIII I Am, I Am."),
        ]
        for test in tests:
            self.assertEqual(toTitleCase(test[0]), test[1])

if __name__ == '__main__':
    unittest.main()
