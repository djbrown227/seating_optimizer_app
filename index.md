---
layout: default
title: Seating Arrangement Optimization
---

# Seating Arrangement Optimization using Simulated Annealing

## 🎯 Project Overview

This project uses **simulated annealing** to optimize seating arrangements at events, ensuring that friends are seated together based on their friendship scores. Given a user-uploaded Excel file and a chosen number of seats per table, the algorithm calculates a seating configuration that maximizes total friendship.

---

## 📽️ Demo Video

  <iframe width="560" height="315" src="https://www.youtube.com/embed/omG6Dd9p_M" frameborder="0" allowfullscreen></iframe>

---

## 🧠 How It Works

Simulated annealing is inspired by the process of **cooling molten metal**. The idea is to allow the system to make poor decisions occasionally (explore worse seating arrangements) to avoid getting stuck in a bad configuration (local optimum). Over time, the probability of accepting worse decisions is reduced, guiding the system to a globally optimized solution.

Here’s a simplified flow:
1. Start with a **random arrangement** of people.
2. Calculate the **friendship score**.
3. Swap two people and evaluate the new score.
4. Accept or reject the new arrangement based on probability.
5. **Repeat until convergence**.

---

## 🖼️ Screenshots & Visuals

### 📊 Friendship Matrix Input

![Friendship matrix sample](/assets/images/Screenshot 2025-05-13 at 2.14.33 PM.png)
> Sample of the uploaded Excel file showing pairwise friendship scores.

### 🪑 Optimized Seating Chart Output

![Seating chart output](/assets/images/Seating_Optimizer/assets/Screenshot 2025-05-13 at 2.34.38 PM.png)
> Optimized table arrangement where high-scoring friendships are grouped together.

---

## ⚙️ Features

- Upload a **friendship matrix** via Excel.
- Customize the number of **seats per table**.
- Generate an **optimized seating arrangement** that maximizes group cohesion.
- See the results **visually** via seating charts and downloadable outputs.
- **Planned Improvements**:
  - Penalize seating people with low friendship scores together.
  - Allow for **mandatory pairings** (e.g., best friends, family members).

---

## 🧪 Example Use Case

A wedding planner uploads a friendship matrix, specifying 10 tables with 8 seats each. The app rearranges guests to seat friends together while minimizing random pairings. With this tool, planners can:
- Increase guest satisfaction,
- Avoid awkward seating, and
- Save time with auto-generated layouts.

---

## 🛠️ How to Use

1. Prepare an Excel file with friendship scores.
2. Upload the file through the app.
3. Set the number of seats per table.
4. Run the algorithm and view the output.
5. Download the results or embed the charts.

---

## 🤝 Contribute

This project is open-source and welcomes contributions!

- Fork the repo
- Make your changes
- Submit a pull request

> For feature suggestions or bug reports, open an [issue](https://github.com/yourusername/seating-app/issues)

---

## 📫 Contact

Have feedback or want to collaborate? Reach out on [GitHub](https://github.com/yourusername) or [Twitter](https://twitter.com/yourhandle).

