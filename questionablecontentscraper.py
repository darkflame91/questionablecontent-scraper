import requests
givendir = raw_input("Enter the path where the images should be stored!\n")
for i in range(1,3180):
    r = requests.get("http://www.questionablecontent.net/comics/"+str(i)+".png")
    if r.status_code == 200:
        with open(givendir+"/"+str(i).zfill(4)+".png", 'wb') as fd:
            for chunk in r.iter_content():
                fd.write(chunk)
        if i%20 == 0:
            print str(i)+" Vairry naice! Great success!"
    else:
        r = requests.get("http://www.questionablecontent.net/comics/"+str(i)+".jpg")
        if r.status_code == 200:
            with open(givendir+"/"+str(i).zfill(4)+".jpg", 'wb') as fd:
                for chunk in r.iter_content():
                    fd.write(chunk)
            if i%20 == 0:
                print str(i)+" Vairry naice! Great success!"
        else:
            r = requests.get("http://www.questionablecontent.net/comics/"+str(i)+".gif")
            if r.status_code == 200:
                with open(givendir+"/"+str(i).zfill(4)+".gif", 'wb') as fd:
                    for chunk in r.iter_content():
                        fd.write(chunk)
                if i%20 == 0:
                    print str(i)+" Vairry naice! Great success!"
            else:
                print str(i)+" Failure! Borat sad! :("
