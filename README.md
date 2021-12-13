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
4. Bash/cmd/shell/whatever: - python run_stream -k "Keyword1,Keyword2,Keyword3"  
You can run a lot of different keywords, there shouldnt be a limit to the amount.  
The stream will start to collect data

Alternatively you can use runinbackground.bat - you need to edit the code inside so it matches your filepath and desired keywords. To stop the stream you need to go and kill the process through task manager (OS dependent. I am running Windows).

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
Working on right now:
Change stream.py def on_status so I can collect tweet ID for further retweet gathering in the future.
Changing SQL database setup and push because of that.

Improve sentiment analysis: After further research, vader actually seems as perfect tool for my purpose. I still can improve the accuracy in different ways, though! Getting rid of spelling mistakes. I would love to be able to do that while I'm grabbing the twitter stream and input the process before sentiment analysis. The more I get to know, the more clear it is that threading will be necessary. Anyway, once I grab the status.text I can run it first through Regular Expression module so I will get rid of repeated alphabets (caaaar, amazzzzing etc). After this is done I can use Pyspellchecker library to correct spelling of the tweets. This should increase the accuracy of my sentiment analysis greatly.

Named entity recognition: get to know other topics the users are tweeting about. Eg my topic is uyghurs in xinjiang. What they talk about the most? China? CCP? 
I looked more into NER. Getting some output with spacy shouldn't be much of an issue. I don't need this to be terrible thorough. 
Few issues I can think of that will need solving:
Where to should I push the output? Inside the SQL library? For one tweet they can be multiple terms.. How to set it up? 
In the end, what can I use this output for? Checking most common keyword-NER pairs? Is it gonna be useful for my analysis?

I would like to push the whole process on some external service. Thinking about Collab. MySQL hosts are plenty. I really want to collect the stream 24/7. See you later, threading!  

Low prio:
Push my Streamlit app to a host service so I can show my data to my friends and collegues online.

setup config.py so you can set up your credentials easier. I tried to do that, run into some issues and ultimately opted to skip this. I will need to learn how to use python for that, though, haha. In the future. Maybe.  

Deprecated:
I would like to introduce Flair instead of Vader and stack it with ELMo. Thus, I will need to train my own Flair model, then introduce it instead of VADER into stream. I might need to introduce threading so the script can keep up. Hopefully not.

## Shoutout
Yes, this script is super heavily inspired by https://github.com/jonathanreadshaw/streamlit-twitter-stream so shout out is due and here it goes.  
It didn't work for me properly from the get go and neither it did for other git users. I made necessary changes to get rid of errors so it should be pretty easy to set up for any of you now. 

Also, it broke connection frequently, so I introduced some code to combat that. It seems stable now.  

# Useful links
https://developer.twitter.com/en/docs/twitter-api/metrics  
https://developer.twitter.com/en/docs/twitter-api/annotations/overview - NER?  
https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet  
https://developer.twitter.com/en/docs/twitter-api/expansions  
https://developer.twitter.com/en/docs/twitter-api/fields  
https://stackoverflow.com/questions/13928155/spell-checker-for-python  
https://blog.quantinsti.com/vader-sentiment/  
