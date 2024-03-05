import keyring as kring

kring.set_password('OTT_Details_API','api_key','c29ca49425msheaa52ccaa3c97d1p1b0376jsn2fe766fafc0e')
kring.set_password('OTT_Details_API','host_name','moviesminidatabase.p.rapidapi.com')

print(kring.get_password('OTT_Details_API','host_name'))
