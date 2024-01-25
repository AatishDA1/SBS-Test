from django.shortcuts import render

# Database Connection
import mysql.connector    
cnx = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='licensedatav2')

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def member_zone(request):
    # Fetching data
    result = []
    try:
        cursor = cnx.cursor()
        cursor.execute("""
            SELECT id, `First Name`, `Last Name`, `Date of Birth`, `Place of Birth`, `Gender`, `Date of Issue`, `Date of Expiry`, `Issuing Authority`, `License Number`, `Address`, `Dataset` FROM licensedatav2.license_data;
        """)
        result = cursor.fetchall()
    except:
        pass
    return render(request, 'member_zone.html', {"data":result})