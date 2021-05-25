## Author: lehag
## Code: T1590-005-GatherVictimNetworkInformationIPAddresses.ps1

(Invoke-WebRequest -uri "http://ipinfo.io/ip/").Content
