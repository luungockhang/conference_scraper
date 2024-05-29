from django.shortcuts import render # type: ignore
from sqlserverconnect.models import sqlserverconn
from django.db.models import Q # type: ignore
import pyodbc # type: ignore

def search(request):
    if request.method == "POST":
        searched = request.POST.get("searched")
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-TVR6JU9\MSSQLSERVER6;'
                              'Database=JJ;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        # Sử dụng parameterized query để tránh SQL injection
        cursor.execute("SELECT * FROM Conferences WHERE UPPER(Conference) LIKE ? ORDER BY Conference ASC, CityCountry ASC, Date ASC", '%' + searched.upper() + '%')
        result = cursor.fetchall()
        conn.close()  # Đóng kết nối sau khi sử dụng
        return render(request, 'search.html', {'sqlserverconn': result})
    
def connsql(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-TVR6JU9\MSSQLSERVER6;'
                        'Database=JJ;'
                        'Trusted_Connection=yes;')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Conferences ORDER BY Conference ASC, CityCountry ASC, Date ASC")
    result=cursor.fetchall()
    conn.close()
    return render(request,'Index.html',{'sqlserverconn':result})


