# MTC_Octoprint
A MTConnect Agent/Adapter for Octoprint

The included python file was run from inside the PyCharm IDE across a LAN to a Raspberry Pi at the IP specified to retrieve data from the Octoprint API

Unfortunatley, the architecture of Octoprint means the executed command (M114) returns the X, Y, and Z coordinates to the web based termininal, no data is returned to the API, except http session data.

A discussion with Gina Häußge (the developer) yielded some insight as to why this was so, and a new approach will be tried: i.e. I'll attempt to write a custom logging filter for the logging plugin, then parse the logging tools output, format it to the string pairs needed by the MTConnect Agent and run from there.


if you know a better way, please let me know! 
TIA, James
