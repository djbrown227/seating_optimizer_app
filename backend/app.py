# Import the required modules
from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd

# Initialize Flask app
template_folder = '../frontend/templates'  # Adjust if necessary based on your actual folder structure
app = Flask(__name__, template_folder=template_folder)

# Generate initial seating arrangement
def generate_initial_seating(num_people, num_tables, num_seats_per_table):
    people = list(range(num_people))
    np.random.shuffle(people)
    tables = []
    start = 0
    for seats in num_seats_per_table:
        tables.append(people[start:start + seats])
        start += seats
    return tables

# Calculate score based on seating arrangement and friendship matrix
def calculate_score(seating_arrangement, friendship_matrix):
    total_score = 0
    for table in seating_arrangement:
        for person1 in table:
            for person2 in table:
                if person1 != person2:
                    total_score += friendship_matrix[person1][person2]
    return total_score

# Simulated annealing algorithm for optimizing seating arrangement
def simulated_annealing(initial_seating_arrangement, friendship_matrix, temperature_decay=0.99):
    current_seating_arrangement = initial_seating_arrangement
    best_seating_arrangement = initial_seating_arrangement
    best_score = calculate_score(best_seating_arrangement, friendship_matrix)
    current_temperature = 1.0
    while current_temperature > 0.001:
        table1, table2 = np.random.choice(len(current_seating_arrangement), 2, replace=False)
        person1 = np.random.choice(current_seating_arrangement[table1])
        person2 = np.random.choice(current_seating_arrangement[table2])
        current_seating_arrangement[table1].remove(person1)
        current_seating_arrangement[table2].remove(person2)
        current_seating_arrangement[table1].append(person2)
        current_seating_arrangement[table2].append(person1)
        new_score = calculate_score(current_seating_arrangement, friendship_matrix)
        if new_score >= best_score or np.random.rand() < np.exp((new_score - best_score) / current_temperature):
            best_seating_arrangement = [table.copy() for table in current_seating_arrangement]
            best_score = new_score
        current_temperature *= temperature_decay
    return best_seating_arrangement, best_score

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_seating', methods=['POST'])
def generate_seating():
    if 'friendship_file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['friendship_file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    num_seats_per_table = request.form.get('num_seats_per_table', type=lambda v: [int(i) for i in v.split(',')])
    if not num_seats_per_table:
        return jsonify({'error': 'Seats per table data is missing'}), 400

    friendships_df = pd.read_excel(file, index_col=0)
    friendships_df.fillna(0, inplace=True)
    friendships_df = friendships_df.astype(int)
    index_to_name = friendships_df.index.tolist()

    num_people = len(index_to_name)
    num_tables = len(num_seats_per_table)
    initial_seating_arrangement = generate_initial_seating(num_people, num_tables, num_seats_per_table)

    friendship_matrix = friendships_df.values
    best_seating_arrangement, best_score = simulated_annealing(initial_seating_arrangement, friendship_matrix)

    best_seating_arrangement_with_names = [[index_to_name[person] for person in table] for table in best_seating_arrangement]
    best_score = int(best_score)  # Convert to native Python int for JSON serialization

    return jsonify({'seating_arrangement': best_seating_arrangement_with_names, 'score': best_score})



if __name__ == '__main__':
    app.run(debug=True)
