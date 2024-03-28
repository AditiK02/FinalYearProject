

df.insert(5,"Party",party)

df["Party"].value_counts()

time_sec = list(set(df["last_updated"]))
time_sec.sort()

time_day = set()
time_month = set()
for i in time_sec:
    time_day.add(i.date())
    time_month.add(i.month)
time_day = list(time_day)
time_day.sort()
time_month = list(time_month)
time_month.sort()

time_week = set()
time_fortnight = set()
result=time_day[0]
while result<= time_day[-1]:
    time_week.add(result)
    result+=timedelta(days=7)
time_week = list(time_week)
time_week.sort()

result = time_day[0]
while result<= time_day[-1]:
    time_fortnight.add(result)
    result+=timedelta(days=15)
time_fortnight = list(time_fortnight)
time_fortnight.sort()

all_hour = []
result = time_sec[0]
while result<= time_sec[-1]:
    all_hour.append((result.date(),result.hour))
    result+=timedelta(hours=1)

all_min = []
result = time_sec[0]
while result<= time_sec[-1]:
    all_min.append((result.date(),result.hour,result.minute))
    result+=timedelta(minutes=1)




score_sec = {}
for t in time_sec:
    score_sec[t] = {"BJP":0,"Congress":0,"Other":0}
for i in range(0,39874):
    t = df["last_updated"][i]
    score_sec[t][df["Party"][i]]+=df["Compound"][i]
#print(score_min)

sec_total_bjp, sec_total_cong, sec_total_other = [],[],[]
for i in score_sec:
    try:
        sec_total_bjp.append(score_sec[i]["BJP"]+sec_total_bjp[-1])
    except IndexError:
        sec_total_bjp.append(score_sec[i]["BJP"]+0)

for i in score_sec:
    try:
        sec_total_cong.append(score_sec[i]["Congress"]+sec_total_cong[-1])
    except IndexError:
        sec_total_cong.append(score_sec[i]["Congress"]+0)

for i in score_sec:
    try:
        sec_total_other.append(score_sec[i]["Other"]+sec_total_other[-1])
    except IndexError:
        sec_total_other.append(score_sec[i]["Other"]+0)

plt.rcParams["figure.figsize"] = [20,15]
plt.figure(num ='Lok Sabha')
plt.plot([i  for i in range(0,4248)],sec_total_bjp,label = 'BJP',color = 'orange')
plt.plot([i  for i in range(0,4248)],sec_total_cong,label = 'Congress',color = 'green')
plt.plot([i  for i in range(0,4248)],sec_total_other,label = 'Other',color = 'black')
plt.style.use('fivethirtyeight')
ax = plt.gca()
plt.grid(True)
plt.legend()
plt.show()
plt.close()

st.line_chart(plt)



score_min = {}
for t in all_min:
    score_min[t] = {"BJP":0,"Congress":0,"Other":0}
for i in range(0,39874):
    t = df["last_updated"][i]
    score_min[(t.date(),t.hour,t.minute)][df["Party"][i]]+=df["Compound"][i]

min_total_bjp, min_total_cong, min_total_other = [],[],[]
for i in score_min:
    try:
        min_total_bjp.append(score_min[i]["BJP"]+min_total_bjp[-1])
    except IndexError:
        min_total_bjp.append(score_min[i]["BJP"]+0)

for i in score_min:
    try:
        min_total_cong.append(score_min[i]["Congress"]+min_total_cong[-1])
    except IndexError:
        min_total_cong.append(score_min[i]["Congress"]+0)

for i in score_min:
    try:
        min_total_other.append(score_min[i]["Other"]+min_total_other[-1])
    except IndexError:
        min_total_other.append(score_min[i]["Other"]+0)

plt.rcParams["figure.figsize"] = [20,15]
plt.figure(num ='Lok Sabha')
plt.plot([i  for i in range(0,139741)],min_total_bjp,label = 'BJP',color = 'orange')
plt.plot([i  for i in range(0,139741)],min_total_cong,label = 'Congress',color = 'green')
plt.plot([i  for i in range(0,139741)],min_total_other,label = 'Other',color = 'black')
plt.style.use('fivethirtyeight')
ax = plt.gca()
plt.grid(True)
plt.legend()
plt.show()
plt.close()

score_hour = {}
for t in all_hour:
    score_hour[t] = {"BJP":0,"Congress":0,"Other":0}
for i in range(0,39874):
    t = df["last_updated"][i]
    score_hour[(t.date(),t.hour)][df["Party"][i]]+=df["Compound"][i]


hour_total_bjp, hour_total_cong, hour_total_other = [],[],[]
for i in score_hour:
    try:
        hour_total_bjp.append(score_hour[i]["BJP"]+hour_total_bjp[-1])
    except IndexError:
        hour_total_bjp.append(score_hour[i]["BJP"]+0)

for i in score_hour:
    try:
        hour_total_cong.append(score_hour[i]["Congress"]+hour_total_cong[-1])
    except IndexError:
        hour_total_cong.append(score_hour[i]["Congress"]+0)

for i in score_hour:
    try:
        hour_total_other.append(score_hour[i]["Other"]+hour_total_other[-1])
    except IndexError:
        hour_total_other.append(score_hour[i]["Other"]+0)

plt.rcParams["figure.figsize"] = [20,15]
plt.figure(num ='Lok Sabha')
plt.plot([i  for i in range(1,2331)],hour_total_bjp,label = 'BJP',color = 'orange')
plt.plot([i  for i in range(1,2331)],hour_total_cong,label = 'Congress',color = 'green')
plt.plot([i  for i in range(1,2331)],hour_total_other,label = 'Other',color = 'black')
plt.style.use('fivethirtyeight')
ax = plt.gca()
plt.grid(True)
plt.legend()
plt.show()
plt.close()




score_day = {}
all_days = []
result=time_day[0]
while result<= time_day[-1]:
    all_days.append(result)
    result+=timedelta(days=1)
#print(all_days)
for t in all_days:
    score_day[t] = {"BJP":0,"Congress":0,"Other":0}
for i in range(0,39874):
    t = df["last_updated"][i]
    score_day[t.date()][df["Party"][i]]+=df["Compound"][i]


day_total_bjp, day_total_cong, day_total_other = [],[],[]
for i in score_day:
    try:
        day_total_bjp.append(score_day[i]["BJP"]+day_total_bjp[-1])
    except IndexError:
        day_total_bjp.append(score_day[i]["BJP"]+0)

for i in score_day:
    try:
        day_total_cong.append(score_day[i]["Congress"]+day_total_cong[-1])
    except IndexError:
        day_total_cong.append(score_day[i]["Congress"]+0)

for i in score_day:
    try:
        day_total_other.append(score_day[i]["Other"]+day_total_other[-1])
    except IndexError:
        day_total_other.append(score_day[i]["Other"]+0)

plt.rcParams["figure.figsize"] = [20,15]
plt.figure(num ='Lok Sabha')
plt.plot([i  for i in range(0,98)],day_total_bjp,label = 'BJP',color = 'orange')
plt.plot([i  for i in range(0,98)],day_total_cong,label = 'Congress',color = 'green')
plt.plot([i  for i in range(0,98)],day_total_other,label = 'Other',color = 'black')
plt.style.use('ggplot')
ax = plt.gca()
plt.grid(True)
plt.legend()
plt.show()
plt.close()



 #Per Day Popularity over 100 days
score_day = {}
all_days = []
result=time_day[0]
while result<= time_day[-1]:
    all_days.append(result)
    result+=timedelta(days=1)
#print(all_days)
for t in all_days:
    score_day[t] = {"BJP":0,"Congress":0,"Other":0}
for i in range(0,39874):
    t = df["last_updated"][i]
    score_day[t.date()][df["Party"][i]]+=df["Score"][i]

day_total_bjp, day_total_cong, day_total_other = [],[],[]
for i in score_day:
    try:
        day_total_bjp.append(score_day[i]["BJP"]+day_total_bjp[-1])
    except IndexError:
        day_total_bjp.append(score_day[i]["BJP"]+0)

for i in score_day:
    try:
        day_total_cong.append(score_day[i]["Congress"]+day_total_cong[-1])
    except IndexError:
        day_total_cong.append(score_day[i]["Congress"]+0)

for i in score_day:
    try:
        day_total_other.append(score_day[i]["Other"]+day_total_other[-1])
    except IndexError:
        day_total_other.append(score_day[i]["Other"]+0)


plt.rcParams["figure.figsize"] = [20,15]
plt.figure(num ='Lok Sabha')
plt.plot([i  for i in range(0,98)],day_total_bjp,label = 'BJP',color = 'orange')
plt.plot([i  for i in range(0,98)],day_total_cong,label = 'Congress',color = 'green')
plt.plot([i  for i in range(0,98)],day_total_other,label = 'Other',color = 'black')
plt.style.use('ggplot')
ax = plt.gca()
plt.grid(True)
plt.legend()
plt.show()
plt.close()

# Weekly Popularity over 14 weeks

score_week = {}
for t in time_week:
    score_week[t] = {"BJP":0,"Congress":0,"Other":0}
last = time_day[0]
ctr = 0
while last<=all_days[-1]:
    if last in time_week:
        score_week[last]["BJP"] = day_total_bjp[ctr]
        score_week[last]["Congress"] = day_total_cong[ctr]
        score_week[last]["Other"] = day_total_other[ctr]
    last+= timedelta(days=1)
    ctr+=1

week_total_bjp, week_total_cong, week_total_other = [],[],[]
for i in score_week:
    week_total_bjp.append(score_week[i]["BJP"])
    week_total_cong.append(score_week[i]["Congress"])
    week_total_other.append(score_week[i]["Other"])

plt.rcParams["figure.figsize"] = [20,15]
plt.figure(num ='Lok Sabha')
plt.plot([i  for i in range(1,15)],week_total_bjp,label = 'BJP',color = 'orange')
plt.plot([i  for i in range(1,15)],week_total_cong,label = 'Congress',color = 'green')
plt.plot([i  for i in range(1,15)],week_total_other,label = 'Other',color = 'black')
plt.style.use('fivethirtyeight')
ax = plt.gca()
plt.grid(True)
plt.legend()
plt.show()
plt.close()


# Fortnightly Popularity over 7 fortnights
score_fn = {}
for t in time_fortnight:
    score_fn[t] = {"BJP":0,"Congress":0,"Other":0}
last = time_day[0]
ctr = 0
while last<=all_days[-1]:
    if last in time_fortnight:
        score_fn[last]["BJP"] = day_total_bjp[ctr]
        score_fn[last]["Congress"] = day_total_cong[ctr]
        score_fn[last]["Other"] = day_total_other[ctr]
    last+= timedelta(days=1)
    ctr+=1

fn_total_bjp, fn_total_cong, fn_total_other = [],[],[]
for i in score_fn:
    fn_total_bjp.append(score_fn[i]["BJP"])
    fn_total_cong.append(score_fn[i]["Congress"])
    fn_total_other.append(score_fn[i]["Other"])

plt.rcParams["figure.figsize"] = [30,15]
plt.figure(num ='Lok Sabha')
plt.plot([i  for i in range(1,8)],fn_total_bjp,label = 'BJP',color = 'orange')
plt.plot([i  for i in range(1,8)],fn_total_cong,label = 'Congress',color = 'green')
plt.plot([i  for i in range(1,8)],fn_total_other,label = 'Other',color = 'black')
plt.style.use('fivethirtyeight')
ax = plt.gca()
plt.grid(True)
plt.legend()
plt.show()
plt.close()

# Monthly Popularity over 4 months
score_month = {}
for t in time_month:
    score_month[t] = {"BJP":0,"Congress":0,"Other":0}
for i in range(0,39874):
    t = df["last_updated"][i].month
    score_month[t][df["Party"][i]]+=df["Compound"][i]


month_total_bjp, month_total_cong, month_total_other = [],[],[]
for i in score_month:
    try:
        month_total_bjp.append(score_month[i]["BJP"]+month_total_bjp[-1])
    except IndexError:
        month_total_bjp.append(score_month[i]["BJP"]+0)

for i in score_month:
    try:
        month_total_cong.append(score_month[i]["Congress"]+month_total_cong[-1])
    except IndexError:
        month_total_cong.append(score_month[i]["Congress"]+0)

for i in score_month:
    try:
        month_total_other.append(score_month[i]["Other"]+month_total_other[-1])
    except IndexError:
        month_total_other.append(score_month[i]["Other"]+0)

plt.rcParams["figure.figsize"] = [30,15]
plt.figure(num ='Lok Sabha')
plt.plot([i  for i in range(1,5)],month_total_bjp,label = 'BJP',color = 'orange')
plt.plot([i  for i in range(1,5)],month_total_cong,label = 'Congress',color = 'green')
plt.plot([i  for i in range(1,5)],month_total_other,label = 'Other',color = 'black')
plt.style.use('fivethirtyeight')
ax = plt.gca()
plt.grid(True)
plt.legend()
plt.show()
plt.close()


# Day wise Popularity per State
state_day_score = dict()
for i in set(list(df["State"])):
    if list(df["State"]).count(i)>500 and i!='':
        state_day_score[i]=dict()
        for t in all_days:
            state_day_score[i][t] = {"BJP":0,"Congress":0,"Other":0}

state_day_score["Other"]=dict()
for t in all_days:
            state_day_score["Other"][t] = {"BJP":0,"Congress":0,"Other":0}

for i in range(0,39874):
    t = df["last_updated"][i].date()
    st = df["State"][i]
    pty = df["Party"][i]
    cp = df["Compound"][i]
    if st in state_day_score:
            state_day_score[st][t][pty]+=cp
    else:
        state_day_score["Other"][t][pty]+=cp

state_popularity = dict()
for i in state_day_score:
    state_popularity[i] = {"BJP":[],"Congress":[],"Other":[]}

for st in state_day_score:
    for t in state_day_score[st]:
        try:
            state_popularity[st]["BJP"].append(state_day_score[st][t]["BJP"]+state_popularity[st]["BJP"][-1])
        except IndexError:
            state_popularity[st]["BJP"].append(state_day_score[st][t]["BJP"]+0)
            
for st in state_day_score:
    for t in state_day_score[st]:
        try:
            state_popularity[st]["Congress"].append(state_day_score[st][t]["Congress"]+state_popularity[st]["Congress"][-1])
        except IndexError:
            state_popularity[st]["Congress"].append(state_day_score[st][t]["Congress"]+0)

for st in state_day_score:
    for t in state_day_score[st]:
        try:
            state_popularity[st]["Other"].append(state_day_score[st][t]["Other"]+state_popularity[st]["Other"][-1])
        except IndexError:
            state_popularity[st]["Other"].append(state_day_score[st][t]["Other"]+0)


del state_popularity["Other"]


plt.rcParams["figure.figsize"] = [20,15]
plt.figure(num ='Lok Sabha')
#colors = ["red","blue","orange","purple","green","violet","pink","black","lightblue","lightgreen","darkred","grey"]
ctr=0
for i in state_popularity:
    plt.plot([i  for i in range(0,98)],state_popularity[i]["BJP"],label = i)
    ctr+=1
plt.style.use('fivethirtyeight')
#plt.figure(figsize=(20,20))
plt.title("Popularity of BJP over Time")
ax = plt.gca()
plt.grid(True)
plt.legend( loc='best', bbox_to_anchor=(1, 0,0.2, 1.02))
plt.show()
plt.close()



state_day_score = dict()
for i in set(list(df["State"])):
    if list(df["State"]).count(i)>500 and i!='':
        state_day_score[i]=dict()
        for t in all_days:
            state_day_score[i][t] = {"BJP":0,"Congress":0,"Other":0}

state_day_score["Other"]=dict()
for t in all_days:
            state_day_score["Other"][t] = {"BJP":0,"Congress":0,"Other":0}

for i in range(0,39874):
    t = df["last_updated"][i].date()
    st = df["State"][i]
    pty = df["Party"][i]
    cp = df["Score"][i]
    if st in state_day_score:
            state_day_score[st][t][pty]+=cp
    else:
        state_day_score["Other"][t][pty]+=cp

state_popularity = dict()
for i in state_day_score:
    state_popularity[i] = {"BJP":[],"Congress":[],"Other":[]}

for st in state_day_score:
    for t in state_day_score[st]:
        try:
            state_popularity[st]["BJP"].append(state_day_score[st][t]["BJP"]+state_popularity[st]["BJP"][-1])
        except IndexError:
            state_popularity[st]["BJP"].append(state_day_score[st][t]["BJP"]+0)
            
for st in state_day_score:
    for t in state_day_score[st]:
        try:
            state_popularity[st]["Congress"].append(state_day_score[st][t]["Congress"]+state_popularity[st]["Congress"][-1])
        except IndexError:
            state_popularity[st]["Congress"].append(state_day_score[st][t]["Congress"]+0)

for st in state_day_score:
    for t in state_day_score[st]:
        try:
            state_popularity[st]["Other"].append(state_day_score[st][t]["Other"]+state_popularity[st]["Other"][-1])
        except IndexError:
            state_popularity[st]["Other"].append(state_day_score[st][t]["Other"]+0)


del state_popularity["Other"]


plt.rcParams["figure.figsize"] = [20,15]
plt.figure(num ='Lok Sabha')
#colors = ["red","blue","orange","purple","green","violet","pink","black","lightblue","lightgreen","darkred","grey"]
ctr=0
for i in state_popularity:
    plt.plot([i  for i in range(0,98)],state_popularity[i]["BJP"],label = i)
    ctr+=1
plt.style.use('fivethirtyeight')
#plt.figure(figsize=(20,20))
plt.title("Popularity of BJP over Time")
ax = plt.gca()
plt.grid(True)
plt.legend( loc='best', bbox_to_anchor=(1, 0,0.2, 1.02))
plt.show()
plt.close()



plt.figure(num ='Lok Sabha')
plt.rcParams["figure.figsize"] = [20,15]
for i in state_popularity:
    plt.plot([i  for i in range(0,98)],state_popularity[i]["Congress"],label = i)
plt.style.use('fivethirtyeight')
#plt.figure(figsize=(20,20))
plt.title("Popularity of Congress over Time")
ax = plt.gca()
plt.grid(True)
plt.legend( loc='best', bbox_to_anchor=(1, 0,0.2, 1.02))
plt.show()
plt.close()


plt.figure(num ='Lok Sabha')
plt.rcParams["figure.figsize"] = [20,15]
for i in state_popularity:
    plt.plot([i  for i in range(0,98)],state_popularity[i]["Other"],label = i)
plt.style.use('fivethirtyeight')
#plt.figure(figsize=(20,20))
ax = plt.gca()
plt.grid(True)
plt.title("Popularity of Other Parties over Time")
plt.legend( loc='best', bbox_to_anchor=(1, 0,0.2, 1.02))
plt.show() 
plt.close()



# Plotting Final Popularity before Results
plt.rcParams["figure.figsize"] = [6,6]
x = matplotlib.pyplot.bar(["BJP","Congress","Other"],[max(day_total_bjp),max(day_total_cong),max(day_total_other)],width=0.3,color=["Orange","green","grey"])
plt.legend([x[0],x[1],x[2]],["BJP","Congress","Other"])
plt.title("Final Popularity Index")
















states = list(set(list(df["State"])))
states.remove("")


# Most tweeted from States
state_count = dict(df["State"].value_counts())
del state_count[""]
state_count["Other"] = 0
most_state_count = dict()
most_state_count["Other"] =0

for i in state_count:
    if state_count[i]<150:
        most_state_count["Other"]+=state_count[i]
    else:
        most_state_count[i] = state_count[i]

plt.rcParams["figure.figsize"] = [30,15]
del most_state_count["Other"]
plt.style.use('fivethirtyeight')
fig = plt.bar(list(most_state_count.keys()),list(most_state_count.values()),width = 0.8)
plt.title("Most Tweeted from States")


fp1 = r"INDIA\IND_adm1.shp"
map_df1 = gpd.read_file(fp1)

count = dict(df["State"].value_counts())
states = list(count.keys())
states.remove("")

geo=[]
for i in states:
    for j in range(0,36):
        name1 = i
        name2 = map_df1["NAME_1"][j]
        if(name1==name2):
            geo.append(map_df1["geometry"][j])
            break
        elif len(set(name1.split()).intersection(set(name2.split())))>1:
            geo.append(map_df1["geometry"][j])
            break
        elif name2=="Puducherry" and name1 == "Pondicherry":
            geo.append(map_df1["geometry"][j])
            break


bjp,cong,other,party,tweets,bjppop,congpop,opop=[],[],[],[],[],[],[],[]
partycount = dict()
for i in states:
    partycount[i] = {"BJP":0,"Congress":0,"Other":0,"BJPPop":0,"CongPop":0,"OtherPop":0,
                     'narendramodi':0,'bjp4india':0,'incindia':0,'rahulgandhi':0,
                    "htmodi":0,'htbjp':0,'htloksabha':0,'htcong':0,'htrahulgandhi':0,'htchow':0}        

for i in range(0,39874):
    p = df["Party"][i]
    s = df["State"][i]
    cp = df["Compound"][i]
    temp = df["hashtags"][i]
    user = df["user_mentions_screen_name"][i]
    if s=="":
        continue
    partycount[s][p]+=1
    if p=="BJP":
        partycount[s]["BJPPop"]+=cp
    if p=="Congress":
        partycount[s]["CongPop"]+=cp
    if p=="Other":
        partycount[s]["OtherPop"]+=cp
    for hst in temp.split(','):
        if hst =="BJP":
            partycount[s]['htbjp']+=1
        if hst =="Modi":
            partycount[s]['htmodi']+=1
        if hst =="LokSabhaElections2019":
            partycount[s]['htloksabha']+=1
        if hst =="Congress":
            partycount[s]['htcong']+=1
        if hst =="RahulGandhi":
            partycount[s]['htrahulgandhi']+=1
        if hst =="MainBhiChowkidar":
            partycount[s]['htchow']+=1
    for x in user.split(','):
        if x=="BJP4India":
            partycount[s]['bjp4india']+=1
        if x=="narendramodi":
            partycount[s]['narendramodi']+=1
        if x=="INCIndia":
            partycount[s]['incindia']+=1
        if x=="RahulGandhi":
            partycount[s]['rahulgandhi']+=1 


htbjp,htmodi,htls,htcong,htrg,htchow = [],[],[],[],[],[]
hdbjp,hdmodi,hdcong,hdrg=[],[],[],[]

for i in partycount:
    bjp.append(partycount[i]["BJP"])
    cong.append(partycount[i]["Congress"])
    other.append(partycount[i]["Other"])
    tweets.append(partycount[i]["BJP"]+partycount[i]["Congress"]+partycount[i]["Other"])
    bjppop.append(partycount[i]["BJPPop"])
    congpop.append(partycount[i]["CongPop"])
    opop.append(partycount[i]["OtherPop"])
    
    htbjp.append(partycount[i]['htbjp'])
    htmodi.append(partycount[i]['htmodi'])
    htls.append(partycount[i]['htloksabha'])
    htcong.append(partycount[i]['htcong'])
    htrg.append(partycount[i]['htrahulgandhi'])
    htchow.append(partycount[i]['htchow'])

    hdbjp.append(partycount[i]['bjp4india'])
    hdmodi.append(partycount[i]['narendramodi'])
    hdcong.append(partycount[i]['incindia'])
    hdrg.append(partycount[i]['rahulgandhi'])
    
    if partycount[i]["BJPPop"]>partycount[i]["CongPop"] and partycount[i]["BJPPop"]>partycount[i]["OtherPop"]:
        party.append("BJP")
    elif partycount[i]["BJPPop"]<partycount[i]["CongPop"] and partycount[i]["OtherPop"]<partycount[i]["CongPop"]:
        party.append("Congress")
    else:
        party.append("Other")


testdf = pd.DataFrame({"State":states,"Tweets":tweets,"Geo":geo,"Party":party,"BJP":bjp,"Congress":cong,"Other":other,
                      "BJPPop":bjppop,"Congpop":congpop,"OtherPop":opop,
                      "#BJP":htbjp,"#Modi":htmodi,"#LokSabhaElections2019":htls,"#Congress":htcong,"#RahulGandhi":htrg,"#MainBhiChowkidar":htchow,
                      "@BJP4India":hdbjp,"@narendramodi":hdmodi,"@INCIndia":hdcong,"@RahulGandhi":hdrg})
testdf.head()

gdf = gpd.GeoDataFrame(testdf, geometry="Geo")


                                                     #yaha se map shuru hai
plt.style.use('default')
plt.rcParams["figure.figsize"] = [15,10]
gdf.plot(column="Tweets",legend = True)
plt.title("Most Tweeted from States")


plt.style.use('default')
plt.rcParams["figure.figsize"] = [15,10]
gdf.plot(column="BJP",legend = True,cmap="Reds")
plt.title("States tweeting about BJP")

plt.style.use('default')
plt.rcParams["figure.figsize"] = [15,10]
gdf.plot(column="Congress",legend = True,cmap="Greens")
plt.title("States tweeting about Congress")

plt.style.use('default')
plt.rcParams["figure.figsize"] = [15,10]
gdf.plot(column="Other",legend = True,cmap = "Blues")
plt.title("States tweeting about Other Parties")

plt.style.use('default')
plt.rcParams["figure.figsize"] = [15,10]
gdf.plot(column="Party",legend = True,cmap="inferno")
plt.title("Popularity Trend Across States")

plt.style.use('default')
plt.rcParams["figure.figsize"] = [15,10]
gdf.plot(column="BJPPop",cmap="Reds",legend = True)
plt.title("BJP Popularity")

plt.style.use('default')
plt.rcParams["figure.figsize"] = [15,10]
gdf.plot(column="Congpop",cmap="Greens",legend = True)
plt.title("Congress Popularity")

plt.style.use('default')
plt.rcParams["figure.figsize"] = [15,10]
gdf.plot(column="OtherPop",cmap="Blues",legend = True)
plt.title("Other Party Popularity")
plt.show()





# Most Tweeted from Cities

city_count = dict(df["City"].value_counts())
city_count["Other"] = 0
del city_count[""]
most_city_count = dict()
most_city_count["Other"] = 0

for i in city_count:
    if city_count[i]<200:
        most_city_count["Other"]+=city_count[i]
    else:
        most_city_count[i] = city_count[i]

del most_city_count["Other"]
plt.rcParams["figure.figsize"] = [30,15]
plt.style.use('fivethirtyeight')
fig = plt.bar(list(most_city_count.keys()),list(most_city_count.values()),width = 0.8)
plt.title("Most Tweeted from Cities")






# Most Popular Hashtags

hashtags = []
for i in list(df["hashtags"]):
    x = i.split(',')
    for j in x:
        hashtags.append(j)
hashdata = [i for i in hashtags if i!=""]

hash_count = dict()
hash_count["Other"] = 0
for i in set(hashtags):
    x = hashtags.count(i)
    if x<60: #70 is best count
        hash_count["Other"]+= x
    else:
        hash_count[i] = x
del hash_count[""]
del hash_count["Other"]

plt.style.use("fivethirtyeight")
plt.rcParams["figure.figsize"] = [30,15]
fig = plt.bar(list(hash_count.keys()),list(hash_count.values()),width = 0.5)
plt.title("Most Popular Hashtags")

plt.style.use('default')            #yaha se dushra round ka india map shuru
plt.rcParams["figure.figsize"] = [10,5]
gdf.plot(column="#BJP",legend = True,cmap="Reds")
plt.title("#BJP")

plt.style.use('default')
plt.rcParams["figure.figsize"] = [10,5]
gdf.plot(column="#Modi",legend = True,cmap="Reds")
plt.title("#Modi")

plt.style.use('default')
plt.rcParams["figure.figsize"] = [10,5]
gdf.plot(column="#Congress",legend = True,cmap="Greens")
plt.title("#Congress")

plt.style.use('default')
plt.rcParams["figure.figsize"] = [10,5]
gdf.plot(column="#RahulGandhi",legend = True,cmap="Greens")
plt.title("#RahulGandhi")


plt.style.use('default')
plt.rcParams["figure.figsize"] = [10,5]
gdf.plot(column="#MainBhiChowkidar",legend = True,cmap="Reds")
plt.title("#MainBhiChowkidar")

plt.style.use('default')
plt.rcParams["figure.figsize"] = [10,5]
gdf.plot(column="#LokSabhaElections2019",legend = True)
plt.title("#LokSabhaElections2024")




# Most Tagged Handles
handles = []
for i in df["user_mentions_screen_name"]:
    x = i.split(',')
    for j in x:
        handles.append(j)
handles = [i for i in handles if i!=""]

handle_count = dict()
handle_count["Other"] = 0
for i in set(handles):
    x = handles.count(i)
    if x<120:
        handle_count["Other"]+= x
    else:
        handle_count[i] = x
#del handle_count[""]
del handle_count["Other"]

plt.rcParams["figure.figsize"] = [20,10]
fig = plt.bar(list(handle_count.keys()),list(handle_count.values()),width = 0.8)
plt.title("Most Tagged Handles")

#third round india maping shuru

plt.style.use('default')               
plt.rcParams["figure.figsize"] = [10,5]
gdf.plot(column="@narendramodi",legend = True,cmap="Reds")
plt.title("People tagging @Modi")

plt.style.use('default')
plt.rcParams["figure.figsize"] = [10,5]
gdf.plot(column="@BJP4India",legend = True,cmap="Reds")
plt.title("People tagging @BJP4India")

plt.style.use('default')
plt.rcParams["figure.figsize"] = [10,5]
gdf.plot(column="@INCIndia",legend = True,cmap="Greens")
plt.title("People tagging @Congress")

plt.style.use('default')
plt.rcParams["figure.figsize"] = [10,5]
gdf.plot(column="@RahulGandhi",legend = True,cmap="Greens")
plt.title("People tagging @RahulGandhi")




# Frequency of Tweets per Day

tweets_per_day = dict()
for i in all_days:
    tweets_per_day[i]=0
for i in range(0,39874):
    tweets_per_day[df["last_updated"][i].date()]+=1

temp = dict()
for i in tweets_per_day:
    if tweets_per_day[i]!=0:
        temp[i] = tweets_per_day[i]
        #tweets_per_day[i] = tweets_per_day[i-timedelta(days=1)]     
tweets_per_day = temp

plt.rcParams["figure.figsize"] = [15,10]
plt.plot([i  for i in range(len(tweets_per_day.keys()))],list(tweets_per_day.values()))
plt.style.use('fivethirtyeight')
#plt.figure(figsize=(20,20))
ax = plt.gca()
plt.grid(True)
plt.title("Frequency of Tweets per Day")
#plt.legend( loc='best', bbox_to_anchor=(1, 0,0.2, 1.02))
plt.show()
plt.close()



# Tagging Frequency over Time

ht = ["narendramodi","BJP4India","RahulGandhi","INCIndia"]
ht_time = dict()
for i in all_days:
    ht_time[i] = {"narendramodi":0,"BJP4India":0,"RahulGandhi":0,"INCIndia":0}

for i in range(0,39874):
    t = df["last_updated"][i].date()
    temp = df["user_mentions_screen_name"][i].split(',')
    for j in temp:
        if j in ht:
            ht_time[t][j]+=1

modi_tag1 = []
bjp_tag1 = []
rahulgandhi_tag1 = []
cong_tag1 = []
modi_tag2 = []
bjp_tag2 = []
rahulgandhi_tag2 = []
cong_tag2 = []

for t in ht_time:
    temp = ht_time[t]
    try:
        modi_tag1.append(temp["narendramodi"])
        modi_tag2.append(modi_tag2[-1]+temp["narendramodi"])
    except:
        modi_tag2.append(0+temp["narendramodi"])

for t in ht_time:
    temp = ht_time[t]
    try:
        bjp_tag1.append(temp["BJP4India"])
        bjp_tag2.append(bjp_tag2[-1]+temp["BJP4India"])
    except:
        bjp_tag2.append(0+temp["BJP4India"])
        
for t in ht_time:
    temp = ht_time[t]
    try:
        rahulgandhi_tag1.append(temp["RahulGandhi"])
        rahulgandhi_tag2.append(rahulgandhi_tag2[-1]+temp["RahulGandhi"])
    except:
        rahulgandhi_tag2.append(0+temp["RahulGandhi"])
        
for t in ht_time:
    temp = ht_time[t]
    try:
        cong_tag1.append(temp["INCIndia"])
        cong_tag2.append(cong_tag2[-1]+temp["INCIndia"])
    except:
        cong_tag2.append(0+temp["INCIndia"])


tagged_scores = {"narendramodi":[modi_tag1,modi_tag2],"BJP4India":[bjp_tag1,bjp_tag2],
                "RahulGandhi":[rahulgandhi_tag1,rahulgandhi_tag2],"INCIndia":[cong_tag1,cong_tag2]}



plt.figure(num ='Lok Sabha')
plt.rcParams["figure.figsize"] = [15,10]
for i in ht:
    plt.plot([i  for i in range(0,98)],tagged_scores[i][0],label = i)
plt.style.use('fivethirtyeight')
plt.title("Frequency of Tagging")
plt.grid(True)
ax = plt.gca()
plt.legend(loc='best', bbox_to_anchor=(1, 0,0.2, 1.02))
plt.show()
plt.close()

plt.figure(num ='Lok Sabha')
plt.rcParams["figure.figsize"] = [15,5]
for i in ht:
    plt.plot([i  for i in range(0,98)],tagged_scores[i][1],label = i)
plt.style.use('fivethirtyeight')
plt.title("Popularity of Handles over Time")
plt.grid(True)
ax = plt.gca()
plt.legend(loc='best', bbox_to_anchor=(1, 0,0.2, 1.02))
plt.show()
plt.close()



# Discrete Probabilites

vote_score = dict()
for i in all_days:
  vote_score[i] = {"bjp_votes":0, "cong_votes":0, "other_votes":0, "cong_coal":0, "bjp_coal":0,"total":0}
#bjp_votes, cong_votes, other_votes, cong_coal, bjp_coal = [0 for i in range(5)]
total = 0
for i in range(0,39874):
  t = df["last_updated"][i].date()
  party = df["Party"][i]
  score = df["Score"][i]
  scoreadd=1
  if party=="BJP":
    if score>0:
      vote_score[t]["bjp_votes"]+=scoreadd
      vote_score[t]["total"]+=1
    else:
      if score >=-0.4 and score <=0:
        vote_score[t]["cong_coal"]+=scoreadd
        vote_score[t]["total"]+=1
      else:
        vote_score[t]["cong_votes"]+=scoreadd
        vote_score[t]["total"]+=1
  elif party=="Congress":
    if score>0:
      vote_score[t]["cong_votes"]+=scoreadd
      vote_score[t]["total"]+=1
    else:
      if score >=-0.4 and score <=0:
        vote_score[t]["bjp_coal"]+=scoreadd
        vote_score[t]["total"]+=1
      else:
        vote_score[t]["bjp_votes"]+=scoreadd
        vote_score[t]["total"]+=1
  else:
    if score>0:
      vote_score[t]["other_votes"]+=scoreadd
      vote_score[t]["total"]+=1
    elif score >=-0.4 and score <=0:
      if vote_score[t]["bjp_votes"]>vote_score[t]["cong_votes"]:
        vote_score[t]["bjp_coal"]+=scoreadd
        vote_score[t]["total"]+=1
      else:
        vote_score[t]["cong_coal"]+=scoreadd
        vote_score[t]["total"]+=1




vote_bjp1, vote_cong1, vote_other1, vote_bjp_coal1, vote_cong_coal1 = [],[],[],[],[]
vote_bjp2, vote_cong2, vote_other2, vote_bjp_coal2, vote_cong_coal2 = [],[],[],[],[]
temp = dict()
for i in vote_score:
    if vote_score[i]["total"]!=0:
        temp[i] = vote_score[i]
vote_score=temp
for t in vote_score:
  if vote_score[t]['total']==0:
    continue
  vote_bjp1.append((vote_score[t]["bjp_votes"]/vote_score[t]["total"]))
  try:
    vote_bjp2.append((vote_score[t]["bjp_votes"]+vote_bjp2[-1])/(vote_score[t]["total"]+vote_score[t-timedelta(days=1)]["total"]))
  except:
    vote_bjp2.append((vote_score[t]["bjp_votes"]/vote_score[t]["total"]))

for t in vote_score:
  if vote_score[t]['total']==0:
    continue
  vote_cong1.append((vote_score[t]["cong_votes"]/vote_score[t]["total"]))
  try:
    vote_cong2.append((vote_score[t]["cong_votes"]+vote_cong2[-1])/(vote_score[t]["total"]+vote_score[t-timedelta(days=1)]["total"]))
  except:
    vote_cong2.append((vote_score[t]["cong_votes"]/vote_score[t]["total"]))

for t in vote_score:
  if vote_score[t]['total']==0:
    continue
  vote_other1.append((vote_score[t]["other_votes"]/vote_score[t]["total"]))
  try:
    vote_other2.append((vote_score[t]["other_votes"]+vote_other2[-1])/(vote_score[t]["total"]+vote_score[t-timedelta(days=1)]["total"]))
  except:
    vote_other2.append((vote_score[t]["other_votes"]/vote_score[t]["total"]))

for t in vote_score:
  if vote_score[t]['total']==0:
    continue
  vote_bjp_coal1.append((vote_score[t]["bjp_coal"]/vote_score[t]["total"]))
  try:
    vote_bjp_coal2.append((vote_score[t]["bjp_coal"]+vote_bjp_coal2[-1])/(vote_score[t]["total"]+vote_score[t-timedelta(days=1)]["total"]))
  except:
    vote_bjp_coal2.append((vote_score[t]["bjp_coal"]/vote_score[t]["total"]))

for t in vote_score:
  if vote_score[t]['total']==0:
    continue
  vote_cong_coal1.append((vote_score[t]["cong_coal"]/vote_score[t]["total"]))
  try:
    vote_cong_coal2.append((vote_score[t]["cong_coal"]+vote_cong_coal2[-1])/(vote_score[t]["total"]+vote_score[t-timedelta(days=1)]["total"]))
  except:
    vote_cong_coal2.append((vote_score[t]["cong_coal"]/vote_score[t]["total"]))


plt.figure(num ='Lok Sabha')
plt.rcParams["figure.figsize"] = [15,5]
labels = ["BJP","Congress","Other","BJP Coalition","Congress Coalition"]
x = [vote_bjp1, vote_cong1, vote_other1, vote_bjp_coal1, vote_cong_coal1]
for i in x:
    plt.plot([j  for j in range(len(i))],i,label= labels[x.index(i)])
plt.style.use('fivethirtyeight')
plt.title("Winning Probability")
plt.grid(True)
ax = plt.gca()
plt.legend(loc='best', bbox_to_anchor=(1, 0,0.2, 1.02))
plt.show()
plt.close()

plt.figure(num ='Lok Sabha')
plt.rcParams["figure.figsize"] = [15,5]
labels = ["BJP","Congress","Other","BJP Coalition","Congress Coalition"]
x = [vote_bjp2,vote_cong2, vote_other2, vote_bjp_coal2, vote_cong_coal2]
for i in x:
    plt.plot([j  for j in range(len(i))],i,label = labels[x.index(i)])
plt.style.use('fivethirtyeight')
plt.title("Chances of Winning")
plt.grid(True)
ax = plt.gca()
plt.legend(loc='best', bbox_to_anchor=(1, 0,0.2, 1.02))
plt.show()
plt.close()





                                




