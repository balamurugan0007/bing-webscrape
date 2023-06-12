from bs4 import BeautifulSoup
import requests
import json


quary=input('enter :')
#if ' ' in quary:
    #x=quary.replace(' ',"+") 
    #print(x)

#================================search====================================

search_json_result=[]
def search():
    
    
    url = f"https://www.bing.com/search?q={quary}"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    result=soup.find_all('li', class_='b_algo')
    for results in result:
        title = results.find('h2').text
        link = results.find('a')['href']
    
    
    #des=results.find('div',class_='Z26q7c UK95Uc')
        description = results.find("p").text
    
        search_result={
            "title":title,
            "link":link,
            "description":description
        }
        
        search_json_result.append(search_result)
    
        
        
search()

#==================================images results====================================

image_json_result=[]
def images():
    
    url = f"https://www.bing.com/images/search?q={quary}"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    imges_result=soup.find_all('div',class_='img_cont')
    ref_image=soup.find_all('li',class_='item col')
    for image in imges_result:
        link=image.find('img')
        
        
        
        if link:
    # Access the 'src' attribute if it exists
            src = link.get('src')
            if src:
                img_link=src
            else:
                #img_link='none'
                continue
        else:
            #img_link='none'
            continue
        
        image_result={
            "image":img_link
        }
        image_json_result.append(image_result)
            
        
        
        
    for i in ref_image:
        head=i.find('span').text
        if head=='':
            continue
        
        ref_img_search={
            'title':head
        }
        image_json_result.append(ref_img_search)
        
images()

#===============================videos search==================

video_json_result=[]

def videos():
    url=f"https://www.bing.com/videos/search?q={quary}"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    vid=soup.find_all("div",class_="dg_u")
    vid_ref=soup.find_all("li",class_='item col')
    
    for video in vid :
        vid_link=video.find('div',class_='mc_vtvc_con_rc')['ourl']
        title=video.find('strong').text
        views=video.find('div',class_='mc_vtvc_meta_row').span.text
        img=video.find('div',class_='rms_iac')
        if img:
            img_link=img.get('data-src')
            if img_link:
                image=img_link
            else:
                image="none"
        else:
            image="none"
        
       
        
        """
        if img:
            image=img.get('src')
            if image:
                print("yes")
            else:
                print('no')
        else:
            print("no")"""
            
        video_result={
            "title":title,
            "img":image,
            "views":views,
            "video":vid_link
        }     
        video_json_result.append(video_result)   
    for j in vid_ref:
        link=j.find('a')['href']
        title=j.find('strong').text
        #print(title)
        
        video_ref={
            "title":title,
            "link":link
        }
        video_json_result.append(video_ref)
        
        
        
    
videos()


#reustss
search_response=json.dumps(search_json_result,indent=4)
img_response=json.dumps(image_json_result,indent=5)
video_response=json.dumps(video_json_result,indent=5)
print(search_response)
#print(img_response)
#print(video_response)