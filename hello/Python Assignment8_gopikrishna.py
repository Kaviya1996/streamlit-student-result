import streamlit as st
import re

#log = """
#2026-03-30 10:15:32 192.168.1.10 GET /home 200
#2026-03-30 10:16:45 10.0.0.5 POST /login 401
#2026-03-30 10:17:01 172.16.0.3 GET /dashboard 200
#2026-03-30 10:18:22 192.168.1.10 GET /profile 404
#"""

log = st.text_area(f'Enter the logs:')

if st.button("Scearch 🔎"):
    # Finding IP Address
    # By using below regex
    ipaddress = r'\d{3}\.\d{3}\.\d{3}\.\d{3}'
    # \d - finding the one or more digits
    # {3} - repeating three times
    # \. - dot character
    ipaddmatches = re.findall(ipaddress,log)

    # Finding URL's
    # By using below regex
    urls = r'/[a-zA-Z0-9]+'
    # / - for searching the URL starts with
    # [a-zA-Z0-9]+ - for searching the characters(upper and lower) and number 
    urlmatches = re.findall(urls,log)

    # Finding Status Codes
    # By using below regex
    statuscodes = r'\s(\d{3})$'
    # \d - finding the one or more digits
    # {3} - repeating three times
    # \d{3} - exactly 3 digits of number
    # re.MULTLINE - its for multiple line for checking each lines seperately
    sc_matches = re.findall(statuscodes, log,re.MULTILINE)
    listcode={}
    for item in sc_matches:
        listcode[item] = listcode.get(item, 0) + 1

    # Finding Successfull request
    # By using below regex
    successcode = r'\s(/[\w]+)\s200'
    # \s - matches any whitespace
    # (/[\w]+) - serching url
    # \s200 - serching 200
    successcodematches = re.findall(successcode,log)

    st.write(f'DISPLAYING THE LOG DATA USING REGULUR EXPRESSION')
    st.write(f'\n IP ADDRESSES : {ipaddmatches}')
    st.write(f'\n URLs : {urlmatches}')
    st.write(f'\n STATUS COUNTS : {listcode}')
    st.write(f'\n SUCCESSFULL GET REQUEST : {successcodematches}')