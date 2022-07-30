import pandas as pd
import warnings
warnings.filterwarnings('ignore')
data=pd.read_csv('u.data',sep='\t',header=None)
data.columns=['user_id','movie_id','rating','timestamp']
moviedata=pd.read_csv('u.item',sep="\|",header=None)
moviedata= moviedata[[0,1]]
moviedata.columns=['movie_id','title']
def moviepredict(moviename):
    df=pd.merge(data,moviedata,on="movie_id")
    ratings=df.groupby('title').mean().sort_values('rating',ascending=False)['rating']
    ratings=pd.DataFrame(ratings)
    count=df.groupby('title').count()
    count=count.sort_values('rating',ascending=False)['rating']
    df=pd.merge(count,ratings,on='title')
    df.columns=['ratecount','rate']
    # df['title']
    df=pd.DataFrame(df)
    newdf=pd.merge(data,moviedata,on="movie_id")
    movie_table=pd.pivot_table(data=newdf,index='user_id',columns='title',values='rating')
    starwars_rating=movie_table[moviename]
    count=pd.DataFrame(count)
    starwars_corl=movie_table.corrwith(starwars_rating)


    starwars_corl=pd.DataFrame(starwars_corl,columns=['corelations'])
    starwars_corl.dropna(inplace=True)

    new_mat=pd.merge(starwars_corl,count,on='title')

    
    final=new_mat[new_mat['rating']>100].sort_values('corelations',ascending=False)
    final=pd.merge(final,moviedata,on="title").head(n=10)
    return final

print(moviepredict('Liar Liar (1997)'))
    
    
    
    
    