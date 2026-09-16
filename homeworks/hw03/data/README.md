# Ann Arbor wind snapshot

Source: Iowa Environmental Mesonet ASOS/AWOS/METAR archive.
Station: ARB (KARB). Downloaded 2026-09-14.
Interval: 2025-09-01 00:00 UTC through, but not including, 2025-09-08 00:00 UTC.
Report types: routine and special METAR (3 and 4).

[Exact download query](https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?station=ARB&data=drct&data=sknt&year1=2025&month1=9&day1=1&year2=2025&month2=9&day2=8&tz=Etc%2FUTC&format=onlycomma&latlon=no&elev=no&missing=M&trace=T&direct=no&report_type=3&report_type=4)

The CSV preserves the downloaded response: station, valid (UTC), drct (degrees from true north), sknt (knots). M indicates missing data. These are sustained winds, not gusts. Reports are irregularly spaced.

The notebook retains nonnegative finite speeds, converts calm observations to zero vectors regardless of direction, and otherwise requires a finite direction from 0 to 360 degrees. It excludes unusable reports and sorts by time. It embeds an identical CSV snapshot for standalone Colab use; keep both copies synchronized if the data change.

The nominal runway bearings are intentionally simplified, not surveyed headings. No runway-selection or safety thresholds are modeled.
