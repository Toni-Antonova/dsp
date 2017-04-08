import csv
import string 
import itertools

with open('metis/prework/dsp/python/faculty.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    #number of different degrees, frequency of each

    def degree_amount_frequency ():
        degree_list = [r[' degree'] for r in reader]
        degree_formatted_one_of_three = [l.lower().translate(None, string.punctuation).split() for l in degree_list]
        degree_formatted_two_of_three = list(itertools.chain.from_iterable(degree_formatted_one_of_three))
        degree_formatted_three_of_three = list(itertools.chain.from_iterable(degree_formatted_one_of_three))

        for s in degree_formatted_two_of_three:
            if s.isdigit():
                degree_formatted_three_of_three.remove(s)
            else:
                pass

        degree_set = set(degree_formatted_three_of_three)

        print ('There are ' + str(len(degree_set)) + ' different degrees.')

        for s in degree_set:
            print (s + ' : ' + str(degree_formatted_three_of_three.count(s)))

 #   degree_amount_frequency()


    #number of different titles, frequency of each

    def title_amount_frequency():
        title_list = [r[' title'] for r in reader]
        title_formatted_one_of_two = [l.lower().translate(None, string.punctuation) for l in title_list]
        title_formatted_two_of_two = [l.lower().translate(None, string.punctuation) for l in title_list]

        for s in title_formatted_one_of_two:
            
            splt = s.split()

            for x in splt:
                if len(x)<4:
                    splt.remove(x)
                    new = ' '.join(splt)
                else:
                    new = s

            title_formatted_two_of_two= [w.replace(s, new) for w in title_formatted_two_of_two]


        title_set = set(title_formatted_two_of_two)

        print ('There are ' + str(len(title_set)) + ' different titles.')


        for s in title_set:
            count = 0
            for x in title_formatted_one_of_two:
                x_diff = set(x.split()).difference(set(s.split()))
                s_diff =set(s.split()).difference(set(x.split()))
                if len(x_diff)==1 and len(s_diff) == 0:
                    count+=1
                else: 
                    pass
            print (s + ' : ' + str(count))

 #   title_amount_frequency()

    #print a list of email addresses

    def email_list_print():
        email_list = [r[' email'] for r in reader]
        return email_list

 #   email_list_print()

    #how many different email domains are there
    #print a list of unique email domains

    def unique_domain_counter():
        email_list = email_list_print()
        domain_set =set()
        for email in email_list:
            index = email.index('@') +1
            domain_set.add(email[index:])
        print('There are ' + str(len(domain_set)) + ' different email domains. Here is the list. ' + str(domain_set))

    unique_domain_counter() 

