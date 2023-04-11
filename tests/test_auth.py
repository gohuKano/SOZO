'''
Python file where all the tests related to the client 
authentification. 
Either for the Register of the Login
'''

def email_match(email, email_to_confirm):
    if email == email_to_confirm:
        return 1
    else: return 0

def password_match(password, password_to_confirm):
    if password == password_to_confirm:
        return 1
    else: return 0

def user_already_register(get_db_connection, email):
    '''
    check if the email already exists in the database
    if the mail exist the function returns 1 and so the
    user is supposed to already has an account
    '''
    # search into the database if the email is already register
    conn = get_db_connection
    cur = conn.cursor()
    cur.execute(
        'SELECT email FROM accounts WHERE email = %s',
        (email,)
    )
    existing_email = cur.fetchone()
    
    if existing_email:
        # return 1 if user already register
        # 1 is yes, the user is already register
        return 1
    else:
        # return 0 if user is not already register
        # 0 is no, the user is not already register
        return 0
    
def write_user_registration_in_db(get_db_connection, prenom, nom, email, password):
    '''
    function that writes into the database
    the data is supposed to have been checked
    before writing to the database
    '''
    conn = get_db_connection
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO accounts (prenom, nom, email, password)'
        'VALUES (%s, %s, %s, %s)',
        (
            prenom,
            nom,
            email,
            password
        )
    )
    conn.commit()

    print("data write into database")

