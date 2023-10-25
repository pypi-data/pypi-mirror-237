import validators

from .c2intelfeeds import c2intelFeedsApi
from .feodotracker import feodoTrackerApi
from .openphish import openPhishApi
from .phishingdatabase import phishingDatabaseApi
from .phishstats import phishstatsApi
from .phishunt import phishuntApi
from .sslblacklist import sslBlackListApi
from .threatview import threatViewApi
from .tweetfeed import tweetFeedApi
from .urlhaus import urlHausApi
from .usom import usomApi
from .vxvault import vxVaultApi


class OsintApi:

    def __init__(self):
        self.message="Scan Status: {}, Keyword:{}, Type:{}"

    def runall(self,keyword):

        scan_result = list()

        if validators.url(keyword):
            print(self.message.format('started',keyword,'url'))

            status_vxvault, error_vxvault, response_vxvault = vxVaultApi().get_result(keyword)
            if status_vxvault:scan_result.append({"source": "vxvault", "result": response_vxvault})

            status_phishunt, error_phishunt, response_phishunt = phishuntApi().get_result(keyword)
            if status_phishunt:scan_result.append({"source": "phishunt", "result": response_phishunt})

            status_openphish, error_phishunt, response_openphish = openPhishApi().get_result(keyword)
            if status_openphish:scan_result.append({"source": "openphish", "result": response_openphish})

            status_usom, error_usom, response_usom = usomApi().get_result(keyword)
            if status_usom:scan_result.append({"source": "usom", "result": response_usom})

            status_phishingdatabase, error_phishingdatabase, response_phishingdatabase = phishingDatabaseApi('url').get_result(keyword)
            if status_phishingdatabase:scan_result.append({"source": "phishing.database", "result": response_phishingdatabase})

            status_threatview, error_threatview, response_threatview = threatViewApi('url').get_result(keyword)
            if status_threatview:scan_result.append({"source": "threatview", "result": response_threatview})

            status_urlhaus, error_urlhaus, response_urlhaus = urlHausApi().get_result(keyword)
            if status_urlhaus:scan_result.append({"source": "urlhaus", "result": response_urlhaus})

            status_phishstats, error_phishstats, response_phishstats = phishstatsApi('url').get_result(keyword)
            if status_phishstats:scan_result.append({"source": "phishstats", "result": response_phishstats})

            status_tweetfeed, error_tweetfeed, response_tweetfeed = tweetFeedApi().get_result(keyword)
            if status_tweetfeed:scan_result.append({"source": "tweetfeed", "result": response_tweetfeed})

            print(self.message.format('finished',keyword,'url'))

        elif validators.ipv4(keyword):
            print(self.message.format('started', keyword, 'ipv4'))

            status_phishstats, error_phishstats, response_phishstats = phishstatsApi('ip').get_result(keyword)
            if status_phishstats:scan_result.append({"source": "phishstats", "result": response_phishstats})

            status_phishingdatabase, error_phishingdatabase, response_phishingdatabase = phishingDatabaseApi('ip').get_result(keyword)
            if status_phishingdatabase:scan_result.append({"source": "phishing.database", "result": response_phishingdatabase})

            status_tweetfeed, error_tweetfeed, response_tweetfeed = tweetFeedApi().get_result(keyword)
            if status_tweetfeed:scan_result.append({"source": "tweetfeed", "result": response_tweetfeed})

            status_feodotracker, error_feodotracker, response_feodotracker = feodoTrackerApi().get_result(keyword)
            if status_feodotracker:scan_result.append({"source": "feodotracker", "result": response_feodotracker})

            status_sslblacklist, error_sslblacklist, response_sslblacklist = sslBlackListApi().get_result(keyword)
            if status_sslblacklist:scan_result.append({"source": "sslblacklist", "result": response_sslblacklist})

            status_c2intelfeeds, error_c2intelfeeds, response_c2intelfeeds = c2intelFeedsApi('ip').get_result(keyword)
            if status_c2intelfeeds:scan_result.append({"source": "c2intelfeeds", "result": response_c2intelfeeds})

            print(self.message.format('finished', keyword, 'ipv4'))

        elif validators.domain(keyword):
            print(self.message.format('started', keyword, 'domain'))

            status_phishingdatabase, error_phishingdatabase, response_phishingdatabase = phishingDatabaseApi('domain').get_result(keyword)
            if status_phishingdatabase:scan_result.append({"source": "phishing.database", "result": response_phishingdatabase})

            status_tweetfeed, error_tweetfeed, response_tweetfeed = tweetFeedApi().get_result(keyword)
            if status_tweetfeed:scan_result.append({"source": "tweetfeed", "result": response_tweetfeed})

            status_c2intelfeeds, error_c2intelfeeds, response_c2intelfeeds = c2intelFeedsApi('domain').get_result(keyword)
            if status_c2intelfeeds:scan_result.append({"source": "c2intelfeeds", "result": response_c2intelfeeds})

            print(self.message.format('finished', keyword, 'domain'))
        else:
            scan_result.append({'status':"not allowed asset type"})


        return scan_result
        
def osintradar(asset: str):
    response = OsintApi().runall(asset)
    return response
