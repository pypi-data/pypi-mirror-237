def news():
    import requests
    from bs4 import BeautifulSoup
    
    url = 'https://finance.naver.com/'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # 헤드라인 정보가 담긴 태그를 찾습니다.
            headlines = soup.find_all('div', class_='section_strategy')
            
            # 헤드라인을 출력합니다.
            print("주요 뉴스 헤드라인:")
            for headline in headlines:
                print(headline.text)
        else:
            print('뉴스 정보를 가져올 수 없습니다.')
    except Exception as e:
        print(f'오류 발생: {str(e)}')
