import random
from bs4 import BeautifulSoup as bs
import requests
import re

def get_movie_name():
  import random
  r= random.randint(1,7)
  base_link= 'https://www.listchallenges.com/250-movies-worth-your-time/list/'

  get_movie= requests.get(base_link+str(r))
  if get_movie.status_code == 200:
    doc= bs(get_movie.text,'html.parser')

  movie_name_tags= doc.find_all('div',class_='item-name')
  movie_list= [i.text.strip() for i in movie_name_tags]
  return random.sample(movie_list,1)[0]

def clean_name(movie_name):
  pattern= re.compile(r'[a-zA-Z0-9]+')
  return ' '.join(re.findall(pattern,movie_name.split('(')[0].strip()))

def movie_generator():
  movie_name=get_movie_name()
  movie= clean_name(movie_name).lower()
  print(movie)
  sample_alpha=random.sample(movie,2)
  guess_list= ['_']*len(movie)
  for i,j in enumerate(movie):
    if j in sample_alpha:
      guess_list[i]=j

    elif j==' ':
      guess_list[i]= ' '
  return movie,guess_list



def game_play(check, random_movie):
  print(f'''
          {' '.join(random_movie)}
          ''')
  segment= list('HOLLYWOOD')
  guess_len= len(segment)
  while guess_len!=0:
    user_char= input('enter the alphabet: ')
    if user_char in random_movie:
      print('''
            Alphabet already present.
            Try with different character!!!
            ''')
    if user_char in check:
      for i,j in enumerate(check):
        
        if j == user_char:
          random_movie[i]= j  

      print(f'''
            Correct Guess
            \t {' '.join(random_movie)}
            now take a next guess
      ''')
      print()
    else:
      segment[len(segment)-guess_len]='*'
      print(f'''
            {' '.join(segment)}
            ''')
      guess_len-=1
      print(f'''
            WRONG GUESS!!!
            now you have {guess_len} guesses left.
            \t {' '.join(random_movie)} 
            Try again.
      ''')
      print()
    
      
    if '_' not in random_movie:
      print(f'''
              you guessed the name of the movie correctly!!!
              And the movie name is "{check}"
            ''')
      break

  if guess_len==0:
    print(f'''
            you failed to guess the movie,
            here is the movie name:-
            "{check.upper()}"
    ''')

movie_original,movie_list =movie_generator()
# print(movie_list) 
game_play(movie_original,movie_list)