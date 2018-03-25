

```python
from citipy import citipy
import matplotlib.pyplot as plt
import pandas as pd
import random
import requests
from pylab import figure
```


```python
city = citipy.WORLD_CITIES_DICT
```


```python
cities=[]
city_names= []
country_codes =[]
latitudes = []
longitudes = []
temperature = []
humidity = []
wind_speed = []
clouds = []
coordinates_list = list(city.keys())
for i in range(500):
    random_city= random.choice(coordinates_list)
    cities.append(random_city)
    near_by_city= citipy.nearest_city(*cities[i])
    country_codes.append(near_by_city.country_code)
    city_names.append(near_by_city.city_name)
    lat,lon = cities[i]
    latitudes.append(lat)
    longitudes.append(lon)
    url = "http://api.openweathermap.org/data/2.5/weather?"
    query_url = url + "lat=" + str(latitudes[i]) + "&lon=" + str(longitudes[i])+"&APPID=413085cb59d82f11b14672ef99d1e023"+"&units = metric"
    weather_response = requests.get(query_url)
    weather_json = weather_response.json()
    print(f"we are looking in to data for: {city_names[i]}.")
    print(query_url)
    temperature.append(weather_json["main"]["temp"])
    humidity.append(weather_json["main"]["humidity"])
    wind_speed.append(weather_json["wind"]["speed"])
    clouds.append(weather_json["clouds"]["all"])
```

    we are looking in to data for: beach park.
    http://api.openweathermap.org/data/2.5/weather?lat=42.4222222&lon=-87.8572222&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: galashiels.
    http://api.openweathermap.org/data/2.5/weather?lat=55.6&lon=-2.816667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bato.
    http://api.openweathermap.org/data/2.5/weather?lat=10.825&lon=119.471&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: guindulman.
    http://api.openweathermap.org/data/2.5/weather?lat=9.7629&lon=124.4878&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: saquisili.
    http://api.openweathermap.org/data/2.5/weather?lat=-0.8333333&lon=-78.6666667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: karlsfeld.
    http://api.openweathermap.org/data/2.5/weather?lat=48.216667&lon=11.466667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sao jose do rio pardo.
    http://api.openweathermap.org/data/2.5/weather?lat=-21.6&lon=-46.9&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: scarisoara.
    http://api.openweathermap.org/data/2.5/weather?lat=44.0&lon=24.566667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: iskenderun.
    http://api.openweathermap.org/data/2.5/weather?lat=36.587185&lon=36.173468&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: charsadda.
    http://api.openweathermap.org/data/2.5/weather?lat=34.143453&lon=71.731731&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: gheorgheni.
    http://api.openweathermap.org/data/2.5/weather?lat=46.716667&lon=25.616667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: jaltenango.
    http://api.openweathermap.org/data/2.5/weather?lat=15.916667&lon=-92.716667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: dera ismail khan.
    http://api.openweathermap.org/data/2.5/weather?lat=31.832691&lon=70.902398&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ribeirao.
    http://api.openweathermap.org/data/2.5/weather?lat=41.360807&lon=-8.567738&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: karben.
    http://api.openweathermap.org/data/2.5/weather?lat=50.233333&lon=8.75&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: grants.
    http://api.openweathermap.org/data/2.5/weather?lat=35.1472222&lon=-107.8508333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: changzhou.
    http://api.openweathermap.org/data/2.5/weather?lat=31.783333&lon=119.966667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: stari banovci.
    http://api.openweathermap.org/data/2.5/weather?lat=44.986389&lon=20.286667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: suslonger.
    http://api.openweathermap.org/data/2.5/weather?lat=56.315556&lon=48.253056&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: porto calvo.
    http://api.openweathermap.org/data/2.5/weather?lat=-9.066667&lon=-35.4&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: malaga.
    http://api.openweathermap.org/data/2.5/weather?lat=36.726666&lon=-4.434802&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: la romana.
    http://api.openweathermap.org/data/2.5/weather?lat=18.4166667&lon=-68.9666667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: peplos.
    http://api.openweathermap.org/data/2.5/weather?lat=40.9583333&lon=26.2655556&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: baixa grande.
    http://api.openweathermap.org/data/2.5/weather?lat=-11.95&lon=-40.183333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: parfenyevo.
    http://api.openweathermap.org/data/2.5/weather?lat=58.483958&lon=43.408764&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: dao.
    http://api.openweathermap.org/data/2.5/weather?lat=12.0998&lon=125.4372&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bremervorde.
    http://api.openweathermap.org/data/2.5/weather?lat=53.483333&lon=9.133333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bryansk.
    http://api.openweathermap.org/data/2.5/weather?lat=53.252089&lon=34.371666&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sallaumines.
    http://api.openweathermap.org/data/2.5/weather?lat=50.417491&lon=2.861742&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: cestas.
    http://api.openweathermap.org/data/2.5/weather?lat=44.743446&lon=-0.67905&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: usilampatti.
    http://api.openweathermap.org/data/2.5/weather?lat=9.966667&lon=77.8&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: manzanares.
    http://api.openweathermap.org/data/2.5/weather?lat=5.324722&lon=-75.156944&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: russkoye.
    http://api.openweathermap.org/data/2.5/weather?lat=43.839722&lon=44.615&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: yuki.
    http://api.openweathermap.org/data/2.5/weather?lat=36.3&lon=139.883333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: zambrano.
    http://api.openweathermap.org/data/2.5/weather?lat=9.747238&lon=-74.815298&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: panay.
    http://api.openweathermap.org/data/2.5/weather?lat=6.497778&lon=124.638333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sorso.
    http://api.openweathermap.org/data/2.5/weather?lat=40.8&lon=8.577222&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: rogatica.
    http://api.openweathermap.org/data/2.5/weather?lat=43.8008333&lon=19.0025&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: portmarnock.
    http://api.openweathermap.org/data/2.5/weather?lat=53.4230556&lon=-6.1375&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: narkevychi.
    http://api.openweathermap.org/data/2.5/weather?lat=49.517173&lon=26.641782&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: stangaceaua.
    http://api.openweathermap.org/data/2.5/weather?lat=44.6&lon=23.316667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: feliciano.
    http://api.openweathermap.org/data/2.5/weather?lat=11.5787&lon=122.3583&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: rakai.
    http://api.openweathermap.org/data/2.5/weather?lat=-0.72&lon=31.4838889&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: guio-ang.
    http://api.openweathermap.org/data/2.5/weather?lat=9.7922&lon=124.509&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ceska skalice.
    http://api.openweathermap.org/data/2.5/weather?lat=50.394014&lon=16.049184&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ardesen.
    http://api.openweathermap.org/data/2.5/weather?lat=41.191111&lon=40.9875&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: gangiova.
    http://api.openweathermap.org/data/2.5/weather?lat=43.9&lon=23.85&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: dealu morii.
    http://api.openweathermap.org/data/2.5/weather?lat=46.316667&lon=27.233333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: jaboticabal.
    http://api.openweathermap.org/data/2.5/weather?lat=-21.266667&lon=-48.316667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ibbenburen.
    http://api.openweathermap.org/data/2.5/weather?lat=52.266667&lon=7.733333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: linguere.
    http://api.openweathermap.org/data/2.5/weather?lat=15.4&lon=-15.1166667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sakhnovshchyna.
    http://api.openweathermap.org/data/2.5/weather?lat=49.151664&lon=35.871978&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: xining.
    http://api.openweathermap.org/data/2.5/weather?lat=36.616667&lon=101.766667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: chato.
    http://api.openweathermap.org/data/2.5/weather?lat=-2.6377778&lon=31.7669444&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: turje.
    http://api.openweathermap.org/data/2.5/weather?lat=46.98366&lon=17.107417&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: batasan.
    http://api.openweathermap.org/data/2.5/weather?lat=12.766667&lon=120.783333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: taipu.
    http://api.openweathermap.org/data/2.5/weather?lat=-5.616667&lon=-35.6&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: san juan.
    http://api.openweathermap.org/data/2.5/weather?lat=10.099047&lon=-84.242856&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ukwa.
    http://api.openweathermap.org/data/2.5/weather?lat=21.966667&lon=80.466667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: khrustalnyy.
    http://api.openweathermap.org/data/2.5/weather?lat=44.350556&lon=135.097222&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: lebanon.
    http://api.openweathermap.org/data/2.5/weather?lat=40.3408333&lon=-76.4116667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: portpatrick.
    http://api.openweathermap.org/data/2.5/weather?lat=54.85&lon=-5.116667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: grefrath.
    http://api.openweathermap.org/data/2.5/weather?lat=51.3&lon=6.316667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: manglaur.
    http://api.openweathermap.org/data/2.5/weather?lat=29.8&lon=77.866667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: verkhnya syrovatka.
    http://api.openweathermap.org/data/2.5/weather?lat=50.82902&lon=34.958613&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: baguio.
    http://api.openweathermap.org/data/2.5/weather?lat=16.416389&lon=120.593056&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: cocoyoc.
    http://api.openweathermap.org/data/2.5/weather?lat=18.866667&lon=-98.983333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: samana.
    http://api.openweathermap.org/data/2.5/weather?lat=19.2166667&lon=-69.3166667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: coroata.
    http://api.openweathermap.org/data/2.5/weather?lat=-4.133333&lon=-44.133333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ramgarh.
    http://api.openweathermap.org/data/2.5/weather?lat=27.25&lon=75.183333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: pitmedden.
    http://api.openweathermap.org/data/2.5/weather?lat=57.333333&lon=-2.183333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: maseru.
    http://api.openweathermap.org/data/2.5/weather?lat=-29.3166667&lon=27.4833333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: azagra.
    http://api.openweathermap.org/data/2.5/weather?lat=9.4779&lon=123.1367&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bolotesti.
    http://api.openweathermap.org/data/2.5/weather?lat=45.833333&lon=27.066667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: hanyu.
    http://api.openweathermap.org/data/2.5/weather?lat=36.166667&lon=139.533333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: darpas.
    http://api.openweathermap.org/data/2.5/weather?lat=40.8380556&lon=44.4233333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: lengshuitan.
    http://api.openweathermap.org/data/2.5/weather?lat=26.411098&lon=111.595592&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: dingzhou.
    http://api.openweathermap.org/data/2.5/weather?lat=38.513056&lon=114.995556&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: roncade.
    http://api.openweathermap.org/data/2.5/weather?lat=45.63&lon=12.374167&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: liliw.
    http://api.openweathermap.org/data/2.5/weather?lat=14.1313&lon=121.4362&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: saulesti.
    http://api.openweathermap.org/data/2.5/weather?lat=44.8&lon=23.483333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: itzican.
    http://api.openweathermap.org/data/2.5/weather?lat=20.333333&lon=-102.95&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: yanam.
    http://api.openweathermap.org/data/2.5/weather?lat=16.733333&lon=82.216667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: dracsenei.
    http://api.openweathermap.org/data/2.5/weather?lat=44.216667&lon=24.983333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: palmas.
    http://api.openweathermap.org/data/2.5/weather?lat=-26.5&lon=-52.0&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: hiratsuka.
    http://api.openweathermap.org/data/2.5/weather?lat=35.323056&lon=139.342222&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: tver.
    http://api.openweathermap.org/data/2.5/weather?lat=56.860491&lon=35.876027&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: encarnacion.
    http://api.openweathermap.org/data/2.5/weather?lat=21.516667&lon=-102.233333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: caraycaray.
    http://api.openweathermap.org/data/2.5/weather?lat=11.5551&lon=124.415&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: canete.
    http://api.openweathermap.org/data/2.5/weather?lat=-37.8&lon=-73.383333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: novi bilokorovychi.
    http://api.openweathermap.org/data/2.5/weather?lat=51.115477&lon=28.05463&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sebring.
    http://api.openweathermap.org/data/2.5/weather?lat=27.4952778&lon=-81.4411111&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: lakitelek.
    http://api.openweathermap.org/data/2.5/weather?lat=46.876009&lon=19.995042&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: northbrook.
    http://api.openweathermap.org/data/2.5/weather?lat=39.2463889&lon=-84.5836111&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: nageshwari.
    http://api.openweathermap.org/data/2.5/weather?lat=25.9666667&lon=89.7166667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bihoro.
    http://api.openweathermap.org/data/2.5/weather?lat=43.822778&lon=144.104444&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: aleysk.
    http://api.openweathermap.org/data/2.5/weather?lat=52.4926&lon=82.7822&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: semme.
    http://api.openweathermap.org/data/2.5/weather?lat=15.2&lon=-12.95&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: hotonj.
    http://api.openweathermap.org/data/2.5/weather?lat=43.8947222&lon=18.3727778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ahumada.
    http://api.openweathermap.org/data/2.5/weather?lat=30.616667&lon=-106.516667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: glinka.
    http://api.openweathermap.org/data/2.5/weather?lat=54.64043&lon=32.878109&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ferrara.
    http://api.openweathermap.org/data/2.5/weather?lat=44.833333&lon=11.583333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kroonstad.
    http://api.openweathermap.org/data/2.5/weather?lat=-27.65036&lon=27.234879&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: lae.
    http://api.openweathermap.org/data/2.5/weather?lat=-6.7333333&lon=147.0&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: cuyali.
    http://api.openweathermap.org/data/2.5/weather?lat=13.8833333&lon=-86.55&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: corralillo.
    http://api.openweathermap.org/data/2.5/weather?lat=22.9819444&lon=-80.5855556&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: badah.
    http://api.openweathermap.org/data/2.5/weather?lat=27.333333&lon=68.016667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: zerbst.
    http://api.openweathermap.org/data/2.5/weather?lat=51.966667&lon=12.083333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: pontivy.
    http://api.openweathermap.org/data/2.5/weather?lat=48.066539&lon=-2.96442&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bacsbokod.
    http://api.openweathermap.org/data/2.5/weather?lat=46.124996&lon=19.156207&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sao jeronimo.
    http://api.openweathermap.org/data/2.5/weather?lat=-29.966667&lon=-51.716667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kyshtym.
    http://api.openweathermap.org/data/2.5/weather?lat=55.714&lon=60.5528&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: agria.
    http://api.openweathermap.org/data/2.5/weather?lat=39.3333333&lon=23.0166667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: lypcha.
    http://api.openweathermap.org/data/2.5/weather?lat=48.261075&lon=23.383364&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bhim tal.
    http://api.openweathermap.org/data/2.5/weather?lat=29.35&lon=79.566667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: stirion.
    http://api.openweathermap.org/data/2.5/weather?lat=38.4&lon=22.7166667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: cotusca.
    http://api.openweathermap.org/data/2.5/weather?lat=48.133333&lon=26.85&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: amli.
    http://api.openweathermap.org/data/2.5/weather?lat=20.283333&lon=73.016667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: peterhead.
    http://api.openweathermap.org/data/2.5/weather?lat=57.5&lon=-1.783333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: podborany.
    http://api.openweathermap.org/data/2.5/weather?lat=50.226883&lon=13.409585&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: rincon de la victoria.
    http://api.openweathermap.org/data/2.5/weather?lat=36.716141&lon=-4.287813&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: hajipur.
    http://api.openweathermap.org/data/2.5/weather?lat=31.975556&lon=75.757778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: moravsky beroun.
    http://api.openweathermap.org/data/2.5/weather?lat=49.796431&lon=17.444735&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: erpeli.
    http://api.openweathermap.org/data/2.5/weather?lat=42.805838&lon=46.977321&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: brahmapuri.
    http://api.openweathermap.org/data/2.5/weather?lat=20.6&lon=79.866667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: burevestnik.
    http://api.openweathermap.org/data/2.5/weather?lat=56.144029&lon=43.788324&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: soma.
    http://api.openweathermap.org/data/2.5/weather?lat=39.185535&lon=27.609449&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: linares.
    http://api.openweathermap.org/data/2.5/weather?lat=24.857778&lon=-99.567778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kinango.
    http://api.openweathermap.org/data/2.5/weather?lat=-4.1333333&lon=39.3166667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: litokhoron.
    http://api.openweathermap.org/data/2.5/weather?lat=40.1005556&lon=22.4977778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: compostela.
    http://api.openweathermap.org/data/2.5/weather?lat=10.455&lon=124.0106&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: itabaianinha.
    http://api.openweathermap.org/data/2.5/weather?lat=-11.266667&lon=-37.783333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: harman.
    http://api.openweathermap.org/data/2.5/weather?lat=45.716667&lon=25.683333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: menges.
    http://api.openweathermap.org/data/2.5/weather?lat=46.1669444&lon=14.575&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: beba.
    http://api.openweathermap.org/data/2.5/weather?lat=28.925&lon=30.9833333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: yanahuanca.
    http://api.openweathermap.org/data/2.5/weather?lat=-10.5166667&lon=-76.4986111&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: koshki.
    http://api.openweathermap.org/data/2.5/weather?lat=54.209142&lon=50.467667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: alacaygan.
    http://api.openweathermap.org/data/2.5/weather?lat=10.86324&lon=123.082704&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: starokostyantyniv.
    http://api.openweathermap.org/data/2.5/weather?lat=49.757637&lon=27.20342&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: wallacetown.
    http://api.openweathermap.org/data/2.5/weather?lat=-46.333333&lon=168.266667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: gland.
    http://api.openweathermap.org/data/2.5/weather?lat=46.421233&lon=6.266986&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: tulsa.
    http://api.openweathermap.org/data/2.5/weather?lat=36.1538889&lon=-95.9925&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: agbannawag.
    http://api.openweathermap.org/data/2.5/weather?lat=15.6792&lon=121.0833&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: groditz.
    http://api.openweathermap.org/data/2.5/weather?lat=51.416667&lon=13.45&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kepno.
    http://api.openweathermap.org/data/2.5/weather?lat=51.278425&lon=17.985831&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: phatthalung.
    http://api.openweathermap.org/data/2.5/weather?lat=7.617861&lon=100.077917&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: los tangos.
    http://api.openweathermap.org/data/2.5/weather?lat=15.15&lon=-88.6833333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: mezohegyes.
    http://api.openweathermap.org/data/2.5/weather?lat=46.316667&lon=20.816667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: guibuangan.
    http://api.openweathermap.org/data/2.5/weather?lat=10.1157&lon=123.4944&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: roubaix.
    http://api.openweathermap.org/data/2.5/weather?lat=50.694207&lon=3.174556&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: pemberton.
    http://api.openweathermap.org/data/2.5/weather?lat=50.316667&lon=-122.816667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: zonalnaya stantsiya.
    http://api.openweathermap.org/data/2.5/weather?lat=56.430278&lon=85.012778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: deva.
    http://api.openweathermap.org/data/2.5/weather?lat=45.883333&lon=22.9&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: caravaggio.
    http://api.openweathermap.org/data/2.5/weather?lat=45.5&lon=9.633333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ferry pass.
    http://api.openweathermap.org/data/2.5/weather?lat=30.51&lon=-87.2125&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: aanekoski.
    http://api.openweathermap.org/data/2.5/weather?lat=62.6&lon=25.733333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: pedro ii.
    http://api.openweathermap.org/data/2.5/weather?lat=-4.416667&lon=-41.466667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: stepantsevo.
    http://api.openweathermap.org/data/2.5/weather?lat=56.13143&lon=41.703199&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: gumia.
    http://api.openweathermap.org/data/2.5/weather?lat=23.783333&lon=85.816667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: san pedro.
    http://api.openweathermap.org/data/2.5/weather?lat=25.433333&lon=-103.216667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: scotch plains.
    http://api.openweathermap.org/data/2.5/weather?lat=40.6552778&lon=-74.3902778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: penablanca.
    http://api.openweathermap.org/data/2.5/weather?lat=17.624211&lon=121.786647&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: muqui.
    http://api.openweathermap.org/data/2.5/weather?lat=-20.95&lon=-41.3&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: apozol.
    http://api.openweathermap.org/data/2.5/weather?lat=21.483333&lon=-103.1&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: saitama.
    http://api.openweathermap.org/data/2.5/weather?lat=35.895534&lon=139.67747&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: valvatna.
    http://api.openweathermap.org/data/2.5/weather?lat=59.766667&lon=5.416667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: los patios.
    http://api.openweathermap.org/data/2.5/weather?lat=7.837931&lon=-72.503696&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: coral gables.
    http://api.openweathermap.org/data/2.5/weather?lat=25.7211111&lon=-80.2686111&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: adiake.
    http://api.openweathermap.org/data/2.5/weather?lat=5.286337&lon=-3.304025&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: mora.
    http://api.openweathermap.org/data/2.5/weather?lat=11.0425&lon=14.1447222&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: keetmanshoop.
    http://api.openweathermap.org/data/2.5/weather?lat=-26.5833333&lon=18.1333333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: tapilon.
    http://api.openweathermap.org/data/2.5/weather?lat=11.2774&lon=124.0306&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: monreale.
    http://api.openweathermap.org/data/2.5/weather?lat=38.083333&lon=13.283333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kastamonu.
    http://api.openweathermap.org/data/2.5/weather?lat=41.378052&lon=33.775275&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: karoi.
    http://api.openweathermap.org/data/2.5/weather?lat=-16.8166667&lon=29.6833333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: as.
    http://api.openweathermap.org/data/2.5/weather?lat=51.016667&lon=5.583333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: mayakovski.
    http://api.openweathermap.org/data/2.5/weather?lat=40.2522222&lon=44.6383333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: morayfield.
    http://api.openweathermap.org/data/2.5/weather?lat=-27.108761&lon=152.949066&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: calbe.
    http://api.openweathermap.org/data/2.5/weather?lat=51.9&lon=11.766667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: el cerrito.
    http://api.openweathermap.org/data/2.5/weather?lat=37.9158333&lon=-122.3105556&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: navadwip.
    http://api.openweathermap.org/data/2.5/weather?lat=23.416667&lon=88.366667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: chojnow.
    http://api.openweathermap.org/data/2.5/weather?lat=51.273155&lon=15.935862&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: cuca.
    http://api.openweathermap.org/data/2.5/weather?lat=44.95&lon=24.516667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: yautepec.
    http://api.openweathermap.org/data/2.5/weather?lat=18.883333&lon=-99.066667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: san isidro.
    http://api.openweathermap.org/data/2.5/weather?lat=8.258333&lon=124.593056&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: schladming.
    http://api.openweathermap.org/data/2.5/weather?lat=47.383333&lon=13.683333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: san manuel chaparron.
    http://api.openweathermap.org/data/2.5/weather?lat=14.516667&lon=-89.766667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: hampden.
    http://api.openweathermap.org/data/2.5/weather?lat=44.7444444&lon=-68.8375&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: palakkad.
    http://api.openweathermap.org/data/2.5/weather?lat=10.7725&lon=76.651389&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: yelizavetinskaya.
    http://api.openweathermap.org/data/2.5/weather?lat=45.044462&lon=38.795803&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: evangelista.
    http://api.openweathermap.org/data/2.5/weather?lat=13.3335&lon=121.0972&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: gumaus.
    http://api.openweathermap.org/data/2.5/weather?lat=14.3103&lon=122.7229&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sanary-sur-mer.
    http://api.openweathermap.org/data/2.5/weather?lat=43.117835&lon=5.800065&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: gardiner.
    http://api.openweathermap.org/data/2.5/weather?lat=44.23&lon=-69.7758333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: campbellsville.
    http://api.openweathermap.org/data/2.5/weather?lat=37.3433333&lon=-85.3419444&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: nawalgarh.
    http://api.openweathermap.org/data/2.5/weather?lat=27.85&lon=75.266667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: dubki.
    http://api.openweathermap.org/data/2.5/weather?lat=43.021163&lon=46.837457&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sanbu.
    http://api.openweathermap.org/data/2.5/weather?lat=22.36078&lon=112.688088&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: gaesti.
    http://api.openweathermap.org/data/2.5/weather?lat=44.716667&lon=25.316667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: san jose.
    http://api.openweathermap.org/data/2.5/weather?lat=16.983333&lon=-89.9&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: stepnoye.
    http://api.openweathermap.org/data/2.5/weather?lat=44.270833&lon=44.585&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: rudraprayag.
    http://api.openweathermap.org/data/2.5/weather?lat=30.283333&lon=78.983333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bethlehem.
    http://api.openweathermap.org/data/2.5/weather?lat=40.6258333&lon=-75.3708333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kintore.
    http://api.openweathermap.org/data/2.5/weather?lat=57.216667&lon=-2.35&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: cheektowaga.
    http://api.openweathermap.org/data/2.5/weather?lat=42.9033333&lon=-78.755&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: solin.
    http://api.openweathermap.org/data/2.5/weather?lat=43.55&lon=16.5&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: puerto lempira.
    http://api.openweathermap.org/data/2.5/weather?lat=15.2666667&lon=-83.7666667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: tileagd.
    http://api.openweathermap.org/data/2.5/weather?lat=47.066667&lon=22.2&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: caminawit.
    http://api.openweathermap.org/data/2.5/weather?lat=12.33135&lon=121.082513&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: crestline.
    http://api.openweathermap.org/data/2.5/weather?lat=34.2419444&lon=-117.2847222&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: nema.
    http://api.openweathermap.org/data/2.5/weather?lat=57.506751&lon=50.501147&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: lakhnau.
    http://api.openweathermap.org/data/2.5/weather?lat=26.85&lon=80.916667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: vyshhorod.
    http://api.openweathermap.org/data/2.5/weather?lat=50.584758&lon=30.489799&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: narvik.
    http://api.openweathermap.org/data/2.5/weather?lat=68.435556&lon=17.437222&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: athol.
    http://api.openweathermap.org/data/2.5/weather?lat=42.5958333&lon=-72.2272222&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: shaygino.
    http://api.openweathermap.org/data/2.5/weather?lat=57.76751&lon=46.861811&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: virginia.
    http://api.openweathermap.org/data/2.5/weather?lat=-28.10391&lon=26.86593&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: dolores.
    http://api.openweathermap.org/data/2.5/weather?lat=14.0165&lon=121.4011&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: la union.
    http://api.openweathermap.org/data/2.5/weather?lat=17.966667&lon=-101.816667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: arkadelphia.
    http://api.openweathermap.org/data/2.5/weather?lat=34.1208333&lon=-93.0536111&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: tapiosag.
    http://api.openweathermap.org/data/2.5/weather?lat=47.401999&lon=19.630468&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: nakuru.
    http://api.openweathermap.org/data/2.5/weather?lat=-0.2833333&lon=36.0666667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ilampillai.
    http://api.openweathermap.org/data/2.5/weather?lat=11.6&lon=78.0&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: petapa.
    http://api.openweathermap.org/data/2.5/weather?lat=14.502778&lon=-90.551667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: vancouver.
    http://api.openweathermap.org/data/2.5/weather?lat=45.6388889&lon=-122.6602778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: reo.
    http://api.openweathermap.org/data/2.5/weather?lat=12.3166667&lon=-2.4666667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: spasskoye.
    http://api.openweathermap.org/data/2.5/weather?lat=48.659833&lon=35.052423&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: pepingen.
    http://api.openweathermap.org/data/2.5/weather?lat=50.75&lon=4.15&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: delogozdi.
    http://api.openweathermap.org/data/2.5/weather?lat=41.2572222&lon=20.7236111&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: mijas.
    http://api.openweathermap.org/data/2.5/weather?lat=36.595299&lon=-4.639861&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: betare oya.
    http://api.openweathermap.org/data/2.5/weather?lat=5.6&lon=14.0833333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: baracatan.
    http://api.openweathermap.org/data/2.5/weather?lat=6.9675&lon=125.415833&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: flores da cunha.
    http://api.openweathermap.org/data/2.5/weather?lat=-29.0287&lon=-51.1822&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: gracias.
    http://api.openweathermap.org/data/2.5/weather?lat=14.5833333&lon=-88.5833333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: binan.
    http://api.openweathermap.org/data/2.5/weather?lat=14.263732&lon=121.052638&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: horasan.
    http://api.openweathermap.org/data/2.5/weather?lat=40.045833&lon=42.172778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: laguna.
    http://api.openweathermap.org/data/2.5/weather?lat=-28.483333&lon=-48.783333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: earlston.
    http://api.openweathermap.org/data/2.5/weather?lat=55.633333&lon=-2.666667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: krathum baen.
    http://api.openweathermap.org/data/2.5/weather?lat=13.653298&lon=100.259717&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: martelange.
    http://api.openweathermap.org/data/2.5/weather?lat=49.833333&lon=5.733333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: gera.
    http://api.openweathermap.org/data/2.5/weather?lat=50.866667&lon=12.083333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: chebenki.
    http://api.openweathermap.org/data/2.5/weather?lat=51.93872&lon=55.700977&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: meycauayan.
    http://api.openweathermap.org/data/2.5/weather?lat=14.7328&lon=120.96&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: moka.
    http://api.openweathermap.org/data/2.5/weather?lat=-20.2188889&lon=57.4958333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: dundalk.
    http://api.openweathermap.org/data/2.5/weather?lat=39.2505556&lon=-76.5208333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: celmira.
    http://api.openweathermap.org/data/2.5/weather?lat=8.5333333&lon=-82.8&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: adelfia.
    http://api.openweathermap.org/data/2.5/weather?lat=41.0&lon=16.866667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: burla.
    http://api.openweathermap.org/data/2.5/weather?lat=21.5&lon=83.866667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: pindorama.
    http://api.openweathermap.org/data/2.5/weather?lat=-21.2&lon=-48.916667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sao gotardo.
    http://api.openweathermap.org/data/2.5/weather?lat=-19.316667&lon=-46.05&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: la herradura.
    http://api.openweathermap.org/data/2.5/weather?lat=8.8522222&lon=-79.8072222&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: nouvelle france.
    http://api.openweathermap.org/data/2.5/weather?lat=-20.3705556&lon=57.5611111&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: nabannagan.
    http://api.openweathermap.org/data/2.5/weather?lat=18.071486&lon=121.533751&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: rijswijk.
    http://api.openweathermap.org/data/2.5/weather?lat=52.025498&lon=4.310793&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bellegarde-sur-valserine.
    http://api.openweathermap.org/data/2.5/weather?lat=46.110377&lon=5.830437&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: wyszkow.
    http://api.openweathermap.org/data/2.5/weather?lat=52.596407&lon=21.457539&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ipil.
    http://api.openweathermap.org/data/2.5/weather?lat=9.7907&lon=125.4386&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: telimele.
    http://api.openweathermap.org/data/2.5/weather?lat=10.9&lon=-13.0333333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: istisu.
    http://api.openweathermap.org/data/2.5/weather?lat=39.947532&lon=45.962121&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kulpahar.
    http://api.openweathermap.org/data/2.5/weather?lat=25.316667&lon=79.65&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: goshen.
    http://api.openweathermap.org/data/2.5/weather?lat=41.5822222&lon=-85.8344444&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: viseu.
    http://api.openweathermap.org/data/2.5/weather?lat=-1.2&lon=-46.116667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: pilisszanto.
    http://api.openweathermap.org/data/2.5/weather?lat=47.669088&lon=18.887617&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: jinji.
    http://api.openweathermap.org/data/2.5/weather?lat=23.228056&lon=110.826111&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: lajkovac.
    http://api.openweathermap.org/data/2.5/weather?lat=44.369444&lon=20.165278&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ibague.
    http://api.openweathermap.org/data/2.5/weather?lat=4.438889&lon=-75.232222&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: auxerre.
    http://api.openweathermap.org/data/2.5/weather?lat=47.7996&lon=3.57033&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: osinki.
    http://api.openweathermap.org/data/2.5/weather?lat=52.8432&lon=49.5132&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: weston-super-mare.
    http://api.openweathermap.org/data/2.5/weather?lat=51.345833&lon=-2.967778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: salice salentino.
    http://api.openweathermap.org/data/2.5/weather?lat=40.383333&lon=17.966667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: dusti.
    http://api.openweathermap.org/data/2.5/weather?lat=37.3486111&lon=68.6733333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: nueva loja.
    http://api.openweathermap.org/data/2.5/weather?lat=0.0847222&lon=-76.8827778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: beysehir.
    http://api.openweathermap.org/data/2.5/weather?lat=37.677348&lon=31.724577&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: hodasz.
    http://api.openweathermap.org/data/2.5/weather?lat=47.918339&lon=22.201534&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ponferrada.
    http://api.openweathermap.org/data/2.5/weather?lat=42.546638&lon=-6.596187&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: mixtepec.
    http://api.openweathermap.org/data/2.5/weather?lat=16.283333&lon=-96.333333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: klimovo.
    http://api.openweathermap.org/data/2.5/weather?lat=52.380534&lon=32.192328&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: la porte.
    http://api.openweathermap.org/data/2.5/weather?lat=29.6655556&lon=-95.0191667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: palairos.
    http://api.openweathermap.org/data/2.5/weather?lat=38.7833333&lon=20.8833333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bierbeek.
    http://api.openweathermap.org/data/2.5/weather?lat=50.833333&lon=4.766667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: erbaa.
    http://api.openweathermap.org/data/2.5/weather?lat=40.668889&lon=36.5675&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: largs.
    http://api.openweathermap.org/data/2.5/weather?lat=55.783333&lon=-4.85&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: mayskiy.
    http://api.openweathermap.org/data/2.5/weather?lat=50.519881&lon=36.458777&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bogatoye.
    http://api.openweathermap.org/data/2.5/weather?lat=53.0601&lon=51.3325&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: soka.
    http://api.openweathermap.org/data/2.5/weather?lat=35.820278&lon=139.804444&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: novokubansk.
    http://api.openweathermap.org/data/2.5/weather?lat=45.117&lon=41.0267&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: wolcott.
    http://api.openweathermap.org/data/2.5/weather?lat=41.6022222&lon=-72.9872222&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: numbrecht.
    http://api.openweathermap.org/data/2.5/weather?lat=50.9&lon=7.55&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kacuni.
    http://api.openweathermap.org/data/2.5/weather?lat=44.065&lon=17.9386111&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: show low.
    http://api.openweathermap.org/data/2.5/weather?lat=34.2541667&lon=-110.0291667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: corralillo.
    http://api.openweathermap.org/data/2.5/weather?lat=22.9819444&lon=-80.5855556&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: petrinja.
    http://api.openweathermap.org/data/2.5/weather?lat=45.4375&lon=16.29&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: fort-shevchenko.
    http://api.openweathermap.org/data/2.5/weather?lat=44.516667&lon=50.266667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: blacksburg.
    http://api.openweathermap.org/data/2.5/weather?lat=37.2294444&lon=-80.4141667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: arue.
    http://api.openweathermap.org/data/2.5/weather?lat=-17.5166667&lon=-149.5&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: letohrad.
    http://api.openweathermap.org/data/2.5/weather?lat=50.035969&lon=16.496683&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kallithea.
    http://api.openweathermap.org/data/2.5/weather?lat=40.2763889&lon=22.5783333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ponnani.
    http://api.openweathermap.org/data/2.5/weather?lat=10.766667&lon=75.9&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: atripalda.
    http://api.openweathermap.org/data/2.5/weather?lat=40.916667&lon=14.833333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: haskovo.
    http://api.openweathermap.org/data/2.5/weather?lat=41.9402778&lon=25.5694444&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: norcasia.
    http://api.openweathermap.org/data/2.5/weather?lat=5.577815&lon=-74.885206&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: narauis.
    http://api.openweathermap.org/data/2.5/weather?lat=10.2453&lon=122.8869&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: rio pardo.
    http://api.openweathermap.org/data/2.5/weather?lat=-29.983333&lon=-52.366667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: santa catarina.
    http://api.openweathermap.org/data/2.5/weather?lat=18.966667&lon=-99.133333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: gura vitioarei.
    http://api.openweathermap.org/data/2.5/weather?lat=45.15&lon=26.033333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: meresti.
    http://api.openweathermap.org/data/2.5/weather?lat=46.233333&lon=25.45&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kunhegyes.
    http://api.openweathermap.org/data/2.5/weather?lat=47.366667&lon=20.633333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: niederzier.
    http://api.openweathermap.org/data/2.5/weather?lat=50.883333&lon=6.466667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: mandera.
    http://api.openweathermap.org/data/2.5/weather?lat=3.9261111&lon=41.8461111&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: dewas.
    http://api.openweathermap.org/data/2.5/weather?lat=22.966667&lon=76.066667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: palana.
    http://api.openweathermap.org/data/2.5/weather?lat=59.116667&lon=159.966667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ponte nova.
    http://api.openweathermap.org/data/2.5/weather?lat=-20.4&lon=-42.9&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: coyaima.
    http://api.openweathermap.org/data/2.5/weather?lat=3.799359&lon=-75.194669&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: otrokovice.
    http://api.openweathermap.org/data/2.5/weather?lat=49.207366&lon=17.523862&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sarretudvari.
    http://api.openweathermap.org/data/2.5/weather?lat=47.233333&lon=21.2&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: pincher creek.
    http://api.openweathermap.org/data/2.5/weather?lat=49.483333&lon=-113.95&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: batangafo.
    http://api.openweathermap.org/data/2.5/weather?lat=7.3&lon=18.3&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bodoc.
    http://api.openweathermap.org/data/2.5/weather?lat=45.95&lon=25.85&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sayanogorsk.
    http://api.openweathermap.org/data/2.5/weather?lat=53.0875&lon=91.399722&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: totkomlos.
    http://api.openweathermap.org/data/2.5/weather?lat=46.416667&lon=20.733333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: carora.
    http://api.openweathermap.org/data/2.5/weather?lat=10.1777778&lon=-70.0805556&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: nidzica.
    http://api.openweathermap.org/data/2.5/weather?lat=53.360936&lon=20.426476&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: peruibe.
    http://api.openweathermap.org/data/2.5/weather?lat=-24.316667&lon=-47.0&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: hantsport.
    http://api.openweathermap.org/data/2.5/weather?lat=45.066667&lon=-64.183333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: mecayapan.
    http://api.openweathermap.org/data/2.5/weather?lat=18.216667&lon=-94.833333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: rapperswil.
    http://api.openweathermap.org/data/2.5/weather?lat=47.227986&lon=8.825954&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: zomin.
    http://api.openweathermap.org/data/2.5/weather?lat=39.9605556&lon=68.3958333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: geeste.
    http://api.openweathermap.org/data/2.5/weather?lat=52.6&lon=7.266667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ganserndorf.
    http://api.openweathermap.org/data/2.5/weather?lat=48.35&lon=16.733333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: miedzychod.
    http://api.openweathermap.org/data/2.5/weather?lat=52.599017&lon=15.890664&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: tuymazy.
    http://api.openweathermap.org/data/2.5/weather?lat=54.606657&lon=53.709699&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: dudley.
    http://api.openweathermap.org/data/2.5/weather?lat=42.045&lon=-71.9305556&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: polonnaruwa.
    http://api.openweathermap.org/data/2.5/weather?lat=7.9333333&lon=81.0&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: rancho mirage.
    http://api.openweathermap.org/data/2.5/weather?lat=33.7397222&lon=-116.4119444&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kardzhin.
    http://api.openweathermap.org/data/2.5/weather?lat=43.264639&lon=44.295374&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kolar.
    http://api.openweathermap.org/data/2.5/weather?lat=13.133333&lon=78.133333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: san juan.
    http://api.openweathermap.org/data/2.5/weather?lat=15.7333333&lon=-87.5&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: saveh.
    http://api.openweathermap.org/data/2.5/weather?lat=35.0213&lon=50.3566&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: stonehouse.
    http://api.openweathermap.org/data/2.5/weather?lat=55.666667&lon=-3.983333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: la orotava.
    http://api.openweathermap.org/data/2.5/weather?lat=28.387309&lon=-16.516774&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: rye brook.
    http://api.openweathermap.org/data/2.5/weather?lat=41.0191667&lon=-73.6838889&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: dinanagar.
    http://api.openweathermap.org/data/2.5/weather?lat=32.15&lon=75.466667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: dolni bojanovice.
    http://api.openweathermap.org/data/2.5/weather?lat=48.857761&lon=17.028111&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: melnikovo.
    http://api.openweathermap.org/data/2.5/weather?lat=56.555833&lon=84.085&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: nova bana.
    http://api.openweathermap.org/data/2.5/weather?lat=48.4333333&lon=18.65&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: new york.
    http://api.openweathermap.org/data/2.5/weather?lat=40.7141667&lon=-74.0063889&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: vuktyl.
    http://api.openweathermap.org/data/2.5/weather?lat=63.856667&lon=57.309444&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: tinglev.
    http://api.openweathermap.org/data/2.5/weather?lat=54.93099&lon=9.252433&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: osterholz-scharmbeck.
    http://api.openweathermap.org/data/2.5/weather?lat=53.233333&lon=8.8&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: dulangan.
    http://api.openweathermap.org/data/2.5/weather?lat=11.4561&lon=122.9557&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: san jose.
    http://api.openweathermap.org/data/2.5/weather?lat=13.925556&lon=-90.824444&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: maur.
    http://api.openweathermap.org/data/2.5/weather?lat=30.083333&lon=75.25&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: panay.
    http://api.openweathermap.org/data/2.5/weather?lat=11.557778&lon=122.794167&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: cuajinicuilapa.
    http://api.openweathermap.org/data/2.5/weather?lat=16.466667&lon=-98.416667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: nanzhang.
    http://api.openweathermap.org/data/2.5/weather?lat=31.783941&lon=111.827518&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: milas.
    http://api.openweathermap.org/data/2.5/weather?lat=46.816667&lon=24.433333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: lyubertsy.
    http://api.openweathermap.org/data/2.5/weather?lat=55.677193&lon=37.893217&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: medway.
    http://api.openweathermap.org/data/2.5/weather?lat=42.1416667&lon=-71.3972222&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: vitoria.
    http://api.openweathermap.org/data/2.5/weather?lat=-20.316667&lon=-40.35&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: hamilton.
    http://api.openweathermap.org/data/2.5/weather?lat=-37.783333&lon=175.283333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: rozhdestveno.
    http://api.openweathermap.org/data/2.5/weather?lat=53.237446&lon=50.059706&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kamalapuram.
    http://api.openweathermap.org/data/2.5/weather?lat=14.583333&lon=78.65&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: dolni poustevna.
    http://api.openweathermap.org/data/2.5/weather?lat=50.991419&lon=14.293227&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sekudai.
    http://api.openweathermap.org/data/2.5/weather?lat=1.533333&lon=103.666667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: lagos.
    http://api.openweathermap.org/data/2.5/weather?lat=37.101782&lon=-8.674242&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ambositra.
    http://api.openweathermap.org/data/2.5/weather?lat=-20.5166667&lon=47.25&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: mount rainier.
    http://api.openweathermap.org/data/2.5/weather?lat=38.9413889&lon=-76.9652778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: selma.
    http://api.openweathermap.org/data/2.5/weather?lat=32.4072222&lon=-87.0211111&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: tomares.
    http://api.openweathermap.org/data/2.5/weather?lat=37.372807&lon=-6.04589&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: pawa.
    http://api.openweathermap.org/data/2.5/weather?lat=13.1335&lon=123.8915&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: pilion.
    http://api.openweathermap.org/data/2.5/weather?lat=36.8477778&lon=27.1613889&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: nagas.
    http://api.openweathermap.org/data/2.5/weather?lat=13.4357&lon=123.6781&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: shamli.
    http://api.openweathermap.org/data/2.5/weather?lat=29.45&lon=77.316667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: aginskoye.
    http://api.openweathermap.org/data/2.5/weather?lat=55.2586&lon=94.9079&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bolshegrivskoye.
    http://api.openweathermap.org/data/2.5/weather?lat=53.913611&lon=74.913056&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sobralinho.
    http://api.openweathermap.org/data/2.5/weather?lat=38.917031&lon=-9.026562&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bolaoit.
    http://api.openweathermap.org/data/2.5/weather?lat=15.934&lon=120.432&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ohrid.
    http://api.openweathermap.org/data/2.5/weather?lat=41.1172222&lon=20.8019444&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: majitha.
    http://api.openweathermap.org/data/2.5/weather?lat=31.758333&lon=74.954444&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sazonovo.
    http://api.openweathermap.org/data/2.5/weather?lat=59.0919&lon=35.2268&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: anori.
    http://api.openweathermap.org/data/2.5/weather?lat=7.072725&lon=-75.147677&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: pinos.
    http://api.openweathermap.org/data/2.5/weather?lat=22.3&lon=-101.566667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: primo tapia.
    http://api.openweathermap.org/data/2.5/weather?lat=32.22&lon=-116.917222&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: pretoria.
    http://api.openweathermap.org/data/2.5/weather?lat=-25.706944&lon=28.229444&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: moelv.
    http://api.openweathermap.org/data/2.5/weather?lat=60.933333&lon=10.7&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: aflao.
    http://api.openweathermap.org/data/2.5/weather?lat=6.1177778&lon=1.1927778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: wadersloh.
    http://api.openweathermap.org/data/2.5/weather?lat=51.733333&lon=8.25&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: venice.
    http://api.openweathermap.org/data/2.5/weather?lat=27.0994444&lon=-82.4544444&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: apopka.
    http://api.openweathermap.org/data/2.5/weather?lat=28.6802778&lon=-81.5097222&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: luna.
    http://api.openweathermap.org/data/2.5/weather?lat=9.737&lon=125.4976&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sansai.
    http://api.openweathermap.org/data/2.5/weather?lat=18.83075&lon=99.003806&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ixtlan del rio.
    http://api.openweathermap.org/data/2.5/weather?lat=21.033333&lon=-104.366667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: aparecida.
    http://api.openweathermap.org/data/2.5/weather?lat=-22.8418&lon=-45.2287&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: erdokertes.
    http://api.openweathermap.org/data/2.5/weather?lat=47.672609&lon=19.30786&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: republic.
    http://api.openweathermap.org/data/2.5/weather?lat=37.12&lon=-93.48&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sebastian.
    http://api.openweathermap.org/data/2.5/weather?lat=27.8161111&lon=-80.4708333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: oirschot.
    http://api.openweathermap.org/data/2.5/weather?lat=51.50343&lon=5.308304&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: olimpia.
    http://api.openweathermap.org/data/2.5/weather?lat=-20.733333&lon=-48.9&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: morong.
    http://api.openweathermap.org/data/2.5/weather?lat=14.678889&lon=120.266111&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: vitoria.
    http://api.openweathermap.org/data/2.5/weather?lat=42.85&lon=-2.666667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: gottingen.
    http://api.openweathermap.org/data/2.5/weather?lat=51.533333&lon=9.933333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sendriceni.
    http://api.openweathermap.org/data/2.5/weather?lat=47.95&lon=26.3&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: rio rita.
    http://api.openweathermap.org/data/2.5/weather?lat=9.3038889&lon=-79.7944444&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: new agutaya.
    http://api.openweathermap.org/data/2.5/weather?lat=10.561389&lon=119.307778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: porong.
    http://api.openweathermap.org/data/2.5/weather?lat=-7.5406&lon=112.6888&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: san francisco.
    http://api.openweathermap.org/data/2.5/weather?lat=37.775&lon=-122.4183333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: yarkovo.
    http://api.openweathermap.org/data/2.5/weather?lat=54.8056&lon=82.5989&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: malkerns.
    http://api.openweathermap.org/data/2.5/weather?lat=-26.5666667&lon=31.1833333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: orimattila.
    http://api.openweathermap.org/data/2.5/weather?lat=60.8&lon=25.75&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: burias.
    http://api.openweathermap.org/data/2.5/weather?lat=11.4463&lon=122.5497&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: holsted.
    http://api.openweathermap.org/data/2.5/weather?lat=55.510864&lon=8.918721&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: urubamba.
    http://api.openweathermap.org/data/2.5/weather?lat=-13.3077778&lon=-72.1152778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: tukums.
    http://api.openweathermap.org/data/2.5/weather?lat=56.9669444&lon=23.1552778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: warrensville heights.
    http://api.openweathermap.org/data/2.5/weather?lat=41.435&lon=-81.5363889&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: energetik.
    http://api.openweathermap.org/data/2.5/weather?lat=51.7445&lon=58.7934&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: tibacuy.
    http://api.openweathermap.org/data/2.5/weather?lat=4.351111&lon=-72.456389&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: hata.
    http://api.openweathermap.org/data/2.5/weather?lat=26.746111&lon=83.740278&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: san martin jilotepeque.
    http://api.openweathermap.org/data/2.5/weather?lat=14.787778&lon=-90.7925&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: todiresti.
    http://api.openweathermap.org/data/2.5/weather?lat=46.85&lon=27.366667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: arara.
    http://api.openweathermap.org/data/2.5/weather?lat=-6.833333&lon=-35.75&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: rakitnoye.
    http://api.openweathermap.org/data/2.5/weather?lat=50.8389&lon=35.8515&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: totonicapan.
    http://api.openweathermap.org/data/2.5/weather?lat=14.916667&lon=-91.366667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: hingham.
    http://api.openweathermap.org/data/2.5/weather?lat=42.2416667&lon=-70.8902778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: praid.
    http://api.openweathermap.org/data/2.5/weather?lat=46.55&lon=25.133333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kawhia.
    http://api.openweathermap.org/data/2.5/weather?lat=-38.066667&lon=174.816667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bana.
    http://api.openweathermap.org/data/2.5/weather?lat=5.15&lon=10.2666667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: poros.
    http://api.openweathermap.org/data/2.5/weather?lat=37.4994444&lon=23.4536111&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: general zuazua.
    http://api.openweathermap.org/data/2.5/weather?lat=25.9&lon=-100.116667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: briceni.
    http://api.openweathermap.org/data/2.5/weather?lat=48.357222&lon=27.703611&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: nova mayachka.
    http://api.openweathermap.org/data/2.5/weather?lat=46.599956&lon=33.22707&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: santarem.
    http://api.openweathermap.org/data/2.5/weather?lat=-2.433333&lon=-54.7&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sabanalarga.
    http://api.openweathermap.org/data/2.5/weather?lat=10.629617&lon=-74.92063&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sukabumi.
    http://api.openweathermap.org/data/2.5/weather?lat=-6.918056&lon=106.926667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: chone.
    http://api.openweathermap.org/data/2.5/weather?lat=-0.6833333&lon=-80.1&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: marovoay.
    http://api.openweathermap.org/data/2.5/weather?lat=-16.1&lon=46.6333333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: mbuyapey.
    http://api.openweathermap.org/data/2.5/weather?lat=-26.2&lon=-56.75&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: jaguimitan.
    http://api.openweathermap.org/data/2.5/weather?lat=11.14&lon=122.7236&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: sanmartin.
    http://api.openweathermap.org/data/2.5/weather?lat=46.266667&lon=25.933333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: senai.
    http://api.openweathermap.org/data/2.5/weather?lat=1.6006&lon=103.6419&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: oliveirinha.
    http://api.openweathermap.org/data/2.5/weather?lat=40.607146&lon=-8.591978&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: eatonton.
    http://api.openweathermap.org/data/2.5/weather?lat=33.3266667&lon=-83.3886111&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: rantepao.
    http://api.openweathermap.org/data/2.5/weather?lat=-2.9701&lon=119.8978&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: draganesti-olt.
    http://api.openweathermap.org/data/2.5/weather?lat=44.166667&lon=24.533333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: gatehouse of fleet.
    http://api.openweathermap.org/data/2.5/weather?lat=54.883333&lon=-4.183333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: san cristobal acasaguastlan.
    http://api.openweathermap.org/data/2.5/weather?lat=14.916667&lon=-89.883333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: pontalina.
    http://api.openweathermap.org/data/2.5/weather?lat=-17.516667&lon=-49.45&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: jiangmen.
    http://api.openweathermap.org/data/2.5/weather?lat=22.583333&lon=113.083333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: taiping.
    http://api.openweathermap.org/data/2.5/weather?lat=4.85&lon=100.733333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bolshaya vishera.
    http://api.openweathermap.org/data/2.5/weather?lat=58.914611&lon=32.08712&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: yarmouth.
    http://api.openweathermap.org/data/2.5/weather?lat=43.8005556&lon=-70.1872222&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: glendale.
    http://api.openweathermap.org/data/2.5/weather?lat=43.1352778&lon=-87.9355556&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: arinos.
    http://api.openweathermap.org/data/2.5/weather?lat=-15.916667&lon=-46.066667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ayia paraskevi.
    http://api.openweathermap.org/data/2.5/weather?lat=40.4833333&lon=23.05&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: lanivtsi.
    http://api.openweathermap.org/data/2.5/weather?lat=49.863275&lon=26.09082&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: atlatongo.
    http://api.openweathermap.org/data/2.5/weather?lat=19.666667&lon=-98.9&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: puntarenas.
    http://api.openweathermap.org/data/2.5/weather?lat=9.976149&lon=-84.838754&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: necsesti.
    http://api.openweathermap.org/data/2.5/weather?lat=44.25&lon=25.15&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: lewiston.
    http://api.openweathermap.org/data/2.5/weather?lat=46.4166667&lon=-117.0166667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: as.
    http://api.openweathermap.org/data/2.5/weather?lat=51.016667&lon=5.583333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: san juan.
    http://api.openweathermap.org/data/2.5/weather?lat=10.3865&lon=122.8651&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: provadija.
    http://api.openweathermap.org/data/2.5/weather?lat=43.1833333&lon=27.4333333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: rottingdean.
    http://api.openweathermap.org/data/2.5/weather?lat=50.8&lon=-0.05&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: yong peng.
    http://api.openweathermap.org/data/2.5/weather?lat=2.0136&lon=103.0659&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kauswagan.
    http://api.openweathermap.org/data/2.5/weather?lat=8.789722&lon=124.775556&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: faleapuna.
    http://api.openweathermap.org/data/2.5/weather?lat=-13.8666667&lon=-171.5666667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ozark.
    http://api.openweathermap.org/data/2.5/weather?lat=31.4588889&lon=-85.6405556&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: lyubokhna.
    http://api.openweathermap.org/data/2.5/weather?lat=53.503322&lon=34.388469&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bom conselho.
    http://api.openweathermap.org/data/2.5/weather?lat=-9.166667&lon=-36.683333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: salmas.
    http://api.openweathermap.org/data/2.5/weather?lat=38.1973&lon=44.7653&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kecsked.
    http://api.openweathermap.org/data/2.5/weather?lat=47.522985&lon=18.309386&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: pogana.
    http://api.openweathermap.org/data/2.5/weather?lat=46.316667&lon=27.566667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: taganrog.
    http://api.openweathermap.org/data/2.5/weather?lat=47.23617&lon=38.896878&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: putatan.
    http://api.openweathermap.org/data/2.5/weather?lat=5.8947&lon=116.0464&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: saint austell.
    http://api.openweathermap.org/data/2.5/weather?lat=50.338333&lon=-4.765833&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: san giovanni la punta.
    http://api.openweathermap.org/data/2.5/weather?lat=37.583333&lon=15.116667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: vostok.
    http://api.openweathermap.org/data/2.5/weather?lat=48.916667&lon=148.9&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kitango.
    http://api.openweathermap.org/data/2.5/weather?lat=6.948333&lon=124.441111&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ayni.
    http://api.openweathermap.org/data/2.5/weather?lat=39.3975&lon=68.5405556&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bekesszentandras.
    http://api.openweathermap.org/data/2.5/weather?lat=46.866667&lon=20.483333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: qax.
    http://api.openweathermap.org/data/2.5/weather?lat=41.4225&lon=46.924167&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: cotabato.
    http://api.openweathermap.org/data/2.5/weather?lat=7.223611&lon=124.246389&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: amacalan.
    http://api.openweathermap.org/data/2.5/weather?lat=15.5815&lon=120.6112&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: new delhi.
    http://api.openweathermap.org/data/2.5/weather?lat=28.6&lon=77.2&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: binguang.
    http://api.openweathermap.org/data/2.5/weather?lat=17.461944&lon=121.782778&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: lens.
    http://api.openweathermap.org/data/2.5/weather?lat=50.431178&lon=2.833213&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: carthage.
    http://api.openweathermap.org/data/2.5/weather?lat=37.1763889&lon=-94.31&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: bay-khaak.
    http://api.openweathermap.org/data/2.5/weather?lat=51.166667&lon=94.5&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: lacaron.
    http://api.openweathermap.org/data/2.5/weather?lat=11.422&lon=122.7422&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: burien.
    http://api.openweathermap.org/data/2.5/weather?lat=47.4705556&lon=-122.3455556&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: arlington.
    http://api.openweathermap.org/data/2.5/weather?lat=41.6958333&lon=-73.8972222&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ixtlahuacan de los membrillos.
    http://api.openweathermap.org/data/2.5/weather?lat=20.35&lon=-103.183333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: damolog.
    http://api.openweathermap.org/data/2.5/weather?lat=10.766667&lon=124.0&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: orkney.
    http://api.openweathermap.org/data/2.5/weather?lat=-26.980232&lon=26.672717&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ligatne.
    http://api.openweathermap.org/data/2.5/weather?lat=57.2333333&lon=25.05&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: malia.
    http://api.openweathermap.org/data/2.5/weather?lat=23.083333&lon=70.766667&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: cienaga.
    http://api.openweathermap.org/data/2.5/weather?lat=11.007029&lon=-74.247646&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: kolosovka.
    http://api.openweathermap.org/data/2.5/weather?lat=56.467786&lon=73.610957&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: ayia paraskevi.
    http://api.openweathermap.org/data/2.5/weather?lat=38.0166667&lon=23.8333333&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: temirtau.
    http://api.openweathermap.org/data/2.5/weather?lat=53.1377&lon=87.4538&APPID=413085cb59d82f11b14672ef99d1e023&units = metric
    we are looking in to data for: jawar.
    http://api.openweathermap.org/data/2.5/weather?lat=23.0&lon=76.5&APPID=413085cb59d82f11b14672ef99d1e023&units = metric



```python
cities_df = pd.DataFrame({"City":city_names,
                 "Country Code":country_codes,
                 "Latitude":latitudes ,
                 "Longitude":longitudes,"Temperature":temperature,
                 "Humidity":humidity,
                 "Cloudiness":clouds,
                 "Wind Speed":wind_speed}, 
                  columns = ["City","Country Code","Latitude","Longitude","Temperature","Humidity","Cloudiness","Wind Speed"])
cities_df["Temperature"] = cities_df["Temperature"] - 273.15
cities_df.to_csv("Output.csv", sep='\t', encoding='utf-8')
cities_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Country Code</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Temperature</th>
      <th>Humidity</th>
      <th>Cloudiness</th>
      <th>Wind Speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>beach park</td>
      <td>us</td>
      <td>42.422222</td>
      <td>-87.857222</td>
      <td>2.760</td>
      <td>40</td>
      <td>1</td>
      <td>8.70</td>
    </tr>
    <tr>
      <th>1</th>
      <td>galashiels</td>
      <td>gb</td>
      <td>55.600000</td>
      <td>-2.816667</td>
      <td>2.480</td>
      <td>75</td>
      <td>0</td>
      <td>3.10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>bato</td>
      <td>ph</td>
      <td>10.825000</td>
      <td>119.471000</td>
      <td>26.429</td>
      <td>92</td>
      <td>12</td>
      <td>6.83</td>
    </tr>
    <tr>
      <th>3</th>
      <td>guindulman</td>
      <td>ph</td>
      <td>9.762900</td>
      <td>124.487800</td>
      <td>25.079</td>
      <td>100</td>
      <td>88</td>
      <td>7.83</td>
    </tr>
    <tr>
      <th>4</th>
      <td>saquisili</td>
      <td>ec</td>
      <td>-0.833333</td>
      <td>-78.666667</td>
      <td>22.000</td>
      <td>40</td>
      <td>40</td>
      <td>4.10</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.scatter(cities_df["Latitude"], cities_df["Temperature"],marker="o", facecolors="blue", edgecolors="black", alpha=0.75)
plt.title("City Latitude vs City Temperature")
plt.xlabel("City Latitude")
plt.ylabel("City Temperature(C)")
plt.savefig("City Latitude vs City Temperature.png")
plt.show()
```


![png](output_4_0.png)



```python
plt.scatter( cities_df["Latitude"],cities_df["Humidity"], marker="o", facecolors="blue", edgecolors="black", alpha=0.75)
plt.title("City Latitude vs City Humidity")
plt.xlabel("City Latitude")
plt.ylabel("City Humidity(%)")
plt.savefig("City Latitude vs City Humidity.png")
plt.show()
```


![png](output_5_0.png)



```python
plt.scatter(cities_df["Latitude"],cities_df["Cloudiness"],  marker="o", facecolors="blue", edgecolors="black", alpha=0.75)
plt.title("City Latitude vs City Cloudiness")
plt.xlabel("City Latitude")
plt.ylabel("City Cloudiness(%)")
plt.savefig("City Latitude vs City Cloudiness.png")
plt.show()
```


![png](output_6_0.png)



```python
plt.scatter( cities_df["Latitude"], cities_df["Wind Speed"],marker="o", facecolors="blue", edgecolors="black", alpha=0.75)
plt.title("City Latitude vs City Wind Speed")
plt.xlabel("City Latitude")
plt.ylabel("City Wind Speed(meters/sec)")
plt.savefig("City Latitude vs City Wind Speed.png")
plt.show()
```


![png](output_7_0.png)

