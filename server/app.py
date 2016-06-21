import falcon
import imp

champion_model = imp.load_source('champion', 'src/models/champion.py')
Champion = champion_model.Champion
Base = champion_model.Base

api = application = falcon.API()

champion_cont = imp.load_source('champions', 'src/controllers/champions.py')

# champions_index = champion_cont.ChampionIndex()

champion_show = champion_cont.ChampionShow()

# api.add_route('/heroes', heroes_index)
api.add_route('/champions/{name}', champion_show)
