from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root():
    markers = [
        {
            'lat': 50.07438247049003,
            'lon': 19.997914202272927,
            'popup': 'Kraków'
        },
        {
            'lat': 49.66470807332711,
            'lon': 19.17558698086457,
            'popup': 'Żywiec'
        },
        {
            'lat': 48.1827046149569,
            'lon': 17.133237368382456,
            'popup': 'Bratislava'
        },
        {
            'lat': 47.87307534835404,
            'lon': 18.197423518835084,
            'popup': 'Hurbanovo'
        },
        {
            'lat': 47.71120416869094,
            'lon': 19.126217731112206,
            'popup': 'Budapest'
        },
        {
            'lat': 44.480767378960685,
            'lon': 26.07425147903249,
            'popup': 'București'
        },
        {
            'lat': 42.44547383474794,
            'lon': 25.633728801974815,
            'popup': 'Stara Zagora'
        },
        {
            'lat': 42.643794944227125,
            'lon': 23.40063672394767,
            'popup': 'Sofia'
        },
        {
            'lat': 37.98489198757109,
            'lon': 23.676490299886968,
            'popup': 'Athens'
        },
        {
            'lat': 44.25118634534947,
            'lon': 22.208442225264704,
            'popup': 'Zaječar'
        },
        {
            'lat': 44.82192308928189,
            'lon': 20.39635386431966,
            'popup': 'Belgrade'
        },
        {
            'lat': 45.749508006799815,
            'lon': 15.465696602856067,
            'popup': 'Karlovac'
        },
        {
            'lat': 46.062214030663256,
            'lon': 14.50093429464718,
            'popup': 'Ljubljana'
        },
        {
            'lat': 48.06984411136749,
            'lon': 16.56522651242416,
            'popup': 'Sopron'
        },
        {
            'lat': 48.14630007558788,
            'lon': 16.467222905009013,
            'popup': 'Schwechat'
        },
        {
            'lat': 48.289750595199365,
            'lon': 14.308549557870531,
            'popup': 'Linz'
        },
        {
            'lat': 46.8475877471935,
            'lon': 9.523248766357897,
            'popup': 'Chur'
        },
        {
            'lat': 47.081653465337304,
            'lon': 8.313594009938567,
            'popup': 'Lucerne'
        },
        {
            'lat': 45.607831043104106,
            'lon': 9.663346355674525,
            'popup': 'Bergamo'
        },
        {
            'lat': 45.736680316609316,
            'lon': 7.366676075070608,
            'popup': 'Aosta'
        },
        {
            'lat': 43.43069870310304,
            'lon': 5.395644154396415,
            'popup': 'Marseille'
        },
        {
            'lat': 40.51958783235161,
            'lon': -3.7083059974097425,
            'popup': 'Madrid'
        },
        {
            'lat': 37.409030671599716,
            'lon': -5.961071949709163,
            'popup': 'Seville'
        },
        {
            'lat': 38.86188832561436,
            'lon': -9.099241501422123,
            'popup': 'Vialonga'
        },
        {
            'lat': 50.23668343590079,
            'lon': 2.0318396824581444,
            'popup': 'Rueil - Malmaison'
        },
        {
            'lat': 49.89819101775653,
            'lon': 7.3052767541486565,
            'popup': 'Schiltigheim'
        },
        {
            'lat': 51.89346132201856,
            'lon': 2.8228552432117135,
            'popup': 'Mons - en - Barœul'
        }, {
            'lat': 51.060833345413975,
            'lon': 4.45364956441463,
            'popup': 'Mechelen'
        },
        {
            'lat': 51.00772186831265,
            'lon': 5.3009700522357495,
            'popup': 'Alken'
        },
        {
            'lat': 52.153791414700535,
            'lon': 4.522329113258527,
            'popup': 'Zoeterwoude'
        },
        {
            'lat': 52.37567574340661,
            'lon': 4.89174436645768,
            'popup': 'Amsterdam'
        },
        {
            'lat': 52.646674520129814,
            'lon': 13.459194294628634,
            'popup': 'Berlin'
        },
        {
            'lat': 50.62187892831178,
            'lon': 13.700893493747778,
            'popup': 'Krušovice'
        },
        {
            'lat': 50.31419312188857,
            'lon': 14.447964015048651,
            'popup': 'Praha'
        },
        {
            'lat': 49.17292392847964,
            'lon': 16.641296706293957,
            'popup': 'Brno'
        }

        # PL    Kraków
        # PL    Żywiec
        # SK    Bratislava
        # SK    Hurbanovo
        # HU    Budapest
        # RO    Bucuresti
        # BG    Stara Zagora
        # BG    Sofia
        # GR    Athens
        # RS    Zaječar
        # RS    Belgrade
        # HR    Karlovac
        # SI    Ljubljana
        # HU    Sopron
        # AT    Schwechat
        # AT    Linz
        # CH    Chur
        # CH    Lucerne
        # IT    Bergamo
        # IT    Aosta
        # FR    Marseille
        # ES    Madrid
        # ES    Seville
        # PT    Vialonga
        # FR    Rueil - Malmaison
        # FR    Schiltigheim
        # FR    Mons - en - Barœul
        # BE    Mechelen
        # BE    Alken
        # NL    Zoeterwoude
        # NL    Amsterdam
        # DE    Berlin
        # CZ    Krušovice
        # CZ    Praha
        # CZ    Brno

    ]
    return render_template('index.html', markers=markers)


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
