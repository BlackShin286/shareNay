import os, sys, requests, threading, time

def Clear():
    os.system("cls" if os.name=="nt" else "clear")

def Logo():
    Clear()
    Banner()

def Banner():
    logo = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                  ██╗██╗██████╗  █████╗ ██╗   ██╗             ║
║                  ██║██║██╔══██╗██╔══██╗╚██╗ ██╔╝             ║
║                  ██║██║██████╔╝███████║ ╚████╔╝              ║
║             ██╗  ██║██║██╔══██╗██╔══██║  ╚██╔╝               ║
║             ╚█████╔╝██║██║  ██║██║  ██║   ██║                ║
║              ╚════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝                ║
║══════════════════════════════════════════════════════════════║
║           YOUTUBE  : Jiray Software                          ║
║           Telegram : @DucThinhEXE                            ║
║           Zalo     : 0978200223                              ║
║           Facebook : www.facebook.com/100082234812595        ║
╚══════════════════════════════════════════════════════════════╝
"""
    for X in logo:
        sys.stdout.write(X)
        sys.stdout.flush() 
        time.sleep(0.000125)

def line():
    line="════════════════════════════════════════════════════════════════\n"
    
    for X in line:
        sys.stdout.write(X)
        sys.stdout.flush() 
        time.sleep(0.0125)

def GetAccessToken(cookie):
    urlGetAct = requests.get("https://adsmanager.facebook.com/adsmanager/manage/campaigns",cookies= {"cookie":cookie},allow_redirects=False).text
    try:
        act = urlGetAct.split("act=")[1].split('&')[0]
        urlGetToken = requests.get(f"https://adsmanager.facebook.com/adsmanager/manage/campaigns?act={act}&nav_source=no_referrer",cookies = {"cookie":cookie}).text
        accessToken = urlGetToken.split('window.__accessToken="')[1].split('"')[0]
        return accessToken
    except:
        return False

def CheckLoginFacebook(cookie):
    loginUrl = requests.get("https://mbasic.facebook.com/profile.php",cookies={"cookie":cookie}).text
    try:
        fb_dtsg = loginUrl.split('input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
        jazoest = loginUrl.split('input type="hidden" name="jazoest" value="')[1].split('"')[0]
        idacc   = loginUrl.split('input type="hidden" name="target" value="')[1].split('"')[0]
        name    = loginUrl.split('<title>')[1].split('</title>')[0]
        return idacc,name
    except:
        return False

def GetListUidPage(cookie,accessToken):
    dictIdPage = []
    getListPageId = requests.get(f'https://graph.facebook.com/me?fields=id,name,facebook_pages.limit(10000){{additional_profile_id}}&access_token={accessToken}',cookies={"cookie":cookie}).json()
    try:
        for i in getListPageId["facebook_pages"]["data"]:
            idpage = i["additional_profile_id"]
            dictIdPage.append(idpage)
        return dictIdPage
    except:
        return dictIdPage

def ApiShareByPage(cookie, idPost, idPage, soLuong=None):
    getData = requests.get("https://mbasic.facebook.com/profile.php",cookies={"cookie":cookie}).text
    fb_dtsg = getData.split('input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = getData.split('input type="hidden" name="jazoest" value="')[1].split('"')[0]
    idacc   = getData.split('input type="hidden" name="target" value="')[1].split('"')[0]
    for _ in range(soLuong):
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': cookie,
            'dpr': '1',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-full-version-list': '"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.171", "Chromium";v="115.0.5790.171"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'viewport-width': '301',
            'x-asbd-id': '129477',
            'x-fb-friendly-name': 'useCometFeedToFeedReshare_FeedToFeedMutation',
        }

        data = {
            'av': idPage,
            'dpr': '1',
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'useCometFeedToFeedReshare_FeedToFeedMutation',
            'variables': '{"input":{"attachments":{"link":{"share_scrape_data":"{\\"share_type\\":22,\\"share_params\\":['+idPost+']}"}},"audiences":{"undirected":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}}},"idempotence_token":"63ef5cef-0484-4c63-9860-66e824d364c6","is_tracking_encrypted":true,"navigation_data":{"attribution_id_v2":"CometSinglePostRoot.react,comet.post.single,via_cold_start,1692110427921,106137,,"},"source":"www","tracking":["AZX-uqQ5XzDix4-WiXUVKdS4AAwqaa7i2SUEBLR7q6COj6UWuNwrTsfGtKemB1aooBk_9Xg_Wk7kmLnsiOoNVH8vLXvJ2OJTl-NNqVFqTNY4SJGoK1lRCLJ8wX0Cui6Bdkm-mNgC7OJzms2LqAj49ivsMWDB3QkSDxbodRG2yjU6x_IzdJnpM2Aa4s7W_H6A-2Wd5zHeKK8vrtRD14k2qKMYfMXf5yKavrKSys1cVmI0RszkrT6XTnw7q_UdzX02N1kiqIMXCmlb2nJglWjWp6zyOLv06LEbvLlbQZNYrRYHqcT7Uy2jfgW9j-GQPhunG1AYUQLtXnCBirAf0k-Y3N9w0YrDGoHiNIa2n-NK7zCi3Q"],"actor_id":"'+idPage+'","client_mutation_id":"1"},"renderLocation":"homepage_stream","scale":1,"privacySelectorRenderLocation":"COMET_STREAM","useDefaultActor":false,"displayCommentsContextEnableComment":null,"feedLocation":"NEWSFEED","displayCommentsContextIsAdPreview":null,"displayCommentsContextIsAggregatedShare":null,"displayCommentsContextIsStorySet":null,"displayCommentsFeedbackContext":null,"feedbackSource":1,"focusCommentID":null,"UFI2CommentsProvider_commentsKey":"CometModernHomeFeedQuery","__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__StoriesRingrelayprovider":false}',
            'server_timestamps': 'true',
            'doc_id': '6392497637508564',
        }

        response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).text
        if "post_id" in response:
            return {"status":1,"message":f"[ JIRAY ] IDPOST : {idPost} => SUCCESS [ {idPage}_{idPost} ]"}
        else:
            return {"status":0,"message":f"[ JIRAY ] IDPOST : {idPost} => ERROR"}
        time.sleep(1.5)
Logo()
cookie = input("Cookie Facebook : ")
if CheckLoginFacebook(cookie=cookie)==False:
    print("Cookie Die Hoặc Không Tồn Tại, Vui Lòng Xem Lại!")
    exit()
else:
    name = CheckLoginFacebook(cookie)[1]
    idacc = CheckLoginFacebook(cookie)[0]
    line()
    print(f"LOGIN SUCCESS : {name} <> UID : {idacc}")
    time.sleep(2)
Logo()
idPost = input("ID POST BUFF SHARE : ")
soLuong = int(input("SÔ LƯỢNG SHARE / 1 PAGE : "))
time.sleep(1.5)

Logo()
print(f"ACCOUNT NAME : {name} | UID : {idacc}")
line()
def main(cookie,idPost,idPage,soLuong):
    if ApiShareByPage(cookie,idPost,idPage,soLuong)["status"]==1:
        msg = ApiShareByPage(cookie,idPost,idPage,soLuong)["message"]
        print(msg)
        time.sleep(1)
    else:
        msg = ApiShareByPage(cookie,idPost,idPage,soLuong)["message"]
        print(msg,end='\r')
        time.sleep(1)
while True:
    # try:
    accessToken = GetAccessToken(cookie)
    dictIdpage = GetListUidPage(cookie,accessToken)
    while True:
        for idPage in dictIdpage:
            threading.Thread(target=main,args=(cookie,idPost,idPage,soLuong)).start()
    # except:
    #     exit()

# print(ApiShareByPage("sb=F_XBZOJpb907pbzc-Twa_gXF;datr=F_XBZF20nrRaL6JJa2bJjiMc;c_user=100082234812595;m_page_voice=100082234812595;usida=eyJ2ZXIiOjEsImlkIjoiQXJ6ZnJldjdnYWdqMCIsInRpbWUiOjE2OTIxMDg2Nzl9;xs=12%3Ad3H8OmgWmPFeQg%3A2%3A1691623322%3A-1%3A6298%3A%3AAcXwjjA10iBVx8lk6eHvTXDrr5-kuWc0-IVTNbN46HA;fr=0gz4Cc4a6Mw79oesN.AWVQ1BJPdExxNbrWgpHGGtYAMaY.Bk24eI.O_.AAA.0.0.Bk24eI.AWVELYhP9O8;cppo=1;wd=681x649;presence=EDvF3EtimeF1692108734EuserFA21B82234812595A2EstateFDutF0CEchF_7bCC;","158380500246443","100093441309069"))