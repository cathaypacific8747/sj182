import csv
from colour import Color

linestrings = ''
field = 3
with open('interpolated.csv', 'r', newline='') as f:
    data = list(csv.reader(f))
    min_color = Color("#ff0000")
    max_color = Color("#00ffff")

    min_color = Color("#00ffff")
    max_color = Color("#ff0000")
    colors = list(min_color.range_to(max_color, 256))
    # pct = int(12.5/100*255)
    # print(pct/255, colors[pct])
    mx = max([float(r[field]) for r in data])
    mn = min([float(r[field]) for r in data])
    # print(mn, mx)
    for r in range(len(data)-1):
        thisData = float(data[r+1][field])
        thisColor = colors[int((thisData-mn)/(mx-mn)*255)].hex_l
        linestrings += f'''        <Placemark>
            <Style>
                <LineStyle>
                    <color>ff{thisColor[5:7]}{thisColor[3:5]}{thisColor[1:3]}</color>
                    <width>2</width>
                </LineStyle>
            </Style>
            <MultiGeometry>
                <LineString>
                    <tessellate>1</tessellate>
                    <altitudeMode>absolute</altitudeMode>
                    <coordinates>{data[r][1]},{data[r][0]},{data[r][2]} {data[r+1][1]},{data[r+1][0]},{data[r+1][2]}</coordinates>
                </LineString>
            </MultiGeometry>
            <name>{r}-{r+1}</name>
        </Placemark>'''

kml = f'''<?xml version="1.0" encoding="UTF-8"?>
<kml
	xmlns="http://www.opengis.net/kml/2.2">
	<Document>
		<name>SJ182/SJY182</name>
		<Folder>
			<name>Trail</name>
{linestrings}
		</Folder>
	</Document>
</kml>'''
print(kml)