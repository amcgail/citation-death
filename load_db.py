from knowknow import *

db = Dataset('sociology-wos-74b')

db.groupings.append([
    'c', {
        'Coleman, J.|f social theory': 'Coleman, J.|fdn social theory',
        'Coleman, J.|fdn social theory': 'Coleman, J.|fdn social theory',
        'Coleman, J.|foundations of socia': 'Coleman, J.|fdn social theory'
    }
])

db.groupings.append([
    'c', {
        'Tocqueville, A.|1945|democracy in america,v1':'Tocqueville, A.|democracy am',
        'Tocqueville, A.|democracy am':'Tocqueville, A.|democracy am',
        'Detocqueville, A.|democracy am':'Tocqueville, A.|democracy am',
        'Tocqueville, A.|democracy am':'Tocqueville, A.|democracy am',
        'Detocqueville, A.|1945|democracy am,v2':'Tocqueville, A.|democracy am'
    }
])

db.groupings.append([
    'c', {
        'Latour, B.|lab life constructio':'Latour, B.|laboratory life soci',
        'Latour, B.|laboratory life soci':'Latour, B.|laboratory life soci'
    }
])