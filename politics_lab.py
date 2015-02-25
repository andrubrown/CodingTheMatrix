# version code d345910f07ae+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

# Be sure that the file voting_record_dump109.txt is in the matrix/ directory.




## 1: (Task 1) Create Voting Dict
def create_voting_dict(strlist):
    """
    Input: a list of strings.  Each string represents the voting record of a senator.
           The string consists of 
              - the senator's last name, 
              - a letter indicating the senator's party,
              - a couple of letters indicating the senator's home state, and
              - a sequence of numbers (0's, 1's, and negative 1's) indicating the senator's
                votes on bills
              all separated by spaces.
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting record.
    Example: 
        >>> create_voting_dict(['Kennedy D MA -1 -1 1 1', 'Snowe R ME 1 1 1 1'])
        {'Snowe': [1, 1, 1, 1], 'Kennedy': [-1, -1, 1, 1]}

    You can use the .split() method to split each string in the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.

    You can use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    The lists for each senator should preserve the order listed in voting data.
    In case you're feeling clever, this can be done in one line.
    """
    d = {}
    for str in strlist:
        pieces = str.split()
        d[pieces[0]] = [int(v) for v in pieces[3:]]
    return d


## 2: (Task 2) Policy Compare
def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    The code should correct compute dot-product even if the numbers are not all in {0,1,-1}.
        >>> policy_compare('A', 'B', {'A':[100,10,1], 'B':[2,5,3]})
        253
        
    You should definitely try to write this in one line.
    """
    return sum([v[0]*v[1] for v in zip(voting_dict[sen_a],voting_dict[sen_b])])



## 3: (Task 3) Most Similar
def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    name = ''
    min = float('-infinity')
    for key in voting_dict.keys():
        if key != sen:
            diff = policy_compare(sen, key, voting_dict)
            if diff > min:
                name = key
                min = diff
    return name



## 4: (Task 4) Least Similar
def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        >>> least_similar('a', vd)
        'c'
    """
    name = ''
    max = float('infinity')
    for key in voting_dict.keys():
        if key != sen:
            diff = policy_compare(sen, key, voting_dict)
            if diff < max:
                name = key
                max = diff
    return name



## 5: (Task 5) Chafee, Santorum
f = open('voting_record_dump109.txt')
voting_dict = create_voting_dict(list(f))

most_like_chafee    = most_similar('Chafee', voting_dict)
least_like_santorum = least_similar('Santorum', voting_dict)



## 6: (Task 6) Most Average Democrat
def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    compares = [policy_compare(sen, other, voting_dict) for other in sen_set if sen != other]
    return sum(compares)/len(compares)

f = open('voting_record_dump109.txt')
democrats = {pieces[0] for line in list(f) for pieces in [line.split()] if pieces[1] == 'D'}
most_average_Democrat = ''
most_average_average = float('-infinity')
for democrat in democrats:
    average = find_average_similarity(democrat, democrats, voting_dict)
    if average > most_average_average:
        most_average_average = average
        most_average_Democrat = democrat



## 7: (Task 7) Average Record
def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
        >>> d = {'c': [-1,-1,0], 'b': [0,1,1], 'a': [0,1,1], 'e': [-1,-1,1], 'd': [-1,1,1]}
        >>> find_average_record({'a','c','e'}, d)
        [-0.6666666666666666, -0.3333333333333333, 0.6666666666666666]
        >>> find_average_record({'a','c','e','b'}, d)
        [-0.5, 0.0, 0.75]
        >>> find_average_record({'a'}, d)
        [0.0, 1.0, 1.0] 
    """
    average = None
    for sen in sen_set:
        if average == None:
            average = list(voting_dict[sen])
        else:
            average = [com[0]+com[1] for com in zip(average, voting_dict[sen])]
                       
    return [value/len(sen_set) for value in average]

average_Democrat_record = find_average_record(democrats, voting_dict)

#most_average_Democrat = ''
#most_average_average = float('-infinity')
#for democrat in democrats:
#    compare = sum([v[0]*v[1] for v in zip(average_Democrat_record,voting_dict[democrat])])
#    if compare > most_average_average:
#        most_average_average = compare
#        most_average_Democrat = democrat


## 8: (Task 8) Bitter Rivals
def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    rivals = ()
    min = float('infinity')
    for senator in voting_dict.keys():
        rival = least_similar(senator, voting_dict)
        diff = policy_compare(senator, rival, voting_dict)
        if diff < min:
            rivals = (senator, rival)
            min = diff
    return rivals

