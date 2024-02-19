import csv
import matplotlib.pyplot as plt

'''This code loops through Honda Car Data and tries to visualize what each trim of a civic or accord 
according to rating'''


def plotCarRatings(ratings, models, car):
        
    plt.boxplot(ratings, labels = models)
    plt.title(f'{car} Ratings by Trim')
    plt.xlabel(f'{car} Trim')
    plt.ylabel('Ratings')
    plt.savefig(f'{car}_ratings_boxplot.png')
    plt.clf()

# find the trim with the best average rating
def findBestAvg(carDict):
    for value in carDict:
        totRatings = 0
        numRatings = 0
        for i in carDict[value]:
            totRatings += i
            numRatings += 1
            
        
        carDict[value] = round(totRatings / numRatings, 2)
    
    
    bestAvg = 0
    for values in carDict:
        if carDict[values] > bestAvg:
            bestCar = values
            bestAvg = carDict.get(values)
    foundValLst = [bestCar, bestAvg]
    return foundValLst

if __name__ == "__main__":
# ###################################
# -- Honda Civic -- #
# ################################### 
    # Open OG data CSV in read mode
    with open('honda_sell_data.csv', 'r') as hondaData:
        # Loop though CSV and obtain only data as it relates to all models of Honda Civic 
        csvfile = csv.reader(hondaData, delimiter = ',')
        header = next(csvfile)
        # Create new CSV to ensure that data is being manipulated correctly 
        with open('civic_data.csv', 'w', newline = '\n') as civicResults:
            writer = csv.writer(civicResults, delimiter = ' ')
            for row in csvfile:
                for col in row:
                    if "Civic" in col:
                        writer.writerow(row)

    # Open civic_data and start categorizing model and rating
    with open('civic_data.csv', 'r') as allCivics:
        # Initalize empty lst that will hold all model years in dataset
        modelYearsCivic = []
        allModelsCivic = []
        csvfile = csv.reader(allCivics, delimiter = ' ')
        for row in csvfile:
            if int(row[0]) not in modelYearsCivic:
                modelYearsCivic.append(int(row[0]))
            if row[2] not in modelYearsCivic:
                allModelsCivic.append(row[2])

    with open('civic_data.csv', 'r') as civicData:
        csvfile = csv.reader(civicData, delimiter = ' ')

        # Save ratings corresponding to each model
        sport_ratings = [] 
        sexy_si_ratings = []
        type_r_ratings = [] 
        hybrid_ratings = [] 
        EX_ratings = [] 
        touring_ratings = [] 
        LX_ratings = [] 

        # Assign ratings corresponding to each trim
        for row in csvfile:   
            if "Civic Sport" in row[2]:
                sport_ratings.append(float(row[5]))
            elif "Civic Si" in row[2]:
                sexy_si_ratings.append(float(row[5]))
            elif "Civic Type R" in row[2]:
                type_r_ratings.append(float(row[5]))
            elif "Civic Hybrid" in row[2]:
                hybrid_ratings.append(float(row[5]))
            elif "Civic EX" in row[2]:
                EX_ratings.append(float(row[5]))
            elif "Civic Touring" in row[2]:
                touring_ratings.append(float(row[5]))
            elif "Civic LX" in row[2]:
                LX_ratings.append(float(row[5]))

    all_civic_models = ["Sport", "Si", "Type-R", "Hybrid", "EX", "Touring", "LX"]

    all_civic_ratings = [sport_ratings, sexy_si_ratings, type_r_ratings,
                hybrid_ratings, EX_ratings, touring_ratings,
                LX_ratings]
    
    # Create boxplot for each civic trim
    plotCarRatings(all_civic_ratings, all_civic_models, "Civic")

    # Create Civic Dictionary and print trim with highest rating
    civicDict = {all_civic_models[i]:all_civic_ratings[i] for i in range(len(all_civic_models))}
    bestCivic = findBestAvg(civicDict)
    print(f"OUTPUT The Honda Civic with the highest average rated trim is the '{bestCivic[0]}' with an average score of {bestCivic[1]:.2f}")


# ###################################
# -- Honda Accord -- #
# ################################### 
    with open('honda_sell_data.csv', 'r') as hondaData:
        # Loop though CSV and obtain only data as it relates to all models of Honda Accord 
        csvfile = csv.reader(hondaData, delimiter = ',')
        header = next(csvfile)
        # Create new CSV to ensure that data is being manipulated correctly 
        with open('accord_data.csv', 'w', newline = '\n') as accordResult:
            writer = csv.writer(accordResult, delimiter = ' ')
            for row in csvfile:
                for col in row:
                    if "Accord" in col:
                        writer.writerow(row)

    # Open accord_data and start categorizing model and rating
    with open('accord_data.csv', 'r') as allAccords:
        # Initalize empty lst that will hold all model years in dataset
        modelYearsAccord = []
        allModelsAccord = []
        csvfile = csv.reader(allAccords, delimiter = ' ')
        for row in csvfile:
            if int(row[0]) not in modelYearsAccord:
                modelYearsAccord.append(int(row[0]))
            if row[2] not in allModelsAccord:
                allModelsAccord.append(row[2])

    with open('accord_data.csv', 'r') as accordData:
        csvfile = csv.reader(accordData, delimiter = ' ')

        # Save ratings corresponding to each model
        sport_accord = []
        ex_accord = [] 
        hybrid_accord = []
        touring_accord = [] 
        lx_accord = [] 
        crosstour_accord = []

        # Assign values for each trim
        for row in csvfile:   
            if "Accord Sport" in row[2] or "Accord SE" in row[2]:
                sport_accord.append(float(row[5]))
            elif "Accord EX" in row[2]:
                ex_accord.append(float(row[5]))
            elif "Accord Hybrid" in row[2] or "Accord Plug-In" in row[2]:
                hybrid_accord.append(float(row[5]))
            elif "Accord Touring" in row[2]:
                touring_accord.append(float(row[5]))
            elif "Accord LX" in row[2]:
                lx_accord.append(float(row[5]))
            elif "Accord Crosstour" in row[2]:
                crosstour_accord.append(float(row[5]))

    all_accord_models = ["Sport", "EX", "Hybrid", "Touring", "LX", "Crosstour"]
    all_accord_ratings = [sport_accord, ex_accord, hybrid_accord, touring_accord, lx_accord, crosstour_accord]

    # Create boxplot corresponding to each Accord trim
    plotCarRatings(all_accord_ratings, all_accord_models, "Accord")

    # Create Accord Dictionary and print trim with highest rating
    accordDict = {all_accord_models[i]:all_accord_ratings[i] for i in range(len(all_accord_models))}
    bestAccord = findBestAvg(accordDict)
    print(f"OUTPUT The Honda Accord with the highest average rated trim is the '{bestAccord[0]}' with an average score of {bestAccord[1]:.2f}")