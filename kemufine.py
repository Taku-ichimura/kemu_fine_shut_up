import os
import sys
import glob
import tweepy
import datetime
import schedule
import time
import numpy as np

consumer_key="YOUR CONSUMER_KEY"
consumer_secret="YOUR CONSUMER_SECRET_KEY"
access_token="YOUR ACCESS_TOKEN"
access_token_secret="YOUR ACCESS_SECRET_TOKEN"

check_path = './check_point.txt'

target = ["Chem_ddr","fines_CNT"]

def reply_team_fines():
    print("start")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    with open(check_path) as f:
        check_point = datetime.datetime.strptime(f.readline(), '%Y-%m-%d %H:%M:%S.%f')
    
    tl=api.mentions_timeline()
    rep_target=[]
    
    d=tl[0].created_at
    final_d=d.strftime('%Y-%m-%d %H:%M:%S.%f')
    for t in tl:
        d=t.created_at
        if((d-check_point).total_seconds()>0):
            rep_target.append(t)
            print("date update")
               
    if(len(rep_target)!=0):
        with open(check_path, mode='w') as f:
            f.write(final_d)
            
    for t in rep_target:
        rep_name=t.author.screen_name
        rep_id=t.id
        if(rep_name in target):
            message="@"+rep_name+" "+"だまれ"
            api.update_status(message,rep_id)
            print("reply  kemu or fines")
        else:
            continue    
    print("end")

if __name__ == '__main__':
    schedule.every(30).seconds.do(reply_team_fines)
    while True:
        schedule.run_pending()
        time.sleep(1)
