def test_signup_new_account(app):
    username = 'test2'
    password = 'test2'
    app.james.ensure_user_exists(username, password)
