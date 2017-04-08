import csv


with open ('metis/prework/dsp/python/emails.csv','w+a') as writtenfile:
    writer = csv.writer(writtenfile)

    with open('metis/prework/dsp/python/faculty.csv') as readfile:
        reader = csv.DictReader(readfile)

        email_list = [r[' email'] for r in reader]

        writer.writerow(['Emails'])

        for email in email_list:
            writer.writerow([email])

