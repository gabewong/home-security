import os
import os.path
from datetime import datetime
import zipfile
import shutil


image_dir = os.getenv("HOME") + '/Dropbox/Apps/gabewong-home-security/Home.Security'
print "Scanning Directory: " + image_dir


dirs = os.listdir( image_dir )
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

# Loop through the directory
for file in dirs:
    path = image_dir + '/' + file
    if os.path.isdir( path ) == True:

        print path

        now_object = datetime.now()
        datetime_object = datetime.strptime( file , '%Y-%m-%d')



        # Check if the date
        if datetime_object.strftime( '%Y-%m-%d' ) < now_object.strftime( '%Y-%m-%d' ):
            # print datetime_object.strftime('%Y-%m-%d')
            # print now_object.strftime('%Y-%m-%d')

            # Zip up the directory
            zippath = image_dir + '/' + datetime_object.strftime('%Y-%m-%d') + '.zip'
            zipf = zipfile.ZipFile( zippath , 'w', zipfile.ZIP_DEFLATED)
            zipdir( path , zipf)
            zipf.close()

            # remove directory if the zip file exists
            if os.path.isfile(zippath) is True:
                shutil.rmtree(image_dir + '/' + datetime_object.strftime('%Y-%m-%d'))

                # Connect to NAS via smb

                # Check if the file exists on the NAS

