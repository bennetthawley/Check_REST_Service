import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

testURL = 'https://www.fws.gov/wetlands/arcgis/services/Wetlands/MapServer/WMSServer?request=GetCapabilities&service=WMS'
#testURL = 'http://www.groupkt.com/post/f2129b88/free-restful-web-services-to-consume-and-test.htm'

def check_connection(REST):

    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    for count in range(1,4):
        print '\nTesting connection to web service'
        print 'Test: {}/3...\n'.format(count)

        try:
            response = requests.get(REST, verify=False)
            response.raise_for_status()
            status = response.status_code
            if status == 200:
                print 'Status: {}'.format(status)
                print 'Connection Successful!'
                break
            else:
                print 'Status: {}'.format(status)
        except requests.exceptions.ConnectionError as e:
            print "Connection Error to Service"
            print e
            print 'Retrying Connection...'
        except requests.exceptions.ConnectTimeout as e:
            print 'Connection Timeout Error to Service'
            print e
            print 'Retrying Connection...'
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)

check_connection(testURL)

