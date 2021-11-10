import os

def countWorkers():
	
	fileContent = open( "feherBt.txt", "r", encoding="utf-8" )
	counter = 0
	row = fileContent.readline()
	while( row ):
		row = fileContent.readline()
		if( len( row ) != 0 ):
			counter += 1
	
	fileContent.close()
	return counter


def countAverageSalary( workers ):
	
	fileContent = open( "feherBt.txt", "r", encoding="utf-8" )
	sumSalary = 0
	
	row = fileContent.readline()
	while( row ):
		
		row = fileContent.readline()
		if( len( row ) != 0 ):
			rowList = row.strip().split( ":" )
			sumSalary += float( rowList[3] )
	
	fileContent.close()
	average = sumSalary / workers
	return average
	
def highestSalary( city ):
	
	fileContent = open( "feherBt.txt", "r", encoding="utf-8" )
	highest = 0
	luckyPerson = []
	
	row = fileContent.readline()
	while( row ):
		
		row = fileContent.readline()
		if( len( row ) != 0 ):
			rowList = row.strip().split( ":" )
			if( rowList[1] == city ):
				if( float( rowList[3] ) > highest ):
					highest = float( rowList[3] )
					luckyPerson = rowList
	
	fileContent.close()
	return luckyPerson
	
def start():
	
	if( os.path.exists( "feherBt.txt" )):
		
		print( "Készítő: Rékási József\n2021.11.7\n" )
		print( "Első feladat: Dolgozók megszámlása:" )
		workers = countWorkers()
		print( "\tA dolgozók létszáma: ", workers )
		
		print( "\nMásodik feladat: Átlagfizetések számítása:" )
		average = countAverageSalary( workers ) / 1000
		print( "\tA dolgozók átlagfizetése: {:.1f} ezer".format( average ) )
		
		print( "\nHarmadik feladat: Adott város legjobban kereső dolgozója:" )
		city = input( "Kérem a várost: " )
		lucky = highestSalary( city )
		for data in lucky:
			print( data )
	else:
		print( "Nincs meg a fájl!" )

start()
