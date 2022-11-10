
 p1 = Player(firstname='Tim'
                    , lastname='Mossuz'
                    , username='jack1'
                    , age=19
                    , password='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055')
        p1.save()

        game_master_p1 = GameMaster(username='jack1')
        basic_player_p1 = BasicPlayer(username='jack1')
        
        scen1p1 = Scenario(name='The scary movie'
                            , description='Come with us play on a movie'
                            , username='jack1')

        game_master_p1.add_scenario(scen1p1)

        p1.game_master = game_master_p1
        p1.basic_player = basic_player_p1
        p1.tables = [27]
        p1.halfday = [2]

        p2 = Player(firstname='Jean'
                    , lastname='Valjean'
                    , username='jack2'
                    , age=19
                    , password='5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055')
        p2.save()

        game_master_p2 = GameMaster(username='jack2')
        basic_player_p2 = BasicPlayer(username='jack2')
        
        char1p2 = Character(name='cafej2'
                            , level=3
                            , race='rogue'
                            , equipment='pony'
                            , skill='longswords'
                            , id=4
                            , username='jack2')


        basic_player_p2.add_character(char1p2)

        p2.basic_player = basic_player_p2
        p2.game_master = game_master_p2
        p2.tables = [27]
        p2.halfday = [2]

        id_scenario = scen1p1.id
        id_game = 27

        expected_table = Table(half_day=2
                                , active=True
                                , id=27)
        
        expected_table.scenario = scen1p1
        expected_table.characters.append(char1p2)
        expected_table.players.append(p1)
        expected_table.players.append(p2)

        # WHEN
        add_game_master = TableDao().add_gm_to_table(id_scenario,id_game)
        loaded_table_after_added_gm = TableDao().load(id_game)
