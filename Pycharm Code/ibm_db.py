import ibm_db

# Replace placeholders with your actual values from the JSON provided
dsn_hostname = "2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud"
dsn_uid = "lng74408"
dsn_pwd = "EOhU147W29sA4x6n"
dsn_port = 30756
dsn_security = "SSL"  # If SSL is enabled

# Construct the connection string
dsn = (
    "DATABASE=bludb;"
    "HOSTNAME={0};"
    "PORT={1};"
    "PROTOCOL=TCPIP;"
    "UID={2};"
    "PWD={3};"
    "SECURITY={4};"
).format(dsn_hostname, dsn_port, dsn_uid, dsn_pwd, dsn_security)

# Establish the connection
try:
    conn = ibm_db.connect(dsn, "", "")
    print("Connected to the database!")

    # Prepare and execute a sample SQL query
    sql_query = "SELECT * FROM census_data"  # Replace 'your_table_name' with an actual table name
    stmt = ibm_db.exec_immediate(conn, sql_query)

    # Fetch and display the results
    while ibm_db.fetch_row(stmt) != False:
        print(ibm_db.result(stmt, 0), ibm_db.result(stmt, 1))  # Adjust column indices as needed

    # Close the connection
    ibm_db.close(conn)
    print("Connection closed.")

except Exception as e:
    print("Unable to connect:", e)