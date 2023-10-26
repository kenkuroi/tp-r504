from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)
 
# MySQL configuration
db_config = {
    'host': '172.19.0.2',
    'user': 'root',
    'password': 'foo',
    'database': 'tp4-sql'
}

# Initialize MySQL connection
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor() 


@app.route('/')
def index():
    # Sample query
    query = "SELECT * FROM myTable"
    cursor.execute(query)
    data = cursor.fetchall()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
    

