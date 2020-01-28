from website.models import User

def validate_login(username, password):
    user = User.objects.filter(username=username)
    if not user:
        return False
    passw = User.objects.filter(username=user[0].username, password=password)
    if passw:
        if passw[0].password == password :
            print("Hello")
            return True
    return False

def validate_registration(username, password1, password2, email):
    user = User.objects.filter(username=username)
    
    if user:
        print("user already exists")
        return False
    if password1 != password2 :
        print("Retyped password didn't match")
        return False
    
    email = User.objects.filter(email=email)
    if email:
        print("email already exists")
        return False
    
    return True