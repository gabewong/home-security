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
# This would print all the files and directories
for file in dirs:
    path = image_dir + '/' + file
    if os.path.isdir( path ) == True:

        print path

        now_object = datetime.now()
        datetime_object = datetime.strptime( file , '%Y-%m-%d')



        if datetime_object.strftime( '%Y-%m-%d' ) < now_object.strftime( '%Y-%m-%d' ):
            print datetime_object.strftime('%Y-%m-%d')
            print now_object.strftime('%Y-%m-%d')


            # newZip = zipfile.ZipFile('new.zip', 'w')
            zippath = image_dir + '/' + datetime_object.strftime('%Y-%m-%d') + '.zip'
            zipf = zipfile.ZipFile( zippath , 'w', zipfile.ZIP_DEFLATED)
            zipdir( path , zipf)
            zipf.close()

            if os.path.isfile(zippath) is True:
                shutil.rmtree(image_dir + '/' + datetime_object.strftime('%Y-%m-%d'))


                # print "\n"