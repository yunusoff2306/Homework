import sqlite3

# Step 1: Connect to database (or create it if it doesn't exist)
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# Step 2: Create the Roster table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
""")

# Step 3: Insert values into the table
cursor.executemany("""
    INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

# Step 4: Update Jadzia Dax to Ezri Dax
cursor.execute("""
    UPDATE Roster
    SET Name = 'Ezri Dax'
    WHERE Name = 'Jadzia Dax'
""")

# Step 5: Fetch and display all Bajorans
cursor.execute("""
    SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
""")

print("\n📌 Bajorans in the Roster:")
for row in cursor.fetchall():
    print(f"👤 Name: {row[0]}, Age: {row[1]}")

# Commit changes and close connection
conn.commit()
conn.close()
