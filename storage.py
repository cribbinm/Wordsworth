import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create primary all_words table which contains each unique word.
c.execute('''
    CREATE TABLE all_words
        (word_id, word, date_submitted, submitted_by, status)
    word_id INT NOT NULL,
    word VARCHAR(35),
    date_submitted DATE NOT NULL,
    submitted_by VARCHAR(35) NOT NULL,
    status VARCHAR(35),
    PRIMARY KEY (word_id)
    '''
          )


# Create votes table which contains each vote and links to each unique word.
c.execute('''CREATE TABLE votes
        (vote_id, word_id, voter, vote_value, date_voted)
    vote_id INT NOT NULL,
    word_id INT NOT NULL,
    voter VARCHAR(35),
    vote_value INT NOT NULL,
    date_voted DATE NOT NULL,
    PRIMARY KEY (vote_id),
    FOREIGN KEY (word_id) REFERENCES (all_word(word_id))
    ''')

score_count_query = '''
    SELECT
        word_id,
        SUM(vote_value)
    FROM
        all_words AS aw
    LEFT JOIN
        votes AS v ON aw.word_id = v.word_id
    GROUP BY
        word_id;
    '''

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()