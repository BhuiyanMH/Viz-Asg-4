import pycountry_convert as pc
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#read the data frame
df = pd.read_csv('gender.csv')

def get_continent(country_code):
    '''
    :param country_code: ISO 3166-1 alpha-3 country code of a country
    :return: the name of the continent to which the country belongs, 'Unknown' if the country code is not valid
    '''

    continent_names = {

        'NA': 'North America',
        'SA': 'South America',
        'AS': 'Asia',
        'OC': 'Oceania',
        'AF': 'Africa',
        'AN': 'Antarctica',
        'EU': 'Europe'
    }

    try:
        continent_code = pc.country_alpha2_to_continent_code(pc.country_alpha3_to_country_alpha2(country_code))
        continent = continent_names[continent_code]
    except:
        continent = 'Unknown'

    return continent

#create a new column named Continent
df['Continent'] = df['Country Code'].apply(get_continent)

df = df[(df.Continent != 'Unknown')]

df.to_csv('gender_with_continent.csv', index=False)

