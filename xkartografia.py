import pandas as pd
import geopandas as gpd
import folium
import webbrowser
dane_gus_ludnosc_file = 'LUDN_2137_CTAB_20210526043119 . csv'
dane_gus_bezrobocie_file = 'RYNE_1944_CTAB_20210526043442 . csv'
ludnosc_gus = pd.read_csv ( dane_gus_ludnosc_file , delimiter = ';')
ludnosc_gus = ludnosc_gus.iloc [: , 0:3]
ludnosc_gus.columns = [ ' TERYT ' , ' Nazwa ' , ' Ludnosc ']
bezrobocie_gus = pd . read_csv ( dane_gus_bezrobocie_file , delimiter = ';')
bezrobocie_gus = bezrobocie_gus.iloc [: , [0 , 2]]
bezrobocie_gus.columns = [ ' TERYT ' , ' Bezrobotni ']
dane_gus = pd.merge ( ludnosc_gus , bezrobocie_gus , how = ' inner ' , on = ' TERYT ')
dane_gus [ ' Stopa_bezrobocia '] = 100* dane_gus [ ' Bezrobotni '] /\
    dane_gus [ ' Ludnosc ']
mapa_gmn = gpd . read_file ( ' jednostki_administracyjne / Gminy . shp ')
mapa_gmn = mapa_gmn [[ ' JPT_KOD_JE ' , " geometry " ]]
dane_gus [ ' TERYT_gmn '] = dane_gus . TERYT . apply (lambda x : '0 '+ str( x ) if len ( str ( x )) < 7 else str ( x ))
dane_gus_gmn = dane_gus [ dane_gus . TERYT_gmn .str [4:7] != ' 000 ']
mapa_gmn . geometry = mapa_gmn . geometry . simplify (0.005)
gmn_geoPath = mapa_gmn . to_json ()
mapa = folium . Map ([52 , 19] , zoom_start =6)
folium . Choropleth ( geo_data = gmn_geoPath ,
data = dane_gus_gmn ,
columns =[ ' TERYT_gmn ' , ' Stopa_bezrobocia '] ,
key_on = ' feature . properties . JPT_KOD_JE ' ,
fill_color = ' YlOrRd ' ,
fill_opacity = 0.7,
line_opacity = 0.2,
legend_name = " Stopa bezrobocia w gminie " ).\
add_to ( mapa )
mapa . save ( outfile = ' bezrobocie_gminy . html ')
webbrowser . open_new_tab ( " bezrobocie_gminy . html " )