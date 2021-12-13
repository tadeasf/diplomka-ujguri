# Tweepy Stream + Push to SQL + Streamlit dashboard
At this moment this repo does multiple things.
## Features: Tweepy stream + Push to SQL
You can launch tweepy twitter stream with run_stream.py and collect tweets with keywords of your liking.  
Stream starts collecting the text of the tweet, location, date, user verification, number of followers and performs sentiment analysis with VADER  
After this, data are pushed to mysql database. You can use your own local database, I advise starting with fresh scheme as script will set the table up for you. mssql can be used too with some changes in the code. I was too lazy to do that so it is not included.  
### How to start the stream
0. Install prerequisites as stated in "verymessyprerequisiteshavefun.txt".  Ideally in new virtenviron. Yes, you will run into issues. Those are mostly sorted by common sense but feel free to write them down for me and I will try to help you sort the out if needed.  
1. Setup fresh mysql database scheme with https://www.mysql.com/ - mySQL workbench will make this easy for you.  
2. Insert your user:password@host:port/schemename inside "app.py" and "run_stream.py" scripts accordingly  
3. Insert your api,apisecret,accesstoken,accesssecrettoken credentials inside "run_stream.py" as illustrated in the code.  
4. Open console - python run_stream -k "Keyword1,Keyword2,Keyword3"  
You can run a lot of different keywords, there shouldnt be a limit to the amount.  
The stream will start to collect data  
NOTICE: You need to have twitter developer account. Consult: https://dev.to/sumedhpatkar/beginners-guide-how-to-apply-for-a-twitter-developer-account-1kh7  
  
## Feature: Streamlit dashboard
Streamlit app that shows you a lot of useful data so you can monitor the progress of the script IRL without constantly checking your mysql database. It shows tweets of most followed people in your stream as well as recent tweets so you can check your stream is collecting data.  
It shows you tweet volumes and mean sentiment graphs - again good to check if you are collecting the data you want.  
If you are lucky enough and your tweets include location, nice map will show and plot user location for you  
### How to start Streamlit dashboard
1. Run command console  
2. streamlit run app.py  
3. Enjoy  
  
# TODO
setup config.py so you can set up your credentials easier. I tried to do that, run into some issues and ultimately opted to skip this. I will need to learn how to use python for that, though. In the future. Maybe.  
Named entity recognition: get to know other topics the users are tweeting about. Eg my topic is uyghurs in xinjiang. What they talk about the most? China? CCP? Dissent? I want to know and I will add this to the stream on_status in the future.  
Improve sentiment analysis. I would like to introduce Flair instead of Vader and stack it with ELMo. Thus, I will need to train my own Flair model, then introduce it instead of VADER into stream. I might need to introduce threading so the script can keep up. Hopefully not.  
I would like to push the whole process on some external service. Thinking about Collab. MySQL hosts are plenty. I really want to collect the stream 24/7. See you later, threading!  

## Shoutout
Yes, this script is super heavily inspired by https://github.com/jonathanreadshaw/streamlit-twitter-stream so shout out is due and here it goes.  
It didn't work for me and neither it did for other git users as well from the get go. I made necessary changes so it should be pretty easy to set up for any of you now. Also, it broke connection frequently, so I introduced some code to combat that. It seems stable now.  