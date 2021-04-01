import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "user-agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}


def get_general_data(headers):
    '''
    Funcion que extrae los datos generales de cada pokemon
    :param headers: Parametro que define el user-agent
    :return: devuelve un dataframe con los datos extraidos de la web
    '''

    pokemon_name_list = []
    pokemon_evolution_list = []
    pokemon_type_list = []
    pokemon_total_list = []
    pokemon_hp_list = []
    pokemon_attack_list = []
    pokemon_defense_list = []
    pokemon_sp_atk_list = []
    pokemon_sp_def_list = []
    pokemon_speed_list = []
    # details
    species_list = []
    height_list = []
    weight_list = []
    abilities_list = []
    ev_yield_list = []
    catch_rate_list = []
    base_friendship_list = []
    base_experience_list = []
    growth_rate_list = []
    eggs_groups_list = []
    gender_rate_list = []
    eggs_cycles_rate_list = []

    # url = "http://www.frikea.es/PrecioCartasPokemon.php?cate=349"
    url = "https://pokemondb.net/pokedex/all"
    url_details = "https://pokemondb.net/pokedex/"

    # https://stackoverflow.com/questions/23013220/max-retries-exceeded-with-url-in-requests
    try:
        respuesta = requests.get(url, headers=headers)
        print(respuesta.status_code)
    except requests.exceptions.ConnectionError:
        status_code = "Connection refused"
        print(status_code)

    soup = BeautifulSoup(respuesta.text, 'html.parser')

    pokemon_table = soup.find('table', id='pokedex')

    for pokemon in pokemon_table.find_all('tbody'):
        rows = pokemon.find_all('tr')
        for row in rows:
            pokemon = row.find('td', class_='cell-name')
            pokemon_name = pokemon.find('a', class_='ent-name').text
            pokemon_ref = pokemon.find('a', class_='ent-name').get('href')
            print(pokemon_ref)

            pokemon_type = row.find_all('td', class_='cell-icon')[0].text
            try:
                pokemon_evolution = row.find(class_='text-muted').text
            except AttributeError as err:
                pokemon_evolution = " "

            pokemon_total = row.find('td', class_='cell-total').text
            pokemon_hp = row.find_all('td', class_='cell-num')[1].text
            pokemon_attack = row.find_all('td', class_='cell-num')[2].text
            pokemon_defense = row.find_all('td', class_='cell-num')[3].text
            pokemon_sp_atk = row.find_all('td', class_='cell-num')[4].text
            pokemon_sp_def = row.find_all('td', class_='cell-num')[5].text
            pokemon_speed = row.find_all('td', class_='cell-num')[6].text

            pokemon_name_list.append(pokemon_name)
            pokemon_evolution_list.append(pokemon_evolution)
            pokemon_type_list.append(pokemon_type)
            pokemon_total_list.append(pokemon_total)
            pokemon_hp_list.append(pokemon_hp)
            pokemon_attack_list.append(pokemon_attack)
            pokemon_defense_list.append(pokemon_defense)
            pokemon_sp_atk_list.append(pokemon_sp_atk)
            pokemon_sp_def_list.append(pokemon_sp_def)
            pokemon_speed_list.append(pokemon_speed)


            pokemon_details_list = get_detailed_data(headers, pokemon_ref)

            species_list.append(pokemon_details_list[0])
            height_list.append(pokemon_details_list[1])
            weight_list.append(pokemon_details_list[2])
            abilities_list.append(pokemon_details_list[3])
            ev_yield_list.append(pokemon_details_list[4])
            catch_rate_list.append(pokemon_details_list[5])
            base_friendship_list.append(pokemon_details_list[6])
            base_experience_list.append(pokemon_details_list[7])
            growth_rate_list.append(pokemon_details_list[8])
            eggs_groups_list.append(pokemon_details_list[9])
            gender_rate_list.append(pokemon_details_list[10])
            eggs_cycles_rate_list.append(pokemon_details_list[11])

    df = pd.DataFrame(
        {'Name': pokemon_name_list,
         'Evolution': pokemon_evolution_list,
         'Type': pokemon_type_list,
         'Total': pokemon_total_list,
         'HP': pokemon_hp_list,
         'Attack': pokemon_attack_list,
         'Defense': pokemon_defense_list,
         'Sp.Atk': pokemon_sp_atk_list,
         'Sp.Def': pokemon_sp_def_list,
         'Speed': pokemon_speed_list,
         'Species': species_list,
         'Height': height_list,
         'Weight': weight_list,
         'abilities': abilities_list,
         'ev_yield': ev_yield_list,
         'catch_rate': catch_rate_list,
         'base_friendship': base_friendship_list,
         'base_experience': base_experience_list,
         'growth_rate': growth_rate_list,
         'eggs_groups': eggs_groups_list,
         'gender_rate': gender_rate_list,
         'eggs_cycles_rate': eggs_cycles_rate_list,
         })

    return df


def get_detailed_data(headers, pokemon_ref):
    '''
    :param headers:
    :param pokemon_name:
    :return:
    '''


    url_details = "https://pokemondb.net"+pokemon_ref
    print(url_details)
    respuesta_details = requests.get(url_details, headers=headers)
    soup_details = BeautifulSoup(respuesta_details.text, 'html.parser')

    pokemon_data = soup_details.find_all('table', class_='vitals-table')

    for item in pokemon_data[0].find_all('tbody'):
        rows = item.find_all('tr')

        species = rows[2].find('td').text.strip()
        height = rows[3].find('td').text.strip()
        weight = rows[4].find('td').text.strip()
        abilities = rows[5].find('td').text.strip()

    for item in pokemon_data[1].find_all('tbody'):
        rows = item.find_all('tr')

        ev_yield = rows[0].find('td').text.strip()
        catch_rate = rows[1].find('td').text.strip()
        base_friendship = rows[2].find('td').text.strip()
        base_experience = rows[3].find('td').text.strip()
        growth_rate = rows[4].find('td').text.strip()

    for item in pokemon_data[2].find_all('tbody'):
        rows = item.find_all('tr')
        eggs_groups = rows[0].find('td').text.strip()
        gender_rate = rows[1].find('td').text.strip()
        eggs_cycles_rate = rows[2].find('td').text.strip()

    detailed_data_list = [
        species, height, weight,
        abilities, ev_yield, catch_rate,
        base_friendship, base_experience,
        growth_rate, eggs_groups, gender_rate,
        eggs_cycles_rate
    ]

    return detailed_data_list


pokemon_df = get_general_data(headers)
pokemon_df.to_csv('pokemon.csv', encoding='utf-8-sig')
