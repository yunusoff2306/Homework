import sqlite3
import pandas as pd

# Connect to the Chinook database
conn = sqlite3.connect("chinook.db")

# 1. Customer Purchases Analysis
query = """
    SELECT CustomerId, FirstName || ' ' || LastName AS CustomerName, SUM(Total) AS TotalSpent
    FROM Invoice
    JOIN Customer USING(CustomerId)
    GROUP BY CustomerId
    ORDER BY TotalSpent DESC
    LIMIT 5;
"""
top_customers = pd.read_sql(query, conn)
print("Top 5 Customers with Highest Purchases:")
print(top_customers)

# 2. Album vs. Individual Track Purchases

# Get all purchases (InvoiceLines)
invoice_lines = pd.read_sql("SELECT InvoiceId, TrackId FROM InvoiceLine", conn)

# Get album details
album_tracks = pd.read_sql("""
    SELECT Album.AlbumId, Track.TrackId
    FROM Album
    JOIN Track USING(AlbumId);
""", conn)

# Count tracks per album
album_track_counts = album_tracks.groupby("AlbumId")["TrackId"].count().to_dict()

# Count customer purchases per album
customer_purchases = pd.read_sql("""
    SELECT Invoice.CustomerId, Invoice.InvoiceId, Track.AlbumId, COUNT(DISTINCT InvoiceLine.TrackId) AS TracksBought
    FROM InvoiceLine
    JOIN Invoice USING(InvoiceId)
    JOIN Track USING(TrackId)
    GROUP BY Invoice.CustomerId, Track.AlbumId;
""", conn)

# Determine album purchases
customer_purchases["FullAlbum"] = customer_purchases.apply(
    lambda row: row["TracksBought"] == album_track_counts.get(row["AlbumId"], 0),
    axis=1
)

# Get percentage of customers preferring individual tracks vs. full albums
album_purchases = customer_purchases.groupby("CustomerId")["FullAlbum"].any().value_counts(normalize=True) * 100
print("\nCustomer Purchase Preferences:")
print(f"Full Albums: {album_purchases.get(True, 0):.2f}%")
print(f"Individual Tracks: {album_purchases.get(False, 0):.2f}%")

# Close connection
conn.close()
