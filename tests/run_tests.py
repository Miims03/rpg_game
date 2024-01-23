import unittest
import sys
import os

# Ajouter le répertoire racine du projet au chemin de recherche des modules
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, project_root)

def run_tests():

    # Charger et exécuter tous les tests dans le module unittest
    loader = unittest.TestLoader()
    suite = loader.discover(project_root)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

if __name__ == "__main__":
    run_tests()