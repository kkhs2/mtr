


# the script should start by ascertaining how much money the player has, so it needs the game to pass the balance of the player.

# Hong Kong MTR API - returns real time data for the AEL, TCL, WRL and TKL stations. The Next Train API provides the train arrival schedule for MTR Airport Express Line, Tung Chung Line, West Rail Line and Tseung Kwan O Line. Valid result will be returned only if the combination of parameter 1(line) and parameter 2(sta) is correct. Example request: https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?line=TKL&sta=TKO


mtrApi = 'https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php'

# multi assocative dictonaries for the lines and stations
lines = {
  'TCL': {		
    'HOK': 'Hong Kong',
		'KOW': 'Kowloon',
		'OLY': 'Olympic',
		'NAC': 'Nam Cheong',
		'LAK': 'Lai King',
		'TSY': 'Tsing Yi',
		'SUN': 'Sunny Bay',
		'TUC': 'Tung Chung'
	},
  'WRL': {
    'HUH': 'Hung Hom',
    'ETS': 'East Tsim Sha Tsui',
    'AUS': 'Austin',
    'NAC': 'Nam Cheong',
    'MEF': 'Mei Foo',
    'TWW': 'Tsuen Wan West',
    'KSR': 'Kam Sheung Road',
    'YUL': 'Yuen Long',
    'LOP': 'Long Ping',
    'TIS': 'Tin Shui Wai',
    'SIH': 'Siu Hong',
    'TUM': 'Tuen Mun'
  },
  'TKL': {
    'NOP': 'North Point',
    'QUB': 'Quarry Bay',
    'YAT': 'Yau Tong',
    'TIK': 'Tiu Keng Leng',
    'TKO': 'Tseung Kwan O',
    'LHP': 'LOHAS Park',
    'HAH': 'Hang Hau',
    'POA': 'Po Lam'  
  }
}




priceMap = {
  'HOK': {
    'HUN': 30.00,
    'ETS': 30.00,
    'AUS': 30.00,
    'NAC': 30.00,
    'MEF': 30.00,
    'TWW': 29.00,
    'KSR': 19.00,
    'YUL': 15.50,
    'LOP': 14.50,
    'TIS': 11.50,
    'SIH': 11.50,
    'TUM': 14.00 
  },
  'KOW': {
    'HUN': 22.00,
    'ETS': 22.00,
    'AUS': 22.00,
    'NAC': 22.00,
    'MEF': 22.00,
    'TWW': 21.00,
    'KSR': 11.00,
    'YUL': 10.00,
    'LOP': 6.00,
    'TIS': 5.00,
    'SIH': 5.00,
    'TUM': 7.00
  },
	'OLY': {
    'HUN': 21.00,
    'ETS': 21.00,
    'AUS': 21.00,
    'NAC': 21.00,
    'MEF': 21.00,
    'TWW': 19.00,
    'KSR': 10.00,
    'YUL': 7.50,
    'LOP': 5.00,
    'TIS': 5.00,
    'SIH': 6.00,
    'TUM': 7.00
  },
	'NAC': {
    'HUN': 18.00,
    'ETS': 18.00,
    'AUS': 18.00,
    'NAC': 18.00,
    'MEF': 18.00,
    'TWW': 16.50,
    'KSR': 9.50,
    'YUL': 6.00,
    'LOP': 'No stop',
    'TIS': 6.00,
    'SIH': 6.50,
    'TUM': 6.50
  },
	'LAK': {
    'HUN': 19.00,
    'ETS': 19.00,
    'AUS': 19.00,
    'NAC': 19.00,
    'MEF': 19.00,
    'TWW': 18.00,
    'KSR': 6.00,
    'YUL': 5.00,
    'LOP': 6.00,
    'TIS': 10.00,
    'SIH': 12.00,
    'TUM': 9.50
  },
	'TSY': {
    'HUN': 21.00,
    'ETS': 21.00,
    'AUS': 21.00,
    'NAC': 21.00,
    'MEF': 21.00,
    'TWW': 19.00,
    'KSR': 6.00,
    'YUL': 6.00,
    'LOP': 7.50,
    'TIS': 12.00,
    'SIH': 12.00,
    'TUM': 11.50
  },
	'SUN': {
    'HUN': 29.00,
    'ETS': 29.00,
    'AUS': 29.00,
    'NAC': 29.00,
    'MEF': 29.00,
    'TWW': 28.50,
    'KSR': 18.00,
    'YUL': 14.50,
    'LOP': 14.50,
    'TIS': 16.50,
    'SIH': 16.00,
    'TUM': 19.50
  },
	'TUC': {
    'HUN': 31.50,
    'ETS': 31.50,
    'AUS': 31.50,
    'NAC': 31.50,
    'MEF': 31.50,
    'TWW': 31.00,
    'KSR': 22.00,
    'YUL': 16.50,
    'LOP': 16.50,
    'TIS': 20.50,
    'SIH': 20.50,
    'TUM': 25.00
  }

}







