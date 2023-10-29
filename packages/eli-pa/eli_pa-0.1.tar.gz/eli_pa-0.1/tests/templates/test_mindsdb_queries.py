from string import Template


def test_template_values():
    user = "Soumyadip Moni"
    ask = "Where is london?"

    sql_ask_query = Template('''
    SELECT response
    FROM mindsdb.gpt_model
    WHERE author_username = "$user"
    AND text = "$ask";
    ''')

    expected_output = '''
    SELECT response
    FROM mindsdb.gpt_model
    WHERE author_username = "Soumyadip Moni"
    AND text = "Where is london?";
    '''

    assert sql_ask_query.substitute(user=user, ask=ask) == expected_output
