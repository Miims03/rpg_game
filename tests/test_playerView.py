import unittest
from view.player_view import *




class TestPlayer(unittest.TestCase):

    def setUp(self):
        
        self.player = Player(name="player1")
        self.player.pv_max = 99
        self.player.pv = 99
        self.player.stamina = 2
        self.player.mana_max = 200
        self.form = PlayerView(self.player)
        
    
    def test_view_player(self):
        self.form.show()
        self.app.exec()
        pv_expected = 0
        for _ in range(self.player.pv_max):
            self.player.pv=self.player.pv-1
            self.form.update_progressBar()
        print("player pv ",self.form.actor.pv)
        self.assertEqual(self.player.pv, pv_expected)
        self.assertEqual(self.player, self.form.actor)
        
        
  
if __name__ == '__main__':
    unittest.main()