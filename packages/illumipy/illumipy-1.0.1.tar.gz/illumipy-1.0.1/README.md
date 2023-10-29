illumipy is a Python module for estimating outside Illumination
levels for given location, date and time.()
Requires an OpenWeatherMap API-key (see: https://openweathermap.org/appid)

### Current limitations:
- cloud level, sunrise and sunset are not available for dates in the past. Results might therefore be unreliable. Times for sunrise and sunset will always be for the current day.
- at 100% cloud coverage, Results might be unreliable.

To use the module, simply import illumipy and call the function
data.light_data(): This returns a dictionary object with
the following information:
\t['illuminance']: Outside Brightness in Lux
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;['time']: Time used as %-H (e.g. 4 or 12)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;['date']: Date used as YYYY-MM-DD
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;['city']: City Used
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;['country']: Country Used
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;['cloud_coverage']: Cloud coverage in %
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;['et_illuminance']: Extraterrestrial Illuminance in Lux
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;['direct_illuminance']: Direct Illuminance in Lux
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;['horizontal_illuminance']: Horizontal Illuminance in Lux
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;['horizontal_sky_illuminance']: Horizontal Sky Illuminance in Lux
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;['sunrise']: Time of Sunrise as hh:mm
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;['sunset']: Time of sunset as hh:mm
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;['sun_altitude']: Sund altitude at [Time] in degrees.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;['day']: True if there is daylight at [Time].
It Takes the following arguments:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time: str=[0-24], date: str=[YYYY-MM-DD], city: str=['City'],
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;country: str=['Country'], api_key: str=['api key']
If no arguments are provided, defaults to values defined in defaults.py.

Requirements:
 - Python3
 - Python packages:
 - requests
   - logging
   - math
   - sys
   - datetime
   - argparse
 - OpenWeatherMap API-Key

Author: Kalle Fornia
GitHub: https://github.com/duckwilliam/illumipy
PyPi: https://pypi.org/project/illumipy
Version: 1.0.0
10/2023