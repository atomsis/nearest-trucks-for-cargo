## API for finding the nearest trucks to a given geographical point(spec for WelbeX)
## Stack and Functionality
__Stack__:<br/>

__Framework__:<br/>
 -Django Rest Framework<br/> 
__Database__:<br/>
 -PostgreSQL<br/>
__Deployment__:<br/>
 -Docker Compose<br/>
__Functionality__:<br/>

1. Cargo Management:

- Create new cargo with pick-up and delivery locations determined by the entered zip code.
- Retrieve a list of cargos, including pick-up and delivery locations and the number of nearest trucks within a specified radius.
- Retrieve detailed information about a specific cargo by ID, including pick-up and delivery locations, weight, description, and a list of all truck numbers with distances to the cargo.
- Update cargo details such as weight and description.
- Delete cargo by ID.
- Truck Management:

2. Retrieve a list of trucks.
- Update a truck's location by ID, determined by the entered zip code.
3. Location Management:

 - Import a list of unique locations from a provided CSV file into the PostgreSQL database upon application startup.
4. Distance Calculation:

 - Calculate distances between cargos and trucks based on their geographical locations using the geopy library.
 - Display distances in miles.
5. Additional Features:

 - Filter the list of cargos by weight and distance to nearest trucks.
 - Automatic update of truck locations every 3 minutes.
## Sample Usage Scenarios:
1. Scenario 1: Creating a New Cargo:
 - A user submits a request to create a new cargo, providing pick-up and delivery zip codes, weight, and description.
 - The system creates a new cargo entry in the database, assigning it a unique ID and determining pick-up and delivery locations based on the provided zip codes.
2. Scenario 2: Retrieving Detailed Cargo Information:

 - A user requests detailed information about a specific cargo by providing its ID.
 - The system retrieves the cargo's details from the database, including pick-up and delivery locations, weight, description, and a list of all truck numbers with distances to the cargo.
3. Scenario 3: Updating Truck Location:

 - A user updates a truck's location by providing its ID and a new zip code.
 - The system updates the truck's location in the database based on the provided zip code.
4. Scenario 4: Filtering Cargos:

 - A user filters the list of cargos based on weight and distance to nearest trucks.
 - The system retrieves cargos from the database that meet the specified criteria and returns the filtered list to the user.
5. Scenario 5: Automatic Location Update:

 - Trucks' locations are automatically updated every 3 minutes, ensuring real-time data accuracy and reflecting the dynamic nature of truck movements.
