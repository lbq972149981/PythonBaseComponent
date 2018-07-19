#5-11
def Rate(origin,userInput):
    if not (isinstance(origin,str) and isinstance(userInput,str)):
        print('The teo parameters must be strings.')
        return
    if len(origin)<len(userInput):
        print('Sorry.I suppose the seond parmeter string is shorter.')
        return
    right=0
    for origin_char,user_char in zip(origin,userInput):
        if origin_char==user_char:
            right+=1
    return right/len(origin)
origin='Shandong Institute of Business and Technology'
uesrInput='Shandong institute of business and technology'
print(Rate(origin,uesrInput))