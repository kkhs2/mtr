


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
    'TUM': 'Tuen Mun',
    'SIH': 'Siu Hong',
    'TIS': 'Tin Shui Wai',
    'LOP': 'Long Ping',
    'YUL': 'Yuen Long',
    'KSR': 'Kam Sheung Road',
    'TWW': 'Tsuen Wan West',
    'MEF': 'Mei Foo',
    'NAC': 'Nam Cheong',
    'AUS': 'Austin',
    'ETS': 'East Tsim Sha Tsui',
    'HUH': 'Hung Hom'
  },
  'TKL': {
    'NOP': 'North Point',
    'QUB': 'Quarry Bay',
    'YAT': 'Yau Tong',
    'TIK': 'Tiu Keng Leng',
    'TKO': 'Tseung Kwan O',
    'HAH': 'Hang Hau',
    'POA': 'Po Lam',
    'LHP': 'LOHAS Park'
  }
}




priceMap = {
  'TCL': {
    'HOK': {
      'WRL': {
        'TUM': 30.00,
        'SIH': 30.00,
        'TIS': 30.00,
        'LOP': 30.00,
        'YUL': 30.00,
        'KSR': 29.00,
        'TWW': 19.00,
        'MEF': 15.50,
        'NAC': 14.50,
        'AUS': 11.50,
        'ETS': 11.50,
        'HUH': 14.00
      },
      'TKL': {
        'NOP': 7.50,
        'QUB': 7.50,
        'YAT': 15.50,
        'TIK': 15.50,
        'TKO': 15.50,
        'HAH': 15.50,
        'POA': 15.50,
        'LHP': 15.50
      }
    },
    'KOW': {
      'WRL': {
        'TUM': 22.00,
        'SIH': 22.00,
        'TIS': 22.00,
        'LOP': 22.00,
        'YUL': 22.00,
        'KSR': 21.00,
        'TWW': 11.00,
        'MEF': 10.00,
        'NAC': 6.00,
        'AUS': 5.00,
        'ETS': 5.00,
        'HUH': 7.00
      },
      'TKL': {
        'NOP': 14.50,
        'QUB': 14.50,
        'YAT': 10.00,
        'TIK': 12.00,
        'TKO': 12.00,
        'HAH': 12.00,
        'POA': 12.00,
        'LHP': 12.00
      }
    },
	  'OLY': {
      'WRL': {
        'TUM': 21.00,
        'SIH': 21.00,
        'TIS': 21.00,
        'LOP': 21.00,
        'YUL': 21.00,
        'KSR': 19.00,
        'TWW': 10.00,
        'MEF': 7.50,
        'NAC': 5.00,
        'AUS': 5.00,
        'ETS': 6.00,
        'HUH': 7.00
      },
      'TKL': {
        'NOP': 14.50,
        'QUB': 15.50,
        'YAT': 10.00,
        'TIK': 12.00,
        'TKO': 12.00,
        'HAH': 12.00,
        'POA': 12.00,
        'LHP': 12.00
      }
    },
	  'NAC': {
      'WRL': {
        'TUM': 18.00,
        'SIH': 18.00,
        'TIS': 18.00,
        'LOP': 18.00,
        'YUL': 18.00,
        'KSR': 16.50,
        'TWW': 9.50,
        'MEF': 6.00,
        'NAC': 'No stop',
        'AUS': 6.00,
        'ETS': 6.50,
        'HUH': 6.50
      },
      'TKL': {
        'NOP': 15.50,
        'QUB': 15.50,
        'YAT': 12.00,
        'TIK': 12.00,
        'TKO': 12.00,
        'HAH': 12.00,
        'POA': 12.00,
        'LHP': 12.00
      }
    },
	  'LAK': {
      'WRL': {
        'TUM': 19.00,
        'SIH': 19.00,
        'TIS': 19.00,
        'LOP': 19.00,
        'YUL': 19.00,
        'KSR': 18.00,
        'TWW': 6.00,
        'MEF': 5.00,
        'NAC': 6.00,
        'AUS': 10.00,
        'ETS': 12.00,
        'HUH': 9.50
      },
      'TKL': {
        'NOP': 15.50,
        'QUB': 15.50,
        'YAT': 12.00,
        'TIK': 12.00,
        'TKO': 12.00,
        'HAH': 12.00,
        'POA': 14.50,
        'LHP': 14.50
      }
    },
	  'TSY': {
      'WRL': {
        'TUM': 21.00,
        'SIH': 21.00,
        'TIS': 21.00,
        'LOP': 21.00,
        'YUL': 21.00,
        'KSR': 19.00,
        'TWW': 6.00,
        'MEF': 6.00,
        'NAC': 7.50,
        'AUS': 12.00,
        'ETS': 12.00,
        'HUH': 11.50 
      },
      'TKL': {
        'NOP': 15.50,
        'QUB': 15.50,
        'YAT': 12.00,
        'TIK': 12.00,
        'TKO': 14.50,
        'HAH': 14.50,
        'POA': 14.50,
        'LHP': 14.50
      }
    },
	  'SUN': {
      'WRL': {
        'TUM': 29.00,
        'SIH': 29.00,
        'TIS': 29.00,
        'LOP': 29.00,
        'YUL': 29.00,
        'KSR': 28.50,
        'TWW': 18.00,
        'MEF': 14.50,
        'NAC': 14.50,
        'AUS': 16.50,
        'ETS': 16.50,
        'HUH': 19.50
      },
      'TKL': {
        'NOP': 27.00,
        'QUB': 27.00,
        'YAT': 24.50,
        'TIK': 24.50,
        'TKO': 24.50,
        'HAH': 24.50,
        'POA': 24.50,
        'LHP': 24.50
      }
    },
	  'TUC': {
      'WRL': {
        'TUM': 31.50,
        'SIH': 31.50,
        'TIS': 31.50,
        'LOP': 31.50,
        'YUL': 31.50,
        'KSR': 31.00,
        'TWW': 22.00,
        'MEF': 16.50,
        'NAC': 16.50,
        'AUS': 20.50,
        'ETS': 20.50,
        'HUH': 25.00
      },
      'TKL': {
        'NOP': 30.00,
        'QUB': 30.00,
        'YAT': 27.00,
        'TIK': 27.00,
        'TKO': 27.00,
        'HAH': 27.00,
        'POA': 27.00,
        'LHP': 27.00
      }
    }
  },
  'WRL': {
    'TUM': {
      'TCL': {
        'HOK': 30.00,
		    'KOW': 22.00,
		    'OLY': 21.00,
		    'NAC': 18.00,
		    'LAK': 19.00,
		    'TSY': 21.00,
		    'SUN': 29.00,
		    'TUC': 31.50
      },
      'TKL': {
        'NOP': 31.00,
        'QUB': 31.00,
        'YAT': 27.00,
        'TIK': 27.00,
        'TKO': 27.00,
        'LHP': 27.00,
        'HAH': 27.00,
        'POA': 27.00 
      }
    },
    'SIH': {
      'TCL': {
        'HOK': 30.00,
		    'KOW': 22.00,
		    'OLY': 21.00,
		    'NAC': 18.00,
		    'LAK': 19.00,
		    'TSY': 21.00,
		    'SUN': 29.00,
		    'TUC': 31.50 
      },
      'TKL': {
        'NOP': 31.00,
        'QUB': 31.00,
        'YAT': 27.00,
        'TIK': 27.00,
        'TKO': 27.00,
        'LHP': 27.00,
        'HAH': 27.00,
        'POA': 27.00  
      }
    },
    'TIS': {
      'TCL': {
        'HOK': 30.00,
		    'KOW': 22.00,
		    'OLY': 21.00,
		    'NAC': 18.00,
		    'LAK': 19.00,
		    'TSY': 21.00,
		    'SUN': 29.00,
		    'TUC': 31.50 
      },
      'TKL': {
        'NOP': 31.00,
        'QUB': 31.00,
        'YAT': 27.00,
        'TIK': 27.00,
        'TKO': 27.00,
        'LHP': 27.00,
        'HAH': 27.00,
        'POA': 27.00  
      }
    },
    'LOP': {
      'TCL': {
        'HOK': 30.00,
		    'KOW': 22.00,
		    'OLY': 21.00,
		    'NAC': 18.00,
		    'LAK': 19.00,
		    'TSY': 21.00,
		    'SUN': 29.00,
		    'TUC': 31.50 
      },
      'TKL': {
        'NOP': 31.00,
        'QUB': 31.00,
        'YAT': 27.00,
        'TIK': 27.00,
        'TKO': 27.00,
        'LHP': 27.00,
        'HAH': 27.00,
        'POA': 27.00  
      }
    },
    'YUL': {
      'TCL': {
        'HOK': 30.00,
		    'KOW': 22.00,
		    'OLY': 21.00,
		    'NAC': 18.00,
		    'LAK': 19.00,
		    'TSY': 21.00,
		    'SUN': 29.00,
		    'TUC': 31.50 
      },
      'TKL': {
        'NOP': 31.00,
        'QUB': 31.00,
        'YAT': 27.00,
        'TIK': 27.00,
        'TKO': 27.00,
        'LHP': 27.00,
        'HAH': 27.00,
        'POA': 27.00  
      }
    },
    'KSR': {
      'TCL': {
        'HOK': 29.00,
		    'KOW': 21.00,
		    'OLY': 19.00,
		    'NAC': 16.50,
		    'LAK': 18.00,
		    'TSY': 19.00,
		    'SUN': 28.50,
		    'TUC': 31.00
      },
      'TKL': {
        'NOP': 30.00,
        'QUB': 30.00,
        'YAT': 25.50,
        'TIK': 25.50,
        'TKO': 25.50,
        'LHP': 25.50,
        'HAH': 25.50,
        'POA': 25.50 
      }
    },
    'TWW': {
      'TCL': {
        'HOK': 19.00,
		    'KOW': 11.00,
		    'OLY': 10.00,
		    'NAC': 9.50,
		    'LAK': 6.00,
		    'TSY': 6.00,
		    'SUN': 18.00,
		    'TUC': 22.00
      },
      'TKL': {
        'NOP': 20.50,
        'QUB': 20.50,
        'YAT': 15.00,
        'TIK': 15.00,
        'TKO': 15.00,
        'LHP': 15.00,
        'HAH': 15.00,
        'POA': 15.00 
      }
    },
    'MEF': {
      'TCL': {
        'HOK': 15.50,
		    'KOW': 10.00,
		    'OLY': 7.50,
		    'NAC': 6.00,
		    'LAK': 5.00,
		    'TSY': 6.00,
		    'SUN': 14.50,
		    'TUC': 16.50
      },
      'TKL': {
        'NOP': 15.50,
        'QUB': 15.50,
        'YAT': 12.00,
        'TIK': 12.00,
        'TKO': 12.00,
        'LHP': 12.00,
        'HAH': 12.00,
        'POA': 12.00 
      }
    },
    'NAC': {
      'TCL': {
        'HOK': 14.50,
		    'KOW': 6.00,
		    'OLY': 5.00,
		    'NAC': 'No stop',
		    'LAK': 6.00,
		    'TSY': 7.50,
		    'SUN': 14.50,
		    'TUC': 16.50
      },
      'TKL': {
        'NOP': 15.50,
        'QUB': 15.50,
        'YAT': 12.00,
        'TIK': 12.00,
        'TKO': 12.00,
        'LHP': 12.00,
        'HAH': 12.00,
        'POA': 12.00 
      }
    },
    'AUS': {
      'TCL': {
        'HOK': 11.50,
		    'KOW': 5.00,
		    'OLY': 5.00,
		    'NAC': 6.00,
		    'LAK': 10.00,
		    'TSY': 12.00,
		    'SUN': 16.50,
		    'TUC': 20.50
      },
      'TKL': {
        'NOP': 14.50,
        'QUB': 14.50,
        'YAT': 10.00,
        'TIK': 12.00,
        'TKO': 12.00,
        'LHP': 12.00,
        'HAH': 12.00,
        'POA': 11.50  
      }
    },
    'ETS': {
      'TCL': {
        'HOK': 11.50,
		    'KOW': 5.00,
		    'OLY': 5.00,
		    'NAC': 6.50,
		    'LAK': 12.00,
		    'TSY': 12.00,
		    'SUN': 16.50,
		    'TUC': 20.50
      },
      'TKL': {
        'NOP': 14.50,
        'QUB': 14.50,
        'YAT': 10.00,
        'TIK': 12.00,
        'TKO': 12.00,
        'LHP': 12.00,
        'HAH': 12.00,
        'POA': 12.00 
      }
    },
    'HUH': {
      'TCL': {
        'HOK': 14.00,
		    'KOW': 7.00,
		    'OLY': 7.00,
		    'NAC': 6.50,
		    'LAK': 9.50,
		    'TSY': 11.50,
		    'SUN': 19.50,
		    'TUC': 25.00
      },
      'TKL': {
        'NOP': 16.50,
        'QUB': 16.50,
        'YAT': 11.50,
        'TIK': 11.50,
        'TKO': 13.00,
        'LHP': 13.00,
        'HAH': 13.00,
        'POA': 13.00
      }
    }
  },
  'TKL': {
    'NOP': {
      'TCL': {
        'HOK': 7.50,
		    'KOW': 14.50,
		    'OLY': 14.50,
		    'NAC': 15.50,
		    'LAK': 15.50,
		    'TSY': 15.50,
		    'SUN': 27.00,
		    'TUC': 30.00
      },
      'WRL': {
        'TUM': 31.00,
        'SIH': 31.00,
        'TIS': 31.00,
        'LOP': 31.00,
        'YUL': 31.00,
        'KSR': 30.00,
        'TWW': 20.50,
        'MEF': 15.50,
        'NAC': 15.50,
        'AUS': 14.50,
        'ETS': 14.50,
        'HUH': 16.50
      }
    },
    'QUB': {
      'TCL': {
        'HOK': 7.50,
		    'KOW': 14.50,
		    'OLY': 15.50,
		    'NAC': 15.50,
		    'LAK': 15.50,
		    'TSY': 15.50,
		    'SUN': 27.00,
		    'TUC': 30.00
      },
      'WRL': {
        'TUM': 31.00,
        'SIH': 31.00,
        'TIS': 31.00,
        'LOP': 31.00,
        'YUL': 31.00,
        'KSR': 30.00,
        'TWW': 20.50,
        'MEF': 15.50,
        'NAC': 15.50,
        'AUS': 14.50,
        'ETS': 14.50,
        'HUH': 16.50 
      }
    },
    'YAT': {
      'TCL': {
        'HOK': 15.50,
		    'KOW': 10.00,
		    'OLY': 10.00,
		    'NAC': 12.00,
		    'LAK': 12.00,
		    'TSY': 12.00,
		    'SUN': 24.50,
		    'TUC': 27.00
      },
      'WRL': {
        'TUM': 27.00,
        'SIH': 27.00,
        'TIS': 27.00,
        'LOP': 27.00,
        'YUL': 27.00,
        'KSR': 25.50,
        'TWW': 15.00,
        'MEF': 12.00,
        'NAC': 12.00,
        'AUS': 10.00,
        'ETS': 10.00,
        'HUH': 11.50
      }
    },
    'TIK': {
      'TCL': {
        'HOK': 15.50,
		    'KOW': 12.00,
		    'OLY': 12.00,
		    'NAC': 12.00,
		    'LAK': 12.00,
		    'TSY': 12.00,
		    'SUN': 24.50,
		    'TUC': 27.00
      },
      'WRL': {
        'TUM': 27.00,
        'SIH': 27.00,
        'TIS': 27.00,
        'LOP': 27.00,
        'YUL': 27.00,
        'KSR': 25.50,
        'TWW': 15.00,
        'MEF': 12.00,
        'NAC': 12.00,
        'AUS': 12.00,
        'ETS': 12.00,
        'HUH': 11.50 
      }
    },
    'TKO': {
      'TCL': {
        'HOK': 15.50,
		    'KOW': 12.00,
		    'OLY': 12.00,
		    'NAC': 12.00,
		    'LAK': 12.00,
		    'TSY': 14.50,
		    'SUN': 24.50,
		    'TUC': 27.00 
      },
      'WRL': {
        'TUM': 27.00,
        'SIH': 27.00,
        'TIS': 27.00,
        'LOP': 27.00,
        'YUL': 27.00,
        'KSR': 25.50,
        'TWW': 15.00,
        'MEF': 12.00,
        'NAC': 12.00,
        'AUS': 12.00,
        'ETS': 12.00,
        'HUH': 13.00
      }
    },
    'HAH': {
      'TCL': {
        'HOK': 15.50,
		    'KOW': 12.00,
		    'OLY': 12.00,
		    'NAC': 12.00,
		    'LAK': 12.00,
		    'TSY': 14.50,
		    'SUN': 24.50,
		    'TUC': 27.00 
      },
      'WRL': {
        'TUM': 27.00,
        'SIH': 27.00,
        'TIS': 27.00,
        'LOP': 27.00,
        'YUL': 27.00,
        'KSR': 25.50,
        'TWW': 15.00,
        'MEF': 12.00,
        'NAC': 12.00,
        'AUS': 12.00,
        'ETS': 12.00,
        'HUH': 13.00
      }
    },
    'POA': {
      'TCL': {
        'HOK': 15.50,
		    'KOW': 12.00,
		    'OLY': 12.00,
		    'NAC': 12.00,
		    'LAK': 14.50,
		    'TSY': 14.50,
		    'SUN': 24.50,
		    'TUC': 27.00
      },
      'WRL': {
        'TUM': 27.00,
        'SIH': 27.00,
        'TIS': 27.00,
        'LOP': 27.00,
        'YUL': 27.00,
        'KSR': 25.50,
        'TWW': 15.00,
        'MEF': 12.00,
        'NAC': 12.00,
        'AUS': 12.00,
        'ETS': 12.00,
        'HUH': 13.00
      }
    },
    'LHP': {
      'TCL': {
        'HOK': 15.50,
		    'KOW': 12.00,
		    'OLY': 12.00,
		    'NAC': 12.00,
		    'LAK': 14.50,
		    'TSY': 14.50,
		    'SUN': 24.50,
		    'TUC': 27.00 
      },
      'WRL': {
        'TUM': 27.00,
        'SIH': 27.00,
        'TIS': 27.00,
        'LOP': 27.00,
        'YUL': 27.00,
        'KSR': 25.50,
        'TWW': 15.00,
        'MEF': 12.00,
        'NAC': 12.00,
        'AUS': 12.00,
        'ETS': 12.00,
        'HUH': 13.00
      }
    }
  }
}












