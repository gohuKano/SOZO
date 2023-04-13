'''
Python file of all functions related to the newslatter
'''

def verify_subscription_newslatter(get_db_connection, email, prenom, nom):
    '''
    function that verifies if the user is already registered in the newsletter
    '''
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT email FROM newsletter_subscribers
        WHERE email = %s AND prenom = %s AND nom = %s
        """,
        (email, prenom, nom)
    )
    result = cur.fetchone()
    if result:
        # return 1 : the user is already registered
        return 1
    else:
        # return 0 : the user is not registered
        return 0


def subscription_to_newslatters(get_db_connection, prenom, nom, email):
    '''
    function that will write the data into the newsletter table
    '''
    conn = get_db_connection
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO newsletter_subscribers (prenom, nom, email)
        VALUES (%s, %s, %s)
        """,
        (prenom, nom, email)
    )
    conn.commit()

def remove_from_newsletter(get_db_connection, email, prenom, nom):
    '''
    function that removes the email address, prenom et nom, from the db
    '''
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute(
        """
        DELETE FROM newsletter_subscribers
        WHERE email = %s AND prenom = %s AND nom = %s
        """,
        (email, prenom, nom)
    )