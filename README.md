# kemu_fine_shut_up
Reply to kemu and fines  "Shut up" automatically

## requirements
- python3

- numpy

- tweepy

- schedule


## Usage

__Confirm kemufine.py and check_point.txtin exists in same directory__

Check_point.txt is written datetime last mention

~~~
python kemufine.py
~~~

In default , get your mention __every 30 seconds.__

__If you wants to reply as soon as possible__ , please change as below

~~~python
schedule.every(30).seconds.do(reply_team_fines)
→
schedule.every(13).seconds.do(reply_team_fines)
~~~

You can get your mention-timeline 75times/15min , so upperlimit is about 12sec(+request reply).
