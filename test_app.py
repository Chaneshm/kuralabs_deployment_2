from application import app

# def test_quick():
#   a = "jeff"
#   greeting = greet(a)
#   assert greeting == "Hi jeff"

def test_home_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    
def testGo():
    response = app.test_client().get('/go')
    assert response.status_code == 302
    assert response.location == 'http://google.com'    
