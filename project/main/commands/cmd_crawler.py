def crawler_command():
    
    #Crawl static web pages section
    from lxml import etree
    import requests
    from curl_cffi import requests as curl_requests
    
    def count_down(a):
        import time
        a = 0
        for i in range(300):
            print(f"\r{a:.2f}",end="",flush=True)
            a -= 0.01
            time.sleep(0.01)
        print(f"\r{a:.2f}",end="",flush=True)

    requests_headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "accept-language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "accept-encoding":"gzip, deflate, br, zstd",
                "referer":"https://www.google.com/",
                "sec-ch-ua":"'Google Chrome';v='91', ' Not;A Brand';v='99', 'Chromium';v='91'",
                "sec-ch-ua-mobile":"?0",
                "sec-ch-ua-platform":"\"Windows\""
                }    

    url = input("Please enter your url:")   
    
    try:
        count_down(3.00)
        response = curl_requests.get(url, headers=requests_headers, timeout=10)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            print(response.text)
        else:
            print("error",response.status_code)
    except Exception as e:
        print("error", e)
        count_down(3.00)
        response = curl_requests.post(url, headers=requests_headers, timeout=10)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            print(response.text)
        else:
            print("error",response.status_code) 
    #Parse the HTML content
    try:
        tree = etree.HTML(response.text)
        items = tree.xpath('//a/@href')
        print(items)
    except Exception as e:
        print("error",e)





    #Crawl dynamic web pages section

    import re
    from playwright.sync_api import Playwright, sync_playwright, expect


    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page() 
        page.goto("https://www.baidu.com/")

    # ---------------------
        context.close()
        browser.close()


    with sync_playwright() as playwright:
        run(playwright)



    return 0
