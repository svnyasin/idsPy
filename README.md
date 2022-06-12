# idsPy

note: the listening port must be configured as a different interface than the one used for communication in the internal network, because when the communication and listening job are used from the same interface, the delete function is also listened, so the file information to be deleted will be detected in the packet content and captured again.

Installation / step-by-step (ubuntu_server_22.04)

- sudo apt install python3-pip (u need pip3 for install other dependencies)
- sudo apt install tshark
    - select “yes”
- sudo pip3 install django django-filter pyshark pycountry
- rm db.sqlite3
- rm alert/migrations/0001_initial.py
- sudo python3 [manage.py](http://manage.py) makemigrations
    - stop command with ctrl+z when you see “- Create model CapturedPacket”
- sudo python3 [manage.py](http://manage.py) migrate
    - stop command with ctrl+z when you see “Applying sessions.0001.initial... OK”
- sudo python3 [manage.py](http://manage.py) createsuperuser
    - select eth or wlan temporarily listen for this step
    - type username
    - type email (optional)
    - when superuser created successfully, you can exit with ctrl+c
- That was it, you can start your server now!

Start Server

- sudo python3 [manage.py](http://manage.py) runserver 0:80


-------------------------------------------------------------------------------------------------------------------------------------

proje raporu

 https://github.com/svnyasin/idsPy/blob/main/yasin_seven_2017469044_bitirme_rapor.docx
