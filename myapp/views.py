import subprocess
import pwd
import datetime
import pytz
from django.http import HttpResponse

def htop_view(request):
    full_name = "Ayush Kumar"  # Replace with your actual name
    username = pwd.getpwuid(1000).pw_name  # Fetch system username
    ist_time = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
    top_output = subprocess.getoutput("top -b -n 1")

    response_content = f"""
    <pre>
    Name: {full_name}
    Username: {username}
    Server Time (IST): {ist_time.strftime("%Y-%m-%d %H:%M:%S.%f")}
    
    TOP output:
    {top_output}
    </pre>
    """
    return HttpResponse(response_content, content_type="text/html")
