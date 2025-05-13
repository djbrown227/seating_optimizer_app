### Seating Arrangement Optimization Web Application

#### Overview
This project offers a web application for optimizing seating arrangements based on friendship relationships. The application utilizes the simulated annealing algorithm to generate seating arrangements that maximize the overall friendship score. Users can upload an Excel file containing friendship data and specify the number of seats per table to generate optimized seating arrangements.

#### Features
1. **Seating Arrangement Generation:** Generates initial seating arrangements based on user-defined parameters such as the number of people, tables, and seats per table.
2. **Friendship Data Upload:** Allows users to upload an Excel file containing friendship data. Missing or incomplete data is handled gracefully.
3. **Simulated Annealing Optimization:** Utilizes the simulated annealing algorithm to optimize seating arrangements by maximizing the overall friendship score.
4. **User-Friendly Interface:** Provides an intuitive web interface for users to input parameters, upload data, and view the optimized seating arrangement along with the calculated score.
5. **Dynamic Interaction:** Enables real-time interaction where users can adjust parameters, upload new data, and visualize different seating arrangements.

#### Technologies Used
- **Flask:** Backend framework for handling HTTP requests and responses.
- **HTML/CSS/JavaScript:** Frontend development for creating a user-friendly interface.
- **Pandas:** Python library for data manipulation, particularly for reading and processing Excel files.
- **NumPy:** Used for numerical computations, array manipulation, and random number generation.
- **Simulated Annealing Algorithm:** Implemented to optimize seating arrangements based on friendship scores.

#### How to Use
1. Clone the repository to your local machine.
2. Install the required dependencies listed in the requirements.txt file.
3. Run the Flask application.
4. Access the web interface in your browser.
5. Specify the number of seats per table and upload an Excel file containing friendship data.
6. Click on "Generate Seating Arrangement" to see the optimized seating arrangement and score.

#### Future Improvements
- Implementation of additional optimization algorithms for comparison.
- Integration of user authentication for secure data uploads.
- Enhancement of the frontend interface with more interactive features and visualizations.
- Support for exporting generated seating arrangements to various formats.
- Performance optimizations for handling larger datasets efficiently.
