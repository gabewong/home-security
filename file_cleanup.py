import os
import os.path
from datetime import datetime
import zipfile
import ntpath

import shutil


image_dir = os.getenv("HOME") + '/Dropbox/Apps/gabewong-home-security/Home.Security'
print "Scanning Directory: " + image_dir


dirs = os.listdir( image_dir )
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            filename = os.path.join(root, file)
            ziph.write(filename , ntpath.basename(filename) )

# Loop through the directory
for file in dirs:
    path = image_dir + '/' + file

    if os.path.isdir( path ) == True and len(file) == 10:

        now_object = datetime.now()
        datetime_object = datetime.strptime( file , '%Y-%m-%d')



        # Check if the date
        if datetime_object.strftime( '%Y-%m-%d' ) < now_object.strftime( '%Y-%m-%d' ):
            # print datetime_object.strftime('%Y-%m-%d')
            # print now_object.strftime('%Y-%m-%d')

            # Zip up the directory
            print "Zipping up " + path
            zippath = image_dir + '/' + datetime_object.strftime('%Y-%m-%d') + '.zip'
            zipf = zipfile.ZipFile( zippath , 'w', zipfile.ZIP_DEFLATED)
            zipdir( path , zipf)
            zipf.close()

            # remove directory if the zip file exists
            if os.path.isfile(zippath) is True:
                zipped_dir = image_dir + '/' + datetime_object.strftime('%Y-%m-%d')
                shutil.rmtree( zipped_dir )
                print "Removed Directory: " + zipped_dir

                # Connect to NAS via smb

                # Check if the file exists on the NAS


