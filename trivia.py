print('Hello, welcome to Stonk triva!')
print('Created by NumbersCanBeFun')

ans = input ('Are you ready to play? (yes/no): ')
score = 0
total_q = 4


if ans.lower() == 'yes':

    ans = input('1. What is the memeist stock in the entire market?: ')
    if ans.lower() == '$gme' or ans.lower() == 'gamestop' or ans.lower() == 'gme' :
        score += 1
        print ('Correct')
    else:
        print ('Incorrect')

    ans = input('2. What is the name of the most popular $GME subreddit?: ')
    if ans.lower() == 'superstonk' :
        score += 1
        print ('Correct')
    else:
        print ('Incorrect')
    
    ans = input('3. Who made $GME popular?: ')
    if ans.lower() == 'dfv' or ans.lower() == 'deepfuckingvalue' or ans.lower() == "roaringkitty" : 
        score += 1
        print ('Correct')
    else:
        print ('Incorrect')

    ans = input('4. What is the name of the subreddit DFV posted in?: ')
    if ans.lower() == 'wallstreetbets' or ans.lower() == 'wsb' : 
        score += 1
        print ('Correct')
    else:
        print ('Incorrect')

print ('Thank you for playing you got ', score, " questions correct.")
mark = (score/total_q) *100

print ("Score: ", mark)
print ('Goodbye :)')
